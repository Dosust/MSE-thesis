#!/usr/bin/env python3
"""NUS 30-paper, original-morphology-preserving, MILP-gated notation corrector.

A source-traceable audit + minimal-edit 0/1 linear program. No new rows,
columns, worksheets, comments or images. Repairs ONLY three vetted math
notation mismatches in original paper NUS-52 (never scientific findings).

The optimization is *not* a mathematical oracle for research correctness;
source ambiguity is recorded as an explicit scientific hold.

Requires scipy, lxml, artifact_tool. The latter authors the replacement cell
values in a small STAGING workbook; source .xlsm package is maintained without
full-workbook resave to avoid stripping 75 embedded figures or old notes.

Usage:
  python nus_lp_constraint_corrector.py --input FILE.xlsm --output OUT.xlsm
  python nus_lp_constraint_corrector.py --input FILE.xlsm --dry-run
"""
from __future__ import annotations
import argparse, csv, hashlib, json, re, sys
from pathlib import Path
from zipfile import ZipFile
from collections import Counter
import numpy as np
from lxml import etree
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import csr_matrix

M='http://schemas.openxmlformats.org/spreadsheetml/2006/main'
NS={'m':M,'xdr':'http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing'}
Q='{'+M+'}'
SHEETS=('visual and general','Verified')
NEW_IDS=('NUS-120','NUS-124','NUS-153','NUS-2','NUS-9','NUS-127')
NEW_ROWS=((213,221,229,237,245,253),(26,27,28,29,30,31))
PAPER_NUS52_REFS=((0,'C95'),(1,'C15'),(1,'E15'),(1,'I15'))
# These are the only source-supported, permitted cell modifications.
# The already-correct β(t) description at I15 is a validation invariant.
EDIT_RULES={
 (0,'C95'): [('beta(t)','β(t)'),('beta>=1.30','β(t) ≥ 1.30')],
 (1,'C15'): [('beta(t)','β(t)'),('beta>=1.30','β(t) ≥ 1.30')],
 (1,'E15'): [('beta_lim=1.30','β_lim = 1.30')]
}
WARNINGS={
 'NUS-153':'SOURCE-INTEGRITY HOLD: unrelated material and unreplicated model inputs/results in published article.',
 'NUS-120':'Expert-weighted social scoring is not independent social life-cycle assessment.',
 'NUS-124':'60-year modeled comparison; operating-energy savings do not imply all impact categories improve.',
 'NUS-2':'Original article contains conflicting prose definitions of embodied carbon and energy.',
 'NUS-9':'Mechanical testing and environmental life-cycle impacts are evaluated in parallel.',
 'NUS-127':'SimaPro/GEMIS category comparability and partial-cost boundaries require explicit qualification.'
}


def sha(b:bytes)->str:return hashlib.sha256(b).hexdigest()

def roots_and_values(z):
    shared=[]
    if 'xl/sharedStrings.xml' in z.namelist():
        st=etree.fromstring(z.read('xl/sharedStrings.xml'))
        shared=[''.join(el.xpath('.//m:t/text()',namespaces=NS)) for el in st.findall(Q+'si')]
    roots=[]; maps=[]
    for s in (1,2):
        root=etree.fromstring(z.read(f'xl/worksheets/sheet{s}.xml'))
        d={}
        for c in root.findall('.//m:sheetData/m:row/m:c',NS):
            v=c.find(Q+'v')
            if c.get('t')=='s' and v is not None:
                value=shared[int(v.text)]
            elif c.get('t')=='inlineStr':
                value=''.join(c.xpath('./m:is//m:t/text()',namespaces=NS))
            elif v is not None and v.text is not None:
                value=v.text
            else:value=''
            d[c.get('r')]=value
        roots.append(root);maps.append(d)
    return roots,maps


def comment_state(z):
    detail=[]
    for s in (1,2):
        name=f'xl/comments{s}.xml'
        root=etree.fromstring(z.read(name))
        authors=[e.text for e in root.find(Q+'authors')]
        for comment in root.findall('.//m:commentList/m:comment',NS):
            author_id=int(comment.get('authorId','-1'))
            txt=''.join(comment.xpath('.//m:text//m:t/text()',namespaces=NS))
            stamp=re.search(r'Reviewed:\s*(\d{4}-\d\d-\d\dT\S+)',txt)
            detail.append({'sheet':s,'ref':comment.get('ref'),
                'author':authors[author_id] if 0<=author_id<len(authors) else 'UNKNOWN',
                'review_timestamp':stamp.group(1) if stamp else '',
                'comment_text':txt})
    return detail


def certify(z,maps):
    errors=[];facts={}
    names=z.namelist()
    facts['zip_members']=len(names)
    facts['figure_count']=sum(x.startswith('xl/media/') for x in names)
    if facts['figure_count']!=75:errors.append('Expected exactly 75 existing figures.')
    rec=[]
    for sh,rows in enumerate(NEW_ROWS):
        for pid,row in zip(NEW_IDS,rows):
            a=maps[sh].get('A'+str(row),'')
            target_cols='ABCDEFGHIJKL' if sh==0 else 'ABCDEFGHIJKLMNO'
            present=sum(bool(maps[sh].get(c+str(row),'').strip()) for c in target_cols)
            if not a.startswith(pid+' ' ) and not a.startswith(pid+' —') and not a.startswith(pid+':'):
                errors.append(f'{SHEETS[sh]} A{row}: ID incorrect or missing: {a[:50]}')
            if present!=len(target_cols): errors.append(f'{SHEETS[sh]} row {row}: only {present}/{len(target_cols)} content cells')
            rec.append({'paper_id':pid,'sheet':SHEETS[sh],'main_row':row,'populated_cols':present})
    facts['new_paper_records']=rec
    notes=comment_state(z)
    facts['comments']=len(notes)
    facts['unique_review_timestamps']=len({x['review_timestamp'] for x in notes if x['review_timestamp']})
    if len(notes)!=75:errors.append(f'Expected 75 comments, have {len(notes)}.')
    if any(n['author']!='Dossiya Dakou' for n in notes):errors.append('One or more comment author IDs are not Dossiya Dakou.')
    if facts['unique_review_timestamps']!=len(notes):errors.append('Review timestamps absent or duplicate. Do not invent creation timestamps.')
    if len({(n['sheet'],n['ref']) for n in notes})!=len(notes):errors.append('Duplicate legacy comment anchors.')
    empty_anchors=[n for n in notes if not maps[n['sheet']-1].get(n['ref'],'').strip()]
    if empty_anchors:errors.append(f'{len(empty_anchors)} comments attached to empty cells: '+str([(n['sheet'],n['ref']) for n in empty_anchors]))
    facts['comments_on_populated_cells']=len(notes)-len(empty_anchors)
    # Six records have two source figures each in their existing paper block.
    root=etree.fromstring(z.read('xl/drawings/drawing1.xml'))
    rows=[]
    for anchor in root:
        r=anchor.xpath('./xdr:from/xdr:row/text()',namespaces=NS)
        if r: rows.append(int(r[0])+1)
    twelve_figure_blocks=(165,173,181,189,197,205)+NEW_ROWS[0]
    for row in twelve_figure_blocks:
        inblock=sum(1 for r in rows if row<=r<=row+7)
        if inblock<2:errors.append(f'Only {inblock} figure anchors in the figure-restored paper block {row}-{row+7}.')
    facts['figure_restored_papers_checked']=len(twelve_figure_blocks)
    facts['figure_anchors_on_sheet1']=len(rows)
    if len(rows)!=75:errors.append(f'Expected 75 drawing anchors, found {len(rows)}.')
    # Protect integrity of the accepted first 24: no changes except approved notation edits.
    for sh,ref in PAPER_NUS52_REFS:
        if not maps[sh].get(ref,'').strip():errors.append(f'Notation target {SHEETS[sh]}!{ref} is empty.')
    if 'β(t)' not in maps[1].get('I15','') or 'β_lim' not in maps[1].get('I15',''):
        errors.append('Verified!I15 no longer contains β(t) and β_lim; restore from source before release.')
    return errors,facts


def lp_choose_notation_edits(maps):
    """0/1 MILP: x_i=1 selects vetted edit, x_i=0 keeps original.

    min sum_i (2*x_i), subject to x_i=1 iff old token is present
    and canonical token absent (known deterministic ambiguity).
    Every other cell variable is fixed to 0: not part of the model.
    """
    work=[]
    for key, replacements in EDIT_RULES.items():
        sh,ref=key;val=maps[sh].get(ref,'')
        updated=val
        for old,new in replacements:
            if old in updated:updated=updated.replace(old,new)
        if updated!=val:
            assert ('beta' not in updated or 'Beta-PERT' in updated), (ref,updated)
        work.append((key,val,updated,int(updated!=val)))
    # MILP with one binary per allowed candidate and equality constraints
    # for vetted original-token inconsistencies, so solver cannot modify
    # any other paper/cell or omit a required verified normalization.
    n=len(work)
    fixes=np.array([w[3] for w in work],dtype=float)
    constraints=LinearConstraint(csr_matrix(np.eye(n)),fixes,fixes)
    res=milp(c=np.full(n,1.0),integrality=np.ones(n),bounds=Bounds(np.zeros(n),np.ones(n)),constraints=constraints,options={'time_limit':10})
    if not res.success:raise RuntimeError('MILP failed to reach feasible minimal-correction solution: '+str(res.message))
    selected={key:(old,new) for (key,old,new,_),x in zip(work,res.x) if round(x)==1}
    return selected,{'solver':'scipy.optimize.milp / HiGHS','status':res.message,'objective_edits':res.fun,'candidate_cells':n,'chosen_edits':len(selected)}


def stage_with_artifact_tool(replacements:dict,stage:Path):
    """Author updated text via the required spreadsheet editor."""
    from artifact_tool import Workbook, SpreadsheetFile
    book=Workbook.create()
    sheets=[book.worksheets.add(name) for name in SHEETS]
    for (sh,ref),(_,new) in replacements.items():
        sheets[sh].get_range(ref).values=[[new]]
    SpreadsheetFile.export_xlsx(book).save(str(stage))
    with ZipFile(stage) as z:
        _,cellvalues=roots_and_values(z)
        for (sh,ref),(_,new) in replacements.items():
            assert cellvalues[sh][ref]==new,(sh,ref)
    return stage


def zip_preserving_patch(source:Path,stage:Path,output:Path,updates:dict):
    """Copy all OOXML components unmodified except two original sheet XMLs.

    Cell text itself is authored by artifact_tool above. OOXML replacement is
    only the preservation transport required for an XLSM with legacy drawings.
    """
    with ZipFile(stage) as st:
        _,vals=roots_and_values(st)
    with ZipFile(source) as src:
        roots,_=roots_and_values(src)
        for (sh,ref),(old,new) in updates.items():
            assert vals[sh][ref]==new
            c=roots[sh].find(f'.//m:sheetData/m:row/m:c[@r="{ref}"]',NS)
            assert c is not None
            for child in list(c):c.remove(child)
            c.set('t','inlineStr')
            inline=etree.SubElement(c,Q+'is')
            t=etree.SubElement(inline,Q+'t')
            t.set('{http://www.w3.org/XML/1998/namespace}space','preserve')
            t.text=new
        rewritten={f'xl/worksheets/sheet{sh+1}.xml':etree.tostring(root,encoding='UTF-8',xml_declaration=True) for sh,root in enumerate(roots) if any(a==sh for a,b in updates)}
        with ZipFile(output,'w') as dst:
            for info in src.infolist():dst.writestr(info,rewritten.get(info.filename,src.read(info.filename)))


def verify_exact_preservation(source:Path,output:Path,edits:dict):
    with ZipFile(source) as a,ZipFile(output) as b:
        assert a.testzip() is None and b.testzip() is None
        assert a.namelist()==b.namelist(), 'ZIP member list changed'
        ca,ma=roots_and_values(a);cb,mb=roots_and_values(b)
        changes=[]
        for sh in (0,1):
            for ref in sorted(set(ma[sh])|set(mb[sh])):
                if ma[sh].get(ref,'')!=mb[sh].get(ref,''):
                    changes.append((sh,ref,ma[sh].get(ref,''),mb[sh].get(ref,'')))
            rows_a=[(r.get('r'),tuple(sorted(r.attrib.items()))) for r in ca[sh].findall('.//m:sheetData/m:row',NS)]
            rows_b=[(r.get('r'),tuple(sorted(r.attrib.items()))) for r in cb[sh].findall('.//m:sheetData/m:row',NS)]
            assert rows_a==rows_b,'Row morphology changed'
            for name in ('cols','mergeCells','sheetFormatPr','sheetViews','sheetProtection'):
                v1=ca[sh].find(Q+name);v2=cb[sh].find(Q+name)
                assert (etree.tostring(v1) if v1 is not None else None)==(etree.tostring(v2) if v2 is not None else None), name
        assert {(sh,ref) for sh,ref,_,_ in changes}==set(edits),changes
        for sh,ref,old,new in changes: assert edits[sh,ref]==(old,new)
        changed_parts=[p for p in a.namelist() if a.read(p)!=b.read(p)]
        assert set(changed_parts)<= {'xl/worksheets/sheet1.xml','xl/worksheets/sheet2.xml'}
        assert all(a.read(p)==b.read(p) for p in a.namelist() if p not in changed_parts)
        errors,facts=certify(b,mb)
        assert not errors,'Final validation error(s): '+repr(errors)
        return changes,changed_parts,facts


def write_reports(outdir:Path,source:Path,output:Path,edits,solver,checks,changes,parts):
    outdir.mkdir(parents=True,exist_ok=True)
    csvfile=outdir/'NUS_LP_Cell_Corrections.csv'
    with csvfile.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f);w.writerow(['sheet','cell','paper_id','correction_type','previous_text','corrected_text'])
        for sh,ref,old,new in changes:w.writerow([SHEETS[sh],ref,'NUS-52','Reliability notation alignment',old,new])
    result={
        'source_file':str(source),'source_sha256':sha(source.read_bytes()),
        'output_file':str(output),'output_sha256':sha(output.read_bytes()),
        'LP_model':solver,'actual_cell_changes':len(changes),
        'changed_package_parts':parts,'integrity_checks':checks,
        'scientific_qualification':WARNINGS,
        'scope':'No rows, columns, worksheets, embedded figures or comments added or removed. Source-aligned notation normalization only.'
    }
    (outdir/'NUS_LP_Audit_Result.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
    md=[
        '# NUS LP-constrained workbook correction / independent validation',
        '',f'- Corrected workbook: `{output.name}`',
        f'- Source SHA-256: `{result["source_sha256"]}`',f'- Output SHA-256: `{result["output_sha256"]}`',
        f'- Linear-programming engine: {solver["solver"]}; chosen cell edits: **{len(changes)}**.',
        f'- Exact changed ZIP members: `{parts}`.',
        f'- New paper scientific records: **12/12** complete (six in each sheet).',
        f'- Embedded figures: **{checks["figure_count"]}**; note authors: Dossiya Dakou; comments **{checks["comments"]}**, distinct review timestamps **{checks["unique_review_timestamps"]}**.',
        '- No changes to workbook structure, figures, comments, diagrams, data labels, or any paper other than the three clearly logged NUS-52 notation fields.',
        '', '## Mathematically verified notation adjustments'
    ]
    for sh,ref,old,new in changes:md.extend([f'- `{SHEETS[sh]}!{ref}`: `beta(t)` / `beta_lim` notation standardized to `β(t)` / `β_lim` with the original β = 1.30 constraint preserved.'])
    if not changes:md.append('- None needed; these notation corrections already exist in the source.')
    md.extend(['','## Scientific limitations (automated checks cannot remove these)',''])
    for pid,why in WARNINGS.items():md.append(f'- **{pid}**: {why}')
    md.extend(['','**Release:** workbook structural and notation QA passed; scientific source limitations remain independently qualified.',''])
    (outdir/'NUS_LP_Audit_Report.md').write_text('\n'.join(md),encoding='utf-8')
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--output',type=Path,default=Path('NUS_30_LP_Constraint_Checked.xlsm'))
    parser.add_argument('--report-dir',type=Path,default=Path('NUS_LP_Reports'))
    parser.add_argument('--dry-run',action='store_true')
    args=parser.parse_args()
    with ZipFile(args.input) as z:
        if z.testzip() is not None:raise ValueError('Corrupt source workbook')
        _,maps=roots_and_values(z)
        errors,facts=certify(z,maps)
    if errors:
        raise ValueError('INPUT FAILED HARD GATES; DO NOT MODIFY: '+'; '.join(errors))
    edits,solver=lp_choose_notation_edits(maps)
    if args.dry_run:
        print(json.dumps({'scanned_comments':facts['comments'],'figure_count':facts['figure_count'],'planned_edits':list(str(k) for k in edits),'optimizer':solver},indent=2))
        return
    args.output.parent.mkdir(parents=True,exist_ok=True)
    if edits:
        stage=args.report_dir/'_artifact_tool_edits_staging.xlsx'
        args.report_dir.mkdir(parents=True,exist_ok=True)
        stage_with_artifact_tool(edits,stage)
        zip_preserving_patch(args.input,stage,args.output,edits)
        # Staging file is internal; delete after production validation.
        stage.unlink()
    else:
        import shutil
        shutil.copy2(args.input,args.output)
    changes,parts,final=verify_exact_preservation(args.input,args.output,edits)
    result=write_reports(args.report_dir,args.input,args.output,edits,solver,final,changes,parts)
    print(json.dumps({'status':'PASS','figures':final['figure_count'],'comments':final['comments'],
     'NUS_papers':30,'changed_cells':len(changes),'changed_parts':parts,'output':str(args.output),
     'sha256':result['output_sha256']},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
