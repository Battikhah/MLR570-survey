# T16 final audit of the survey

Scope: `paper/survey/main.tex` and `sections/01`–`10`. Auditor: Claude (Orca task task_c645540df8ac), 2026-11-08.

## Checklist

| # | Check | Result | Evidence |
|---|---|---|---|
| 1a | Every `\cite` key exists in `literature/sources.yaml` | PASS | 187 cited keys, 0 missing; `uv run python scripts/build_bib.py --check` prints "citation check OK", exit 0 |
| 1b | Every cited record has `verified_by` | PASS | 0 cited records lack it |
| 1c | No unverified record carries a number | PASS | Only cited unverified record is `xue2024caat` (CA-AT). Its single use, `07_emerging.tex:10`, carries no number and says "its record remains an unverified preprint" |
| 1d | Unused registry records (not deleted) | INFO | 47 before the fix, 44 after (see below) |
| 2 | Accuracies match §VIII or primary source | PASS | Automatic check of all 277 two-decimal numbers in main.tex and §I–VII, IX, X: 248 appear in `08_benchmarks.tex` or `docs/survey/*.md`. The other 29 were each checked against the primary PDF or an earlier review (table below) |
| 3 | Guidelines G1–G11 | PASS (11/11) | see G table |
| 4 | Draft preservation | PASS after fix | see section 4 |
| 5 | Consistency | PASS | 0 undefined refs/cites; all 12 section files keep the `% Owner:` header on line 1; no "[To be written" / TODO in the text (the only `XXXX` is the TMLR template's unused `\openreview` macro, `main.tex:23`) |
| 5b | No PCD over-weighting | PASS, one flag | 21 "PCD" mentions: §VI-A 6, §VI-B 8, §IX 3, §I/§VIII/§X 1 each. Intro and conclusion present it as one option among gradient rules with no numbers |
| 6 | Style | PASS | 0 hits for delve/crucial/landscape/notably/pivotal/tapestry/groundbreaking/remarkable/cutting-edge; 0 `---` em-dashes outside comments. "state-of-the-art" appears only as the scope term |
| 7 | Clean build | PASS | `latexmk` exit 0; 0 undefined citations/references; one overfull hbox of 4.3pt (< 10pt); "Float too large" warning fixed; **54 pages** |

### Numbers not in §VIII, checked at the source (29)

| Location | Numbers | Source checked |
|---|---|---|
| 02_prelim:140, 03a:66 | 73.70, 75.09 | LDRLD arXiv 2507.15911 text |
| 03a:11 | 75.51, 75.63 | DKD arXiv 2203.08679 text |
| 03a:60,66,363 | 76.63, 75.92 | `survey-t5t6-codex.md`; 75.92 also in EKD CVF PDF |
| 03a:102–103,369 | 51.08, 27.21, 46.11, 13.25 | `survey-t5t6-codex.md` (LTKD Table 1) |
| 03a:150 | 77.01 | `phase7-codex-reviews-claude.md` |
| 03a:231 | 72.54 | EKD ICCV 2025 CVF PDF |
| 03b:32 | 32.71, 61.07 | `survey-t7t8-claude.md` |
| 06b:128–130,228 | 87.58, 87.81, 87.83, 93.83, 93.81 | TPKD arXiv 2609.39338 text |
| 06b:158–159 | 73.66, 73.56 | DOT arXiv 2307.08436 text |
| 06b:162,225 | 77.03 | DeepKD arXiv 2505.15133 text (v1; camera-ready not compared, as already noted in `survey-t11.md`) |
| 06b:178,229 | 80.54, 81.80 | MEMA source arXiv 2606.24557 text |

Check was string presence in the extracted text, not a re-read of each table row's context.

## G1–G11

| G | Result | Evidence |
|---|---|---|
| G1 title | PASS | `main.tex:13` names the topic, task and years |
| G2 abstract | PASS | motivation, contributions, structure, trends (aligned in T15, commit 18ae3b4) |
| G3 problem/importance/trends | PASS | §I opening and "Motivation and gap" (`01_intro.tex:17`) |
| G4 motivation and gaps | PASS | `01_intro.tex:17` |
| G5 scope, categories, outline | PASS | "Scope and inclusion criteria" :28, "Taxonomy" :51, "Organisation" :67 |
| G6 method comparisons | PASS | comparison paragraphs per section, e.g. "Comparing reliability signals" `05_reliability.tex:39`; comparison tables |
| G7 visual aids | PASS | 3 figures (taxonomy, gradient-rule diagrams) and 11 tables |
| G8 strengths/weaknesses/applicability | PASS | per-method limitations in §III–VI; applicability paragraph `05_reliability.tex:42` |
| G9 future directions from gaps | PASS | §IX, 7 paragraphs each ending in a "Direction:" tied to a cited gap |
| G10 conclusion | PASS | §X |
| G11 references | PASS | natbib author-year with `tmlr.bst` throughout (per `tasks/plan.md:62`); 187 verified registry records |

## 4. Draft preservation

Claim maps cover the draft (`Project Files/Current_Survey.md`) as follows: L12–34 `survey-t8-preservation.md`; L36–106 `survey-t9.md`; L108–187 `survey-t11.md`. The rest was checked here:

| Draft lines | Claim | New location |
|---|---|---|
| L1, L3 | Title, authors | Title replaced by a more specific one (G1); author block is a human decision |
| L7 | "The abstract goes here." | Placeholder; replaced by the T15 abstract |
| L8 | Keywords | Topics are covered in the abstract and §I; TMLR template has no keyword field |
| L191 | Rejection may discard useful info; RLD and label revision repair instead | §V, `05_reliability.tex:23,25` |
| L192 | Teacher accuracy is not transfer utility (Yuan et al. CVPR 2020) | **was missing**; restored in §IX "Which teacher signal to trust", `\citet{yuan2020labelkd}` |
| L193 | Imitation and generalisation differ (Stanton et al. NeurIPS 2021) | **was missing**; restored in the same paragraph, `\citet{stanton2021kdwork}` |
| L194 | Recipe choices change conclusions (Beyer et al. CVPR 2022) | **was missing**; restored in §IX "A comparable leaderboard", `\citet{beyer2022patientkd}` |

## Fixes made

1. `09_future.tex`: restored the three dropped draft claims (L192–194) with their original, verified citations.
2. `03b_feature.tex:71`: feature-KD comparison table `\small` → `\footnotesize`; removes "Float too large for page by 53.5pt".

## Unused registry records (44, kept)

acar2021feddyn, agarwal2018reductions, agarwal2024gkd, askin2026fedrevive, chamon2020pacc, chaudhry2019tiny, cotter2019twoplayer, deng2022pebkd, farajtabar2019ogd, gallegoposada2025cooper, goldblum2020ard, hu2020softgem, hu2022fedmgda, huang2023adaad, irshaid2026fedpcd, jang2025vl2lite, jiang2024gaqat, jung2024peeraid, karimireddy2020scaffold, khan2024hydrafl, ko2024distillm, ko2025distillm2, lee2025igdm, lee2025saad, li2020fedprox, li2020qffl, li2021ditto, li2024promptkd, lin2019paretomtl, lin2020feddf, lin2022randomweighting, liu2021imtl, lu2025ciard, mcmahan2017fedavg, mohri2019afl, sagawa2020groupdro, senushkin2023alignedmtl, skalse2022lmorl, wang2020fednova, wang2021fedfv, wu2023tinyclip, zhang2019trades, zhu2021fedgen, zi2021rslad

## For humans

- Author block and whether to keep the draft's keyword list.
- `08_benchmarks.tex:330` calls methods "the direct rivals of the project's PCD optimiser". This is the only project framing left in the body; decide whether a survey reader should see it.
- Open items carried over from `survey-t11.md`: FAMO venue, SCOPE full text (MDPI 403), DeepKD camera-ready vs arXiv v1.
- Read the restored §IX sentences against Yuan/Stanton/Beyer once more; their wording follows the draft bullets.
- Page count 54, relevant if the instructor sets a length limit.
- No Codex cross-review of this audit has run yet (`tasks/todo.md` T16 asks for one).
