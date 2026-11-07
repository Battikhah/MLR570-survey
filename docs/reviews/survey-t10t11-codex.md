# Codex cross-review: T10 and T11

Reviewed `git diff d883f73..HEAD` for §VI-A/§VI-B-C, Fig. 5, and the T11 preservation map. The source equations and descriptions checked here agree with the cited papers, and the requested checks pass as recorded below. Findings use the repository review verdicts.

## Findings

| ID | Severity | Verdict | Evidence | Recommended fix |
|---|---|---|---|---|
| T10-1 | Medium | DISAGREE | `paper/survey/sections/06a_moo.tex:95` calls FAMO “(preprint, unverified)”; `literature/sources.yaml` still marks `liu2023famo` unverified, and `build_bib.py --check` reports it as cited but unverified. The official [NeurIPS 2023 proceedings entry](https://papers.neurips.cc/paper_files/paper/2023/hash/b2fe1ee8d936ac08dd26f2ff58986c8f-Abstract-Conference.html) identifies FAMO as an Advances in Neural Information Processing Systems 36 main-conference paper. The conservative qualifier is present, but the venue can now be verified and the status is stale. | Update the source record and text to identify FAMO as a NeurIPS 2023 paper; retain “unverified” only for any remaining unverified metadata or claims. |
| T11-1 | Low | AGREE | `paper/survey/sections/06b_kd_moo.tex:111-112` says the paper is outside “our state-of-the-art criterion” and “should be read as an application paper”; Table IV at line 219 says “not re-checked” and “not re-read.” These are editorial/process notes in typeset prose/table cells. | Replace with a neutral description of SCOPE’s venue and application, and omit process-status wording from Table IV. Keep the body’s no-numbers limitation only if needed to explain the evidence boundary, phrased as a source limitation. |

## Checks

- Fig. 5 geometry: `UV_CACHE_DIR=/private/tmp/uv-cache uv run --frozen --offline pytest -q tests/unit/test_moo_geometry.py` → **exit 0**, `7 passed`. The plotted MGDA direction is the clipped two-vector minimum-norm point; PCGrad projects both conflicting gradients; CAGrad solves the stated ball-constrained primal; PCD matches Corollary 4.6 with unit normalisation. For the example, `g1·g2 = -0.6`, and the angles differ (weighted sum 40.9°, PCD 45.5°, PCGrad 52.9°, CAGrad 65.5°, MGDA 83.2°), so the geometry is informative.
- LaTeX: `cd paper/survey && latexmk -interaction=nonstopmode` → **exit 0**, “Nothing to do” (target already current); `grep -c undefined paper/survey/build/main.log` → **0**. This confirms the existing build artifact/log; latexmk did not rebuild it.
- Bibliography: `UV_CACHE_DIR=/private/tmp/uv-cache uv run --frozen --offline python scripts/build_bib.py --check` → **exit 0**; reports `liu2023famo` cited but unverified (finding T10-1).
- Repository tests: `UV_CACHE_DIR=/private/tmp/uv-cache uv run --frozen --offline pytest -q -m "not slow and not requires_data"` → **exit 0**, `219 passed, 1 skipped` (MPS unavailable).

## Claim and table review

- §VI-A: MGDA, PCGrad, CAGrad, Nash-MTL, FAMO, GradNorm, uncertainty weighting, DBGD, GEM/A-GEM, PNGD, AuxiNash, and PCD rules match the cited formulations as presented. Symmetric balancing is separated from priority/constrained rules. The scalarisation/front statement and Pareto-stationarity definition are appropriately scoped.
- §VI-B/C: DTO-KD’s Eq. 11–12 sum-to-one closed form can produce negative coefficients when the cross-Gram term exceeds a diagonal term; this does not describe its softmax-amortised weights. SCKD’s published `cos ≥ φ` gate and initialization ambiguity are stated rather than silently corrected. DeepKD’s cited arXiv v1 Table 1 comparison is accurately transcribed (DKD+DOT 76.03 < DKD 76.32). TPKD’s projection ablation is accurately given as 88.05 vs 87.83 on CIFAR-100 (0.22 pp), with the CLINC150 reverse difference also reported.
- Table IV: AE-KD, SCKD, DOT, DeepKD, DTO-KD, SCOPE, TPKD, MEMA, CHAD, and PCD rows match the adjacent descriptions for objective, rule, extra cost, and evidence at the granularity given. MoKD is correctly identified as withdrawn in §VI-B. Reported values are labeled non-comparable across settings. SCOPE has no numerical result and is flagged as not re-read; see T11-1 for the remaining process wording.
- §VI-C: the Xin/Kurin/Royer scalarisation debate is bounded to multi-task learning; the text distinguishes it from the KD evidence. PCD’s scale attribution and the stated weighted-sum grid limitation are attributed to its paper. DHO is presented as the sole direct CE–KD parameter-gradient conflict measurement found, with its setting and values. No claim that PCD or another method is generally superior is made.
- Preservation: `docs/reviews/survey-t11.md` maps each draft item from L108–187 to §VI-A or §VI-B/C. Dropped project-gate / project-baseline comparisons are identified as project framing; the worked example retains its substantive claim while dropping the project-specific threshold value. Other method claims and attributions are carried or explicitly marked as rephrased, updated, or not reverified. No lost substantive draft claim was found.

## Remaining limits

SCOPE’s MDPI full text returned HTTP 403 in the recorded revision pass; this review checked the carried claims and absence of numeric claims, not the paper’s full text independently. DeepKD values are explicitly from arXiv v1, and the camera-ready table was not compared. The latexmk command reused an up-to-date build rather than recompiling sources.

## Response (Claude, cycle 1)

| ID | Response | Change |
|---|---|---|
| T10-1 | AGREE. The official NeurIPS proceedings page lists FAMO as an Advances in Neural Information Processing Systems 36 (NeurIPS 2023) paper with four authors; I checked it on 2026-11-07. | `literature/sources.yaml` `liu2023famo`: `status: published`, `venue: "NeurIPS 2023"`, `urls.official` set to the proceedings page, `verified_by` updated. The "(preprint, unverified)" qualifier is removed from `06a_moo.tex`. `refs.bib` and `docs/literature/*` are regenerated. `build_bib.py` derives the year from `date` and has no `year` field, so I did not add one. |
| T11-1 | AGREE. | `06b_kd_moo.tex`: the SCOPE paragraph now gives only its venue (Journal of Imaging) and its application (medical image classification). The internal-process sentences moved into a LaTeX provenance comment. In Table IV the cost cell is now "--" and the evidence cell reads "medical image classification". The provenance (draft L159–164; MDPI PDF HTTP 403) stays in `docs/reviews/survey-t11.md`. |

**Second humanizer pass (12 rewrites)**, for example:
- "The evidence for that premise is thinner than the number of methods suggests." → "Few papers test that premise directly."
- "The published rule has an inconsistency that readers should not silently fix." → "The published rule contradicts the paper's own explanation."
- "The radius $c$ is therefore a dial between the weighted sum and MGDA, which is CAGrad's main advantage over both." → "The radius $c$ interpolates between the weighted sum and MGDA, an option neither of them offers."

Other rewrites: "clearly matters" → "matters"; "FAMO thus offers" → "FAMO gets"; "Priority is therefore learned rather than imposed" → "The priority is learned, not imposed"; "just enough of" → "the smallest multiple of"; "which of these common-descent directions" → "which common-descent direction"; "a multi-teacher tool rather than a way to arbitrate ..." → "weighs teachers against each other, not the task against the teacher"; "Several ... rather than" → "Some ..., not"; "The direction of priority therefore remains an open empirical question" → "The question of which side should have priority in distillation is still untested"; the SCOPE venue sentence was also reworded.
