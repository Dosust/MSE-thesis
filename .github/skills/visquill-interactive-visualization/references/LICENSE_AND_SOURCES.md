# VisQuill Official Source, Installation and License Notes

**Verified documentation snapshot:** 2026-10-08. Pages and versions change; check before implementation. Not legal advice.

## Official pages
- Product: https://visquill.com/
- Overview/install: https://visquill.com/developers/
- Guide: https://visquill.com/developers/guide/
- Interactive tutorials: https://visquill.com/developers/tutorials
- Lab: https://visquill.com/developers/lab
- API: https://visquill.com/developers/api
- Package product overview: https://visquill.com/products/
- Pricing/current written terms: https://visquill.com/pricing
- Separate older license page: https://visquill.com/licence/
- Vendor example source repository: https://github.com/visquill/visquill-lab

## Vendor-documented install
```bash
npm create visquill@latest
# or within an existing modern TypeScript browser project:
npm install @visquill/visquill-gdk
```
Follow scaffold prompts and consult generated package scripts, rather than assuming the dev/build commands. Match docs to the locally installed package version. Some crawled vendor pages displayed v1.0.1 whereas the API catalog listed v1.0.2 in October 2026; **do not claim a single globally verified latest version without checking npm/package-lock at build time**.

## Licensing distinctions and attribution
- **GDK is vendor-proprietary / separately licensed**, not equivalent to MIT.
- Published terms permit noncommercial academic, research, personal and educational use subject to visible *Made with VisQuill* attribution. Preserve the actual version's label exactly, even if older documents use *VisQuill.com* instead.
- Commercial products, paid client deliverables or removal of attribution require commercial arrangements. Do not guess prices or licensing conditions: review current site.
- VisQuill **Lab source** examples are separately marked MIT by the vendor. Source license does not make the binary GDK MIT.
- VisQuill **Lens** is a separate product; its exported viewer attribution/white-label terms differ and must be checked separately.
- Recheck current specific license terms immediately before public distribution, academic deployment, or including compiled library in a repository. Do not strip or obscure output watermark/attribution.
- Never commit downloaded `node_modules`, vendor GDK source/bundles, API keys, commercial license keys or user-sensitive measurements into thesis GitHub.

## Practical portability
Develop scientific results in reproducible Python/other scientific software; save data arrays and provenance separately. Use VisQuill only as an optional visualization layer. The thesis PDF/slides must retain standalone readable plots/figures independent of a running interactive web viewer.

## Evidence hierarchy
Vendor documentation supports **software API / installation / license** claims; it does **not** support physical assumptions about transformers, chargers, cross-system thermal dependency, or model accuracy. All such research content must cite primary scientific and equipment sources under repository evidence/citation standards.
