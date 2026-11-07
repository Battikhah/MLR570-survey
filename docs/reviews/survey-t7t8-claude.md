# Cross-review: survey T7 (§III-B) and T8 (§IV) — Claude reviews Codex

- Scope: `git diff d883f73..HEAD` (commit 37bef02) on `Battikhah/survey-p1-feature-schemes-codex`.
- Reviewer: Claude (Orca task `task_2097fa177f21`), 2026-11-07.
- Method: I downloaded the primary PDFs: 22 from arXiv, plus RSD and AID from the ICCV 2025 CVF open-access pages. I extracted them with `pdftotext -layout` into a scratch directory outside the repo and compared every number and every table/caption against the extracted text. Line numbers refer to `paper/survey/sections/03b_feature.tex` (03b) and `04_schemes.tex` (04) at 37bef02.
- Verdict key (AGENTS.md §5): **AGREE** / **DISAGREE** / **UNSUPPORTED**.

## 1. Build and checks

| Command | Result | Exit |
|---|---|---|
| `cd paper/survey && latexmk -interaction=nonstopmode` | `build/main.pdf` produced. There are 2 overfull hboxes, both in `02_prelim`/`03a_logit`, which are outside this diff. | 0 |
| `uv run --frozen python scripts/build_bib.py --check` | `wrote paper/survey/refs.bib (158 entries)` / `citation check OK` | 0 |
| `uv run --frozen pytest -q -m "not slow and not requires_data"` | `213 passed in 4.21s` | 0 |

## 2. Table II (`tab:feature-methods`, 03b:47–92), row by row

| Row | Value in survey | Primary-source evidence | Verdict |
|---|---|---|---|
| SimKD | R32×4→R8×4 78.08 | SimKD Table 1, row "SimKD 75.56 ± 0.27 **78.08** ± 0.15 …", in the ResNet-8x4 / ResNet-32x4 column. Its own KD baseline is 74.42 (same table). | AGREE (the own-baseline caveat in 03b:13 is correct) |
| FCFD | 76.62 | FCFD Table 1 "Ours* 76.43 75.46 71.96 **76.62** 75.22", and Table 4 FCFD row (R32x4→R8x4 column) | AGREE (number). The "Projector?" cell is wrong; see M2. |
| NORM | 76.49; +KD 76.98 | NORM Table 1 rows "NORM … **76.49** …" and "NORM+KD … **76.98** …", in the column where KD = 73.33 and SimKD = 78.08, i.e. R32×4→R8×4 | AGREE |
| CAT-KD | 76.91 (Table 6) | CAT-KD Table 6 (same-architecture): "CAT-KD 71.62 73.62 **76.91** …", ResNet32×4→ResNet8×4 column | AGREE |
| DiffKD | 76.72 (Table 9) | DiffKD Table 9: "DiffKD … **76.72**±0.15", ResNet-32x4→ResNet-8x4 column | AGREE (number). The heterogeneous cell is questionable; see L1. |
| OFA-KD | Swin-T→R18 71.85 (KD 71.14) | OFA Table 1: header "T. S. FitNet CC RKD CRD KD DKD DIST OFA"; row "Swin-T ResNet18 81.38 69.75 71.18 70.07 68.89 69.09 **71.14** 71.10 70.91 **71.85**" | AGREE |
| VkD | R32×4→ShuffleNetV2 77.51 (Table 7) | VkD Table 7: "Vk D 70.11 70.65 74.95 77.05 **77.51** 77.19"; that column has teacher 79.42 and student 71.82 (ShuffleNetV2) | AGREE (number). The "Architecture-specific recipes" cell is questionable; see L3. |
| Projector study | ImageNet R34→R18 error 28.37 % (KD 29.34 %) (Table 6) | Table 6 caption: "Top-1 and Top-5 **error** rates (%) on ImageNet. ResNet18 as student, ResNet34 as teacher". Header "Teacher Student AT KD CC CRD ReviewKD Ours"; row "26.69 30.25 29.30 **29.34** 30.04 28.62 28.39 **28.37**". The PDF labels this row "acc@1", but the caption says these are error rates. | AGREE (the survey labels it correctly as error) |
| TCS | ConvNeXt-T→R18 81.60 (OFA 80.91) | TCS Table 1 (student ResNet18). Header "T. S. Self-distill KD DKD CRD DIST OFA LSHL2♯ TCS- TCS"; row "ConvNeXt-T … 80.91 (OFA) … **81.60** (TCS)" | AGREE |
| VRM | 78.76 (Table 1), with KD 73.33 and LSKD 76.62 (03b:31) | VRM Table 1: "VRM - 72.09 **78.76**", "KD [27] 70.66 **73.33**", "LSKD [59] 71.43 **76.62**", all in the same column | AGREE |
| RSD | DeiT-T→MobileNetV2 72.18 (RSD Table 2) | RSD (CVF ICCV 2025) Table 2 "Cross-architecture distillation results on ImageNet-1k": row "DeiT-T MobileNetV2 72.19 68.87 … **72.18**". RPKD Table 3 gives the same value in its RSD column. | AGREE. The inventory still says RSD's number was "not extracted"; see L6. |
| RPKD | 72.67 (OFA 71.39) (Table 3) | RPKD Table 3 row "DeiT-T MobileNetV2 … 71.39 71.78 72.18 **72.67**±0.11". The text says "+1.28% over OFA and +0.49% over RSD", which matches 71.39 and 72.18. | AGREE (number). The "Projector?" cell is questionable; see L2. |

## 3. Scheme table (`tab:scheme-comparison`, 04:39–54) and §IV numbers

| Row / claim | Evidence | Verdict |
|---|---|---|
| Offline: external teacher; representative methods SimKD/FCFD/CAT-KD/TCS | All four freeze a pretrained teacher (their method sections). | AGREE |
| Online: SwitOKD, L-MCL; no pretrained teacher | SwitOKD abstract: two co-trained models with "expert mode … learning mode". L-MCL abstract: mutual contrastive learning between peers. | AGREE for the table cell. The body text gets SwitOKD's mechanism wrong; see H1. |
| Self-distillation: DLB, USKD | DLB: "constraining half of each mini-batch coinciding with the previous iteration". USKD is the teacher-free variant in NKD. | AGREE |
| Multi-teacher: MTKD-RL, AGRE-KD | MTKD-RL abstract: "teacher performance and teacher-student gaps as state information to an agent". AGRE-KD abstract: teachers weighted by gradient deviation from a biased model. | AGREE for the table cell. The body text gets AGRE-KD's mechanism wrong; see M1. |
| Assistant / gap: ATS, DPK, AID | ATS: separate temperatures for target and non-target classes. DPK: "randomly mask a subset of feature patches of the student … complementary" teacher features. AID: "fine-tunes the teacher model to produce a more suitable intra-class distribution". | AGREE |
| Data-free: NAYER, SSD-KD; model access needed | NAYER and SSD-KD abstracts | AGREE |
| SSD-KD 75.16 (4.22 h) vs CMI 77.04 (15.42 h), Table 2 (04:31) | SSD-KD Table 2, CIFAR-100 block, first column (teacher 78.05 / student 77.10 = R34→R18): "SSD-KD 75.16(4.22h)", "CMI [10] 77.04(15.42h)" | AGREE |
| NAYER 77.54, CIFAR-100 R34→R18, Table 1 (04:32) | NAYER Table 1 "NAYER (E = 300) … **77.54**", first CIFAR-100 column (student 77.10) | AGREE |

## 4. Mechanism claims (21 of 23 sampled; every 2025–2026 item and the preprint)

SimKD, NORM, CAT-KD, OFA-KD, VkD, projector study, VRM, RSD, RPKD (text), L-MCL ("adaptive layer-matching mechanism trained by meta-optimization"), DLB, MTKD-RL, ATS, DPK, AID, NAYER, SSD-KD and SPOFA (LayerNorm projector plus momentum gradient regulation): **AGREE** with the cited paper. The DISAGREE and UNSUPPORTED items are listed below.

## 5. Findings

| ID | Sev. | Location | Verdict | Finding and evidence | Recommended fix |
|---|---|---|---|---|---|
| H1 | **High** | 04:13, 04:15 | DISAGREE | The survey describes SwitOKD's mechanism backwards. It says "a stronger peer may **pause its expert role**" and that SwitOKD "controls **when teacher-like peer supervision is emitted**". In the paper, expert mode **pauses the teacher's training** while the student keeps learning from it, and learning mode restarts the teacher. SwitOKD abstract: "expert mode (pause the teacher while keep the student learning) and learning mode (restart the teacher)". So what is switched is whether the teacher is updated, not whether it supervises. | Replace with: "SwitOKD switches between an expert mode, which pauses the teacher's updates while the student keeps learning from it, and a learning mode that resumes them; an adaptive threshold on the distillation gap decides the switch." In 04:15, change "pause mechanism" to "pausing the teacher's updates". |
| H2 | **High** | 04:19, 04:25 | n/a (integrity/format) | The body text contains internal notes. 04:19 says "the inventory leaf name should be reviewed by Hasan …". 04:25 says "the original survey draft makes this same point with Cho's attribution, retained here". These are reviewer and process notes, not survey prose. The Cho attribution itself is correct: Cho et al. 2019 is cited and the claim matches draft L13/L26. | Delete both clauses. Move the leaf-name question to the T8 report or `tasks/todo.md`. Keep `\citep{cho2019efficacy}`. |
| M1 | Medium | 04:21 | DISAGREE | The survey says AGRE-KD "uses agreement and group information". AGRE-KD needs **no group labels**. It upweights "teachers with gradient directions deviating from the biased model" so that the student benefits "unknown underrepresented subgroups" (abstract). | Rewrite: "AGRE-KD uses an auxiliary biased model and upweights teachers whose gradients deviate from it, targeting worst-group accuracy without group labels." |
| M2 | Medium | 03b:55 (Table II, FCFD) | DISAGREE | The "Projector?" cell says "No explicit bridge". FCFD §3 uses "a bridge module B, which is a simple combination of one convolution and one BatchNorm layer" to map student features into teacher space before the teacher tail. | Change the cell to "Yes (conv+BN bridge into teacher tail)". |
| M3 | Medium | 03b:21 | UNSUPPORTED | The survey says TCS "construction adds preprocessing and storage requirements". The paper says nothing about storage, and TCS Table 1 reports **lower** memory (5.8 GB vs 7.5 GB for OFA) and runtime (32.14 s/ep vs 52.02) than OFA. | Drop the claim. If a cost is wanted, cite TCS Table 1's memory and runtime rows. Keep the variance-vs-task-relevance caveat and label it INTERPRETATION. |
| M4 | Medium | 03b:25 | Citation hygiene | SPOFA (`yang2026spofa`, `status: under-review`, venue null) is presented as "a 2026 cross-architecture extension" with no preprint qualifier. AGENTS.md §3 and checkpoint rules require unpublished work to be marked as such in the text. | "SPOFA, a 2026 preprint under review, …". |
| M5 | Medium | 03b:37, 03b:45; 04:9, 13, 17, 19, 21, 27, 29, 31, 37; Table III header | Guideline fit (no project framing) | The prose relies on internal pipeline vocabulary: "inventory methods", "CORE entries", "inventory's primary-source checks", "inventory-reported", "registry IDs". Table III prints BibTeX keys (`\texttt{chen2022simkd}`). A reader of the survey has no access to the inventory. | Replace "inventory" with "recent (2022–2026)" or delete it. Drop the `\texttt{key}` column content and cite normally. Rename the header to "Representative methods". |
| M6 | Medium | 03b:53–92 | Layout (verified in `build/main.pdf`) | Table II renders on p. 6 but its `\footnotetext[1..12]` render on p. 7, because `\footnotetext` sits outside the float. All 12 footnotes are boilerplate ("Reported in X's comparison") and add nothing to the `% src:` information. | Remove the footnotes. Put the source table in the cell ("78.08 (T1)", the convention §III-A uses) and the SimKD own-baseline caveat in the caption. |
| L1 | Low | 03b:61 (DiffKD) | DISAGREE (mild) | The cell says "Not established as general". DiffKD Table 9 has a "Heterogeneous architecture style" block (R50→MBV2, R32x4→ShuffleV1/V2), and the paper says it "gains more significant improvements on heterogeneous settings". | "Reported on CIFAR heterogeneous pairs (T9)". |
| L2 | Low | 03b:75 (RPKD) | DISAGREE (mild) | "Projector?: Shared prototypes". RPKD uses per-architecture input projections: the teacher's are fixed random maps and the student's are learned (abstract). | "Fixed random (teacher) + learned (student) maps". |
| L3 | Low | 03b:65 (VkD) | DISAGREE (mild) | "Architecture-specific recipes": VkD's normalisation is **task**-specific, not architecture-specific (abstract and 03b:15 itself). | "Task-specific normalisation". |
| L4 | Low | `docs/reviews/survey-t8-preservation.md` | DISAGREE (line refs) | The map is complete: all 14 draft bullets are mapped, and I checked them line by line. Every line reference is off by two, though. The Intro bullets are L12–15 (not L10–13), Conventional KD is L21–26 (not L19–24), and Types is L30–34 (not L27–31). "Foundations L30" on the capacity row should be L26. Command: `sed -n '10,34p' "Project Files/Current_Survey.md" \| cat -n`. | Shift all references by +2. |
| L5 | Low | `refs.bib` `zagoruyko2017at` | Citation hygiene | The record is now `booktitle = {ICLR 2017}` but still has `year = {2016}`, so the rendered citation reads "2016" for an ICLR 2017 paper. The venue and status change are correct: the ICLR 2017 poster archive is recorded in `verified_by`. | Set year 2017 (keep the arXiv date in `sources.yaml`). Also delete the provenance sentence at 03b:13 ("The ICLR archive lists AT as …"), which belongs in the record, not the prose. |
| L6 | Low | `docs/survey/sota-inventory.md:98, :231` | Stale record | The inventory says RSD's headline number was "not extracted (… RPKD Table 3 gives 72.18 (secondary))". RSD's own Table 2 reports 72.18 for DeiT-T→MobileNetV2 (verified above). | Update the inventory row and item 1 of the open-issues list to "72.18 (RSD Table 2)". |
| L7 | Low | 04:25–27 | Coverage | Inventory row 125 cross-references DIST (§III-A) and TAID/AMiD (§VI) for the capacity gap. §IV mentions none of them. Otherwise coverage is complete: all 12 §III-B CORE items plus WKD-F and SPOFA, all 11 §IV CORE items, all classics, and every leaf in taxonomy 2–8. | Add one sentence that points to DIST (§III-A) and TAID/AMiD (§VI). |
| L8 | Low | `figures/taxonomy.tex:42` vs Table II | Consistency | The taxonomy puts VRM under "Feature: same architecture", but Table II says "Heterogeneous support: Yes". VRM Table 1 does include heterogeneous pairs (e.g. ResNet56→PiT-T). | Move VRM to a relational leaf, or soften the Table II cell. |
| L9 | Low | 03b:15 (NORM) | Precision | "the final merge can simplify the deployed student". The paper says the FT module "will be merged into its subsequent fully connected layer, introducing **no extra parameters**". | "… is merged into the classifier after training, so inference adds no parameters." |

### §III-A consistency (branch `Battikhah/survey-p1-prelim-logit-claude`, `03a_logit.tex`)

I found no contradictions. 03a:48 forward-references USKD to `\S\ref{sec:schemes}`, and 04:17 covers it. 03a:175–182 treats WKD-L as discrete Wasserstein with WKD-F as its Gaussian feature counterpart, which matches 03b:33. The two sections overlap only in these deliberate cross-references.

## 6. Writing (machine-sounding prose)

| Location | Problem | Suggested rewrite |
|---|---|---|
| 03b:13–23, 04:13, 17, 21, 27 | Nearly every method follows the same template: "Compared with X, Y …; however, Z …" or "Relative to X, …". The repetition reads as generated. | Vary the structure. Group the trade-offs by design axis (e.g. one sentence covering SimKD/VkD/NORM on the bridge), as 03b:39 already does well, and cut the per-method "Compared with". |
| 03b:37 vs 03b:45 | The point that results are within-paper and not a leaderboard is made twice. 03b:45 also repeats the VRM/OFA example. | Keep one statement (in the caption) and delete 03b:45. |
| 03b:23, 03b:41, 04:11, 04:25, 04:31 | There are many "X, not Y" closers: "not proof of architecture-neutral performance", "a reference arrangement, not a guarantee", "not proof that every large teacher fails", "rather than universal superiority". | Keep at most one per section and state the positive claim directly. |
| 03b:25 | "This cross-reference matters because …" is meta-commentary. | "Architecture bridging and objective conflict are separate design axes; SPOFA addresses both and is discussed in §VI-B." |
| 04:9 "These 2022--2025 inventory methods represent offline feature KD beyond the original logit objective." | Filler (and see M5). | Delete. |
| 04:13 "Both SwitOKD and L-MCL are 2022--2026 inventory methods." / 04:17 "DLB and USKD are 2022--2026 representatives." / 04:21 "They are 2025 inventory methods …" | Bookkeeping sentences. | Delete. The years are already in the citations. |
| 04:15 "Choose online KD when …; use a frozen offline teacher when …" | The imperative advice repeats the same frame in every paragraph ("Select TAKD when …", "Choose data-free KD when …"). | Keep the guidance and collect it in the closing paragraph (04:56), which already does this. |

## 7. Summary

- High: 2 (H1 SwitOKD mechanism inverted; H2 internal reviewer and process notes in the body).
- Medium: 6 (M1 AGRE-KD group labels; M2 FCFD bridge cell; M3 unsupported TCS cost claim; M4 SPOFA preprint unqualified; M5 inventory/registry jargon and bib keys in the table; M6 Table II footnotes on the wrong page).
- Low: 9.
- All 12 Table II numbers and all §IV numbers AGREE with their primary sources. The build, the bib check and the tests all pass (exit 0).

## Response (Codex, cycle 1)

Findings below refer to the submitted review's line references; evidence line numbers refer to the corrected working tree.

| Finding | Status | Response and evidence |
|---|---|---|
| H1 | FIXED | §IV now says SwitOKD expert mode pauses teacher updates while the student continues learning, and learning mode resumes teacher updates; the follow-up calls this the teacher-update pause (`paper/survey/sections/04_schemes.tex:13,15`). |
| H2 | FIXED | Removed the reviewer/process clauses from body prose, retained `\citep{cho2019efficacy}`, and moved the open leaf-name decision into a LaTeX comment (`paper/survey/sections/04_schemes.tex:19,25`). |
| M1 | FIXED | AGRE-KD is described as using an auxiliary biased model and gradient deviation, targeting worst-group accuracy without group labels (`paper/survey/sections/04_schemes.tex:21,23`). |
| M2 | FIXED | FCFD's table cell now states its convolution-plus-BatchNorm bridge into the teacher tail (`paper/survey/sections/03b_feature.tex:57`). |
| M3 | FIXED | Removed the unsupported preprocessing/storage claim; the interpretation caveat remains and Table 1's memory/runtime values are stated with a source comment (`paper/survey/sections/03b_feature.tex:19`). |
| M4 | FIXED | SPOFA is identified as a 2026 preprint under review (`paper/survey/sections/03b_feature.tex:23`). |
| M5 | FIXED | Removed inventory/CORE/registry terms and BibTeX keys from typeset sections and tables; scheme table now uses method names only (`paper/survey/sections/03b_feature.tex:39,49-81`; `paper/survey/sections/04_schemes.tex:39,41-54`). Search for `inventory|CORE|registry|texttt` in both section files returned no matches. |
| M6 | FIXED | Removed all table footnotes; result cells carry table labels and adjacent `% src:` comments within the float (`paper/survey/sections/03b_feature.tex:55-77`). |
| L1 | FIXED | DiffKD's support cell now states that the paper reports CIFAR heterogeneous pairs (`paper/survey/sections/03b_feature.tex:63`). |
| L2 | FIXED | RPKD's projector cell now distinguishes fixed random teacher maps from learned student maps (`paper/survey/sections/03b_feature.tex:77`). |
| L3 | FIXED | VkD's cell now says task-specific normalization (`paper/survey/sections/03b_feature.tex:67`). |
| L4 | FIXED | Corrected the preservation map against `nl -ba Project Files/Current_Survey.md`: Introduction L12-15, conventional KD L21-26, and knowledge types L30-34 (`docs/reviews/survey-t8-preservation.md:3,7-20`). |
| L5 | FIXED | Set the AT registry date to publication year 2017 while retaining arXiv identifier 1612.03928; regenerated BibTeX now renders `year = {2017}`. Removed the venue-provenance sentence from the paper body (`literature/sources.yaml:1933-1940`; `paper/survey/refs.bib`, `zagoruyko2017at`). |
| L6 | FIXED | Updated RSD's headline result to ImageNet-1K DeiT-T→MobileNetV2 72.18 (Table 2) and reduced the unextracted-number count to three (`docs/survey/sota-inventory.md:98,231`). |
| L7 | FIXED | Added the capacity-gap cross-reference to DIST in §III-A and TAID/AMiD in §VI-B with citations (`paper/survey/sections/04_schemes.tex:27`). |
| L8 | FIXED | Moved VRM out of the same-architecture leaf into the relational/cross-architecture leaf and added the rationale as a LaTeX comment (`paper/survey/figures/taxonomy.tex:17,43-44`). |
| L9 | FIXED | NORM is described as merging into the following classifier after training with no inference-parameter increase; the table states this explicitly (`paper/survey/sections/03b_feature.tex:13,59`). |
| Writing: repeated comparison templates | FIXED | Grouped the projector and relation discussion by design axis, varied sentence structure, and removed repetitive per-method comparison lead-ins (`paper/survey/sections/03b_feature.tex:11-31`). |
| Writing: repeated result synthesis | FIXED | Removed the duplicate results paragraph; the table caption now carries the cross-paper comparability caveat (`paper/survey/sections/03b_feature.tex:39-47,81`). |
| Writing: contrastive closers | FIXED | Recast the noted generic negatives as direct limits or conditions across §III-B and §IV (`paper/survey/sections/03b_feature.tex:19,41`; `paper/survey/sections/04_schemes.tex:11,25,31`). |
| Writing: SPOFA meta-commentary | FIXED | Replaced the meta-transition with a direct description of its feature transfer and optimizer treatment (`paper/survey/sections/03b_feature.tex:23`). |
| Writing: inventory bookkeeping | FIXED | Removed year-tag bookkeeping sentences from scheme descriptions; years remain in citations and references (`paper/survey/sections/04_schemes.tex:9,13,17,21,29`). |
| Writing: repeated imperative selection | FIXED | Removed the repeated imperative chooser constructions and kept scheme guidance in descriptive form and the section synthesis (`paper/survey/sections/04_schemes.tex:15,23,27,31,55`). |

All findings in this review cycle are marked FIXED; none were disputed. The taxonomy leaf name `label-averaging view` remains an owner decision, flagged in a LaTeX comment rather than manuscript prose.
