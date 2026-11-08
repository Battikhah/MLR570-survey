# T12b-S1: systematic search of the CVF venues (CVPR 2022–2026, ICCV 2023/2025, ECCV 2022/2024/2026)

Orca task `task_9a143d79b190`, Claude worker, 2026-11-08. Criteria: `tasks/plan.md` § "Scope decision" (I1–I3, E1–E7,
frozen). Snowballing is not done here (S3 does it).

## 1. Search log

All listings were fetched on **2026-11-08** with `curl` and parsed for `<dt class="ptitle">` entries (main-conference
papers only; workshop pages are separate URLs and were not fetched). The query was a case-insensitive regex on the
**title**: `distil|knowledge transfer|teacher|student`. Neither listing exposes abstracts, so identification is
**title-only** (see limitation L1).

| Source | URL | Papers listed | Title hits |
|---|---|---:|---:|
| CVPR 2022 | `https://openaccess.thecvf.com/CVPR2022?day=all` | 2074 | 53 |
| CVPR 2023 | `https://openaccess.thecvf.com/CVPR2023?day=all` | 2050 | 71 |
| CVPR 2024 | `https://openaccess.thecvf.com/CVPR2024?day=all` | 2716 | 77 |
| CVPR 2025 | `https://openaccess.thecvf.com/CVPR2025?day=all` | 2871 | 62 |
| CVPR 2026 | `https://openaccess.thecvf.com/CVPR2026?day=all` | 4042 | 95 |
| ICCV 2023 | `https://openaccess.thecvf.com/ICCV2023?day=all` | 2156 | 74 |
| ICCV 2025 | `https://openaccess.thecvf.com/ICCV2025?day=all` | 2701 | 84 |
| ECCV 2022 | `https://www.ecva.net/papers.php` (eccv_2022 entries) | 1645 | 58 |
| ECCV 2024 | `https://www.ecva.net/papers.php` (eccv_2024 entries) | 2387 | 82 |
| ECCV 2026 | `https://www.ecva.net/papers.php` | 0 (no eccv_2026 entries on 2026-11-08) | — |
| **Total** | | **22 642** | **656** |

Access notes: the first ecva.net request returned HTTP 500 and a later retry returned 200. The ECVA listing links
point to `.php` pages, and the PDF path had to be read from each page (the naive `.pdf` rewrite returns 404).
One CVF PDF ("Knowledge Transfer from Interaction Learning", ICCV 2025) timed out twice (`curl --max-time 300`) and was
not assessed. ECCV 2026 proceedings are not on ECVA yet, and Springer was not checked for them.

## 2. PRISMA-style flow

```
Identified (title hits)                                   656   (CVF 516, ECCV 140)
After de-duplication                                      656   (no paper appears in two venues; 0 removed)
Screened out on title                                     559   E2 452 · E6 52 · E1 55
Sought for full text                                       97
  Not retrieved                                             1   (PDF timeout, see §1)
Full text assessed                                         96
  Excluded on full text                                    59   E4 55 · E1 3 · E6 1
Included                                                   37   (NEW 18 · existing registry 19); 9 of them tagged AMBIGUOUS
```

The title-screen codes were assigned by reading each of the 656 titles. The per-code split above was then counted with
a keyword rule: dataset-distillation wording → E6; detection/segmentation/3D/generation/video/VLM/LLM and other
non-classification tasks → E2; the rest (continual, federated, semi/self-supervised, domain adaptation, mean-teacher) →
E1. The 97 full-text candidates were picked by hand, and every title that might be a classification KD method was sent
to full text.

## 3. Inclusion table

Pairs use the CRD/mdistiller names. R32x4→R8x4 is CIFAR-100 top-1 and R34→R18 is ImageNet-1K top-1 (%). "T2" means Table 2 of the
CVF/ECVA PDF. For existing registry ids, the CIFAR number is the one already recorded in `literature/sources.yaml`
(re-checked against the PDF here where a table is cited). `n/r` = not reported. `n/x` = reported but not re-extracted in
this pass.

| # | id | NEW? | Method | Venue | arXiv / DOI | Family | Standard pairs reported | R32x4→R8x4 | R34→R18 | Code (licence) | Mechanism |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `zhang2025vrm` | existing | VRM | ICCV 2025 | 2502.20760 | feature/relation | R32x4→R8x4 and others (T1) | **78.76** (T1) | n/x | none found | Virtual relation matching on augmented views |
| 2 | `su2025eakd` | existing | EA-KD (best: EA-MLD+LS) | ICCV 2025 | 2311.13621 | logit/loss | R32x4→R8x4, WRN-40-1, VGG8, MN-V2, R32x4→SN-V2 (T2) | **78.38** EA-MLD+LS (T2); EA-KD 75.46 | 71.99 EA-DKD+LS (T4); EA-KD 71.79 | cpsu00/EA-KD (none) | Entropy-based per-sample weighting of the KD loss |
| 3 | `jeong2026skd` | **NEW** | SKD | CVPR 2026 | none found | hybrid | R56→R20, R32x4→R8x4, WRN-40-2→16-2, VGG13→8 (T1); hetero (T2) | **78.33** (T1) | 71.13 (T3) | none found | Instance KL plus batch Gram-matrix alignment. Note: its KD baseline is 74.75, higher than the usual 73.33 |
| 4 | `sun2024lskd` | existing | LSKD (best: MLKD+LS) | CVPR 2024 | 2403.01427 | logit/loss | standard set (T1, T2) | **78.28** MLKD+LS (T2) | n/x | sunshangquan/logit-standardization-KD (none) | Z-score logit standardisation before the softmax |
| 5 | `huang2024unikd` | **NEW** | UniKD | ECCV 2024 | 2409.18565 / 10.1007/978-3-031-73414-4_4 | hybrid | R56→R20, R110→R32, R32x4→R8x4, WRN-40-2→16-2/40-1, VGG13→8 (T1) | **78.18** (T1) | **72.83** (T3) | none found | Fused multi-layer features predicted as a Gaussian; features and logits distilled together |
| 6 | `chen2022simkd` | existing | SimKD | CVPR 2022 | 2203.14001 | feature/relation | standard set (T1, T2) | 78.08 (T1; its student baseline is 73.09) | n/x | DefangChen/SimKD (none) | Reuses the teacher classifier and aligns penultimate features |
| 7 | `li2023autokd` | **NEW** | Auto-KD | ICCV 2023 | none found | scheme | 10 CIFAR pairs incl. R32x4→R8x4, R32x4→SN-V1/V2 (T3) | 77.61 w/ logit KD; 77.35 w/o (T3) | 72.45 (T4) | lilujunai/Auto-KD (Apache-2.0) | MCTS search over distiller design |
| 8 | `xu2025ldrld` | existing | LDRLD | ICCV 2025 | 2507.15911 | logit/loss | standard set (T1) | 77.20 (T1) | 71.88 (ImageNet table) | yema-web/LDRLD (BSD-2-Clause) | Local dense logit relations |
| 9 | `xiang2025ekd` | existing | EKD | ICCV 2025 | none | logit/loss | standard set (T1) | 77.21 (T1) | n/x (T3) | lyxiang-casia/EKD (none) | Evidential (Dirichlet) treatment of teacher logits |
| 10 | `jin2023mlkd` | existing | MLKD | CVPR 2023 | none | logit/loss | standard set (T2, T3) | 77.08 (T2) | n/x (T4) | Jin-Ying/Multi-Level-Logit-Distillation (none) | Multi-level (instance/batch/class) logit alignment |
| 11 | `guo2023catkd` | existing | CAT-KD | CVPR 2023 | 2304.12777 | feature/relation | standard set | 76.91 (T6) | 71.26 (ImageNet table) | GzyAftermath/CAT-KD (none) | Class-activation-map transfer |
| 12 | `sun2025rld` | existing | RLD | ICCV 2025 | 2408.07703 | reliability | standard set (T1, T2) | 76.64 (T1) | n/x (T3) | zju-SWJ/RLD (none) | Refines teacher logits so wrong top-1 predictions are not transferred |
| 13 | `li2022kcd` | **NEW** | KCD (best: KC-SSKD) | ECCV 2022 | 2207.05409 / 10.1007/978-3-031-20083-0_2 | scheme | 11 CIFAR pairs incl. R32x4→R8x4 (T1) | 76.48 KC-SSKD; KC-KD 74.05 (T1) | 72.13 KC-ReKD (T3, from error 27.87) | dzy3/KCD (none found) | Condenses the transfer set by per-sample knowledge value |
| 14 | `yang2023nkd` | existing | NKD | ICCV 2023 | 2303.13005 | logit/loss | R32x4→R8x4 etc. (T1) | 76.35 (T1) | 71.96 (T1) | yzd-v/cls_KD (Apache-2.0) | Normalised non-target loss plus customised soft labels |
| 15 | `zhao2022dkd` | existing | DKD | CVPR 2022 | 2203.08679 | logit/loss | standard set (T6) | 76.32 (T6) | 71.70 (mdistiller) | megvii-research/mdistiller (MIT) | Decouples target (TCKD) and non-target (NCKD) KD |
| 16 | `wang2024nd` | **NEW** | ND (best: DKD++) | ECCV 2024 | none found / 10.1007/978-3-031-72691-0_2 | feature/relation | R56→R20, WRN-40-2→40-1, R32x4→R8x4, R50→MN-V2, R32x4→SN-V1/V2 (T1) | 76.28 DKD++ (T1) | 72.07 DKD++; KD++ 71.98 (T2) | WangYZ1608/Knowledge-Distillation-via-ND (none found) | Aligns student feature direction to teacher class means and enlarges the norm |
| 17 | `zhao2023dot` | existing | DOT | ICCV 2023 | 2307.08436 | combination/optimizer | R32x4→R8x4 (mdistiller) | 75.12 KD+DOT | 71.72 KD+DOT | megvii-research/mdistiller (MIT) | Separate momentum for task and KD gradients |
| 18 | `choi2023orc` | **NEW** | ORC | ICCV 2023 | 2206.01186 | scheme (online) | 7 CIFAR pairs incl. R32x4→R8x4 (T2) | 75.00 (T2) | 72.00 (T3, from error 28.00; pivot teacher R34) | choijunyong/ORCKD (none found) | Group of networks that swap teacher/student roles online |
| 19 | `lin2022tat` | **NEW** | TaT | CVPR 2022 | 2205.10793 | feature/relation | 7 CIFAR pairs incl. R32x4→R8x4 (T1) | 75.89 (T1, w/o L_KL) | 72.07 (T2) | sihaoevery/TaT (BSD-2-Clause) | Target-aware transformer distils teacher features per student pixel |
| 20 | `qian2025aid` | existing | AID | ICCV 2025 | none | scheme | R32x4→SN-V2, VGG13/R50→MN-V2, R32x4→WRN-16-2 (T3) | n/r (R8x4 only with a WRN-40-2 teacher: 77.45) | **72.01** (T4) | none found | Teacher adapts its knowledge to the student |
| 21 | `wei2024sdd` | existing | SDD (best: SD-NKD) | CVPR 2024 | 2403.13512 | logit/loss | hetero CIFAR pairs; ImageNet | n/x | 72.33 SD-NKD (T3) | shicaiwei123/SDD-CVPR2024 (MIT) | Multi-scale pooled logit decoupling |
| 22 | `hamidi2024mseteacher` | **NEW** | MSE teacher (best: ReviewKD+KD) | ECCV 2024 | 2407.18041 / 10.1007/978-3-031-73024-5_1 | reliability | R56→R20, R110→R20/R32, WRN-40-2→16-2/40-1, VGG13→8 (T1) | n/r | 72.16 (T3; 120 epochs) | ECCV2024MSE/ECCV_MSE_Teacher (none found) | Teacher trained with MSE to one-hot labels approximates the Bayes conditional probability |
| 23 | `li2025fbt` | **NEW** | FBT | ICCV 2025 | 2410.12342 | feature/relation | ImageNet R34→R18, R50→MobileNet (T3); CIFAR cross-arch only | n/r | 72.29 (T3; 100 epochs) | liguopeng0923/FBT (URL 404 on 2026-11-08) | Fuses teacher/student inductive biases before transfer |
| 24 | `deng2022distpro` | **NEW** | DistPro | ECCV 2022 | 2204.05547 | combination/optimizer | WRN-40-2→16-2, R32x4→SN-V1/V2, WRN-40-2→SN-V1, R56→R20, R110→R32 (T1) | n/r (R32x4→SN-V2 77.54) | 71.89 (T4) | xdeng7/DistPro (MIT) | Meta-learns a time-varying weight schedule over KD pathways. Directly relevant to PCD |
| 25 | `chae2025kdas` | **NEW** | KDAS (best: DKD+Ours) | ICCV 2025 | none found | scheme | R32x4→SN-V2, VGG13→VGG8, R56→R20, WRN-40-2→40-1 (T2) | n/r (R32x4→SN-V2 77.17) | 71.81 DKD+Ours (T3) | none found | Adaptive sampling and loss weighting; about 10–30% less training time |
| 26 | `yang2022mgd` | **NEW** | MGD (best: +WSLD) | ECCV 2022 | 2205.01529 / 10.1007/978-3-031-20083-0_4 | feature/relation | ImageNet R34→R18, R50→MobileNet (T1) | n/r | 71.80 MGD+WSLD; MGD 71.58 (T1) | yzd-v/MGD (Apache-2.0) | Masked student features regenerate the teacher's features |
| 27 | `parchami2024e2kd` | **NEW** | e²KD | ECCV 2024 | 2402.03119 / 10.1007/978-3-031-73464-9_18 | logit/loss | ImageNet R34→R18 (T1) | n/r | 71.8 KD+e²KD (= KD at full data; gains only in few-shot) (T1) | m-parchami/GoodTeachersExplain (Apache-2.0) | Adds explanation-map similarity to logit KD |
| 28 | `qian2022switokd` | existing | SwitOKD | ECCV 2022 | 2209.04996 | scheme (online) | ImageNet R34/R18 (T6) | n/r | 71.75 (T6, online) | hfutqian/SwitOKD (Apache-2.0) | The teacher pauses when the gap to the student grows |
| 29 | `miles2024vkd` | existing | VkD | CVPR 2024 | 2403.06213 | feature/relation | R32x4→SN-V2 (registry: Table 7, **not in the CVF PDF** → arXiv/supplementary) | n/r (R32x4→SN-V2 77.51) | n/r | roymiles/vkd (none) | Orthogonal projector plus task normalisation |
| 30 | `wang2024kdci` | **NEW** | KDCI (best: DFND+KDCI) | CVPR 2024 | 2403.19539 | scheme (data-free) | CIFAR-100 WRN-40-2→WRN-16-2 (T1) | n/r; WRN-40-2→16-2 74.52 | n/r | none found | Causal back-door adjustment plug-in for data-free KD |
| 31 | `tran2024nayer` | existing | NAYER | CVPR 2024 | 2310.00258 | scheme (data-free) | CIFAR-100 WRN-40-2→16-2 (T1) | n/r; WRN-40-2→16-2 71.72 (E=300) | n/r | tmtuan1307/NAYER (none) | Noisy-layer data generation |
| 32 | `chen2025cpnet` | **NEW** | CPNet | ICCV 2025 | none found | scheme (data-free) | CIFAR-100 WRN-40-2→16-2 (T1) | n/r; WRN-40-2→16-2 71.90 (CPNet-300) | n/r | none found | Generator coupled to the teacher |
| 33 | `yu2023spaceshipnet` | **NEW** | SpaceshipNet | CVPR 2023 | none found | scheme (data-free) | CIFAR-100 WRN-40-2→16-2 (T1) | n/r; WRN-40-2→16-2 69.95 | n/r | skgyu/SpaceshipNet (none found) | Feature-exchange augmentation plus an activation-region constraint |
| 34 | `liu2024ssdkd` | existing | SSD-KD | CVPR 2024 | 2406.07876 | scheme (data-free) | CIFAR-100 WRN-40-2→16-2 (T2) | n/r; WRN-40-2→16-2 61.44 | n/r | OSVAI/SSD-KD (Apache-2.0) | Small synthetic set with priority sampling |
| 35 | `tang2023kd3` | **NEW** | KD³ | ICCV 2023 | 2307.11469 | scheme (web data) | CIFAR-100 R32x4→R8x4/MN-V2/SN-V1/SN-V2 (T3) | 73.17 (T3, webly-collected training data) | n/r | none found | Distils on web images and corrects the distribution shift |
| 36 | `kim2026ltkd` | existing | LTKD | CVPR 2026 | 2506.18496 | reliability | R32x4→R8x4, VGG13→VGG8 on **CIFAR-100-LT** (T1) | n/r on balanced CIFAR-100 (LT γ=10: 66.76 overall) | n/r (ImageNet-LT only) | none found | Rebalances a teacher biased by a long-tailed distribution |
| 37 | `deng2022pebkd` | **NEW** | PE-BKD | ECCV 2022 | none found | scheme | R32x4→R8x4, WRN-40-2→16-2, VGG13→8, R32x4→SN-V2 (T2) | n/r for a deployable method (T2 "Simulation KD" 79.91 is an oracle) | n/r | Xiang-Deng-DL/PEBKD (none found) | Shows standard students can fully mimic the teacher; proposes blind KD |

Teacher-accuracy and epoch notes: SKD reports R32x4 teacher 79.42 and student 72.48, as mdistiller does, but its KD row
(74.75) and DKD row (76.51) are about 1.4 and 0.2 points above mdistiller's numbers. PE-BKD's teachers (R32x4 79.63, WRN-40-2 76.46) differ from mdistiller.
On ImageNet, MSE teacher trains for 120 epochs and FBT for 100. DistPro uses 240 CIFAR epochs, the same as mdistiller.

### AMBIGUOUS cases (included, coordinator to decide)

- `wang2024kdci`, `tran2024nayer`, `chen2025cpnet`, `yu2023spaceshipnet`, `liu2024ssdkd`. AMBIGUOUS: these are
  data-free KD papers. They report the standard WRN-40-2→WRN-16-2 pair on CIFAR-100 (I3 is met literally), but the
  student never sees CIFAR-100 training images, so the numbers are not comparable to CRD-protocol rows.
- `tang2023kd3`. AMBIGUOUS: R32x4→R8x4 on CIFAR-100, but the student is trained on web-collected images.
- `kim2026ltkd`. AMBIGUOUS: R32x4→R8x4 is reported only on CIFAR-100-LT, not on balanced CIFAR-100.
- `deng2022pebkd`. AMBIGUOUS: the paper is mostly analysis (I1 SUPPORT?). Its only R32x4→R8x4 number above KD is
  an oracle simulation that samples near the test data.
- `miles2024vkd`. AMBIGUOUS: the CVF main-paper PDF has no standard-pair table. The registry's Table 7 figure must come
  from the arXiv version or the supplement. Not re-checked here.

## 4. Full-text exclusions (59)

| Venue | Paper | Code | Reason |
|---|---|---|---|
| CVPR22 | DearKD: Data-Efficient Early KD for Vision Transformers | E4 | ViT/DeiT ImageNet only |
| CVPR22 | Self-Distillation from the Last Mini-Batch (`shen2022dlb`, existing) | E4 | Self-distillation, no teacher→student pair |
| CVPR22 | Co-advise: Cross Inductive Bias Distillation | E4 | DeiT students only |
| CVPR22 | KD As Efficient Pre-Training | E4 | Transfer-learning pre-training, no standard pair |
| CVPR22 | KD: A Good Teacher Is Patient and Consistent (`beyer2022patientkd`, existing) | E4 | BiT ResNet-152→ResNet-50 recipe study |
| CVPR23 | Masked Autoencoders Enable Efficient Knowledge Distillers | E4 | ViT pre-training only |
| CVPR23 | TinyMIM | E4 | ViT MIM pre-training only |
| CVPR23 | AdaAD (`huang2023adaad`, existing) | E4 | Adversarial robustness, WRN-34-10 teacher |
| CVPR23 | Loss Minima Flattening via Parameter Hybridization (online KD) | E4 | CIFAR-100 without standard pairs |
| CVPR23 | DisWOT: Student Architecture Search | E1 | KD used to rank student architectures (NAS) |
| CVPR23 | Learning to Retain While Acquiring (adversarial DFKD) | E4 | Data-free, CIFAR-100 only with R34→R18 |
| CVPR23 | ANN→SNN with KD | E4 | SNN students |
| CVPR24 | DeiT-LT | E4 | ViT long-tail |
| CVPR24 | Aligning Logits Generatively (black-box KD, MEKD) | E4 | Non-standard pairs (R56→VGG11 etc.) |
| CVPR24 | Adversarial Distillation via Slack Matching | E4 | Adversarial robustness, WRN-34-10 teacher |
| CVPR24 | Robust Distillation via Untargeted/Targeted Intermediate Adversarial Samples | E4 | Adversarial robustness, non-standard pairs |
| CVPR24 | PeerAiD (`jung2024peeraid`, existing) | E4 | Adversarial robustness, R18/WRN-34-10 |
| CVPR24 | FreeKD: Semantic Frequency Prompt | E4 | No CIFAR-100 or R34→R18 classification result |
| CVPR24 | Asymmetric Masked Distillation | E4 | ViT pre-training |
| CVPR25 | What Makes a Good Dataset for KD? | E4 | Analysis, CIFAR R34→R18 only (SUPPORT candidate) |
| CVPR25 | VL2Lite (`jang2025vl2lite`, existing) | E4 | VLM teacher, non-standard pairs |
| CVPR25 | Temporal Separation with Entropy Regularization (SNN) | E4 | SNN students |
| CVPR25 | Efficient ANN-Guided Distillation (SNN) | E4 | SNN students |
| CVPR25 | CustomKD | E4 | Foundation-model teachers, semi-supervised setting |
| CVPR26 | Continual Distillation of Teachers from Different Domains | E4 | No standard pair |
| CVPR26 | Unified Framework for Knowledge Transfer in Bidirectional Model Scaling | E4 | No standard pair |
| ICCV23 | DFKD for Fine-grained Visual Categorization | E4 | Fine-grained datasets only |
| ICCV23 | Masked Autoencoders Are Stronger Knowledge Distillers | E4 | ViT pre-training |
| ICCV23 | FerKD | E4 | ImageNet, no R34→R18 / R50→MobileNet |
| ICCV23 | Semi-Supervised Learning via Weight-Aware Distillation | E4 | SSL setting, no standard pair |
| ICCV23 | Bayesian Optimization Meets Self-Distillation | E4 | Self-distillation, no teacher pair |
| ICCV23 | Cumulative Spatial KD for ViTs | E4 | ViT students |
| ICCV23 | Multi-Label Knowledge Distillation | E4 | Multi-label benchmarks |
| ICCV23 | Adversarial Robustness in Low-Label Regime | E4 | Adversarial robustness |
| ICCV25 | Competitive Distillation | E4 | Peer group of R32/44/56, no teacher pair |
| ICCV25 | CIARD (`lu2025ciard`, existing) | E4 | Adversarial robustness |
| ICCV25 | Confound from All Sides (`dong2025mooadv`, existing) | E4 | Zero-shot VLM robustness |
| ICCV25 | Perspective-Aware Teaching | E4 | Cross-architecture pairs only |
| ICCV25 | Cross-Architecture Distillation via Redundancy Suppression (`zhang2025rsd`, existing) | E4 | Swin/DeiT→CNN pairs only |
| ICCV25 | ACAM-KD | E4 | No CIFAR-100 or R34→R18 result |
| ECCV24 | Simple Unsupervised KD with Space Similarity | E4 | Self-supervised students, linear evaluation |
| ECCV24 | Adversarially Robust Distillation (variance gap) | E4 | Adversarial robustness |
| ECCV24 | UNIC: Universal Classification via Multi-teacher | E4 | Foundation-model teachers |
| ECCV24 | Auto-DAS | E1 | Distillation-aware architecture search |
| ECCV24 | Bad Students Make Great Teachers | E1 | Active learning / data selection |
| ECCV24 | Data-to-Model Distillation | E6 | Dataset → model distillation, no teacher network |
| ECCV24 | BKDSNN | E4 | SNN students |
| ECCV24 | AMD: Automatic Multi-step Distillation | E4 | Large-model (ViT) distillation, no standard pair |
| ECCV24 | Role of Masking for Supervised KD of ViTs | E4 | ViT students |
| ECCV24 | Dynamic Guidance Adversarial Distillation | E4 | Adversarial robustness, WRN-34-10 |
| ECCV24 | Markov KD (nasty teachers) | E4 | Nasty-teacher setting, no standard pair |
| ECCV22 | Multi-Teacher Adversarial Distillation | E4 | Adversarial robustness |
| ECCV22 | Zipf's Label Smoothing (one-pass self-KD) | E4 | Self-distillation |
| ECCV22 | Prune Your Model before Distill It | E4 | Pruned-teacher setting, no standard pair |
| ECCV22 | Distilling the Undistillable (nasty teacher) | E4 | No standard pair |
| ECCV22 | Black-Box Few-Shot KD | E4 | Black-box few-shot, no standard pair |
| ECCV22 | MixSKD | E4 | Self-KD, no teacher pair |
| ECCV22 | A Fast KD Framework (FKD) | E4 | Pre-computed soft labels, ResNet-50 student |
| ECCV22 | Self-Regulated Feature Learning (teacher-free) | E4 | Teacher-free |

Totals: E4 55, E1 3 (DisWOT, Auto-DAS, Bad Students), E6 1 = 59.

## 5. Limitations

- **L1 Title-only identification.** CVF and ECVA listings do not show abstracts. A KD method whose title avoids
  distill/teacher/student/knowledge transfer is missed. S3 snowballing should catch these.
- **L2 Title-screen codes.** Codes for the 559 title exclusions were tallied with a keyword rule after reading every title (§2). The split is approximate. The include/exclude decision is not.
- **L3 Existing entries.** ImageNet numbers marked `n/x` were not re-extracted in this pass.
- **L4** One PDF was not retrieved, and ECCV 2026 is not yet online (§1).
