# Implementation Plan: MLR570 survey — State-of-the-Art Knowledge Distillation (with a KD × MOO section)

## Overview
- **What:** a survey of state-of-the-art knowledge distillation (KD), written to `Survey_Guideline.pdf` (requirements G1–G11 in `docs/requirements/assignment-requirements.md`) and modelled on `Survey_Sample.pdf`. The sample has a table comparing existing surveys, a taxonomy figure, preliminaries, many figures and tables, about 230 IEEE references, and a challenges / future-directions section.
- **Relation to the project:** the survey is **not a write-up of the project** (user instruction, 2026-11-03). The project's topics appear only where the state of the art itself uses them. A dedicated section introduces multi-objective optimisation (MOO) and shows how state-of-the-art KD methods use it: AE-KD, SCKD, DOT, DTO-KD, SCOPE, TPKD, MEMA, CHAD. PCD appears there as one priority-based method among others.
- **Draft preservation:** the original draft `Project Files/Current_Survey.md` stays unchanged (`AGENTS.md` §3). Its claims and attributions are carried into the new manuscript, mainly §V and §VI below, reworded from project framing to survey framing.

## Working title and outline (G1, G5)
*State-of-the-Art Knowledge Distillation: A Survey of Knowledge Types, Training Schemes, and Multi-Objective Optimization*

| § | Section | Key content (examples; every source registered and verified before it is cited) | Visual |
|---|---|---|---|
| I | Introduction | problem, importance, trends; motivation and gap; scope; organisation | **Table I:** comparison with existing surveys (Gou 2021 IJCV, Wang & Yoon 2021 TPAMI, Mansourian 2025 TMLR, Moslemi 2024 MLWA, Xu 2024 LLM-KD, Chen 2025 gradient-MOO) · **Fig. 1:** taxonomy |
| II | Preliminaries | Hinton KD, temperature, CE + KL objective, notation; standard benchmarks (CIFAR-100, ImageNet, COCO) and teacher/student pairs | **Fig. 2:** the KD pipeline |
| III | What knowledge is transferred | A. logit-based: KD, DKD, CTKD, DIST, MLKD, LSKD, RLD, WTTM, NKD. B. feature- and relation-based: FitNets, AT, RKD, PKT, CRD, OFD, ReviewKD, SimKD | **Fig. 3:** knowledge types · **Table II:** logit methods |
| IV | Training schemes | offline / online (DML) / self-distillation (BYOT, Born-Again) / multi-teacher / teacher-assistant and capacity gap (TAKD; Cho 2019) / data-free | **Fig. 4:** schemes |
| V | Teacher reliability and selective transfer | carried over from the draft: CTSL, CCKD, Hard-Gate KD, CA-MKD, LR-DS, RLD, CHAD | **Table III:** reliability signals |
| VI | **KD meets multi-objective optimisation** | **A. MOO primer:** Pareto optimality, scalarisation, MGDA, PCGrad, CAGrad, Nash-MTL, FAMO, GradNorm; priority, lexicographic and constrained methods (DBGD, GEM/A-GEM, PNGD, AuxiNash, PCD). **B. How state-of-the-art KD uses MOO:** AE-KD (MGDA), SCKD (gradient gating), DOT (momentum split), DTO-KD (FAMO-style min-norm), SCOPE / TPKD (asymmetric projection), MEMA, CHAD; MoKD noted as withdrawn. **C. Critical view:** symmetric vs priority rules; the scalarisation debate (Xin 2022, Kurin 2022, Royer 2023) | **Fig. 5:** 2-D geometry of weighted sum vs MGDA vs PCGrad vs priority projection · **Table IV:** MOO-in-KD methods |
| VII | Emerging settings | LLM distillation; VLM → small model (DHO, CLIP-KD); adversarially robust KD (ARD, RSLAD, AdaAD, PeerAiD; link to CA-AT); federated distillation | — |
| VIII | Benchmarks and reported results | CIFAR-100 and ImageNet numbers from official sources only, with protocol caveats (e.g. DKD 76.32 in mdistiller vs 75.44 in the DTO-KD paper) | **Tables V–VI** |
| IX | Challenges and future directions | grounded in gaps: recipe sensitivity (Beyer 2022), fidelity vs generalisation (Stanton 2021), unmeasured CE–KD conflict on standard benchmarks, cross-paper comparability, cost of per-objective gradients | — |
| X | Conclusion | recap of contributions and outlook | — |
| — | References | IEEE style, generated from `literature/sources.yaml` | — |

## Architecture decisions
- **Format: LaTeX, TMLR template** (user decision, 2026-11-03).
  - The official `JmlrOrg/tmlr-style-file` (Apache-2.0, upstream commit `7bf90ef`) is vendored in `paper/survey/tmlr/`.
  - The `[preprint]` option shows the team as authors.
  - Citations are natbib author-year (`\citet`/`\citep`, `tmlr.bst`). This satisfies G11's "consistent format (such as IEEE)" requirement with a consistent author-year style.
  - Layout: `paper/survey/main.tex` plus one file per section under `paper/survey/sections/`, with figures under `paper/survey/figures/`.
- **State-of-the-art criterion** (the user's condition for approving the plan):
  - **Core methods** (the ones discussed in depth) must be published 2022–2026 at a major venue (CVPR / ICCV / ECCV / NeurIPS / ICML / ICLR / AAAI / TMLR / TPAMI / IJCV), or be a 2025–2026 preprint with reported results on standard benchmarks.
  - **Classics** (Hinton 2015, FitNets, AT, CRD, RKD, DML, BYOT…) appear only as background and lineage.
  - The verified inventory comes from Task 4b. Checkpoint A shows the user the core list before any section is written.
- **Single source of truth for references:** `literature/sources.yaml` → `scripts/build_bib.py` → `paper/survey/refs.bib`.
  - A check fails the build when a `\cite` key has no record.
  - A source with `status: unverified` may be cited only with an explicit "(preprint / unverified)" qualifier in the text.
- **Write in prose.** The draft's bullet style is converted to prose, and every carried-over claim keeps its citation.
- **Exclusive file ownership** per task. `literature/sources.yaml` is shared, so workers add records only in their own worktree and the coordinator merges them (append-only YAML, so conflicts are trivial).
- **Review:** every section gets an independent Claude↔Codex review against its guideline row (G6–G8), the registry, and the draft-preservation map (`AGENTS.md` §5; maximum 2 cycles).
- **ARIS use:** a survey has no experiments, so `/aris:research-pipeline` applies only at its literature stage: `research-lit`-style searching per section, plus a final `citation-audit`. No experiment, deployment or autonomous review-loop stages run. ORCA does the orchestration.

## Task list
The tasks are in `tasks/todo.md`, with acceptance criteria, verification, dependencies and files. Ordered index:

### Phase 0: Foundation
- [x] T1 Manuscript skeleton and build
- [x] T2 Bibliography pipeline (`sources.yaml` → `refs.bib`) with a cite-key check
- [x] T3 Register and verify the draft's 28 URLs
- [x] T4 Taxonomy (Fig. 1) and existing-survey comparison (Table I)

- [x] T4b State-of-the-art method inventory (2022–2026, verified; gates Checkpoint A)

### Checkpoint A (human): scope, taxonomy, Table I, state-of-the-art inventory confirmed

### Phase 1: Core sections (parallel: Claude / Codex, each cross-reviewed)
- [x] T5 §II Preliminaries + Fig. 2
- [x] T6 §III-A Logit-based state of the art + Table II
- [x] T7 §III-B Feature- and relation-based + Fig. 3
- [x] T8 §IV Training schemes + Fig. 4

### Checkpoint B: sections compile, cross-reviews filed, citations resolve

- [x] T9 §V Teacher reliability (carried over from the draft) + Table III
- [x] T10 §VI-A MOO primer + Fig. 5
- [x] T11 §VI-B/C How state-of-the-art KD uses MOO + Table IV (carried over from the draft)
- [x] T12 §VII Emerging settings

### Checkpoint C: full body draft compiles; draft-preservation map complete

### Phase 2: Synthesis and polish
- [ ] T13 §VIII Benchmarks and reported results (Tables V–VI)
- [ ] T14 §IX Challenges and future directions
- [ ] T15 Title, Abstract, §I Introduction, §X Conclusion (written last)
- [ ] T16 Final audit: citations, guideline G1–G11, draft preservation, clean build

### Checkpoint D (human / team): full manuscript review

## Team ownership (user decision, 2026-11-03: Khalid ≈35%, Aly ≈25%, Hasan ≈25%, Salim ≈10%)

The weights are estimates of each section's share of the manuscript's writing effort.

**How ownership works:**
- ORCA agents (Claude/Codex) produce research, verified sources and a first draft.
- The **owner** edits, finalises and signs off on their section.
- The cross-agent review still applies.
- Foundation and audit tasks (T1–T3, T4b, T16) are done by the agents and are not counted.

| Owner | Sections (task) | Weight |
|---|---|---|
| **Khalid (≈35%)** | §I Introduction + Table I + Fig. 1 taxonomy (T4, T15); §VI-A MOO primer + Fig. 5 (T10); §VI-B/C KD × MOO + Table IV (T11); §IX Future directions (T14); Abstract + §X Conclusion (T15) | 10 + 8 + 12 + 4 + 3 = **37** |
| **Aly (≈25%)** | §II Preliminaries + Fig. 2 (T5); §III-A Logit-based state of the art + Table II (T6); §VIII Benchmarks (T13) | 4 + 15 + 6 = **25** |
| **Hasan (≈25%)** | §III-B Feature- and relation-based + Fig. 3 (T7); §IV Training schemes + Fig. 4 (T8); §VII Emerging settings (T12) | 12 + 9 + 4 = **25** |
| **Salim (≈10%)** | §V Teacher reliability + Table III (T9) | **10** |

Each section file starts with `% Owner: <name>` so that ownership is visible in the source.

## Risks and mitigations
| Risk | Impact | Mitigation |
|---|---|---|
| The survey drifts into a project write-up | High | Every section is reviewed for "is this state of the art, or our project?". PCD gets no more space than its peers in §VI. |
| A hallucinated or unverified citation | High | Registry-only citations, an automatic cite-key check, a verification field per record, and a final citation audit (T16) |
| Cross-paper benchmark numbers are not comparable | Med | Quote official tables only, record the protocol per row, and say so explicitly in §VIII |
| Large scope (sample ≈ 230 references) | Med | Prioritise the most influential and most recent works per category. Length is set after the instructor answers. |
| Concurrent edits to `sources.yaml` | Low | Workers append in their own worktree; the coordinator merges |
| Draft content lost while restructuring | Med | T9, T11 and T16 keep a claim → new-location map for every draft bullet |
| Unknown length limit, deadline or rubric | Med | Open question to the instructor; the structure works at any length |

## Open questions
1. ~~Format~~: resolved, TMLR LaTeX.
2. For the instructor: page or length limit, deadline, rubric, and whether IEEE style is mandatory.
3. ~~Team split~~: resolved (table above).
4. The draft's project framing ("the proposed project…", L175–187) becomes neutral survey framing, with claims and attributions preserved. Please confirm that this rewording is acceptable under the "preserve the draft" rule.
