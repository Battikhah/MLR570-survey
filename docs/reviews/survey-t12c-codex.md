# T12c integration cross-review (Codex)

Scope: `git diff c7d0d09..HEAD -- paper/survey/sections literature/sources.yaml`. I checked 36 method descriptions and reported values across §§III–VI against the inclusion tables in S1–S3 and the gap pass, and checked the earlier preservation maps against the current sections. The checked sample covered all modified sections and included logit, feature, scheme, reliability, and optimizer/distiller-search entries.

| ID | Severity | Verdict | Location | Evidence | Fix |
|---|---|---|---|---|---|
| T12c-C1 | Medium | DISAGREE | `paper/survey/sections/03b_feature.tex:17` | The sentence says SRD reports “only ImageNet among the standard pairs.” The gap-pass inclusion row for `miles2024projector` lists CIFAR-100 R32×4→R8×4 results (76.44 with RandAugment; 78.37 with SSKD teachers) as well as ImageNet 71.63; it explicitly flags the SSKD-teacher result as non-standard. This drops the protocol distinction and incorrectly says there is no CIFAR result. | State both CIFAR results with the augmentation/teacher flags, and distinguish the non-standard SSKD result from the standard-protocol evidence. |
| T12c-C2 | Medium | DISAGREE | `paper/survey/sections/04_schemes.tex:5` | The epistemic label remains typeset as `\textit{INTERPRETATION: ...}`. The request forbids typeset VERIFIED/INTERPRETATION tags; the analogous labels in other edited sections are comments. | Move the label to a LaTeX comment or convert the note into ordinary prose without the tag. |
| T12c-C3 | Medium | DISAGREE | `paper/survey/sections/07_emerging.tex:10` | The trim drops method-specific claims from the previous text: MiniLLM/GKD/DistiLLM/DistiLLM-2 comparison; TinyCLIP's weight inheritance; robust-method differences for ARD, RSLAD, AdaAD, PeerAiD, SAAD and CIARD; and HYDRA-FL/FedRevive. Current text retains only selected pointers/examples (e.g. MiniLLM, UP-MOPD, CLIP-KD/DHO, DFRD/FedGO). This is a material loss of carried-over content, not just shorter wording. | Restore brief, cited clauses for the removed distinctions, or update the preservation record to explicitly mark these claims as intentionally out of scope rather than preserved. |
| T12c-C4 | Medium | DISAGREE | `paper/survey/sections/08_benchmarks.tex` | Coverage check found `li2023kdzero` in the S2 inclusion table (77.85 CIFAR, 72.17 ImageNet; evolutionary search over transform/distance/loss per pair), but no citation in §§III–VI or §VIII. Its family is hybrid/distiller search, so the requested placement is §IV. | Add KD-Zero to §IV with the per-pair search mechanism and preserve its reported 240-epoch/search protocol. |
| T12c-C5 | Low | DISAGREE | `paper/survey/sections/03a_logit.tex:256–258`; `paper/survey/sections/06b_kd_moo.tex:199–202` | “easiest to swap into an existing pipeline” and “They suit settings where a search budget is available; their cost is the outer loop” are plausible generalizations, but read like template-generated takeaways and are not evidenced by a specific comparison in the cited search rows. | Tie each recommendation to a concrete property/result, or remove it and retain the mechanism comparison. |

## Coverage and §VII notes

The 106-method inclusion set is represented in §§III–VI or §VIII except for `li2023kdzero`, which is absent from both. `deng2022pebkd` is correctly a SUPPORT case, not one of the included methods. The §VII trim retains its scope statement and selected links to the core survey, but does not preserve the specific neighboring-method comparisons listed under T12c-C3.

The sampled source checks found no other mechanism, number, venue, or protocol-flag mismatch in the 36 entries reviewed. The logit comparisons keep the stacked/standalone and non-standard-protocol labels where those affect interpretation.

## Checks

- `cd paper/survey && latexmk -interaction=nonstopmode` — exit 0; latexmk reported “Nothing to do” and reused the up-to-date PDF. Existing `paper/survey/build/main.log` contains 0 occurrences of `undefined`; this run did not recompile the edited sources.
- `UV_CACHE_DIR=/private/tmp/uv-cache uv run --frozen --offline python scripts/build_bib.py --check` — exit 0; 233 bibliography entries generated, “cited but unverified (qualify in text): xue2024caat”, then `citation check OK`.
- `UV_CACHE_DIR=/private/tmp/uv-cache uv run --frozen --offline pytest -q` — exit 0; 220 passed, 1 skipped (`MPS unavailable`).

The bibliography check left the worktree clean. The LaTeX success is only an up-to-date check, not a fresh compilation of this diff.

## Coordinator resolution (2026-11-08)

- **C1: withdrawn and gap fixed.** The flagged sentence is about `yang2024srd` (IJCV 2024, "SRD"), which reports only non-standard CIFAR pairs (s3 row). The CIFAR numbers in the finding belong to `miles2024projector`, a different method also abbreviated SRD. I added its 76.44 (RandAugment) and 78.37 (SSKD teachers, flagged as non-standard) to §III-B.
- **C2: fixed.** The §IV label is now a LaTeX comment, followed by ordinary hedged prose.
- **C3: accepted as the planned scope cut** (tasks/plan.md, scope decision of 2026-11-08). The dropped §VII clauses were Phase 1 text, not original-draft claims: none of them appears in `survey-t8-preservation.md`, `survey-t9.md` or `survey-t11.md`. Their sources stay in the registry.
- **C4: fixed.** KD-Zero is added to §VI-B next to Auto-KD (the other distiller-search methods, DistPro, KDAS, Auto-KD and UniADS, already sit there), with its numbers and its per-pair search cost.
