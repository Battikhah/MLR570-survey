# Condensed survey audit (Codex)

Compared `survey-full-v1` to `HEAD` using `git diff survey-full-v1 HEAD -- paper/survey` and inspected tagged source files with `git show survey-full-v1:<file>`. Read-only audit; this report is the only file written.

## Findings

| Severity | File:line | Evidence | Fix |
|---|---|---|---|
| C | `paper/survey/sections/08_benchmarks.tex:65,101` | The two benchmark table header rows contain literal tab characters where LaTeX commands were intended: `R32$<TAB>imes$4$<TAB>o$R8$<TAB>imes$4` and `R34$<TAB>o$R18`. This breaks the pair labels and likely produces malformed LaTeX. | Replace the tabs with `\times` and `\to`; rebuild the paper to verify the tables. |
| M | `paper/survey/sections/03a_logit.tex:35`; full-version `paper/survey/sections/03a_logit.tex` | EKD's teacher top-1 value 79.53 (full version source note: teacher EDL 79.53 vs softmax 79.42) no longer occurs in the condensed paper or `docs/survey/search/*.md`. The student accuracy 77.21 remains. This is an accuracy value removed from the paper entirely. | Restore 79.53 with its teacher context, or explicitly record it as intentionally omitted. |
| M | `paper/survey/sections/08_benchmarks.tex:82,120`; `paper/survey/sections/11_appendix_methods.tex:65` | MCD is included in the benchmark and appendix tables, but its mechanism (“Correctness-Aware KD”) has no explanatory main-text sentence. `tasks/condense.md` specifically requires a mechanism sentence for MCD. | Add a concise mechanism sentence in §III or §V, or document a deliberate exception to the protected list. |

## Protected content check

PASS means the item remains in §I–§X; for named methods this checks for a mechanism sentence as well as the method's presence. Locations are the condensed paper.

| Protected item | Result | Evidence |
|---|---|---|
| §I scope and fixed inclusion criteria | PASS | `paper/survey/sections/01_intro.tex:25-37` |
| I1–I3 and E1–E7 | PASS | `paper/survey/sections/01_intro.tex:25-37` |
| Search counts 2,193 / 445 / 310 / 112 | PASS | `paper/survey/sections/01_intro.tex:39-45` |
| Table I / survey comparison | PASS | `paper/survey/sections/01_intro.tex:64-102` |
| Taxonomy figure | PASS | `paper/survey/sections/01_intro.tex:104-111` |
| Four contributions | PASS | `paper/survey/sections/01_intro.tex:53-62` |
| KD | PASS | `paper/survey/sections/02_prelim.tex:20-32,74-86` — softened teacher distribution plus label loss; temperature exposes class relations |
| DKD | PASS | `paper/survey/sections/03a_logit.tex:16-18` — decouples target and non-target terms |
| MLKD | PASS | `paper/survey/sections/03a_logit.tex:35` — aligns instance, batch and class predictions with temperature augmentation |
| LSKD | PASS | `paper/survey/sections/03a_logit.tex:28` — per-sample logit standardisation |
| CTKD | PASS | `paper/survey/sections/03a_logit.tex:28` — adversarially learned curriculum temperature |
| VRM | PASS | `paper/survey/sections/03b_feature.tex:25` — real/virtual sample affinity graph with unreliable-edge pruning |
| SKD | PASS | `paper/survey/sections/03a_logit.tex:39` — batch Gram-matrix alignment |
| GDKD | PASS | `paper/survey/sections/03a_logit.tex:21` — partitions teacher top classes from the rest |
| EA-KD | PASS | `paper/survey/sections/03a_logit.tex:39` — entropy-based sample weighting |
| RLD | PASS | `paper/survey/sections/03a_logit.tex:39` — label-conditioned masking/refinement prevents copying a wrong top ranking |
| MCD | **FAIL** | `paper/survey/sections/08_benchmarks.tex:82,120`; `paper/survey/sections/11_appendix_methods.tex:65` — table-only, no mechanism sentence |
| LumiNet (ECE source) | PASS | `paper/survey/sections/03a_logit.tex:30` — batch-statistic logit normalisation and ECE comparison |
| SimKD | PASS | `paper/survey/sections/03b_feature.tex:12` — project student penultimate feature and reuse frozen teacher head |
| ReviewKD | PASS | `paper/survey/sections/03b_feature.tex:12` — aggregate multi-stage teacher features into student-stage review representations |
| CRD | PASS | `paper/survey/sections/03b_feature.tex:25` — contrast same-example teacher/student match against negatives |
| TopoKD | PASS | `paper/survey/sections/03b_feature.tex:25` — transfers feature topology through persistence diagrams |
| Projector study (`miles2024projector`) | PASS | `paper/survey/sections/03b_feature.tex:12` — reports projector confounds and recommends projector-only ablations |
| SRD | PASS | `paper/survey/sections/03b_feature.tex:12` — classifier-mediated representation matching with unlabeled data |
| DIST / DIST+ | PASS | `paper/survey/sections/03a_logit.tex:35`; `paper/survey/sections/08_benchmarks.tex:88` — Pearson correlation divergence; DIST+ adds a feature loss (benchmark table flag) |
| §IV schemes | PASS | `paper/survey/sections/04_schemes.tex:8-20` — offline, online, self, multi-teacher, assistant, augmented-view and data-free mechanisms retained |
| §V teacher reliability and gating motivation | PASS | `paper/survey/sections/05_reliability.tex:7-24` — correctness/confidence/usefulness distinctions, gates, repairs, selection and limitations retained |
| §VI-B DTO-KD, DOT, DeepKD, SCKD, SCOPE, TPKD, PCD | PASS | `paper/survey/sections/06b_kd_moo.tex:33-104,108-121` — each mechanism is described; PCD explicitly has no KD evaluation and is framed neutrally |
| §VI-A scalarisation, MGDA, PCGrad, CAGrad | PASS | `paper/survey/sections/06a_moo.tex:22-64` |
| Tuned-scalarisation studies | PASS | `paper/survey/sections/06b_kd_moo.tex:162-173` — Xin, Kurin and Royer cited; one sentence each |
| Other MOO methods grouped | PASS | `paper/survey/sections/06a_moo.tex:65-69` |
| §VIII protocol caveats, comparability and comparison logic | PASS | `paper/survey/sections/08_benchmarks.tex:14-34,40-58` |
| DeepKD camera-ready 79.25 / 78.42 / 73.34 / 74.85 | PASS | `paper/survey/sections/08_benchmarks.tex:42-58`; `paper/survey/sections/11_appendix_methods.tex:27` |
| §IX evidence-backed challenges and restored Yuan/Stanton/Beyer claims | PASS | `paper/survey/sections/09_future.tex:8-20`; restored claims at lines 12-13 |

## Number and appendix checks

- All accuracy values found in the condensed sections and appendix were present in the full paper or search records. DeepKD's four headline values (79.25 / 78.42 / 73.34 / 74.85) already occur in the full version at `paper/survey/sections/08_benchmarks.tex:45,157-158,170`; 77.03 remains as the separate KD+DeepKD result in `paper/survey/sections/06b_kd_moo.tex:160`. A numeric-token scan also found `0.75` absent from the full/search corpus, but its only occurrence is a figure resize fraction (`paper/survey/sections/02_prelim.tex:37`), not an accuracy. This is not an accuracy change.
- Accuracy values removed from main text were checked against the appendix and prose. The EKD teacher value **79.53** is the identified value that disappeared from the paper entirely; it is absent from the search markdown too.
- The appendix contains 112 distinct citation keys, and every key was found in at least one citation in the survey TeX. This matches the 112 included methods listed across `docs/survey/search/README.md` and `manual-pdfs.md`.

## Preservation-map sample

Sampled 24 mapped claims across the four requested maps; each sampled target still states the mapped claim in prose or a table. Examples: T8 output/feature/relational distinctions (`docs/reviews/survey-t8-preservation.md:16-20` → `paper/survey/sections/02_prelim.tex:74-86`, `03b_feature.tex:12,25`); T9 correctness-vs-confidence, label errors, hard gate, CA-MKD, LR-DS, RLD, CHAD and calibration limits (`docs/reviews/survey-t9.md:7-18` → `paper/survey/sections/05_reliability.tex:7-15,22-24`); T11 PCGrad, CAGrad, SCKD, DTO-KD, SCOPE, TPKD and PCD (`docs/reviews/survey-t11.md:26-68` → `paper/survey/sections/06a_moo.tex:47-64`, `06b_kd_moo.tex:33-104`); T16 restored Yuan, Stanton and Beyer claims (`docs/reviews/survey-t16-audit.md:57-66` → `paper/survey/sections/09_future.tex:8-13`). No sampled mapped claim was missing.

## Prose and references

- No broken prose sentences or dangling references to removed numbered tables/figures were found in the inspected sections. The remaining numbered “Table 4” / “Table 5” mentions are primary-source citations in comments, not cross-references to deleted survey tables (`06b_kd_moo.tex:94,119,173`; `08_benchmarks.tex:5`). Survey cross-references resolve to defined labels in the TeX source.
- The malformed benchmark headers above are the only clear humanizer/formatting failure found in this pass. No stylistic rewrites are recommended.

## Counts

- Protected checks: 33 PASS, 1 FAIL (MCD mechanism sentence).
- Number check: no changed accuracy found; 1 accuracy value disappeared entirely (79.53).
- Included methods cited: 112/112.
- Preservation sample: 24/24 claims present.
- Critical findings: 1; major findings: 2.
- Broken prose/dangling survey references: 0 found; malformed table headers: 2.
