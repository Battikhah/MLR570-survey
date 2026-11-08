# T16 audit cross-review (Codex)

Read-only review of the T16 audit and current survey files, 2026-11-08. No network access used. Findings below are limited to claims checked in this sample.

## Number sample: 15/15 matched

Compared each cited survey value to `docs/survey/search/*.md` or the local survey benchmark inventory, per the T16 audit's match criterion. All values and method/configuration descriptions matched:

| Survey location | Values checked | Local corroboration |
|---|---|---|
| `paper/survey/sections/04_schemes.tex:33` | TeKAP 77.36; Angular-KD 77.28; SAKD 77.31 | `docs/survey/search/s2-ml.md:82,77,99` and `docs/survey/search/s3-aaai-journals-arxiv-snowball.md:98,111` identify the same stacked MLKD configurations and scores. |
| `paper/survey/sections/04_schemes.tex:34` | CutMixPick 76.11; KCD 74.05 and 76.48; KD³ 73.17 | `docs/survey/search/spotcheck-codex.md:18`, `docs/survey/search/s1-cvf.md:72,94` corroborate the scores and configurations. |
| `paper/survey/sections/04_schemes.tex:36` | FastDFKD 65.12; MAD 64.05; SpaceshipNet 69.95; RGAL 69.71; CPNet 71.90; DFND+KDCI 74.52 | `docs/survey/search/s3-aaai-journals-arxiv-snowball.md:83,92`; `docs/survey/search/s2-ml.md:89`; `docs/survey/search/s1-cvf.md:89,91,92` match values and WRN-40-2→WRN-16-2 protocol. |
| `paper/survey/sections/06b_kd_moo.tex:157-162` | KD+DOT 75.12 | `docs/survey/search/spotcheck-codex.md:16` and `docs/survey/sota-inventory.md:152` verify the same CIFAR-100 pair/configuration. |
| `paper/survey/sections/06b_kd_moo.tex:178-181` | OFA 80.54 | `docs/survey/sota-inventory.md:154` corroborates the baseline and Swin-T→ResNet18 protocol. |

## Restored draft claims: 3/3 supported

- **Yuan 2020 — supported.** The sentence at `paper/survey/sections/09_future.tex:48` says poorly trained and reversed teachers can yield gains. This tracks the original draft bullet at `Project Files/Current_Survey.md:192` and the registry relevance at `literature/sources.yaml:1031` (weak teachers can still help; counterexample to equating weakness with uselessness).
- **Stanton 2021 — supported.** The same sentence says fidelity and generalisation need not improve together and KD loss is not itself evidence of student utility. The original bullet at `Project Files/Current_Survey.md:193` and registry relevance at `literature/sources.yaml:1046` support that interpretation.
- **Beyer 2022 — supported.** `paper/survey/sections/09_future.tex:20` says training length and consistent teacher/student views are consequential. This matches the original bullet at `Project Files/Current_Survey.md:194` and registry relevance at `literature/sources.yaml:1064`.

## G1–G11 spot-check: 5/5 supported

- **G1, title:** `paper/survey/main.tex:13-14` identifies KD, image classification, the years, and survey scope.
- **G2, abstract:** `paper/survey/main.tex:28-40` includes motivation/scope, search and method-set contribution, organisation, benchmark trends, and limitations of cross-paper comparisons.
- **G5, scope/categories/outline:** `paper/survey/sections/01_intro.tex:28-40` gives inclusion criteria and families and points to later sections; the outline continues after this excerpt.
- **G9, future directions:** `paper/survey/sections/09_future.tex:8-10` states that each paragraph ties a question to survey evidence and ends in a testable direction; e.g. `:15-25` grounds a controlled leaderboard rerun in identified protocol gaps.
- **G11, references:** `paper/survey/main.tex:16-19` has author/institution attribution and `main.tex` uses the TMLR author-year citation setup; the numbered references are produced by the bibliography configuration. Formatting consistency is supported, though the TBD email fields remain a human completion item.

## Project framing

**M (minor), `paper/survey/sections/09_future.tex:60`:** “The project's PCD optimiser” is project-specific framing in the body. The T16 audit's “only project framing” flag is accurate. Replace with a survey-centered form such as “PCD \\citep{varam2026pcd} has no reported distillation result…” The requested literal grep terms `our project`, `the project`, and `we propose` produce no other body hits; the apostrophe form above is why the exact phrase scan alone misses this instance.

## Summary

Verified 15 numeric claims, 3 restored claims, and 5 guideline verdict samples. One minor project-framing correction remains. No other issue was verified in this bounded sample.
