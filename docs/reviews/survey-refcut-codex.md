# Reference-cut audit (Codex)

Audit target: `git diff survey-condensed-v1 HEAD -- paper/survey docs`; read-only review of the reference cut. No files other than this report were changed. Line numbers below refer to HEAD on 2026-11-08.

## Findings

| Severity | Location | Evidence | Fix |
|---|---|---|---|
| M | `paper/survey/sections/02_prelim.tex:119-120` | “CIFAR-100 is close to saturated as a KD benchmark” is labeled INTERPRETATION but states a recognizable paper-specific result. The removed version cited VkD (`miles2024vkd`); that citation is absent here, despite VkD (77.51 on a different CIFAR pair) appearing in `docs/survey/included-methods.md:116` and `docs/survey/search/s1-cvf.md:88`. | Restore `\citep{miles2024vkd}` on the saturation claim, or remove/recast the claim without implying a paper-specific finding. |
| M | `paper/survey/sections/04_schemes.tex:12-22` | Method-attributed assertions are uncited: online/mutual schemes' comparative scores and failure mode (line 12); self-distillation's mechanics and error recycling (line 14); multi-teacher adaptation (line 16); teacher-assistant evidence and examples beyond the cited Cho/DIST pair (line 18); augmented teacher views/data collection (line 20); and data-free synthesis details (line 22). These sentences describe identifiable methods/results, not only general navigation. | Add citations for the named/clearly described methods or shorten to non-paper-specific synthesis supported by nearby citations. |
| M | `paper/survey/sections/03b_feature.tex:19,28` | Line 19 describes recent methods via logit-space projection, teacher-derived PCA, invariance/decorrelation, and random prototypes, then says “One method” adds momentum-aware gradient regulation; none is cited. Line 28 names categories of cross-family methods and their assumptions without sources. | Cite the methods covered by these descriptions, or remove the method-specific characterizations. |
| M | `paper/survey/sections/05_reliability.tex:36,42` | Line 36 describes methods that fuse teacher/label predictions geometrically and group methods that protect tail classes/worst-group accuracy without citations. Line 42 says other methods drop undistillable classes or down-weight biased teacher knowledge, then points to a supplementary list with no paper citations. | Cite the described methods or replace these with a general taxonomy statement. |
| m | `paper/survey/sections/09_future.tex:23` | “A teacher-side group changes the teacher instead.” is an uncited class of methods and reads as a fragment-like sentence between cited paragraphs. | Attach citations for teacher-side methods, or merge with the preceding cited reliability-signal sentence and name its sources. |

## Checks requested

- **Numbers:** no changed-number issue found. A token comparison of current numeric strings across `paper/survey` and `docs/survey/search/*.md` against `survey-condensed-v1` found zero unmatched tokens (`unmatched tokens: []`). The supplementary table says its numbers derive from the old appendix and registry; its 112 rows correspond to the old 112-method appendix. This is a provenance check, not a fresh source-PDF revalidation.
- **Protected keys, MOO set, PCD, comparison baselines:** spot-checked required method coverage against `tasks/condense.md` and `docs/project/comparison-set.md`; citations remain in the survey for the protected optimizer/MOO set (MGDA, PCGrad, CAGrad, PCD; DTO-KD, DOT, DeepKD, SCKD, SCOPE, TPKD), comparison baselines (including NWKD, DKD, VRM, RLD), and the named tuned-scalarisation studies. No missing required key was found in this pass.
- **Preservation maps:** sampled 20 claims across `survey-t8-preservation.md`, `survey-t9.md`, `survey-t11.md`, and `survey-t16-audit.md` §4. All 20 sampled claims remain represented in the named section/table and retain an adjacent method citation or table-row citation. The VkD saturation claim above is an additional claim-level citation issue, outside those sampled claims.
- **Relabelled figures and reliability table:** the restored reliability table at `05_reliability.tex:19-29` cites every row's method(s). Spot-checked visible method labels in the taxonomy and target/scheme figures against the body; their methods are cited in the body. No deleted taxonomy leaf was found to cause a dangling section reference in the checked files.
- **Included methods:** `docs/survey/included-methods.md` contains 112 numbered rows, with author/title/venue/year/reference registry key in each row. The introduction points to it (`01_intro.tex:47`) and §VIII points to it (`08_benchmarks.tex:9`).
- **Sentence/humanizer review:** the uncited assertion in §IX is awkwardly isolated (“A teacher-side group changes the teacher instead.”). Other reviewed cuts read as grammatical; no definite additional broken sentence found.

## Sample of 20 preserved claims

The following sampled map claims still have their corresponding method/factual content and citations; locations are in the current section files unless noted:

1. T8: compact-student motivation — §I.
2. T8: teacher capacity gap — §IV, Cho citation.
3. T8: fixed teacher arrangement — §IV, Hinton citation.
4. T8: softened output/temperature — §II, Hinton citation.
5. T8: CE plus KD objective — §II, Hinton citation.
6. T8: response/logit transfer — §III-A, Hinton citation.
7. T8: feature adapters/hints — §III-B, FitNets citation.
8. T8: relational distances/angles — §III-B, RKD citation.
9. T11: conflict is an optimization property — §VI-B, PCGrad/SCKD citations.
10. T11: PCGrad projection — §VI-A, PCGrad citation.
11. T11: CAGrad average/worst improvement — §VI-A, CAGrad citation.
12. T11: SCKD gradient-similarity gate — §VI-B, SCKD citation.
13. T11: DTO-KD dynamic trade-off — §VI-B, DTO-KD citation.
14. T11: AE-KD gradient-space ensemble — §VI-B, `du2020aekd` citation.
15. T11: SCOPE relation/conflict behavior — §VI-B, SCOPE citation.
16. T11: TPKD margin projection — §VI-B, TPKD citation.
17. T11: DBGD half-space/barrier — §VI-A, DBGD citation.
18. T11: AuxiNash learned preference — §VI-A, AuxiNash citation.
19. T11: PCD EMA-normalised constrained direction — §VI-A, PCD citation.
20. T9: CHAD's BanSum result — §V, CHAD citation.

**Audit result:** 5 findings (4 M, 1 m); 0 untraced numeric tokens; 112/112 inventory rows; 20/20 sampled preservation claims retained. No test/build run because this is a read-only reference audit.
