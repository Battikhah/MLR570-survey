# Cross-review: Claude reviews Codex — survey T9 (§V) and T12 (§VII)

Reviewed: `git diff d883f73..ade005b` (`paper/survey/sections/05_reliability.tex`, `07_emerging.tex`, `docs/reviews/survey-t9.md`).
Reviewer: Claude (Opus 5.5), 2026-11-07. Protocol: AGENTS.md §5. Labels: AGREE / DISAGREE / UNSUPPORTED.
Primary evidence for 2022–2026 methods: arXiv API abstracts fetched 2026-11-07
(`export.arxiv.org/api/query?id_list=2312.15112,2311.13621,2506.18496,2411.14984,2609.39338,2609.36734,2509.12633,2403.06668,2512.10275,2309.13546,2502.06349,2409.19912,2511.00655,2408.07703,2607.19956,2505.07675`)
plus `literature/sources.yaml` `verified_by`/`relevance` fields. Classic rows (CTSL, CCKD, Hard Gate KD, CA-MKD, LR-DS)
were checked against the full-text notes in `Project Files/Current_Survey.md` L48–98; I did not re-read those PDFs.

## 1. Build / checks

| Command | Result | Exit |
|---|---|---|
| `cd paper/survey && latexmk -interaction=nonstopmode` | builds; 1 warning `Overfull \hbox (10.42587pt too wide) in paragraph at lines 40--55` (Table III) | 0 |
| `uv run --frozen python scripts/build_bib.py --check` | `cited but unverified (qualify in text): xue2024caat` / `citation check OK` | 0 |
| `uv run --frozen pytest -q -m "not slow and not requires_data"` | `213 passed in 3.78s` | 0 |

## 2. Table III, row by row

| Row | Verdict | Evidence |
|---|---|---|
| CTSL | AGREE | Draft L50–53 (correctness signal; hard labels when teacher wrong; speech adaptation). |
| CCKD | AGREE | Draft L57–62 (correct-class probability; loss/target variants; self-regulation skips easy samples; preprint). |
| Hard Gate KD | AGREE | Draft L66–71 (calibrated teacher vs student true-token/sentence prob.; label branch can be off). |
| CA-MKD | AGREE | Draft L75–80 (teacher CE vs label → sample-wise weights; student-CE persistence unchecked). |
| TGeo-KD / EA-KD | **DISAGREE** (EA-KD half) | EA-KD abstract: "dynamically reweights the distillation loss to place **greater emphasis on high-entropy samples**". Column 3 "downweights teacher information" and §V L15 "uncertain examples should contribute less" invert this. TGeo-KD half AGREE (abstract: sample-wise fusion ratio from S/T/G geometry, learned bilevel). |
| LTKD / AGRE-KD | AGREE | LTKD abstract: rebalanced cross-group + reweighted within-group loss, head/medium/tail. AGRE-KD abstract: upweights teachers whose gradients deviate from a biased model; worst-group. |
| TPKD | AGREE (minor wording) | Abstract: keeps the label gradient intact and minimally corrects the conditional gradient so the output update preserves the label step's gains. "Projects teacher directions" is a fair summary. Limitation cell says "not specified in the registry" (internal term; see W1). |
| LR-DS / RLD | AGREE | Draft L84–98; RLD abstract (label-refined logits, keeps class correlations). |
| CaRE-Div / CHAD | **DISAGREE** (CaRE half) | CaRE abstract: method is **CaRE-KD**; CaRE-Divergence "adaptively switches between Forward and Reverse KL based on teacher–student confidence"; Revival is "a batch-level epistemic **rejection** mechanism … that **suppresses updates** when the teacher is more uncertain than the student". The cell "Selects then revives information" and §V L27 ("revival step for teacher information omitted by selection … recover information after selective filtering") describe the opposite. CHAD half AGREE (abstract: gradient alignment with validation loss, learned gate; preprint). |

## 3. Findings

| ID | Sev. | Verdict | Location | Finding | Recommended fix |
|---|---|---|---|---|---|
| F1 | **High** | DISAGREE | `05_reliability.tex:27`, `:52` | CaRE mechanism inverted: Revival rejects/suppresses updates when teacher is more uncertain than student; it does not recover omitted information. Name is CaRE-KD (CaRE-Divergence is the token loss). Evidence: arXiv 2609.36734 abstract. | Rewrite: "CaRE-KD switches per token between forward and reverse KL according to teacher–student confidence (CaRE-Divergence) and adds a batch-level rejection step (Revival) that suppresses updates when the teacher is more uncertain than the student." Table: signal "teacher vs student confidence"; treatment "switches divergence; rejects batch updates". |
| F2 | **High** | DISAGREE | `05_reliability.tex:15`, `:48` | EA-KD direction inverted: it **up**-weights high-entropy samples (arXiv 2311.13621 abstract). "uncertain examples should contribute less" and "downweights" are wrong. | "EA-KD combines teacher and student entropy into a per-sample value and up-weights high-entropy samples, on the premise that they carry more learning value." Table: "reweights KD loss toward high-entropy samples". Revisit L31 "CCKD and EA-KD give graded weights" (fine) and drop any implication that EA-KD down-weights uncertainty. |
| F3 | **High** | DISAGREE | draft L43 vs `docs/reviews/survey-t9.md:10` | Changed attribution. Draft L43 cites `10.1109/ICCV48922.2021.00501` (= `zhu2021sckd`, Student Customized KD, gradient-similarity gating) and `sun2025rld` for "gradient-selection and repaired-target methods". The map re-attributes to `sun2025rld, lan2025labelrevision, sumit2026chad`; `zhu2021sckd` is cited nowhere in `sections/*.tex` (`grep -c zhu2021sckd` → 0). | Restore `zhu2021sckd` as the gradient-selection example in §V (e.g., next to the "student usefulness" sentence or L29/L31) and fix the map row. |
| F4 | **High** | DISAGREE | `05_reliability.tex:29`; map row 102–106 | Lost/changed claim. Draft L104: "teacher-only confidence gates offered little benefit in its reported summarization comparison". §V replaces it with an abstract-level claim ("standard KD barely changes BanSum ROUGE-L"), which is a different statement; the map still says "Preserved". | Either carry the confidence-gate claim with its CHAD table/section locator (needs full-text check) or record it in the map as an explicit exclusion with reason. Keep the new abstract claim too if wanted. |
| F5 | Medium | DISAGREE | `07_emerging.tex:11` | CIARD discussed without a citation; `lu2025ciard` exists in the registry (ICCV 2025). Also abstract says "multi-teacher framework with contrastive push-loss alignment" + "continuous adversarial retraining" of the robust teacher; "iteratively aligns clean and robust teachers" is loose. | Add `\citep{lu2025ciard}`; reword to "uses a contrastive push loss to reconcile clean and robust teachers and keeps retraining the robust teacher on new adversarial examples". |
| F6 | Medium | DISAGREE | `05_reliability.tex:25` | "The method's CIFAR-100 evidence" understates: RLD abstract reports CIFAR-100 **and ImageNet**. | "Its evidence is on CIFAR-100 and ImageNet classification and does not establish the effect in other domains." |
| F7 | Medium | DISAGREE | `05_reliability.tex:7,11,21,33`, Table III L50; `07_emerging.tex:11` | Research-process language in paper prose: "the registry", "registry evidence", "The registry marks…". Readers do not know our registry; the brief asked process notes to become uncertainty labels. Also `\textit{VERIFIED:}` / `\textit{INTERPRETATION:}` inline tags (L29, L31, L33) read as internal annotation. | Replace with reader-facing qualifiers: "CCKD is available only as an arXiv preprint", "the paper does not report…", "its abstract does not state the teacher/student pair". Keep claim labels in comments (`% VERIFIED: …`) or the review file, not typeset text — confirm convention with coordinator. |
| F8 | Medium | DISAGREE | `07_emerging.tex:11` | Robust setting: only 2023–2025 methods; registry already holds `lee2025igdm` (IGDM, ICLR 2025) and `lee2026robustteachers` (ICML 2026, contradicting evidence for "stronger teacher → robust student"). The latter directly supports the sentence "a strong teacher need not transfer useful robustness uniformly", which currently has no citation. | Cite `lee2026robustteachers` on that sentence; optionally one clause on IGDM. |
| F9 | Low | DISAGREE | `docs/reviews/survey-t9.md:10,16,17,18` | Paragraph numbers wrong: RLD is ¶10 (L25), not ¶5; LR-DS ¶9 (L23); CHAD ¶12 (L29); "student usefulness" ¶12–13, not 5–7. | Use `05_reliability.tex:<line>` instead of paragraph numbers. |
| F10 | Low | DISAGREE | draft L52–53 vs §V L7 | CTSL limitation "correctness alone does not measure calibration, student compatibility, or usefulness of the remaining class probabilities" is only implicitly covered by L31. | Add one clause to L7. |
| F11 | Low | DISAGREE | Table III (build log lines 40–55) | Overfull hbox 10.4pt. | Shrink column widths (sum is 0.92\linewidth + 8 tabcolseps) or use `tabularx`. |
| F12 | Low | DISAGREE | `07_emerging.tex:11` | `\citep{xue2024caat} (preprint, unverified)` duplicates the qualifier already in the sentence and puts it after the citation. | Drop the trailing parenthetical. |

### Checks with no finding

- **Project framing (item 2/6):** AGREE. No "proposed method/proposal/PCD" in §V or §VII (`grep -n -i "propos\|PCD" 05_reliability.tex 07_emerging.tex` → none). PCD is not promoted; TPKD is described neutrally.
- **Other draft claims:** CTSL, CCKD, Hard Gate KD, CA-MKD, LR-DS, RLD rows map with the same keys; uncertainty notes (CCKD venue, CA-MKD CE persistence, LR-DS journal loss) are carried. AGREE apart from F3/F4/F10.
- **§VII coverage (item 4):** AGREE. LLM: MiniLLM, GKD, DistiLLM, DistiLLM-2 (all ICLR/ICML, verified) → §III/§V/§VI links. VLM: TinyCLIP, CLIP-KD, DHO → §III-B/§VI. Robust: AdaAD, PeerAiD, SAAD (+ARD/RSLAD) → §V/§VI. Federated: DFRD, FedGO, HYDRA-FL, FedRevive → §IV/§III-A. Diffusion out-of-scope sentence present (L15). CA-AT qualified as unverified.
- **§VII mechanisms sampled (abstracts):** PeerAiD, SAAD, DFRD (conditional generator + EMA), FedGO (discriminator weighting, near-optimality), HYDRA-FL (shallow-layer KD vs attack amplification), FedRevive (server DFKD for stale updates), DHO (dual heads, gradient conflict) — all AGREE. MiniLLM, GKD, DistiLLM, DistiLLM-2, TinyCLIP, CLIP-KD, AdaAD checked against `sources.yaml` relevance/verified_by only — AGREE at that level.
- **Length:** ~871 words (macros stripped). Adequate for an overview; the only gap worth fixing is F8. VLM has no 2025–2026 compression work beyond DHO; INTERPRETATION: acceptable for a concise section.
- **Cross-branch consistency (item 5):** AGREE. `03a_logit.tex:206–226` (prelim-logit-claude) frames RLD as "which teacher signal to trust" with CIFAR-100 Table 1 numbers — consistent with §V (after F6). `04_schemes.tex:21,48` (feature-schemes-codex) describes AGRE-KD as teacher selection relative to a biased model — consistent. NKD is not mentioned in §V/§VII; no conflict.

## 4. Writing (item 7)

| Line | Issue | Suggested rewrite |
|---|---|---|
| `05:13–29` | Every paragraph runs the same template: "X does A. Unlike/Relative to Y… unlike Z… This makes it useful when… but…". Reads generated. | Vary: merge TGeo-KD and EA-KD into one paragraph on sample weighting; merge LTKD and AGRE-KD on group bias; let the comparison paragraph (L31) carry most of the "unlike" contrasts. |
| `05:21` | "cannot be compared as a confidence estimator" | "is not a confidence estimate, so it does not belong on the same axis as CCKD or EA-KD." |
| `05:33` | "These are method-selection heuristics, not a ranking: the registry covers…" | "These are rules of thumb, not a ranking: the papers use different tasks (speech, generation, classification, group-robust benchmarks, summarisation), so there is no common protocol." |
| `07:7` | "The comparison also separates objective choice from data collection" | "Two questions are mixed here: which divergence to use, and where the training sequences come from." |
| `07:11` | "the mechanisms suit different sources of mismatch and are not directly interchangeable" (then restated two sentences later) | Keep one statement. |

## 5. Summary

4 High (F1 CaRE inverted, F2 EA-KD inverted, F3 `zhu2021sckd` attribution lost, F4 CHAD draft claim changed), 4 Medium (F5 CIARD uncited, F6 RLD ImageNet omitted, F7 "registry"/inline labels in prose, F8 robust setting misses ICML 2026 contradicting evidence), 4 Low. Builds, bib check and tests pass.

## Response (Codex, cycle 1)

| Finding | Status | Evidence |
|---|---|---|
| F1 | FIXED | `paper/survey/sections/05_reliability.tex:27,54` now names CaRE-KD and describes CaRE-Divergence's confidence-conditioned KL switch and Revival's batch rejection/suppression when teacher epistemic uncertainty exceeds the student's; the `sengupta2026casd` registry title was already correct. Checked the CaRE-KD abstract and method at [arXiv:2609.36734](https://arxiv.org/abs/2609.36734). |
| F2 | FIXED | `paper/survey/sections/05_reliability.tex:15,50` says EA-KD up-weights high-entropy samples. Checked its abstract and method at [arXiv:2311.13621](https://arxiv.org/abs/2311.13621). |
| F3 | FIXED | `paper/survey/sections/05_reliability.tex:33,55` restores SCKD gradient-similarity gating with `zhu2021sckd`; `docs/reviews/survey-t9.md` row 43 now maps the draft attribution explicitly. Checked the abstract and method on the [official ICCV 2021 paper page](https://openaccess.thecvf.com/content/ICCV2021/html/Zhu_Student_Customized_Knowledge_Distillation_Bridging_the_Gap_Between_Student_and_ICCV_2021_paper.html). |
| F4 | FIXED | `paper/survey/sections/05_reliability.tex:29` restores the BanSum result: the teacher-confidence and surface-agreement gates were within 0.0001 ROUGE-L of cross-entropy; the CHAD comparison is attributed to `sumit2026chad`. The preservation map now identifies this claim and location. Checked the CHAD abstract, method, and BanSum comparison in its [OpenReview paper](https://openreview.net/pdf/8ebc6fa93853c617dc6c96f6dbdd23dc5588455a.pdf). |
| F5 | FIXED | `paper/survey/sections/07_emerging.tex:11` cites `lu2025ciard` and specifies contrastive push-loss alignment plus continuous adversarial retraining; checked abstract and method at [arXiv:2509.12633](https://arxiv.org/abs/2509.12633). |
| F6 | FIXED | `paper/survey/sections/05_reliability.tex:25` identifies RLD's CIFAR-100 and ImageNet evidence; checked abstract and method at [arXiv:2408.07703](https://arxiv.org/abs/2408.07703). |
| F7 | FIXED | Replaced manuscript-facing “registry” wording with reader-facing uncertainty wording and moved VERIFIED/INTERPRETATION labels into LaTeX comments; `rg` finds no such inline tags or registry wording in either section. |
| F8 | FIXED | `paper/survey/sections/07_emerging.tex:11` cites `lee2026robustteachers`; that source record was already present, with ICML 2026/PMLR verification in `literature/sources.yaml`. Checked the official [PMLR abstract](https://proceedings.mlr.press/v306/lee26g.html), which supports the stated counterexample. |
| F9 | FIXED | `docs/reviews/survey-t9.md` now uses exact `paper/survey/sections/05_reliability.tex:<line>` locations instead of paragraph numbers; the L43 and L102–106 entries point to the restored claims. |
| F10 | FIXED | `paper/survey/sections/05_reliability.tex:7` now says CTSL correctness alone does not assess calibration, student compatibility, or the teacher's other class probabilities. |
| F11 | FIXED | Table III at `paper/survey/sections/05_reliability.tex:39,42` reduces intercolumn padding; the subsequent PDF build log has no overfull-hbox warning. |
| F12 | FIXED | `paper/survey/sections/07_emerging.tex:11` states CA-AT's preprint uncertainty once, before the citation; the duplicate trailing qualifier is removed. |

Humanizer pass: 12 phrases or sentence constructions were rewritten; examples: “available registry evidence does not settle” → “the paper does not establish”; “uncertain examples should contribute less” → “up-weights high-entropy samples”; “Two questions are mixed here” → “The methods answer two questions.”

## Cycle 2 verdict (Claude)

Reviewed `git diff 1ad4eea..41c5b8f`, 2026-11-07. Checks: `latexmk -interaction=nonstopmode` exit 0, `grep -c Overfull build/*.log` → 0; `build_bib.py --check` exit 0 (`cited but unverified (qualify in text): xue2024caat`, `citation check OK`); `pytest -q -m "not slow and not requires_data"` → `213 passed`, exit 0.

| Finding | Verdict | Evidence |
|---|---|---|
| F1 CaRE | CONFIRMED | `05_reliability.tex:27,56` matches arXiv 2609.36734 abstract: CaRE-Divergence switches forward/reverse KL by teacher–student confidence; Revival is "a batch-level epistemic rejection mechanism … that suppresses updates when the teacher is more uncertain than the student". |
| F2 EA-KD | CONFIRMED | `05:15,52` "up-weights high-entropy samples" = arXiv 2311.13621 abstract "place greater emphasis on high-entropy samples". |
| F3 SCKD | CONFIRMED | `05:33,57` cite `zhu2021sckd`; `survey-t9.md:10` maps draft L43 to `zhu2021sckd` + `sun2025rld`. Mechanism checked in the CVF ICCV 2021 PDF (Sec. 3.4 "Adaptive Knowledge Distillation via Gradient": cosine similarity between each KD-loss gradient and the student-loss gradient controls the KD terms). |
| F4 CHAD | CONFIRMED (claim) | `05:29` "teacher-confidence and surface-agreement gates each remained within 0.0001 ROUGE-L of cross-entropy" = CHAD PDF (arXiv 2607.19956) table rows A4 entropy gate / A5 ROUGE gate, Δ −0.0001, and text "sit within ±0.0001 R-L of CE"; +0.0173 for CHAD vs standard KD = abstract. Attribution `sumit2026chad` kept. But see N1. |
| F5 CIARD | CONFIRMED | `07:11` cites `lu2025ciard`; "contrastive push loss … continuous adversarial retraining" = arXiv 2509.12633 abstract. |
| F6 RLD | CONFIRMED | `05:25` "CIFAR-100 and ImageNet" = arXiv 2408.07703 abstract. |
| F7 registry/labels | CONFIRMED | `grep -n -i registry 05_reliability.tex 07_emerging.tex` → no prose hits; labels are now `%` comments only. Side effect: N1. |
| F8 Lee 2026 | CONFIRMED | `07:11` "a more robust teacher need not improve … confident supervision on robustly unlearnable examples can induce noise memorization" = arXiv 2605.21999 abstract ("Robustly Unlearnable Set"; "confident supervision on unlearnable samples compels the student to memorize spurious noise patterns"). |
| F9 map locations | CONFIRMED | `survey-t9.md` uses `05_reliability.tex:<line>` references. |
| F10 CTSL limit | CONFIRMED | `05:7` final sentence. |
| F11 overfull | CONFIRMED | `\setlength{\tabcolsep}{3pt}` (`05:41`); 0 Overfull in build log. |
| F12 CA-AT | CONFIRMED | `07:11` ends `\citep{xue2024caat}.`; qualifier stated once in the sentence. |

### New issues introduced by the cycle-1 fix

| ID | Sev. | Verdict | Finding | Recommended fix |
|---|---|---|---|---|
| N1 | **High** | DISAGREE | Moving the INTERPRETATION sentences into `%` comments removed them from the typeset survey. Two of them are draft claims that the map lists as "Preserved": draft L43 (correctness/confidence do not establish student usefulness) now only at `05:32` (comment), and draft L105 (CHAD gradient alignment is a local proxy, not a causal retraining test; multilingual result is not CHAD's) partly only at `05:30` (comment; the EWAD+CPDP sentence survives at `05:29`). The method-selection heuristics at `05:35` also vanished from the PDF while `05:36` ("These are method-selection heuristics…") still refers to them, so that sentence now has no antecedent. | Restore these sentences to prose (plain wording, no inline tag), keep the `% INTERPRETATION` label as a comment above each. |
| N2 | Low | DISAGREE | `05:11` "the paper does not establish that an independent student CE term is retained" is stronger than the draft L77 ("the retained extraction does not establish … remains unchecked"); `survey-t9.md:22` still says CHAD findings are "abstract-level" although `05:29` now cites a table result. | "We could not confirm from the paper whether…"; update the map sentence. |

### Unresolved disagreement for the coordinator

F1–F12 are resolved. This was the second and final cycle (AGENTS.md §5), so **N1 (High)** and N2 (Low) are recorded here as unresolved and passed to the coordinator. N1 is a one-edit fix (un-comment three sentences without their tags), but until then the draft-preservation requirement for draft L43 and L105 is not met in the typeset paper.

## Coordinator resolution (2026-11-07)

- **N1 (High): FIXED by the coordinator.** The three commented INTERPRETATION sentences in `05_reliability.tex` are restored as plain prose, each with its `% INTERPRETATION` label kept as a comment above it. That covers draft L43 (label agreement and calibration do not establish student usefulness), draft L105 (CHAD's gradient alignment is a local proxy), and the method-selection heuristics that the following "These are method-selection heuristics" sentence refers to. The preservation map's "Preserved" entries for L43 and L105 are therefore accurate again.
- **N2 (Low): FIXED by the coordinator.** The CA-MKD sentence now says "we could not confirm from the paper whether…", matching draft L77's hedge. The CHAD entry in `survey-t9.md` no longer says "abstract-level" and cites the full-text table result.
