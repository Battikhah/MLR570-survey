# Equation and algorithm source audit

Scope: the `zhu2021sckd` and `hayder2026dtokd` records in `literature/sources.yaml`, and the corresponding paragraphs in `paper/survey/sections/06b_kd_moo.tex` (lines 33–73 at audit time). No LaTeX or registry edits were made.

## Sources and local evidence

- SCKD, official CVF Open Access PDF (the page states it is identical to the accepted version): <https://openaccess.thecvf.com/content/ICCV2021/papers/Zhu_Student_Customized_Knowledge_Distillation_Bridging_the_Gap_Between_Student_and_ICCV_2021_paper.pdf>. Relevant: PDF p. 5 / printed p. 5061, Eq. (6), §3.4 and Algorithm 1; PDF p. 6 / printed p. 5062, continuation of the paragraph following the algorithm.
- DTO-KD, official ICLR 2026 proceedings PDF: <https://proceedings.iclr.cc/paper_files/paper/2026/file/e546ce4230c15bc422a500bb47b341ea-Paper-Conference.pdf>. Relevant: PDF p. 5 / printed p. 5, Eqs. (8)–(10); PDF p. 6 / printed p. 6, Eqs. (11)–(18), Corollary 3.3 and Algorithm 1 on the following page; PDF p. 7 / printed p. 7, Algorithm 1 and Eq. (18) discussion.
- Local downloaded originals: `/private/tmp/aml-source-audit/sckd_iccv2021.pdf`, `/private/tmp/aml-source-audit/dtokd_iclr2026.pdf`.
- Rendered evidence pages: `/private/tmp/aml-source-audit/sckd-p5.png` (Eq. 6, inequality, Algorithm 1), `sckd-p6.png` (continuation); `dtokd-page-05.png` (Eq. 9 and Eq. 10), `dtokd-page-06.png` (Eqs. 11–17), `dtokd-page-07.png` (Algorithm 1, Eq. 18, softmax text). Text extracts are alongside as `sckd.txt` and `dtokd.txt`; conclusions below were checked against the rendered pages, not text extraction alone.
- SCKD’s official CVF listing is <https://openaccess.thecvf.com/content/ICCV2021/html/Zhu_Student_Customized_Knowledge_Distillation_Bridging_the_Gap_Between_Student_and_ICCV_2021_paper.html>; DTO-KD’s official ICLR listing is <https://proceedings.iclr.cc/paper_files/paper/2026/hash/e546ce4230c15bc422a500bb47b341ea-Abstract-Conference.html>. The listings and PDFs did not expose an author-linked code repository; targeted searches found no author-linked code URL. This is a search result, not proof that no code exists.

## Findings

### SCKD — inequality, rationale, and gate persistence

**VERIFIED.** Eq. (6) leaves the supervised student loss ungated and multiplies each KD loss by a binary gate. Section 3.4 says a KD term is treated as negative transfer and removed when `cos(∇θ L_S, ∇θ L_kd_i) ≥ φ`; Algorithm 1 uses the same `≥` condition. The text says experiments use `φ = 0` unless stated otherwise. Under that stated rule, nonnegative cosine values (aligned or orthogonal gradients) are removed; negative cosine values survive. This is directionally opposite to the paragraph’s surrounding explanation of removing negative transfer / conflicting knowledge. Source: PDF p. 5 / 5061, Eq. (6), §3.4 and Algorithm 1; PDF p. 6 / 5062, threshold explanation.

**VERIFIED with internal specification gaps.** Eq. (6) denotes gates with iteration superscript `m`, but Algorithm 1 initializes all gates to 1 once before the training loop and only ever sets a gate to 0 inside the loop; it never resets one to 1. Thus the printed pseudocode makes a removed gate permanent. “Whether a removed term can return ... not stated” in the draft is inaccurate about Algorithm 1. The equation’s per-iteration notation leaves an internal mismatch; do not claim the intended gate lifecycle beyond what the pseudocode does. The paper defines `θ` as the weights updated by the losses and computes both gradients with respect to `θ`, but does not identify a narrower parameter subset for the cosine test.

**RECOMMENDATION.** Preserve the published inequality as printed and explicitly report its conflict with the negative-transfer rationale. Do not silently reverse it to `≤`. Say that Algorithm 1’s gate is sticky as written, while noting Eq. (6)’s per-iteration notation differs. No code linked by the official source was found to disambiguate intent.

### DTO-KD — simplex requirement and closed-form weights

**VERIFIED.** Eq. (8) defines `π` on the simplex (`π₁ + π₂ = 1`, `π₁, π₂ ≥ 0`); Eq. (9) minimizes the norm over that simplex. Theorem 3.1’s Eq. (10), however, prints only `π₁ + π₂ = 1`, and Eqs. (11)–(12) give the unconstrained equality-only minimizer. Those formulas can have negative components, so they are not in general a solution of Eq. (9). Their denominator is `||g₁ − g₂||²`; if the two vectors are equal, it is zero and the displayed formula is undefined, though every simplex weight gives the same combined vector. The draft correctly spots the constraint mismatch and negative-weight conditions (`π₁ < 0 iff g₁₂ > g₂₂`; `π₂ < 0 iff g₁₂ > g₁₁`) but omits the equal-vector degeneracy.

For two vectors, let `t = π₂`. When `d = g₁₁ + g₂₂ − 2g₁₂ > 0`, the unconstrained value is `t₀ = (g₁₁ − g₁₂)/d`; the Eq. (9) minimizer is `t = clamp(t₀, 0, 1)`. When `d = 0`, every `t ∈ [0,1]` is optimal. This is a direct solution of the two-vector quadratic on the simplex, not a claim about an implementation in another paper.

**NUMERIC SELF-CHECK (NumPy, no training).** Orthogonal unit vectors yield `(π₁, π₂) = (0.5, 0.5)` in both formulations (interior). Collinear `g₁=(1,0), g₂=(2,0)` yields equality-only `(2,−1)` but simplex optimum `(1,0)` (boundary); reversing their lengths yields `(−1,2)` but simplex optimum `(0,1)` (other boundary). Equal vectors `(1,0),(1,0)` give a zero denominator; any simplex pair is optimal. All cases confirm the distinction between the printed closed form and the constrained problem.

### DTO-KD — Algorithm 1, Eq. (18), and implementation description

**VERIFIED.** The paper presents the theoretical simplex program in Eqs. (8)–(9), followed by Theorem 3.1’s equality-only closed form in Eqs. (10)–(12). It then describes a practical algorithm (Algorithm 1): student/teacher latent features, projection `P`, separate `DistillHead` and `TaskHead`, weighted log-loss gradients, a student update, and a gradient step on `π` (step 12). Algorithm 1 does not print a softmax step. The following text says obtaining per-task gradients costs two backward passes and introduces Eq. (18) as an amortized *approximation* that avoids the extra backward pass; it then says to renormalize by softmax because Eq. (18) does not ensure `π ∈ Δ`. So the draft’s broad description is directionally right about a gradient-step implementation and the paper’s softmax instruction, but it conflates Algorithm 1 with the distinct amortized Eq. (18) procedure and its accompanying normalization instruction. The paper also calls the Algorithm 1 weights “recalculated in closed form” in the prose immediately before acknowledging that the algorithm requires per-task gradients and then switching to the amortized approximation; the pseudocode itself uses a gradient step, not the closed-form fractions.

**RECOMMENDATION.** Distinguish (a) theoretical Eqs. (8)–(9), with simplex constraints, (b) Theorem 3.1’s Eqs. (10)–(12), which omit nonnegativity and fail in the equal-vector case, and (c) Algorithm 1 plus Eq. (18), the practical gradient-step / amortized procedures with projection and task-specific heads. Attribute softmax renormalization specifically to the Eq. (18) discussion. A logits-only adaptation is not specified by this paper. Avoid calling the practical update “the closed form.”

## Source-safe edit guidance

For SCKD, replace the draft’s assertion that reactivation is unspecified with the narrower observation that Algorithm 1 makes the gate persistent once set to zero, while Eq. (6) uses iteration-indexed gates. State the `≥ φ`, `φ=0` rule and its conflict with the paper’s rationale without choosing which side is a typo.

For DTO-KD, retain the source’s distinction between Eqs. (9) and (10), but call Eqs. (11)–(12) the equality-only formula and state they may violate Eq. (9)’s simplex. Add the zero-denominator/equal-gradient case and clarify that constrained two-vector minimization clips the coefficient to `[0,1]`. Separate Algorithm 1’s gradient update from the Eq. (18) amortized approximation and cite softmax to the latter’s prose.

Possible compact wording (with existing citations only):

> SCKD leaves the supervised loss ungated and gates each KD term by the cosine of its gradient with the supervised gradient. As printed, Section 3.4 and Algorithm 1 remove a term when the cosine is at least `φ` (`φ=0` by default), which removes aligned or orthogonal gradients and conflicts with the text’s description of rejecting negative transfer. Algorithm 1 initializes gates once and only changes `1` to `0`, so its pseudocode makes a removed term stay off; Eq. (6)’s iteration-indexed gate notation does not clarify whether that persistence is intended.

> DTO-KD formulates its min-norm combination over simplex weights in Eqs. (8)–(9), but Theorem 3.1’s Eq. (10) states only the sum-to-one constraint. Its Eqs. (11)–(12) are therefore the equality-only minimizer and can return negative weights; for the simplex problem, the two-gradient coefficient is clipped to `[0,1]`, while identical gradients make the displayed denominator zero and leave every simplex weight optimal. Algorithm 1 and the amortized approximation in Eq. (18) update weights by gradient steps; the paper attaches softmax renormalization to the Eq. (18) discussion. Algorithm 1 also includes a feature projection and separate task and distillation heads, so a logits-only adaptation requires a separate specification.

No proposed change requires a new bibliography entry. No source was inaccessible; the web screenshot endpoint itself returned an HTTP 403 for CVF, so the original PDF was downloaded with approved network access and the relevant original pages rendered locally for inspection.
