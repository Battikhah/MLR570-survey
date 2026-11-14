# First-pass revision resolution

All 98 review findings have an editorial disposition below. This includes explicit qualifications where primary-source uncertainty cannot be resolved from the repository. The manuscript, figures, supplementary source/generator and both delivered PDFs were updated. No commit or push was made.

## Verification

- `pytest -q`: 10 passed.
- `build_bib.py --check`: passed; 239 registry entries, no missing citation keys.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error`: both documents built successfully; no overfull boxes or undefined citations/references in final logs. Ordinary underfull spacing diagnostics remain.
- All 145 citation keys, section Owner headers, 112 included record keys and their four recorded result cells were preserved.
- Generated S2 matches the owning Markdown and generator exactly. Figures/tables and page overview renders were visually inspected; the final CTSL row was also inspected after correction.
- Delivered PDFs match the built files: main 25 pages; supplement 14 pages.
- Two Luna build agents performed implementation. An independent verifier passed the checks and found one CTSL action-label ambiguity, which was corrected. Its final follow-up hit the usage limit; the main session completed the scoped row check, final build/log checks, tests and preservation checks directly.
- No configured Python type-checker or linter was added; relevant checks were pytest, generation consistency, LaTeX build/logs and `git diff --check`.

## Remaining source limitations

SCKD’s threshold/rationale disagreement remains explicitly unresolved; no authoritative code direction was invented. DTO-KD’s published constraint/deployment caveat remains stated. NE denotes an unextracted value whose reporting status is undetermined. Except for checking the CRD author repository pair list, this task did not repeat the primary-paper audit or refresh historical code availability.

## Item dispositions

| ID | Status | Change |
|---|---|---|
| A01 | Addressed | Replaced the “lens” metaphor with classification by gradient-combination rule and kept the explanation caveat. |
| A02 | Addressed | Replaced “We close with” and the long question with a concise list of remaining questions. |
| A03 | Addressed | Named the batch relations and sample weighting changes. |
| A04 | Addressed | Said logit standardisation can combine with several distillation losses. |
| A05 | Addressed | Removed the generic “no scheme dominates” maxim; stated the scheme-specific constraints. |
| A06 | Addressed | Replaced “lineage” with “background precedent” for SCKD; AE-KD heading names teacher balancing. |
| A07 | Addressed | Used label-priority, distillation-priority and symmetric-rule descriptions. |
| A08 | Addressed | Replaced “safe start” with a practical starting point and the conditions for using it. |
| A09 | Addressed | Replaced the unspecified cost fraction with lower inference cost. |
| A10 | Addressed | Specified that the cited survey reviews gradient-based MOO but not distillation. |
| A11 | Addressed | Replaced the progress-story transition with the concrete change and reported accuracy direction. |
| A12 | Addressed | Introduced CTKD’s values directly and retained their baselines and citation. |
| A13 | Addressed | Named RLD’s reliability topic and the next sections’ subjects. |
| A14 | Addressed | Named teacher availability, supervision sources and data access as compute/error factors. |
| A15 | Addressed | Explained that searched accuracy does not isolate one loss’s contribution. |
| A16 | Addressed | Opened with the reliability signals and retained the table reference. |
| A17 | Addressed | Described whether methods weight samples, switch sources, revise targets or select subsets. |
| A18 | Addressed | Stated the primary-label and auxiliary-teacher convention directly. |
| A19 | Addressed | Replaced “give back” with “reduce an existing correct-class margin.” |
| A20 | Addressed | Described MEMA as a continuous per-sample gradient-similarity weight. |
| A21 | Addressed | Distinguished per-pair search from per-step gradient changes. |
| A22 | Addressed | Renamed “scalarisation debate” to evidence from multi-task learning. |
| A23 | Addressed | Introduced TPKD’s projection ablation with its values, separately from interpretation. |
| A24 | Addressed | Stated that PCD’s distillation benefit remains untested. |
| A25 | Addressed | Opened with the reported CIFAR comparison and said differing protocols do not establish a reliable ranking. |
| A26 | Addressed | Replaced the conversion metaphor with the remaining questions. |
| S01 | Addressed | Removed venue inventory from the abstract; venues remain in the inclusion criterion and search protocol. |
| S02 | Addressed | Shortened the abstract’s open-question list and made its topics parallel. |
| S03 | Addressed | Broke I1–I3 into separate description entries, clarified internal targets and MobileNetV1, and stated that families overlap. |
| S04 | Addressed | Separated the accessible inclusion/exclusion sample counts from the two and ten unread samples. |
| S05 | Addressed | Split DKD mechanism, ablation interpretation and reported comparison. |
| S06 | Addressed | Split CTKD’s comparisons from LSKD’s mechanism and reported results. |
| S07 | Addressed | Explained feature values and pairwise-distance invariants before comparing them. |
| S08 | Addressed | Replaced the nested comparison sentence with attachment point, preserved relation and added work. |
| S09 | Addressed | Shortened the opening and separated scope from the detailed methods. |
| S10 | Addressed | Split the LR-DS/RLD and MCD/CHAD mechanism descriptions into paragraphs. |
| S11 | Addressed | Explained Frank–Wolfe’s weight-search role and MGDA-UB’s shared-representation approximation. |
| S12 | Addressed | Gave one rule per sentence; defined primary $f$, constrained $g$ and external criterion $F$. |
| S13 | Addressed | Defined DTO-KD’s $g_{11}$, $g_{12}$ and $g_{22}$ as gradient inner products/norms; retained the derivation and deployment caveat. |
| S14 | Addressed | Put MEMA’s damping formula on a display line and defined its constants. |
| S15 | Addressed | Listed the three proposed baseline groups. |
| S16 | Addressed | Separated KD comparisons, multi-task evidence and the proposed experiment. |
| S17 | Addressed | Replaced the compressed family catalogue with practical trade-offs. |
| F01 | Addressed | Removed arrows between the three knowledge-type panels; labels and examples remain in each panel. |
| F02 | Addressed | Removed arrows between all six training-scheme alternatives and revised the caption to describe the boxes as alternatives. |
| F03 | Addressed | Search flow now shows 2,193 identified, 106 distinct first-search records, 310 full texts, the +2 second pass, −2 coordinator rulings, and +6 manual retrieval arithmetic to 112. It retains 445 second-pass records, 29 re-checked works and 15 manually retrieved papers. No exclusion count was added. |
| F04 | Addressed | The two papers without full text are in a separate unassessed box, outside the final 112 included-record box. |
| F05 | Addressed | Taxonomy labels now separate feature and relational knowledge types from architecture compatibility. Root label says the dimensions overlap. |
| F06 | Addressed | Caption explicitly includes historical background; removed the misleading all-2022–2026 implication. |
| F07 | Addressed | Removed preprint asterisks from taxonomy examples. No publication-status claim was added. |
| F08 | Addressed | Kept verified KD-coverage ratings and replaced the general-MOO all-negative row with a separately labelled background row. |
| F09 | Addressed | Recast the reliability table as Signal/Action/Caveat and split LR-DS from RLD. SCKD’s row states that its published threshold and rationale disagree, with direction unresolved. |
| F10 | Addressed | Moved the geometry legend outside the data grid through `moo_geometry.py`, regenerated its TikZ, and removed the stale unit-test claim from the generator docstring. Vector inputs, formulas and resulting directions were preserved. |
| F11 | Addressed | Caption defines the descent update and makes the positive gradient-arrow convention explicit. |
| F12 | Addressed | Benchmark tables distinguish linked, linked-but-unreachable (as observed 2026-11-08), and not linked. |
| F13 | Addressed | Main benchmark tables use footnotesize tabularx, explicit baseline rows, code status and variant columns; redundant family/venue metadata remains in S2. |
| F14 | Addressed | S2 now uses a landscape longtable with wider Method and Notes columns, a larger table font and a continued-page caption/header. Author-year citations remain generated from the existing registry keys. |
| F15 | Qualified | Source `--` result cells now generate as `NE`; the legend says this means no value was extracted and original-paper reporting status is undetermined. Alternative-pair notes are explicit for HiDFD, VkD, SoTeacher and Bayesian teacher; ABKD's figure-only CIFAR-100 note is retained. Family tags are described as overlapping. |
| F16 | Addressed | Applied hidelinks in both documents; inspected the PDFs without the previous citation/cross-reference rectangles. |
| C01 | Qualified | Reliability table now carries the SCKD threshold/rationale disagreement; it does not choose an unsupported direction. |
| C02 | Addressed | PCD is described as a candidate general rule with no distillation evaluation. |
| C03 | Addressed | Preserved 112 included paper records, including separately listed extensions; corrected the denominator to 80 populated R18 result rows. All reported values are unchanged. |
| C04 | Addressed | Distinguished ten DF records, nine extracted WRN results and HiDFD’s other pair. Four other records have no values extracted in the displayed columns. |
| C05 | Addressed | Used the additive $L_{CE}+\\lambda L_{KD}$ form consistently and gave $\\lambda=\\alpha/(1-\\alpha)$ for $0\\leq\\alpha<1$, with the pure-KD endpoint. |
| C06 | Addressed | Qualified DPK’s teacher-size result to its reported setting. |
| C07 | Addressed | Removed the unsupported 76.0–77.5 summary range; cited GDKD and LDRLD examples instead. |
| C08 | Addressed | Reported MEMA and TPKD ablation values while leaving conflict-vs-rescaling explanations unresolved. |
| C09 | Addressed | Replaced the narrow reliability range with RLD, MCD and updated-teacher KD-AIF examples and their protocol distinction. |
| C10 | Addressed | Distinguished AE-KD’s teacher-to-teacher balancing from DTO-KD’s task/distillation combination. |
| C11 | Addressed | Separated symmetry from guarantees; PCD’s local directional condition is qualified and explicitly not a finite-step guarantee. |
| T01 | Addressed | I1 explicitly includes internally generated targets. |
| T02 | Addressed | Taxonomy and inclusion text state that families/dimensions overlap. |
| T03 | Addressed | Listed all 13 standard CIFAR-100 pairs from the CRD author repository, with MobileNetV1 distinguished for ImageNet. See https://github.com/HobbitLong/RepDistiller#benchmark-results-on-cifar-100. |
| T04 | Addressed | S1 now identifies S1/S2 title queries, S3 Crossref title queries, arXiv abstract query and comparison-table snowballing, with cutoff 2026-11-08. Existing staged counts and arithmetic are preserved. |
| T05 | Qualified | Mapped the convex weight to the additive weight and clarified fixed-learning-rate scaling without claiming optimiser equivalence. |
| T06 | Addressed | Qualified the temperature-one target statement by teacher/label agreement and described the wrong-prediction case. |
| T07 | Addressed | Said SimKD reuses the teacher classifier on learned student features without claiming identical input-space decisions. |
| T08 | Addressed | Replaced the abstract three-question synthesis with examples tied to named methods. |
| T09 | Addressed | Narrowed transfer-data claims to state that data-selection mechanisms are not compared here. |
| T10 | Addressed | Removed orphaned group-metric advice rather than imply an unestablished group method. |
| T11 | Addressed | Removed the uncited mechanism list; retained rule-specific explanations and a general caution about symmetry. |
| T12 | Qualified | Specified feasibility, nonzero secondary gradients, positive margin, and the effect of final rescaling; separated directional progress from finite-step guarantees. |
| T13 | Addressed | Limited conflict-removal framing and distinguished teacher weighting, scale and schedules. |
| T14 | Addressed | Distinguished cross-paper reproduction differences from variation across seeds in benchmark and future-work text. |
| T15 | Addressed | Teacher accuracy is context for TopoKD’s protocol, not grounds to invalidate the student result. |
| T16 | Addressed | Proposed a common top-$k$/threshold policy and an accuracy change after removing selected samples. |
| T17 | Addressed | Replaced gain ratio with absolute gains over matched KD baselines; described requirements for any ratio. |
| T18 | Addressed | Online KD and data-free KD now have separate constraints; data-free still uses a teacher. |
| U01 | Addressed | Removed draft-history narration from the preliminaries. |
| U02 | Addressed | Removed COCO split counts and detection dataset detail from the classification primer. |
| U03 | Addressed | Removed the CHAD attribution-audit aside; retained its BanSum evidence and scope limitation. |
| U04 | Addressed | Replaced the TPKD abstract omission caveat with its pretrained-student evaluation context. |
| U05 | Addressed | Removed the isolated DTO-KD COCO result from the MOO analysis. |
| U06 | Addressed | Replaced repeated CHAD task-specific values with a cross-reference to reliability. |
| U07 | Addressed | Removed generator/unit-test narration from the MOO figure caption. |
| U08 | Addressed | Removed repeated combination-rule recommendation from the optimizer paragraph; retained the baseline comparison in one dedicated paragraph and the future-work experiment. |
| U09 | Addressed | Removed the paragraph-template announcement. |
| U10 | Addressed | Removed the broad uncited neighboring-settings list; retained the scoped DHO example. |

## Follow-up: 2026-11-14 existing-source audit

The subsequent [source audit and figure refresh](survey-source-audit-status.md) supersedes the earlier unresolved-value/code-status snapshot where explicitly supported. It adds no bibliography records or citation keys. The historical first-pass dispositions above remain a record of that pass.
