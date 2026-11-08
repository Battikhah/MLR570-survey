# T13 review — Codex

Reviewed commit `cda3870` read-only, except this report. Evidence was checked against the search logs and registry decisions; the requested sampled numerical checks found no mismatches.

## Findings

### m — Keep DeepKD's leaderboard position explicitly descriptive

**Location:** `paper/survey/sections/08_benchmarks.tex:46-50,63,325-327`; `docs/project/comparison-set.md:21-23`.

**Evidence:** `docs/survey/search/s2-ml.md:95` reports CIFAR 79.25 for CRLD+DeepKD with top-k and separately 79.15 for MLKD+DeepKD. The table flags the row as stacked on CRLD, and nearby prose says stacked results measure combinations. Therefore 79.25 is supported and may lead a list of reported configurations, but it is not evidence DeepKD alone is the best optimizer or a like-for-like win over VRM/SKD. The comparison-set table does identify the stack, but calls it the “Highest reported number on the pair.”

**Fix:** Keep the reported score, but label the top position as the highest reported *configuration* and keep standalone-method rankings separate (or repeat this distinction beside the comparison-set wording). No number correction is warranted.

### m — Align the comparison-set's “strongest logit loss” wording with its actual candidate list

**Location:** `docs/project/comparison-set.md:8-11,32-35,44-46`.

**Evidence:** The CIFAR table lists LSKD as MLKD+LS at 78.28 (`paper/survey/sections/08_benchmarks.tex:67`), while the proposed arms say “DKD or MLKD” and the short list says “LSKD/MLKD.” S1 identifies the 78.28 result as MLKD+LS (`docs/survey/search/s1-cvf.md:63`). Thus the top-level experiment description and the shortlist do not name exactly the same stronger logit candidates.

**Fix:** State the intended loss arms consistently: for example, KD, DKD, MLKD, and MLKD+LS (LSKD), subject to implementation budget. Keep the paper-reported 78.28 separate from expected PCD results.

## Checks completed

- **Numerical spot-checks: 25 values; zero mismatches.** First 10 ranked CIFAR-100 R32x4→R8x4 rows: KD-AIF 82.20, DeepKD 79.25, VRM 78.76, EA-KD 78.38, SKD 78.33, LSKD 78.28, UniKD 78.18, NCKD 78.18, TopKD 78.18, SimKD 78.08 (`paper/survey/sections/08_benchmarks.tex:62-71`; corresponding search records in `docs/survey/search/s1-cvf.md:60-65` and `docs/survey/search/s2-ml.md:95`). Ten additional table values checked against search records: GDKD 77.76 (`s3-aaai-journals-arxiv-snowball.md:106`), MLKD 77.08 (`s1-cvf.md:69`), RLD 76.64 (`s1-cvf.md:71`), MCD 76.81 (`manual-pdfs.md:11`), DTO-KD 76.40 (`s2-ml.md:102`), DOT 75.12 (`s1-cvf.md:76`), DistPro WRN-pair 76.36 (`s1-cvf.md:83`), KDCI 74.52 (`s1-cvf.md:89`), NAYER 71.72 (`s1-cvf.md:90`), and FastDFKD 65.12 (`s3-aaai-journals-arxiv-snowball.md:83`). The comparison-set values KD 73.33, DKD 76.32, MLKD 77.08, LSKD 78.28, GDKD 77.76, SimKD 78.08, VRM 78.76, RLD 76.64 and MCD 76.81 are among these/source-verified values; MGDA and PCGrad are correctly marked as having no reported KD-pair score.
- **Coverage:** The prose and ranked tables cite the included benchmarked methods and the no-tabulated-number subsection cites VkD, SoTeacher, Bayesian teachers and ABKD (`08_benchmarks.tex:291-296`). Data-free inclusions are in a separate, explicitly non-comparable table (`:261-286`). No excluded or SUPPORT record was observed as a ranked row in the inspected tables; PCD is mentioned as out of scope and not ranked.
- **Flags:** Retried/updated teachers, label smoothing, extra epochs, multi-student, data-free and non-standard protocols have flags or adjacent explicit caveats (including KD-AIF, EA-KD/LSKD, MSE teacher, MC-Distil, data-free table, KD³, SRD and PLD). SHAKE's 72.07 row notes the 72.53 multi-teacher variant (`:220`).
- **Comparison logic:** Optimizer-side rivals include weighted sum/NWKD, MGDA, PCGrad, DOT, DTO-KD and DeepKD; DistPro is included as optional. Gated PCD is paired with the loss-side teacher-reliability comparators RLD and MCD (`comparison-set.md:39-40,52-53`). Among reviewed search records, the report includes the higher code-available single-method feature/logit candidates SimKD and GDKD alongside loss-side and optimizer-side rivals; no stronger code-available rival omission was verified from the checked evidence.
- **Writing:** The prose is paragraphs rather than bullet lists and contains none of “delve,” “crucial,” “landscape,” or “notably.” G6/G8 comparisons and applicability/limitations are present. G1–G5 and G9–G11 are paper-wide criteria, so this section alone cannot establish them; visual aid G7 is also outside this section's scope. No violation attributable to §VIII was verified.

## Counts

C: 0. M: 0. m: 2.
