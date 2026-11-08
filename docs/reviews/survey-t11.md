# Survey T11: draft-preservation map for `Project Files/Current_Survey.md` L108–187

Task T11 (owner: Khalid). Drafted 2026-11-07 by the Claude worker (Orca task_286a800577fc).
Every bullet in draft L108–187 is listed below with its new location in
`paper/survey/sections/06a_moo.tex` (§VI-A, LaTeX label `sec:moo*`) or `06b_kd_moo.tex`
(§VI-B/C, `sec:kd_moo*`). Attributions are kept: each claim is cited to the same work the draft cited.

**Status changes since the draft.** I re-read these sources in full this pass (PDF text, 2026-11-07):
PCGrad, CAGrad, SCKD, DTO-KD, AE-KD, DBGD, PNGD, AuxiNash, TPKD and PCD. Where the draft said
"abstract only", the new text now states the rules from the full paper. I could not re-open SCOPE's
MDPI PDF (HTTP 403), so the SCOPE text carries over the draft's claims unchanged and gives no numbers.

**Global exclusion (justified).** Many draft bullets compare a method with "the proposed
correctness-plus-confidence gate", "PCD-KD" or "the project's recipe". The survey is not a write-up
of the project (user instruction 2026-11-03, `tasks/plan.md` L5), so these project-comparison
clauses are dropped. The factual claim about the cited method is kept. These drops are marked
**[proj]** below.

| Draft line | Draft claim (abridged) | New location | Notes |
|---|---|---|---|
| L110 | Heading: a reliability gate and a gradient rule answer different questions | §VI-B intro ("Section~\ref{sec:reliability} covers ... this section asks how the gradients are combined") | kept |
| L112 | A training step moves along a direction computed from the losses; weighted KD combines CE and teacher gradients with weights | §VI-B intro, sentences 2–3 | kept |
| L113 | Negative inner product = opposing first-order preferences; an optimisation property, not teacher correctness [PCGrad; SCKD] | §VI-B intro, `\citep{yu2020pcgrad,zhu2021sckd}` | kept, same citations |
| L114 | Worked example: T=1, teacher (0.85,0.10,0.05), student (0.95,0.03,0.02), label 1, inner product −0.0077; passes a 0.8 threshold | §VI-B intro | Recomputed (LaTeX comment). The "passes a teacher threshold of 0.8" clause refers to the project gate **[proj]**. It is rephrased as "a teacher can predict the correct class with high confidence and still conflict". |
| L115 | Limit: local logit-space calculation, not an experiment or a guarantee for parameter space | §VI-B intro | kept |
| L117–119 | PCGrad: Yu et al., NeurIPS 2020; abstract only | §VI-A PCGrad paragraph | upgraded: rule stated from Alg. 1 |
| L120 | PCGrad projects a conflicting gradient onto the normal plane of the other | §VI-A PCGrad | kept, exact formula added |
| L121 | Strength: optimisation-level response to interference without a teacher-confidence model | §VI-A PCGrad ("keep each task gradient but edit it when it conflicts") | "teacher-confidence model" comparison dropped **[proj]** |
| L122 | Limitation: evidence is multi-task; no supervised-primary hierarchy; not a PCD-KD baseline | §VI-A PCGrad ("It gives no priority to any objective ...") | PCD-KD baseline clause **[proj]** |
| L124–126 | CAGrad: Liu et al., NeurIPS 2021; abstract only | §VI-A CAGrad | upgraded: Eq. (3) and Alg. 1 |
| L127 | Optimises the average loss while regularising with the worst local improvement | §VI-A CAGrad | kept |
| L128 | Strength: addresses imbalance and interference together | §VI-A CAGrad ("a dial between the weighted sum and MGDA") | rephrased |
| L129 | Convergence statements need their own assumptions; not verified for KD | §VI-A CAGrad (inherits symmetry, cost, extra hyperparameter) and §VI-C (no MTL optimiser study covers KD) | The convergence caveat is implicit; no CAGrad KD claim is made anywhere. |
| L131–133 | SCKD: Zhu & Wang, ICCV 2021; full text, p. 5 checked | §VI-B SCKD | kept; re-read 2026-11-07 |
| L134 | Signal: cosine between supervised and each output/feature KD gradient; optimisation state, not teacher top-1 correctness | §VI-B SCKD | kept |
| L135 | Supervised loss ungated in Eq. (6); KD terms switched on/off | §VI-B SCKD | kept (Eq. (6) in comment) |
| L136 | Gate KD losses by gradient similarity, then optimise the sum; not the PCD program | §VI-B SCKD ("the update is the plain sum of the surviving losses, not a constrained program") | kept |
| L137 | Strength: close precedent for supervised-primary selective KD | §VI-B SCKD ("makes the label the primary objective") | kept |
| L138 | Limitation: similarity does not establish teacher reliability or better generalisation | §VI-B SCKD, last sentence | kept |
| L139 | Unresolved: Sec. 3.4/Alg. 1 disable a KD term for cos ≥ threshold, contrary to the surrounding text; check gate reset and parameter subset; do not reverse | §VI-B SCKD | Kept and confirmed against the PDF (Alg. 1: "if cos ≥ φ then γ_i = 0", gates initialised once before the loop, φ = 0 by default). Still unresolved because no authoritative code was found. Not reversed. |
| L141–143 | DTO-KD: Hayder et al., ICLR 2026; full text | §VI-B DTO-KD | kept; Eqs. 7–12, Cor. 3.3 and Eq. 18 re-read |
| L144 | Signal: task/distill gradients and relative progress; no correctness-plus-confidence gate | §VI-B DTO-KD | The gate comparison is dropped **[proj]**. |
| L145 | Task loss is in the objective vector with a dynamic coefficient; strictly positive task weight not verified | §VI-B DTO-KD (sum-to-one only; negative weight when g12 > g22 or g12 > g11) | Sharpened: the closed form can give a negative weight (INTERPRETATION from Eq. 11). The amortised version is renormalised by softmax (Eq. 18 text), so its weights stay positive. |
| L146 | Ideal: log-loss gradients through a multi-objective weight problem; practical method amortises; not identical | §VI-B DTO-KD ("The deployed method is therefore not the closed form") | kept |
| L147 | Strength: direct KD comparator for conflict and dominance rather than fixed weights | §VI-B DTO-KD, Table IV | kept |
| L148 | Limitation: projections and task/distill heads; plain-logit adaptation must be explicit; theory is not a guarantee for other recipes | §VI-B DTO-KD | kept; the project recipe becomes "a plain-logit adaptation would need to be specified separately" **[proj]** |
| L149 | Unresolved: Eq. (9) simplex vs Eq. (10) sum-to-one; check non-negativity, clamping, identical/opposed gradients, zero-loss log safeguards against code | §VI-B DTO-KD | Partly resolved from the paper: Eq. 18 uses softmax renormalisation for the amortised weights. Identical gradients make the denominator of Eqs. 11–12 zero; the paper gives no safeguard and no code. Zero-loss handling is also unverified. Recorded as open. |
| L151–153 | AE-KD: Du et al., NeurIPS 2020; gradient-space ensemble KD with a disagreement tolerance; abstract only | §VI-B AE-KD | upgraded: Eqs. 9–11 read |
| L154 | PCGrad/CAGrad are general ideas; their papers do not establish the KD application | §VI-A (presented as MTL methods) and §VI-C ("None of these studies covers distillation") | kept |
| L155 | SCKD/DTO-KD already apply optimisation to KD, which narrows any "address gradient conflict in KD" contribution | §VI-B (both described as existing KD methods), Table IV | The novelty-of-the-project framing is dropped **[proj]**. The survey presents them as prior art. |
| L157–159 | SCOPE: Chen et al., Journal of Imaging 2026; full text | §VI-B SCOPE | kept; the venue is noted as outside the SOTA criterion |
| L160 | Entropy-derived confidence weights for pairwise relations plus gradient-conflict detection | §VI-B SCOPE | kept |
| L161 | Classification is the reference objective; correction modifies conflicting KD contributions | §VI-B SCOPE | kept |
| L162 | Selective Relation Alignment and Gradient Conflict Resolution | §VI-B SCOPE | kept, both names |
| L163 | Strength: combines reliability-sensitive teacher information with asymmetric treatment | §VI-B SCOPE ("asymmetric counterpart of PCGrad") | kept |
| L164 | Limitation: entropy-weighted relations differ from a hard per-example gate; auxiliary priors and relational losses; extraction does not support every equation | §VI-B SCOPE | Kept, except the "hard per-example gate" comparison **[proj]**. |
| L166–168 | TPKD: Yuan & Tao, arXiv 2026; full text | §VI-B TPKD, marked preprint | kept |
| L169 | Signal: correct-class margins in output space, not a correctness-plus-confidence test | §VI-B TPKD | kept, gate comparison **[proj]** |
| L170 | Keeps the label gradient and conditionally modifies teacher directions | §VI-B TPKD | kept |
| L171 | Projects teacher directions to protect margins in output space; differs from requiring minimum progress on a secondary | §VI-B TPKD ("Unlike SCOPE ... protects a stated output-space quantity") | The comparison with minimum-progress (PCD-style) rules stays implicit in the contrast with PCD's paragraph. |
| L172 | Strength: asymmetric KD that questions unrestricted imitation | §VI-B TPKD, first sentences | kept |
| L173 | Output-space protection transfers to parameters only under stated conditions; projection-removal ablation closely matched | §VI-B TPKD and §VI-C ("Scale or conflict?") | kept, with Table 5 numbers |
| L175–177 | DBGD: Gong, Liu, Liu, NeurIPS 2021; stays close to a preferred gradient under a half-space constraint; barrier schedule and normalisation differ from PCD; ancestry, not a KD method | §VI-A priority-rules paragraph (DBGD sentence) and PCD paragraph | kept |
| L178 | PNGD: Ye & Liu, UAI 2022; reference criterion and gradient constraints within the Pareto set; prior preference-aware constrained optimisation | §VI-A priority-rules paragraph (PNGD sentence) | kept; the "does not establish the proposed gate" clause **[proj]** |
| L179 | AuxiNash: Shamsian et al., ICML 2023; asymmetric bargaining with learned preferences; differs from PCD's anchored program | §VI-A priority-rules paragraph (AuxiNash sentence) and PCD ("compared with AuxiNash, it fixes the priority instead of learning it") | kept |
| L180 | Du et al. 2018 (arXiv, v2 2020): main/auxiliary cosine gating with a binary admission variant; predates SCKD; not PCD-KD or improved generalisation | §VI-B, paragraph after SCKD, `\citet{du2018auxgradsim}` (preprint) | kept; PCD-KD clause **[proj]** |
| L181 | Synthesis: asymmetry, gating and anchored projection have antecedents; PCD acknowledges dynamic-barrier ancestry | §VI-A PCD ("The authors say the program is not new") and §VI-B PCD paragraph | kept |
| L183–185 | PCD: Varam & AlHajri 2026; TMLR status only via arXiv journal ref; OpenReview blocked | §VI-A PCD; §VI-B PCD comment | Status updated: TMLR 09/2026 is now VERIFIED through the TMLR accepted-papers listing and bib (registry `varam2026pcd`). |
| L186 | EMA-normalised gradients; direction closest to the primary subject to secondary-progress inequalities; no correction if already feasible | §VI-A PCD | kept, with Def. 4.1, Cor. 4.6 |
| L187 | Limitation: priority = proximity to primary gradient; no descent inequality on the supervised loss; strong conflict can fail to descend the primary | §VI-A PCD and §VI-B PCD paragraph | kept (Prop. 4.7 cited in comment) |

## Items the owner should decide

1. **FAMO registry status.** `liu2023famo` is `status: unverified` (venue not confirmed), so §VI-A
   cites it with "(preprint, unverified)". Its arXiv v3 PDF has no venue line. If someone confirms
   NeurIPS 2023 on the official proceedings page, the record and that qualifier should be updated
   (the record is append-only for this task, so I did not change it).
2. **SCOPE full text.** The MDPI PDF was blocked (HTTP 403) on 2026-11-07. A human should open the
   article in a browser and check that the SCOPE paragraph is still accurate.
3. **DeepKD numbers** come from arXiv v1 (2505.15133) Table 1. The registry record cites the
   NeurIPS 2025 proceedings page, and I did not check the camera-ready table against v1.
