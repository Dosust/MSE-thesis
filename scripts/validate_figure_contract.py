#!/usr/bin/env python3
"""Fail-closed *structural* figure contract validator; NOT scientific validation.

Zero external dependencies. Does not inspect rendered pixels, verify sources or solve ODEs.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

PALETTE = frozenset('#FFFFFF #000000 #12304A #0072B2 #416985 #006D70 #087E98 #176B42 #B4232C #555D66 #8C1D40 #FFC627 #6ACEEE'.split())
COMPONENTS = frozenset(('P1', 'P2', 'P3', 'P4', 'T1', 'T2', 'T3', 'T4'))
TYPES = frozenset(('AC_POWER', 'DC_POWER', 'HEAT_TRANSFER', 'CONTROL', 'MEASUREMENT', 'CANDIDATE_CAUSAL', 'EXTERNAL_FORCING', 'PROCESS_SEQUENCE'))
STATUSES = frozenset(('ESTABLISHED_GENERIC', 'LITERATURE_SUPPORTED', 'EQUIPMENT_VERIFIED', 'MEASURED', 'MODELED', 'CANDIDATE_UNQUALIFIED', 'UNKNOWN'))
CANDIDATES = frozenset(('I2', 'I3'))
REQUIRED_PROVENANCE = ('source_id', 'scope', 'evidence_status')


class ContractError(ValueError):
    pass


def _require(test: bool, message: str) -> None:
    if not test:
        raise ContractError(message)


def _text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_contract(c: dict) -> dict:
    """Validate admitted data *shape* and conservative electrical visual semantics."""
    _require(isinstance(c, dict), 'contract must be a JSON object')
    for k in ('figure_id', 'scientific_message', 'variant', 'nodes', 'edges', 'style', 'animation'):
        _require(k in c, f'missing {k}')
    _require(all(_text(c[k]) for k in ('figure_id', 'scientific_message', 'variant')), 'figure identity, variant and message must be nonempty')
    _require(isinstance(c['nodes'], list) and len(c['nodes']) > 0, 'nodes must be a nonempty list')
    _require(isinstance(c['edges'], list), 'edges must be a list')

    node_index = {}
    for n in c['nodes']:
        _require(isinstance(n, dict) and all(k in n for k in ('id', 'label', 'system', 'kind')), 'node fields missing')
        nid = n['id']
        _require(_text(nid) and nid not in node_index, 'duplicate or invalid node id')
        _require(nid in COMPONENTS or nid.startswith('EXT_'), 'unknown physical component or external node')
        _require(_text(n['label']) and _text(n['kind']), 'node label and kind must be nonempty strings')
        _require(n['system'] in ('POWER', 'TRANSPORT', 'EXTERNAL'), 'unknown physical system')
        if nid.startswith('P'):
            _require(n['system'] == 'POWER', 'P component must belong to Power System')
        if nid.startswith('T'):
            _require(n['system'] == 'TRANSPORT', 'T component must belong to Transportation System')
        if nid.startswith('EXT_'):
            _require(n['system'] == 'EXTERNAL', 'external forcing node must be external')
        node_index[nid] = n

    edge_ids = set()
    for e in c['edges']:
        _require(isinstance(e, dict) and all(k in e for k in ('id', 'source', 'target', 'type', 'evidence_status', 'label')), 'edge fields missing')
        _require(_text(e['id']) and e['id'] not in edge_ids, 'duplicate or invalid edge id')
        edge_ids.add(e['id'])
        a, b, t, status = e['source'], e['target'], e['type'], e['evidence_status']
        _require(_text(a) and _text(b), 'edge endpoints must be strings')
        _require(a in node_index and b in node_index and a != b, 'edge endpoint unknown or self-loop')
        _require(t in TYPES and status in STATUSES, 'unknown edge type or evidence status')
        _require(_text(e['label']), 'each edge needs an explicit label')
        if t == 'AC_POWER':
            _require((a, b) in (('P1', 'P2'), ('P2', 'T1')), 'ordinary AC supply must follow P1→P2→T1')
        if t == 'DC_POWER':
            _require((a, b) in (('T1', 'T2'), ('T2', 'T4')), 'ordinary DC/vehicle auxiliary supply must remain in T1→T2 or T2→T4')
        if t == 'EXTERNAL_FORCING':
            _require(a.startswith('EXT_') and not b.startswith('EXT_'), 'external heat is forcing from environment to equipment')
        iid = e.get('interface_id')
        _require(iid is None or _text(iid), 'interface_id must be a string if supplied')
        if iid in CANDIDATES:
            _require(t == 'CANDIDATE_CAUSAL', f'{iid} cannot be encoded as established power/heat/control')
            _require(status == 'CANDIDATE_UNQUALIFIED', f'{iid} must stay unqualified')
            _require('not yet qualified' in e['label'].lower(), f'{iid} requires an explicit visual qualifier')
        if t == 'CANDIDATE_CAUSAL':
            _require(iid in CANDIDATES, 'training candidate edge must name I2 or I3')
            _require('not yet qualified' in e['label'].lower(), 'all candidate edges need visible not-yet-qualified status')
            _require(status == 'CANDIDATE_UNQUALIFIED', 'candidate edge cannot be promoted')
            _require(_text(e.get('hypothesis')), 'candidate edge requires explicit hypothesis')
        # The training profile disallows inferred physical transfer between systems.
        source_system, target_system = node_index[a]['system'], node_index[b]['system']
        if {source_system, target_system} == {'POWER', 'TRANSPORT'}:
            normal_ac = t == 'AC_POWER' and (a, b) == ('P2', 'T1')
            i2_candidate = (t == 'CANDIDATE_CAUSAL' and iid == 'I2' and
                            a in ('T1', 'T3') and b in ('P1', 'P2'))
            i3_candidate = (t == 'CANDIDATE_CAUSAL' and iid == 'I3' and
                            a in ('P1', 'P3') and b in ('T1', 'T2'))
            _require(normal_ac or i2_candidate or i3_candidate,
                     'cross-system training edge needs ordinary P2→T1 AC or directed, qualified I2/I3 candidate')
        if t == 'HEAT_TRANSFER':
            _require(a not in ('P2', 'T2') or b not in ('P1', 'T1'), 'heat-transfer link is unsupported for this generic training graph')
        if status in ('LITERATURE_SUPPORTED', 'EQUIPMENT_VERIFIED', 'MEASURED', 'MODELED'):
            prov = e.get('provenance')
            _require(isinstance(prov, dict) and all(_text(prov.get(k)) for k in REQUIRED_PROVENANCE), 'asserted evidence requires source ID, scope and evidence status')

    s = c['style']
    _require(isinstance(s, dict), 'style must be an object')
    _require(s.get('canvas') == '#FFFFFF' and s.get('panel') == '#FFFFFF', 'white canvas and panel required')
    _require(s.get('font') == 'Times New Roman', 'authored font must be Times New Roman')
    _require(s.get('aspect_ratio') == '16:9', '16:9 required')
    colors = s.get('authored_colors')
    _require(isinstance(colors, list) and colors and all(isinstance(v, str) and v in PALETTE for v in colors), 'authored colors outside approved 13-token palette')
    _require(not s.get('gradient') and not s.get('shadow'), 'no gradients or shadows')
    if '#FFC627' in colors:
        _require(s.get('gold_role') == 'SMALL_ASU_INSTITUTIONAL_ACCENT', 'ASU Gold role is restricted')

    an = c['animation']
    _require(isinstance(an, dict) and an.get('kind') in ('EXPLANATORY_REVEAL', 'PHYSICAL_TIME', 'STATIC'), 'unknown animation mode')
    if an['kind'] == 'EXPLANATORY_REVEAL':
        _require(an.get('clock') == 'PRESENTATION_TIME', 'explanatory reveal must use presentation time')
        _require(an.get('physical_time_claim') is False, 'reveal cannot claim physical time')
    elif an['kind'] == 'PHYSICAL_TIME':
        _require(an.get('clock') == 'PHYSICAL_MODEL_TIME', 'physical animation must use physical model time')
        model = an.get('model')
        _require(isinstance(model, dict) and all(_text(model.get(k)) for k in ('equation_ref', 'initial_conditions', 'units', 'parameters_provenance', 'validation_status', 'time_mapping')), 'physical animation lacks declared equation/IC/units/parameters/validation/time mapping')
        _require(model['validation_status'] != 'VALIDATED' or _text(model.get('independent_validation_evidence')), 'validated claim needs independent evidence')
    else:
        _require(an.get('clock') in (None, 'NONE'), 'static has no time clock')

    return {'figure_id': c['figure_id'], 'decision': 'STRUCTURE_ACCEPTED_NOT_SCIENTIFICALLY_VERIFIED', 'nodes': len(node_index), 'edges': len(edge_ids)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('contract', type=Path)
    args = ap.parse_args()
    data = json.loads(args.contract.read_text(encoding='utf-8'))
    try:
        print(json.dumps(validate_contract(data), indent=2))
    except ContractError as ex:
        print(json.dumps({'decision': 'REJECTED', 'reason': str(ex)}, indent=2))
        raise SystemExit(1) from ex


if __name__ == '__main__':
    main()
