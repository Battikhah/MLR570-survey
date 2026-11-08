# T12b-G: closing the recall gaps in the systematic search

Orca task `task_4b8b082fb85b`. The Claude worker ran it on 2026-11-08. The criteria are the frozen I1–I3 and
E1–E7 (`tasks/plan.md` § "Scope decision"), applied exactly as S1–S3 applied them. The gaps are listed in
`docs/survey/search/README.md` § "Recall gaps".

**Labels.** Numbers and table references are **VERIFIED**: I read each one from the paper's own PDF with pdftotext on
2026-11-08. Coding decisions that need judgement are marked **INTERPRETATION**.

## Summary of counts

| Part | Assessed | Included | Excluded / other decision | Not accessible |
|---|---:|---:|---|---:|
| 1. S3's 15 dropped registry matches | 15 (9 new assessments; 6 already decided by S1/S2) | 2 new (`li2023ctkd`, `miles2024projector`); 4 already included by S1/S2 | 9: E4 7 (2 decided by S1, 1 by coordinator ruling), E5 1, E7 1 | 0 |
| 2. Broadened title re-screen | 445 new title hits screened; 16 sought at full text; 13 full texts read | 0 | 445: title/abstract 429 · full text E4 10, E1 2 (1 decided from an abstract), SUPPORT 1, ICLR paper with no full text 1 | 1 |
| 3. Cited 2022+ works not in the union | 29 | 2 (`li2023ctkd`, `miles2024projector`, the same papers as Part 1) | 27: E4 12 · E2 5 · E3 3 · E7 1 · out of scope by design 6 (MOO theory/method) | 0 |
| 4. Second snowball (2026 S1/S2 inclusions) | 4 papers' tables, 6 competitors not resolved at once | 0 | 6: E3 2 · not a method 1 · already in the registry 3 | 0 |

**Net change to the union: +2 included methods (106 → 108), both already in the registry.** No new registry records
were needed. The `verified_by` field of `li2023ctkd`, `miles2024projector` and `hayder2025mokd` was extended
(append-only) with this pass's extraction.

## 1. Log

| # | Part | Source / query | Date | Result |
|---|---|---|---|---|
| G1 | 1 | Full text of the 9 registry matches S3 dropped and that no other search had decided (arXiv PDFs) | 2026-11-08 | 9 read |
| G2 | 2 | The same 25 listing URLs as S1/S2 (CVF ×7, ECVA ×2, papers.nips.cc 2022–24, neurips.cc virtual 2025–26, iclr.cc virtual 2022–26, PMLR v162/202/235/267/306, jmlr.org/tmlr). Title regex `teach\|student\|mimic\|soft label\|dark knowledge\|logit\|temperature scal` (case-insensitive), minus titles that match the original search's regex (S1 `distil\|knowledge transfer\|teacher\|student`; S2 `distill\|knowledge transfer\|teacher`) | 2026-11-08 | 304 new hits (table G2a) |
| G3 | 2 | S3's Crossref filters (AAAI prefix 10.1609; TPAMI and IJCV ISSNs; 2022-01-01 to 2026-11-08), `query.title` = teach / teaching / student / mimic / mimicking / soft label / dark knowledge / logit / logits / temperature scaling. Then the new regex, minus titles that match S3's `distil\|knowledge transfer\|teacher` | 2026-11-08 | 676 regex hits; 573 match only "(Student Abstract)" and are dropped; **103** screened (AAAI 95, TPAMI 4, IJCV 4) |
| G4 | 2 | S3's arXiv Q4 with the new terms on the title: `(ti:teach OR ti:teaching OR ti:teacher OR ti:student OR ti:mimic OR ti:mimicking OR ti:"soft label(s)" OR ti:"dark knowledge" OR ti:logit(s) OR ti:"temperature scaling") AND (cat:cs.CV OR cat:cs.LG) AND (abs:"CIFAR-100" OR abs:CIFAR100 OR abs:ImageNet) AND submittedDate:[202501010000 TO 202611082359] ANDNOT abs:"knowledge distillation"` | 2026-11-08 | 39; 1 already in the registry (LDRLD 2507.15911) → **38** |
| G5 | 3 | Every `\cite*{}` key in `paper/survey/sections/{03a_logit,03b_feature,04_schemes,05_reliability,06b_kd_moo}.tex` (84 keys), restricted to registry year ≥ 2022, minus the union of ids in the S1/S2/S3 inclusion tables and the snowball inclusions (106 ids) | 2026-11-08 | **29**, the same as the coordinator's count |
| G6 | 4 | Comparison tables of the 2026 inclusions of S1/S2: `jeong2026skd` (CVPR 2026, T1–T3), `chen2026djip` (ICLR 2026, T1–T3), `morad2026bayesteacher` (ICLR 2026, T1–T4) and `hayder2026dtokd` (ICLR 2026, T1–T2). `etcibasi2026rpkd` was skipped because S3 Q7 already snowballed it | 2026-11-08 | 6 competitors not found in the registry at once (§5) |

**G2a: new hits per listing** (listed / original-regex hits / new-term-only hits).
CVPR 2022 2074/53/4 · CVPR 2023 2353/80/8 · CVPR 2024 2716/77/4 · CVPR 2025 2871/62/14 · CVPR 2026 4042/95/21 ·
ICCV 2023 2156/74/7 · ICCV 2025 2701/84/5 · ECCV 2022 1645/58/6 · ECCV 2024 2387/82/8 · NeurIPS 2022 2834/50/12 ·
NeurIPS 2023 3540/57/12 · NeurIPS 2024 4493/54/19 · NeurIPS 2025 5858/85/22 · NeurIPS 2026 9098/188/34 ·
ICLR 2022 1095/18/3 · ICLR 2023 1584/32/5 · ICLR 2024 2296/41/8 · ICLR 2025 3827/73/16 · ICLR 2026 5468/93/24 ·
ICML 2022 1233/5/4 · ICML 2023 1828/23/4 · ICML 2024 2610/30/9 · ICML 2025 3330/43/14 · ICML 2026 6552/116/25 ·
TMLR 5056/77/16. **Total 304.** The listing sizes and original-regex hits match S1/S2's logs, with one exception:
CVPR 2023, where the CVF page now lists 2353 papers (S1 logged 2050) and the original regex hits 80 (S1 logged 71).
The 9 extra titles were not re-screened here because they match the old terms. **Coordinator: they are a small
residual S1 gap.**

**Access notes.** OpenReview stayed blocked (as in S2), so *Scaffolding a Student to Instill Knowledge* (ICLR 2023)
could not be read (§4). The arXiv API accepted no multi-word `ti:` queries at first: the http→https redirect
returned nothing, and some requests timed out. With https the queries worked. ICLR proceedings PDFs needed
`--max-time 500`.

## 2. PRISMA-style flow for Part 2

```
Identified: listings 304 + Crossref 103 + arXiv 38                    445
Screened out on title/abstract                                        429   E2 ~262 · E1 ~165 · E6 2 (see the note)
Sought at full text                                                    16
  Not accessible (OpenReview 403, no arXiv copy)                        1   Scaffolding a Student (ICLR 2023)
  Decided from the abstract (machine-teaching theory)                   1   Mentored Learning (ICLR 2025) → E1
  Teaching Invariance Using Privileged Mediation (TMLR)                 1   decided at title level → E1 (privileged-information invariance, not KD)
  Full text read                                                       13
    Excluded                                                           13   E4 10 · E1 2 · SUPPORT 1
Included                                                                0
```

How the title screen was done (INTERPRETATION): the new terms mostly match LLM/VLM "teaching" papers (E2), human or
machine teaching, co-teaching, logit adjustment, calibration and OOD papers (E1), and student-performance
modelling (E1). I read all 445 titles. Any title that could describe a teacher→student classification method went
to full text. The E1/E2 split above is approximate: it came from a keyword pass over titles I had already read.

## 3. Inclusion table (new inclusions to the union)

Columns as in the S1–S3 specs. Family codes: L = logit/target/loss, F = feature/relation.

| id | Method | Venue / year | arXiv / DOI | Fam. | Pairs reported (CIFAR-100 / IN) | R32x4→R8x4 (table) | IN R34→R18 (table) | Protocol notes | Code (licence) | Mechanism | Found via |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `li2023ctkd` | CTKD | AAAI 2023 | 2211.16231 / 10.1609/aaai.v37i2.25236 | L | R56→R20, R110→R32, R110→R20, WRN-40-2→16-2/40-1, R32x4→SV1/SV2 (T1, T3) / R34→R18 | **n/r** (not in the paper; other papers quote 73.39 for KD+CTKD from mdistiller) | 71.32 KD+CTKD; 71.51 DKD+CTKD (T4) | Plug-in on KD/PKT/SP/VID/CRD/SRRL/DKD; CRD teachers; mean ± std over 3 runs | zhengli97/CTKD (Apache-2.0, per registry) | Adversarially learned curriculum temperature (global or per instance) | Parts 1 and 3 |
| `miles2024projector` | Projector / SRD | AAAI 2024 | 2303.11098 / 10.1609/aaai.v38i5.28219 | F | WRN-40-2→16-2/40-1, R56→R20, R32x4→R8x4, VGG13→MBv2, R50→MBv2, R50→VGG8, R32x4→SV1/SV2, WRN-40-2→SV1 (T5) / R34→R18 (T6) | **76.44** (T5, RandAugment); 78.37 (T5, SSKD rotations) | 71.63 (T6, top-1 error 28.37) | **Non-standard teachers and augmentation:** SSKD teacher weights (R32x4 79.63, not 79.42), trained on augmented image pairs. Flag on the leaderboard | roymiles/Simple-Recipe-Distillation (no licence file, per registry) | Projector + BatchNorm-normalised features + LogSum feature loss; the projector implicitly encodes relational information | Parts 1 and 3 |

## 4. Exclusion and decision table

**Part 1: S3's 15 registry matches**

| id | Decision | Evidence |
|---|---|---|
| `li2023ctkd` | **INCLUDE** | §3 |
| `miles2024projector` | **INCLUDE** (flag: SSKD teachers) | §3 |
| `zhou2025tcs` | E4 | T1: CIFAR-100 students are ResNet18 with ViT/Swin/Mixer teachers (images upsampled to 224); T2: ImageNet with DeiT/Swin/Mixer teachers → R18. No CRD pair |
| `yang2025mtkdrl` | E4 | Teacher pools only (T1 CIFAR-100; T2 ImageNet pool R50/R101/WRN-50-2/RNX50 → R18); no single standard teacher→student pair |
| `yang2023lmcl` | E4 | Online mutual KD between peers (T1–T3: ResNet-32+ResNet-110 etc.); no pre-trained teacher → CRD student pair |
| `kang2025dho` | E4 | CLIP (VLM) teacher → R18 from scratch / DINO R50 under few-shot semi-supervision on ImageNet (T1) |
| `yuan2026tpkd` | E4 | VOLO-D2 → PiT-B on CIFAR-100 (T4, 60 epochs); also CLINC150 text |
| `wang2022kdreview` | E5 | Survey (TPAMI 2022) |
| `hayder2025mokd` | E7 | Withdrawn on arXiv (v2). v1 reports 76.34 on R32x4→R8x4 (suppl. T1), but its published successor `hayder2026dtokd` (ICLR 2026, 76.40) is already included |
| `zhang2025rsd` | E4 (decided by S1 at full text) | Swin/DeiT→CNN pairs only |
| `zhang2025vrm` | already included (S1) | — |
| `huang2025deepkd` | already included (S2) | — |
| `bassam2025pld` | already included (S2) | — |
| `etcibasi2026rpkd` | already included (S2) | — |
| `kim2026ltkd` | E4 (coordinator ruling) | CIFAR-100-LT only |

**Part 2: full-text decisions** (title-level decisions for the other 429 records are summarised in §2)

| Paper | Venue | Source | Decision | Reason |
|---|---|---|---|---|
| Asymmetric Temperature Scaling Makes Larger Networks Teach Well Again (`li2022ats`) | NeurIPS 2022 | proceedings PDF | E4 | T2 CIFAR-100 teachers are ResNet110 / WRN28-8 / ResNeXt29-64-4d with VGG8 / SFV1 / MV2 students; none is a CRD pair. No ImageNet. Stays cited in §III |
| Beyond Student: An Asymmetric Network for Neural Network Inheritance (InherNet) | ICLR 2026 | arXiv 2602.09509 | E1 (**INTERPRETATION**, see note) | Builds the "student" by SVD-decomposing the teacher's weights; no teacher→student training signal; its networks are not ResNet8x4 etc. (T1 InherNet-Large 78.53 on the R32x4 column) |
| Compressing Models With Few Samples: Mimicking Then Replacing | CVPR 2022 | CVF PDF | E4 | Few-sample pruning of ImageNet ResNet-34; no CIFAR-100 or standard pair |
| Teaching with Soft Label Smoothing for Mitigating Noisy Labels in Facial Expressions | ECCV 2022 | ECVA PDF | E4 | Facial-expression datasets only |
| Learning From Biased Soft Labels | NeurIPS 2023 | proceedings PDF | SUPPORT | Analysis of soft-label bias; WRN-28/40 own backbones |
| Sharpness-Aware Minimization Activates the Interactive Teaching's Understanding and Optimization | NeurIPS 2024 | proceedings PDF | E1 | Co-teaching for noisy labels |
| Self-supervised Models are Good Teaching Assistants for Vision Transformers | ICML 2022 | PMLR PDF | E4 | DeiT students on ImageNet only |
| Large Language Model Teaches Visual Students | ICML 2026 | PMLR PDF | E4 | Cross-modal LLM→vision transfer; no CIFAR-100 / standard pair |
| CARD: Closing the Teacher-Student Loop for Adversarial Robustness Distillation | arXiv 2026 (2610.19911) | arXiv | E4 | Robustness pairs (CIFAR-10/100, TinyImageNet-10) |
| Collaboratively Guided Adversarial Robust Distillation | arXiv 2026 (2610.11306) | arXiv | E4 | WRN-34-10 robust teacher → RN-18/MN-V2 |
| IB Distillation Through Dual Teachers | arXiv 2026 (2607.27737) | arXiv | E4 | WRN-34-10 robust teachers |
| IMPACTX | arXiv 2025 (2502.12222) | arXiv | E4 | EfficientNet-B2/MobileNet/LeNet-5; no teacher→student CRD pair |
| IDeaL: Data-Free Multi-Teacher Distillation via Improved Dead Leaves | arXiv 2026 (2608.24759) | arXiv | E4 | ViT-B/16 teachers → ViT-S/16 |
| Mentored Learning | ICLR 2025 | iclr.cc abstract | E1 | Machine-teaching / active-learning theory |
| Scaffolding a Student to Instill Knowledge | ICLR 2023 | — | **not accessible** | A KD method by its abstract (teacher censors hard examples). OpenReview 403, no arXiv copy. Could meet I3 |

Note on InherNet (INTERPRETATION): it compares against KD methods on the CRD pairs, so a reader may expect it on the
leaderboard. It is weight inheritance, not distillation into a given student, so I coded it E1. The coordinator may
prefer SUPPORT.

**Part 3: the 29 cited works**

| id | Venue | Decision | Basis |
|---|---|---|---|
| `li2023ctkd` | AAAI 2023 | **INCLUDE** | §3 |
| `miles2024projector` | AAAI 2024 | **INCLUDE** | §3 |
| `li2022ats` | NeurIPS 2022 | E4 | Part 2 full text |
| `zhou2025tcs` | AAAI 2025 | E4 | Part 1 |
| `yang2025mtkdrl` | AAAI 2025 | E4 | Part 1 |
| `yang2023lmcl` | TPAMI 2023 | E4 | Part 1 |
| `kang2025dho` | NeurIPS 2026 | E4 | Part 1 (S2 had coded it E2 at title level) |
| `yuan2026tpkd` | arXiv 2026 | E4 | Part 1 |
| `zhang2025rsd` | ICCV 2025 | E4 | S1 full text |
| `shen2022dlb` | CVPR 2022 | E4 | S1 full text (self-distillation, no teacher→student pair) |
| `dong2025mooadv` | ICCV 2025 | E4 | S1 full text (zero-shot VLM robustness) |
| `jeong2025selfdistill` | ICLR 2025 | E4 | S2 full text |
| `kenfack2025agrekd` | TMLR 2025 | E4 | S2 full text |
| `yang2026spofa` | arXiv 2026 | E4 | Full text (arXiv 2606.24557): heterogeneous Swin-T/ViT-S/Mixer → ResNet18 only (CIFAR-100 and ImageNet) |
| `hayder2025mokd` | arXiv 2025 | E7 | Withdrawn (Part 1) |
| `sengupta2026casd` | NeurIPS 2026 | E2 | LLM distillation (S2 title) |
| `shin2026amid` | ICLR 2026 | E2 | LLM (S2 title) |
| `shing2025taid` | ICLR 2025 | E2 | Language models (S2 title) |
| `lee2022hardgatekd` | EMNLP 2022 | E2 | NLP (and outside the I2 list) |
| `sumit2026chad` | arXiv 2026 | E2 | Low-resource-language summarisation (registry abstract) |
| `chen2026scope` | Journal of Imaging | E3 | Outside-list journal; medical images |
| `lan2025labelrevision` | IEEE TCDS | E3 | Outside-list journal |
| `zhu2026upmopd` | arXiv 2026 | E2 | Multi-teacher on-policy **LLM** distillation |
| `kurin2022unitary` | NeurIPS 2022 | out of scope by design | MOO theory/benchmark (multi-task learning) |
| `xin2022mtohelp` | NeurIPS 2022 | out of scope by design | MOO evaluation (multi-task learning) |
| `royer2023scalarization` | NeurIPS 2023 | out of scope by design | MOO scalarisation (multi-task learning) |
| `shamsian2023auxinash` | ICML 2023 | out of scope by design | Auxiliary-learning MOO |
| `ye2022pngd` | UAI 2022 | out of scope by design | MOO optimiser (outside-list venue too) |
| `varam2026pcd` | TMLR 2026 | out of scope by design | PCD, the project's own MOO method; not a KD method |

**Part 4: second snowball**

The four tables cite these competitors: KD, FitNet, AT, SP, CC, RKD, PKT, FT, VID, OFD, CRD, ReviewKD, ReviewKD++
(`wang2024nd` in the registry), DKD, DIST, MLKD, SDD, RLD, WTTM, LSKD, MCMI (`ye2024mcmi`), MSE teacher
(`hamidi2024mseteacher`), DearKD / USKD / MaskedKD / SRD (= `miles2024projector`) / VkD (DTO-KD's ImageNet DeiT
table). Those not found in the registry at once are listed below.

| Competitor | Seen in | Resolution | Decision |
|---|---|---|---|
| CLKD (Zhang et al., class-aware information) | SKD T1–T2 | reference: arXiv 2211.14773 (2022 preprint) | E3 (preprint before 2025, no listed venue) |
| ITRD (Miles et al.) | DJIP T1 | reference: 2021 | E3 |
| TTDA | Bayesian-teacher T1 | a test-time-augmentation teacher baseline defined in that paper | not a method paper |
| USKD | DTO-KD T1 | already in the registry (`yang2023nkd`, ICCV 2023) | no action |
| DearKD | DTO-KD T1 | S1 E4 (ViT only) | no action |
| MaskedKD (role of masking) | DTO-KD T1 | S1 E4 (ViT students) | no action |

Result: the second snowball finds **no new eligible method**. **INTERPRETATION:** the 2026 papers compare against the
same 2022–2024 set the earlier passes already cover.

## 5. Residual items for the coordinator

1. CVPR 2023: 9 original-regex titles on the current CVF listing that S1's logged count does not cover (§1, G2a).
2. *Scaffolding a Student to Instill Knowledge* (ICLR 2023): not accessible. It joins the 17 in the README's
   "Not assessable" list.
3. InherNet (ICLR 2026): coded E1. SUPPORT is a defensible alternative.
4. `miles2024projector` uses SSKD teachers (79.63) and augmented pairs. Its 78.37 is not comparable to the mdistiller
   protocol; 76.44 (RandAugment) is the closer row.
