#!/usr/bin/env python3
"""Deck3 visual-asset MANIFEST STRUCTURE validator; not source/physics verification."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

PALETTE = frozenset('#FFFFFF #000000 #12304A #0072B2 #416985 #006D70 #087E98 #176B42 #B4232C #555D66 #8C1D40 #FFC627 #6ACEEE'.split())
MODES = {'EMBED_REAL_PHOTO', 'ORIGINAL_SOURCE_GROUNDED', 'NO_PHOTO_SCIENTIFICALLY_JUSTIFIED'}
RIGHTS = {'PERMISSION_VERIFIED', 'REFERENCE_ONLY', 'UNKNOWN', 'REJECTED'}
ARROWS = {'AC_POWER', 'DC_POWER', 'HEAT_TRANSFER', 'EXTERNAL_FORCING', 'CONTROL', 'MEASUREMENT', 'CANDIDATE_P_TO_T', 'CANDIDATE_T_TO_P', 'RESEARCH_SEQUENCE', 'ASSESSMENT_MAPPING'}
STATES = {'ESTABLISHED_GENERIC', 'EQUIPMENT_VERIFIED', 'MEASURED', 'MODELED', 'CANDIDATE_UNQUALIFIED', 'METHODOLOGICAL', 'ASSESSMENT', 'UNKNOWN'}
QA = {'NOT_RUN', 'OPEN', 'PASS', 'FAIL'}

class InvalidManifest(ValueError):
    pass

def require(value, reason):
    if not value:
        raise InvalidManifest(reason)

def nonempty(obj):
    return isinstance(obj, str) and bool(obj.strip())

def check(data):
    require(isinstance(data, dict), 'manifest must be an object')
    for key in ('asset_id', 'slide_number', 'presentation_variant', 'main_message', 'three_bullets', 'visual_purpose', 'asset_only', 'whole_slide_screenshot', 'collage', 'source_mode', 'references', 'embedded_real_photo_count', 'nodes', 'arrows', 'style', 'outputs', 'qa'):
        require(key in data, 'missing ' + key)
    require(all(nonempty(data[k]) for k in ('asset_id', 'main_message', 'visual_purpose')), 'missing identity/message/purpose')
    n = data['slide_number']
    require(type(n) is int and 1 <= n <= 10, 'slide must be 1..10 for this variant')
    require(data['presentation_variant'] == 'TEN_SLIDE_MSE_TRAINING', 'do not conflate variants')
    require(data['asset_only'] is True and data['whole_slide_screenshot'] is False and data['collage'] is False, 'standalone asset required')
    require(isinstance(data['three_bullets'], list) and len(data['three_bullets']) == 3 and all(map(nonempty, data['three_bullets'])), 'exactly three nonempty source bullets required')
    mode = data['source_mode']
    require(mode in MODES, 'unknown source mode')
    refs = data['references']
    require(isinstance(refs, list), 'references must be list')
    count = data['embedded_real_photo_count']
    require(type(count) is int and count >= 0, 'photo count is invalid')
    for ref in refs:
        require(isinstance(ref, dict), 'reference must be object')
        require(all(nonempty(ref.get(k)) for k in ('url', 'provider', 'equipment_match', 'visual_role')), 'reference identification/match incomplete')
        require(type(ref.get('inspected')) is bool, 'inspection must be explicitly boolean')
        require(ref.get('rights_status') in RIGHTS, 'invalid rights status')
    if mode == 'EMBED_REAL_PHOTO':
        usable = [r for r in refs if r['inspected'] and r['rights_status'] == 'PERMISSION_VERIFIED' and r.get('embedded') is True and nonempty(r.get('attribution'))]
        require(count > 0 and len(usable) >= count, 'embedded photo requires inspected, licensed, attributed sources')
    else:
        require(count == 0 and not any(r.get('embedded') for r in refs), 'no embedded photo permitted in this mode')
        if mode == 'ORIGINAL_SOURCE_GROUNDED':
            require(any(r['inspected'] for r in refs), 'source-grounded art requires declared inspected reference')
        else:
            require(nonempty(data.get('no_photo_reason')), 'abstract figure requires explicit no-photo justification')

    nodes = data['nodes']
    require(isinstance(nodes, list) and nodes, 'nodes are required')
    known = {}
    for node in nodes:
        require(isinstance(node, dict) and nonempty(node.get('id')), 'bad node ID')
        nid = node['id']
        require(nid not in known and node.get('system') in ('POWER', 'TRANSPORT', 'EXTERNAL', 'RESEARCH', 'ASSESSMENT'), 'duplicate ID or invalid system')
        if nid in ('P1', 'P2', 'P3', 'P4'):
            require(node['system'] == 'POWER', 'P component membership is wrong')
        if nid in ('T1', 'T2', 'T3', 'T4'):
            require(node['system'] == 'TRANSPORT', 'T component membership is wrong')
        known[nid] = node['system']

    seen = set()
    for edge in data['arrows']:
        require(isinstance(edge, dict) and all(nonempty(edge.get(k)) for k in ('id', 'type', 'source', 'target', 'evidence_status', 'label')), 'incomplete arrow')
        a, b, t, st = edge['source'], edge['target'], edge['type'], edge['evidence_status']
        require(edge['id'] not in seen, 'duplicate arrow ID')
        seen.add(edge['id'])
        require(a in known and b in known and a != b, 'arrow endpoints invalid')
        require(t in ARROWS and st in STATES, 'unknown arrow semantic/status')
        if t == 'AC_POWER':
            require((a, b) in (('P1', 'P2'), ('P2', 'T1')), 'ordinary AC path not P1→P2→T1')
        if t == 'DC_POWER':
            require((a, b) == ('T1', 'T2'), 'ordinary DC charge must be T1→T2')
        if t == 'EXTERNAL_FORCING':
            require(known[a] == 'EXTERNAL' and known[b] in ('POWER', 'TRANSPORT'), 'ambient is externally applied forcing')
        if t in ('CANDIDATE_P_TO_T', 'CANDIDATE_T_TO_P'):
            require(st == 'CANDIDATE_UNQUALIFIED' and 'NOT YET QUALIFIED' in edge['label'].upper(), 'candidate hypothesis needs visible qualification')
            require(nonempty(edge.get('hypothesis')), 'hypothesis ID required')
            systems = ('POWER', 'TRANSPORT') if t == 'CANDIDATE_P_TO_T' else ('TRANSPORT', 'POWER')
            require((known[a], known[b]) == systems, 'hypothesis orientation contradicts label')
        if {known[a], known[b]} == {'POWER', 'TRANSPORT'}:
            require(t == 'AC_POWER' and (a, b) == ('P2', 'T1') or t in ('CANDIDATE_P_TO_T','CANDIDATE_T_TO_P'), 'unqualified cross-system physical/control edge')

    sty = data['style']
    require(isinstance(sty, dict) and sty.get('canvas') == '#FFFFFF' and sty.get('panel') == '#FFFFFF', 'white canvas/interiors required')
    require(sty.get('aspect_ratio') == '16:9' and sty.get('font') == 'Times New Roman', 'aspect ratio/font mismatch')
    colors = sty.get('authored_colors')
    require(isinstance(colors, list) and colors and all(isinstance(x, str) and x in PALETTE for x in colors), 'off-palette authored color')
    require(sty.get('gradient') is False and sty.get('shadow') is False, 'gradients and shadows forbidden')
    if '#FFC627' in colors:
        require(sty.get('gold_role') == 'SMALL_INSTITUTIONAL_ACCENT', 'ASU gold is restricted')
    outputs = data['outputs']
    require(isinstance(outputs, dict) and outputs.get('png') == f'slide{n:02d}.png', 'independent slide-specific PNG export required')
    require(outputs.get('svg') in (None, f'slide{n:02d}.svg'), 'SVG name should match independent asset')
    require(outputs.get('planned_separate_asset') is True, 'output plan must be a separate figure')
    status = data['qa']
    require(isinstance(status, dict) and all(status.get(x) in QA for x in ('science', 'source_rights', 'render', 'canva_editability')), 'QA statuses incomplete or invalid')
    return {'decision': 'STRUCTURE_ACCEPTED_NOT_SCIENCE_OR_RIGHTS_VERIFIED', 'slide_number': n, 'nodes': len(known), 'arrows': len(seen)}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('manifest', type=Path)
    args = p.parse_args()
    try:
        data = json.loads(args.manifest.read_text(encoding='utf-8'))
        print(json.dumps(check(data), indent=2))
    except (OSError, ValueError) as err:
        print(json.dumps({'decision': 'REJECTED', 'reason': str(err)}, indent=2))
        raise SystemExit(1) from err

if __name__ == '__main__':
    main()
