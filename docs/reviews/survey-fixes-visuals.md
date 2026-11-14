# First-pass fixes: figures and supplement

Task 2 disposition note, 2026-11-14. This records changes to the assigned figures, search protocol,
supplement source and generated S2 table. It does not claim verification of cited papers beyond the
local search records.

| ID | Disposition |
|---|---|
| F01 | Removed arrows between the three knowledge-type panels; labels and examples remain in each panel. |
| F02 | Removed arrows between all six training-scheme alternatives and revised the caption to describe the boxes as alternatives. |
| F03 | Search flow now shows 2,193 identified, 106 distinct first-search records, 310 full texts, the +2 second pass, −2 coordinator rulings, and +6 manual retrieval arithmetic to 112. It retains 445 second-pass records, 29 re-checked works and 15 manually retrieved papers. No exclusion count was added. |
| F04 | The two papers without full text are in a separate unassessed box, outside the final 112 included-record box. |
| F05 | Taxonomy labels now separate feature and relational knowledge types from architecture compatibility. Root label says the dimensions overlap. |
| F06 | Caption change is owned by the prose task; no figure-source edit was needed. |
| F07 | Removed preprint asterisks from taxonomy examples. No publication-status claim was added. |
| F10 | Moved the geometry legend outside the data grid through `moo_geometry.py`, regenerated its TikZ, and removed the stale unit-test claim from the generator docstring. Vector inputs, formulas and resulting directions were preserved. |
| F14 | S2 now uses a landscape longtable with wider Method and Notes columns, a larger table font and a continued-page caption/header. Author-year citations remain generated from the existing registry keys. |
| F15 | Source `--` result cells now generate as `NE`; the legend says this means no value was extracted and original-paper reporting status is undetermined. Alternative-pair notes are explicit for HiDFD, VkD, SoTeacher and Bayesian teacher; ABKD's figure-only CIFAR-100 note is retained. Family tags are described as overlapping. |
| T03 | Added the locally documented standard CIFAR-100 CRD pair list and distinguished MobileNetV1 as the ImageNet pair in S1. No additional eligibility pair was inferred beyond the local search records. |
| T04 | S1 now identifies S1/S2 title queries, S3 Crossref title queries, arXiv abstract query and comparison-table snowballing, with cutoff 2026-11-08. Existing staged counts and arithmetic are preserved. |

## Checks

- `python3 scripts/build_supplement.py` regenerated all 112 S2 rows.
- `python3 paper/survey/figures/moo_geometry.py` regenerated the geometry TikZ; printed direction values match the unchanged generator calculations.
- `.venv/bin/python -m pytest tests/unit/test_build_supplement.py`: 3 passed.
- Asserted 112 source rows, 112 generated citation keys, and presence of NE and alternative-pair notes.

No LaTeX build or PDF inspection was run in this task, as the integration pass owns rendering. Landscape
longtable layout and the resized main geometry inclusion still need visual inspection in the integrated PDF.
