# Codex cross-review: T5 and T6

Reviewed `git diff d883f73..HEAD` on 2026-11-07. Scope: §II, Fig. 2, §III-A, Table II, and related registry/bibliography records. Severity labels: High = blocks acceptance; Medium = material correction or coverage gap; Low = polish or qualification.

## Findings

| ID | Severity | Verdict | Evidence | Recommended fix |
|---|---|---|---|---|
| F1 | Medium | DISAGREE | LumiNet is registered as a 2025 TMLR paper, but `literature/sources.yaml` gives its arXiv first-posted date `2023-10-05`; generated `paper/survey/refs.bib:336-344` therefore has `year = {2023}`. With the author-year TMLR bibliography style, its in-text citation renders as 2023 while Table II says TMLR 2025 (§III-A: `paper/survey/sections/03a_logit.tex:255`). | Set the bibliography year used for published citations to 2025, retaining the 2023 preprint date in a separate field if needed; regenerate and inspect the rendered citation. |
| F2 | Medium | DISAGREE | The inventory lists LTKD as a published 2026 CVPR CORE logit method (`docs/survey/sota-inventory.md:77` and `literature/sources.yaml:170-183`), but §III-A and Table II omit it. The section otherwise claims state-of-the-art coverage and the plan criterion spans 2022–2026 (`tasks/plan.md`, “State-of-the-art criterion”). | Add LTKD with a brief mechanism/limitation and sourced table entry, or explicitly delimit this subsection's coverage and explain the omission. |
| F3 | Medium | DISAGREE | The opening generalization says logit methods transfer only output-layer knowledge and cost little more than student-only training (`paper/survey/sections/03a_logit.tex:9-11`), then says the post-2022 gap was closed “without touching features” (`:16`). SDD explicitly pools teacher/student final feature maps to create local logits (`:57-66`; primary paper, Table 6/ablation), and WKD-L estimates a feature-space category-relation cost matrix (`:181-186`; primary paper, §3 and Tables 5, 11). These methods do not fit the blanket cost/feature-free description. | Scope the introductory claim to conventional output-only methods, then identify SDD and WKD-L as logit-supervised methods that also read intermediate features or incur added computation. |
| F4 | Low | DISAGREE | The caption says values are “as reported by each method's own paper” (`paper/survey/sections/03a_logit.tex:234-237`), yet the CTKD cell is explicitly a KD+CTKD reproduction from LSKD Table 2 (`:248`, `:262-264`), not CTKD's own reported value for this pair. The cell is transparent, but the caption overstates provenance. | Change the caption to say each value is reported in the source table named in its cell; identify reproductions separately. |
| F5 | Low | DISAGREE | §II says soft-target gradients scale as `1/T²` without limiting this statement (`paper/survey/sections/02_prelim.tex:85-87`). Hinton's `T²` compensation follows the high-temperature approximation; the exact per-logit derivative shown immediately above at `:54-59` is `(p_s^T-p_t^T)/T`, and its scaling depends on the softened distributions. | Qualify the `1/T²` scaling as an approximate/high-temperature result. |
| F6 | Low | DISAGREE | The alternative convex-combination objective “differs only by a rescaling of the learning rate” (`paper/survey/sections/02_prelim.tex:33-35`). Algebraically this is true for plain SGD when the whole objective is multiplied by a constant; it is not generally optimizer-invariant (e.g., Adam, weight decay, clipping). | Say it is equivalent up to a global scale for plain SGD, or omit the optimizer-wide claim. |
| F7 | Low | DISAGREE | Paragraph §III-A’s comparison/outlook uses an explicit “First / Second / Third” cadence and concludes with a broad practitioner recommendation (`paper/survey/sections/03a_logit.tex:219-230`), which reads formulaic and project-prescriptive for a survey. The sentence “For a practitioner … the default we would try first” also uses an unattributed “we.” | Replace with a compact synthesis tied to observed evidence, e.g. “Across these papers, standardisation combines with both decoupling and multi-level losses; reported scores overlap across reproductions, so the table does not establish a single best method. DKD and KD+LSKD are low-overhead baselines; MLKD+LSKD reports the highest value here but adds loss terms and temperatures.” |

## Table II row checks

All extracted values and venues below AGREE with the primary paper PDFs in `literature/pdfs/`, except PLD, which has no number in the table and is explicitly marked “not extracted.” The cited PDF tables/sections are the evidence locations; `pdftotext -layout` was used to read the tables.

| Table II row | Verdict | Primary-source evidence |
|---|---|---|
| KD | AGREE | Hinton et al., *Distilling the Knowledge in a Neural Network*, workshop paper metadata: NIPS 2014 DL Workshop; comparative baseline 73.33 in DKD PDF, Table 6 (R32×4→R8×4). arXiv first-posted 2015 explains parenthetical. |
| DKD | AGREE | `literature/pdfs/dkd.pdf`, Table 6: 76.32 (KD 73.33); CVPR 2022. |
| DIST | AGREE | `literature/pdfs/dist.pdf`, Table 5: 76.31; NeurIPS 2022. |
| CTKD | AGREE | No R32×4→R8×4 result in CTKD's own relevant CIFAR table; `literature/pdfs/lskd.pdf`, Table 2 reports KD+CTKD 73.39 on the reference pair. Cell labels this as a reproduction and `n/r` for CTKD's own result. Venue AAAI 2023. |
| MLKD | AGREE | `literature/pdfs/mlkd.pdf`, Table 2: 77.08; CVPR 2023. |
| NKD | AGREE | `literature/pdfs/nkd.pdf`, Table 1: 76.35 on CIFAR-100 and 71.96 ImageNet R34→R18; ICCV 2023. |
| WTTM | AGREE | `literature/pdfs/wttm.pdf`, Table 2: 76.06; ICLR 2024. |
| LSKD | AGREE | `literature/pdfs/lskd.pdf`, Table 2: KD+LS 76.62 and MLKD+LS 78.28; CVPR 2024. |
| SDD | AGREE | `literature/pdfs/sdd.pdf`, Table 6: Fusion/SD-KD 76.63 (ablation); CVPR 2024. |
| WKD | AGREE | `literature/pdfs/wkd.pdf`, Appendix Table 11: WKD-L 76.53; NeurIPS 2024. |
| LumiNet | AGREE | `literature/pdfs/luminet.pdf`, Table 1: 77.50 averaged over five runs; TMLR 2025. Venue/date citation rendering issue is F1. |
| RLD | AGREE | `literature/pdfs/rld.pdf`, Table 1: 76.64; ICCV 2025. |
| LDRLD | AGREE | `literature/pdfs/ldrld.pdf`, Table 1: 77.20; ICCV 2025. |
| EKD | AGREE | `literature/pdfs/ekd.pdf`, Table 1: 77.21; ICCV 2025. |
| PLD | AGREE (no number asserted) | Official NeurIPS 2025 abstract page is the cited source; no benchmark value is given in Table II. Registry marks the text's mechanism claims as abstract-only. |

The table's other associated figures also checked: LumiNet ECE 0.06 vs KD 0.11 (`luminet.pdf`, Table 5); SDD ImageNet SD-NKD 72.33 / SD-DKD 72.02 (`sdd.pdf`, Table 3); LDRLD comparison values 75.09 for SDD and 76.16 for LSKD (`ldrld.pdf`, Table 1); EKD SDD reproduction 75.92 (`ekd.pdf`, Table 1); RLD's DKD comparator 76.32 (`rld.pdf`, Table 1); WKD ImageNet WKD-L 72.49 (`wkd.pdf`, Table 4); WTTM ImageNet 72.19 (`wttm.pdf`, Table 5); and CTKD ImageNet comparisons (`ctkd.pdf`, Table 4). Code repository URLs were not independently opened in this review.

## Mechanism spot checks

| Claim | Verdict | Evidence |
|---|---|---|
| DKD splits target-class and non-target logits; weights terms separately | AGREE | DKD PDF, Eqs. 5–7 and ablation/Table 6. |
| NKD normalizes non-target distributions; USKD uses customized soft labels | AGREE | NKD PDF, method section and Table 1; separate USKD section. |
| CTKD adversarially learns temperature with gradient reversal/curriculum | AGREE | CTKD PDF, method equations and curriculum description; Tables 1/4. |
| WTTM transforms teacher only and weights samples using transformed-distribution power sum | AGREE | WTTM PDF, method equations; Tables 1–2. |
| LSKD z-score standardizes logits per sample before softmax and plugs into other logit losses | AGREE | LSKD PDF, method section and Table 2. |
| DIST uses inter-class and intra-class Pearson correlation | AGREE | DIST PDF, method section and Table 10 ablation. |
| MLKD aligns instance, batch, and class levels with multiple-temperature predictions | AGREE | MLKD PDF, method section, Table 2 and ablation Table 6. |
| SDD pools multi-scale feature maps into local logits and separates consistent/complementary terms | AGREE | SDD PDF, method section and Table 6. This also supports F3. |
| WKD-L uses a discrete Wasserstein metric over category relations | AGREE | WKD PDF, method section and Appendix Table 11. |
| LumiNet normalizes class logits using intra-batch statistics | AGREE | LumiNet PDF, method section and Table 1. |
| RLD uses confidence and masked correlation to suppress teacher-ranked classes at/above the label | AGREE | RLD PDF, method equations and ablation Table 6. |
| LDRLD builds adaptive dense pairwise class relations | AGREE | LDRLD PDF, method section and Table 1. |
| EKD distils evidential/Dirichlet outputs | AGREE | EKD PDF, method section and Table 1. |
| PLD's full mechanism properties | UNSUPPORTED beyond author abstract | Full text was not available in the local source set; the section discloses abstract-only verification at `03a_logit.tex:201-203`. |

## T5, citations, and guideline fit

- The Hinton CE + `T² KL` objective and both parameter-gradient expressions are algebraically consistent with the defined softened softmax (`02_prelim.tex:29-30, 53-69`). `g_CE` and `g_KD` are separate objective gradients and their weighted sum matches the later MOO framing. Fig. 2 routes the shared input to a frozen teacher/student, applies `T` only to KL branches and sends gradients to student parameters; this matches the prose and caption. No substantive equation or diagram error found beyond F5/F6 qualifications.
- Every citation in the two sections resolves through `literature/sources.yaml`; the cited records have `verified_by` trails, and there are no cited `status: unverified` records in these sections. The build-bib check passed. PLD text explicitly bounds verification to the abstract. LumiNet year rendering is F1.
- G6 comparisons are explicit in the DKD/NKD, CTKD/LSKD, DIST/LSKD, and broader summary comparisons. G8 limitations/applicability appear for DKD, LDRLD, CTKD, SDD, WTTM, LSKD, DIST, WKD, EKD, and PLD. Main weakness is the inconsistent subsection boundary for feature-using SDD/WKD (F3), not a lack of comparisons. T6 includes 2022–2025 methods but omits inventory CORE LTKD (F2).
- The “First / Second / Third” triad and broad closing recommendation are the remaining machine-sounding/project-prescriptive passage (F7). The rest reads like method-focused survey prose; no other stock paragraph-ending summaries flagged.

## Checks run

| Check | Result |
|---|---|
| `cd paper/survey && latexmk -interaction=nonstopmode` | Exit 0; latexmk reported target up-to-date. Existing PDF metadata: 12 pages. This invocation did not force a rebuild. |
| `uv run --frozen --offline python scripts/build_bib.py --check` | Initial exact invocation failed before execution because `/Users/khalidhamdan/.cache/uv` was not accessible (exit 2). With `UV_CACHE_DIR=/private/tmp/uv-cache-review`, check passed: “wrote paper/survey/refs.bib (160 entries); citation check OK.” |
| `uv run --frozen --offline pytest -q -m "not slow and not requires_data"` | Initial exact invocation failed for the same uv cache permission (exit 2). With the temporary cache override: 212 passed, 1 skipped (MPS unavailable), exit 0. |

No section files were edited. `build_bib.py --check` regenerated `refs.bib`, but `git status --short` remained clean after the run.

## Response (Claude, cycle 1)

| ID | Status | Change / evidence |
|---|---|---|
| F1 | FIXED | Added an optional registry field `year` (venue year) used by `scripts/build_bib.py` before `date`; documented in `literature/README.md`; unit test `test_year_field_overrides_date_for_citation_year` in `tests/unit/test_build_bib.py`. Applied to the cited records with an arXiv-vs-venue mismatch: `hossain2025luminet` (2025), `li2023ctkd` (2023), `sun2025rld` (2025), `tian2020crd` (2020). Rendered PDF now shows "Hossain et al., 2025". `hinton2015kd` left at 2015 (arXiv; workshop has no proceedings). Uncited records with the same mismatch, not changed: agarwal2024gkd, askin2026fedrevive, chaudhry2019agem, chen2018gradnorm, goldblum2020ard, gu2024minillm, hu2022fedmgda, hu2024tgeokd, jeong2025selfdistill, kang2025dho, karimireddy2020scaffold, kendall2018uncertainty, kenfack2025agrekd, lee2025igdm, li2020fedprox, li2020qffl, li2021ditto, mcmahan2017fedavg, miles2024projector, mirzadeh2020takd, qiu2023dpk, romero2015fitnets, shin2026amid, su2025eakd, tran2024nayer, yang2023lmcl, yang2024clipkd, zhang2022camkd, zhou2025tcs (section owners should add `year` when they cite them). |
| F2 | FIXED | LTKD paragraph added to §III-A (decoupling subsection) and a Table II row. Read arXiv 2506.18496v2: it evaluates only long-tailed benchmarks, so the balanced cell is n/r; the row gives CIFAR-100-LT γ=100 R32×4→R8×4 overall 51.08 (Table 1; DKD 46.11). The PDF lists a single author (Seonghak Kim), consistent with the registry. |
| F3 | FIXED | Opening paragraph scoped to "conventional output-only form" and names SDD (local logits from final feature maps) and WKD-L (feature-space cost matrix) as logit-supervised methods that read features and add compute; "without touching features" replaced. |
| F4 | FIXED | Caption now says each value comes from the source table named in its cell, with another paper's name marking a reproduction. |
| F5 | FIXED | §II now says the 1/T² scaling holds in the high-temperature approximation (Hinton et al.). |
| F6 | FIXED | Equivalence restricted to plain SGD; Adam, weight decay and clipping explicitly excluded. |
| F7 | FIXED | First/Second/Third cadence and "we would try first" removed; replaced with a synthesis tied to cited evidence (LSKD Table 2, SDD, cross-paper spread, EKD/LDRLD re-reports). |

Checks after the fix (all exit 0): `latexmk` (undefined = 0, overfull = 0), `build_bib.py --check` (160 entries, OK), `build_literature_docs.py`, `ruff check .`, `pytest -q -m "not slow and not requires_data"` (214 passed), `check_repo_hygiene.py`.

## Cycle 2 verdict (Codex)

Reviewed `git diff a4601e2..b314f6f`. All seven findings are **CONFIRMED fixed**; no unresolved disagreement remains.

| Finding | Verdict | Cycle 2 evidence |
|---|---|---|
| F1 LumiNet venue year | CONFIRMED | `sources.yaml` now sets optional `year: 2025` for LumiNet (while retaining `date: 2023-10-05`); `build_bib.py:53` prefers `year` and falls back to `date`. The unit test `test_year_field_overrides_date_for_citation_year` checks both override and fallback. Generated `refs.bib` changes only four years: LumiNet 2025, CTKD 2023, RLD 2025, and CRD 2020, each matching its registry venue. Extracted rendered PDF text confirms Hossain 2025, Li 2023, Sun/RLD 2025, and Tian/CRD 2020. No unexpected rendered citation-year change found. |
| F2 LTKD coverage | CONFIRMED | New paragraph and Table II row are present in `03a_logit.tex:80-93,269`. [arXiv v2 Table 1](https://arxiv.org/pdf/2506.18496v2) (PDF p. 5) columns for ResNet32×4→ResNet8×4, γ=100 report LTKD tail/overall 27.21/51.08 and DKD 13.25/46.11; `03a_logit.tex:86-88` reports these correctly. The row labels the long-tailed setting and marks the balanced CIFAR-100 value n/r. Mechanism (cross-group rebalancing and equalized within-group contribution) matches arXiv v2 abstract and Eqs. 10–14. |
| F3 output-only/cost scope | CONFIRMED | `03a_logit.tex:9-17` limits the projector/cost claim to conventional output-only methods, names SDD and WKD-L as feature-reading exceptions, and removes “without touching features.” |
| F4 table provenance | CONFIRMED | Caption at `03a_logit.tex:249-252` now says the cited cell source is authoritative and explicitly marks other-paper reproductions. |
| F5 temperature scaling | CONFIRMED | `02_prelim.tex:85-87` qualifies the 1/T² scaling as a high-temperature approximation. |
| F6 convex-combination scaling | CONFIRMED | `02_prelim.tex:33-35` restricts learning-rate equivalence to plain SGD and notes adaptive optimizers, weight decay, and clipping. |
| F7 prose cadence | CONFIRMED | `03a_logit.tex:227-239` replaces the numbered triad and “we would try first” with a sourced synthesis; no formulaic triad remains there. |

The required cycle 2 checks were rerun. `cd paper/survey && latexmk -interaction=nonstopmode`: exit 0, target already up to date; `paper/survey/build/main.log` has no undefined-reference or overfull-box entries. `UV_CACHE_DIR=/private/tmp/uv-cache-review uv run --frozen --offline python scripts/build_bib.py --check`: exit 0, 160 entries, citation check OK. `UV_CACHE_DIR=/private/tmp/uv-cache-review uv run --frozen --offline pytest -q -m "not slow and not requires_data"`: exit 0, 213 passed, 1 skipped (MPS unavailable). The requested diff also changes `paper/survey/sections/02_prelim.tex` and `03a_logit.tex`; this cycle did not edit them. No unresolved issues to escalate from this review.
