# State-of-the-art KD inventory (survey Task 4b)

Verified list of the knowledge-distillation (KD) methods that the survey covers in depth, grouped by category.
It is the input to **Checkpoint A**. Compiled 2026-11-03 by the Claude T4b worker (Orca task `task_7875006d423f`).
Every entry has a record in `literature/sources.yaml` under the id shown. Full author lists, URLs and the exact
verification trail are in that registry. This file gives a summary.

## How to read this file

**Tags**

| Tag | Meaning |
|---|---|
| **CORE** | Meets the SOTA criterion in `tasks/plan.md`: published 2022–2026 at CVPR / ICCV / ECCV / NeurIPS / ICML / ICLR / AAAI / TMLR / TPAMI / IJCV. |
| **CORE-P** | A 2025–2026 preprint with results on a standard benchmark. The survey must cite it with a "(preprint)" qualifier. |
| **CORE-A** | Acceptance at a listed venue is stated by the authors (arXiv comment). The proceedings page did not exist yet or was not checked. Cite it as "to appear". |
| **CLASSIC** | Background and lineage only (pre-2022, or a foundational method). It is not discussed as state of the art. |
| **SUPPORT** | Relevant evidence that does not meet the criterion (non-listed venue, or an analysis paper). Use it only for specific claims. |
| **WITHDRAWN** | Withdrawn or superseded. Do not cite it as a method. |

**How each entry was verified (all checks done on 2026-11-03)**
- **Metadata:** the arXiv API (title, authors, v1 date, author comment) for every arXiv paper.
- **Venue:** checked against the official proceedings wherever one was reachable.
  - CVF open-access listings for CVPR 2022–2025 and ICCV 2023/2025, plus CVF paper pages for the older classics.
  - NeurIPS proceedings listings for 2020 and 2022–2024.
  - ICLR proceedings listings for 2024–2026. The 2023 listing was unreachable, so for ICLR 2023 I used the PDF header "Published as a conference paper at ICLR 2023".
  - PMLR v235 and v267 for ICML 2024 and 2025.
  - The jmlr.org TMLR listing.
  - ecva.net for ECCV 2022.
  - Crossref DOIs for AAAI and TPAMI.
- **Headline numbers:** taken only from the primary paper, by reading its PDF text (pdftotext). The table number is given in each entry. The only exception is DOT, whose number comes from the official README.
- **Code and licence:** the GitHub API, for each repository linked from the paper, abstract or official README. "none" means the repository has no LICENSE file.

**Evidence labels:** the facts in the tables are **VERIFIED** as described above. Comments marked
*INTERPRETATION* are my own judgement.

> **Caution on numbers (VERIFIED, important for Table II).** Different papers report the same method on the same pair
> with different numbers, because they use different reproductions, teachers and augmentations. Three examples:
> - LSKD reports KD+LS = 76.62 (its Table 2), but LDRLD's Table 1 lists LSKD at 76.16.
> - SimKD's 78.08 uses its own student baseline (73.09) and KD baseline (74.42). The usual CRD-protocol values are 72.50 and 73.33.
> - VkD (CVPR 2024) states that the CIFAR-100 benchmark is "increasingly saturated" and that some gains may be regularisation rather than better distillation.
>
> The headline numbers below are each paper's *own* claim. They are not a leaderboard and must not be ranked against one another without that caveat.

Unless stated otherwise, "R32×4→R8×4" means CIFAR-100 top-1 (%) with a ResNet32×4 teacher and a ResNet8×4 student.
On this pair, vanilla KD scores 73.33 in the CRD protocol. "ImageNet R34→R18" means ImageNet-1K top-1 (%) with a ResNet-34 teacher and a ResNet-18 student.

---

## 1. Logit-based KD

| # | Tag | Method (`id`) | Exact title | Authors | Year | Venue | arXiv / DOI | Code (licence) | Key idea | Headline number (source) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CORE | DKD (`zhao2022dkd`) | Decoupled Knowledge Distillation | Zhao, Cui, Song, Qiu, Liang | 2022 | CVPR 2022 (published) | 2203.08679 | megvii-research/mdistiller (MIT) | Splits KD into target-class (TCKD) and non-target (NCKD) terms with separate weights | R32×4→R8×4 **76.32** (Table 6) |
| 2 | CORE | DIST (`huang2022dist`) | Knowledge Distillation from A Stronger Teacher | Huang, You, Wang, Qian, Xu | 2022 | NeurIPS 2022 | 2205.10536 | hunto/DIST_KD (Apache-2.0) | Pearson-correlation (inter- and intra-class relation) matching instead of exact KL; robust to strong teachers | R32×4→R8×4 **76.31** (Table 5); ImageNet R34→R18 **72.07** (Table 2) |
| 3 | CORE | CTKD (`li2023ctkd`) | Curriculum Temperature for Knowledge Distillation | Li, Li, Yang, et al. (8) | 2023 | AAAI 2023 | 2211.16231 / 10.1609/aaai.v37i2.25236 | zhengli97/CTKD (Apache-2.0) | Learnable, adversarially scheduled temperature (easy-to-hard curriculum); plug-in | ImageNet R34→R18 KD 70.83 → KD+CTKD **71.32** (Table 4) |
| 4 | CORE | MLKD (`jin2023mlkd`) | Multi-Level Logit Distillation | Jin, Wang, Lin | 2023 | CVPR 2023 | none (CVF only) | Jin-Ying/Multi-Level-Logit-Distillation (none) | Instance-, batch- and class-level prediction alignment with multiple temperatures | R32×4→R8×4 **77.08** (Table 2) |
| 5 | CORE | NKD / USKD (`yang2023nkd`) | From Knowledge Distillation to Self-Knowledge Distillation: A Unified Approach with Normalized Loss and Customized Soft Labels | Yang, Zeng, Li, et al. (6) | 2023 | ICCV 2023 | 2303.13005 | yzd-v/cls_KD (Apache-2.0) | Normalised non-target loss (NKD); teacher-free customised soft labels (USKD) | R32×4→R8×4 **76.35**; ImageNet R34→R18 **71.96** (Table 1) |
| 6 | CORE | WTTM (`zheng2024wttm`) | Knowledge Distillation Based on Transformed Teacher Matching | Zheng, Yang | 2024 | ICLR 2024 | 2402.11148 | zkxufo/TTM (MIT) | Temperature on the teacher only (Rényi-entropy regulariser view), with sample-adaptive weights | R32×4→R8×4 **76.06** (Table 2); ImageNet R34→R18 **72.19** (Table 5) |
| 7 | CORE | LSKD (`sun2024lskd`) | Logit Standardization in Knowledge Distillation | Sun, Ren, Li, Wang, Cao | 2024 | CVPR 2024 | 2403.01427 | sunshangquan/logit-standardization-KD (none) | Z-score standardisation of logits before softmax; plug-in for KD/CTKD/DKD/MLKD | R32×4→R8×4 KD+LS **76.62**, MLKD+LS **78.28** (Table 2) |
| 8 | CORE | SDD (`wei2024sdd`) | Scale Decoupled Distillation (CVF title: "Scaled Decoupled Distillation") | Wei, Luo, Luo | 2024 | CVPR 2024 | 2403.13512 | shicaiwei123/SDD-CVPR2024 (MIT) | Multi-scale pooled logits split into consistent and complementary local terms | ImageNet R34→R18 SD-NKD **72.33**, SD-DKD **72.02** (Table 3) |
| 9 | CORE | WKD (`lv2024wkd`) | Wasserstein Distance Rivals Kullback-Leibler Divergence for Knowledge Distillation | Lv, Yang, Li | 2024 | NeurIPS 2024 | 2412.08139 | JiamingLv/WKD (none) | Discrete Wasserstein distance over cross-category relations (WKD-L) and Gaussian Wasserstein distance on features (WKD-F) | R32×4→R8×4 WKD-L **76.53**, L+F **77.28** (Table 11); ImageNet R34→R18 WKD-L **72.49** (Table 4) |
| 10 | CORE | LumiNet (`hossain2025luminet`) | LumiNet: Perception-Driven Knowledge Distillation via Statistical Logit Calibration | Hossain, Elahi, Ramasinghe, et al. (7) | 2025 | TMLR (Aug 2025) | 2310.03669 | ismail31416/LumiNet (none) | Recalibrates logits against intra-batch class statistics before distillation | R32×4→R8×4 **77.50** (Table 1) |
| 11 | CORE | RLD (`sun2025rld`) | Knowledge Distillation with Refined Logits | Sun, Chen, Lyu, et al. (6) | 2025 | ICCV 2025 | 2408.07703 | zju-SWJ/RLD (none) | Uses labels to refine teacher logits so wrong teacher predictions do not mislead the student (also §4) | R32×4→R8×4 **76.64** (Table 1) |
| 12 | CORE | LDRLD (`xu2025ldrld`) | Local Dense Logit Relations for Enhanced Knowledge Distillation | Xu, Liu, Liu, et al. (6) | 2025 | ICCV 2025 | 2507.15911 | yema-web/LDRLD (BSD-2-Clause) | Recursive decoupling into local class pairs; distils dense pairwise logit relations with adaptive decay weights | R32×4→R8×4 **77.20** (Table 1) |
| 13 | CORE | EKD (`xiang2025ekd`) | Evidential Knowledge Distillation | Xiang, Gao, Xu | 2025 | ICCV 2025 | none (CVF only) | lyxiang-casia/EKD → now Liangyu-Xiang/EKD (none) | Second-order (evidential) distribution over class probabilities; distils its expectation and the distribution itself | R32×4→R8×4 **77.21** (Table 1) |
| — | cross-ref | ABKD (`wang2025abkd`) | see §6 LLM | | 2025 | ICML 2025 | | | α-β-divergence also evaluated on CIFAR-100 | §6 |
| — | cross-ref | DOT (`zhao2023dot`) | see §5 | | 2023 | ICCV 2023 | | | Optimizer-side; works on top of KD/DKD | §5 |
| C1 | CLASSIC | KD (`hinton2015kd`) | Distilling the Knowledge in a Neural Network | Hinton, Vinyals, Dean | 2015 | NIPS 2014 DL Workshop | 1503.02531 | — | Temperature-softened teacher targets | — |

*INTERPRETATION:* the 2024–2025 frontier on R32×4→R8×4 sits at about 77–78 (LumiNet, LDRLD, EKD, MLKD+LS).
Gains over DKD (76.32) are now about 1–2 points and within the cross-paper reproduction spread noted above.
The open question is no longer "a better divergence" alone. It is *which* teacher signal to trust (RLD) and how the KD term interacts with the task loss (§5).

## 2. Feature- and relation-based KD

| # | Tag | Method (`id`) | Exact title | Authors | Year | Venue | arXiv / DOI | Code (licence) | Key idea | Headline number (source) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CORE | SimKD (`chen2022simkd`) | Knowledge Distillation with the Reused Teacher Classifier | Chen, Mei, Zhang, et al. (6) | 2022 | CVPR 2022 | 2203.14001 | DefangChen/SimKD (none) | Projector-aligned penultimate feature; the frozen teacher classifier is reused at inference | R32×4→R8×4 **78.08** (Table 1; own baselines, see caution) |
| 2 | CORE | FCFD (`liu2023fcfd`) | Function-Consistent Feature Distillation | Liu, Kan, Shan, Chen | 2023 | ICLR 2023 | 2304.11832 | LiuDongyang6/FCFD (none) | Student features made functionally consistent by routing them through the teacher's later layers | R32×4→R8×4 **76.62** (Table 1) |
| 3 | CORE | NORM (`liu2023norm`) | NORM: Knowledge Distillation via N-to-One Representation Matching | Liu, Li, Li, Yao | 2023 | ICLR 2023 | 2305.13803 | OSVAI/NORM (BSD-2-Clause) | N-fold expanded student feature matched slice-wise to the teacher feature; merged after training | R32×4→R8×4 **76.49**, +KD 76.98 (Table 1) |
| 4 | CORE | CAT-KD (`guo2023catkd`) | Class Attention Transfer Based Knowledge Distillation | Guo, Yan, Li, Lin | 2023 | CVPR 2023 | 2304.12777 | GzyAftermath/CAT-KD (none) | Transfers class activation maps (class attention) | R32×4→R8×4 **76.91** (Table 6) |
| 5 | CORE | DiffKD (`huang2023diffkd`) | Knowledge Diffusion for Distillation | Huang, Zhang, Zheng, et al. (7) | 2023 | NeurIPS 2023 | 2305.15712 | hunto/DiffKD (Apache-2.0) | Denoises student features with a lightweight diffusion model before matching | R32×4→R8×4 **76.72** (Table 9, appendix) |
| 6 | CORE | OFA-KD (`hao2023ofakd`) | One-for-All: Bridge the Gap Between Heterogeneous Architectures in Knowledge Distillation | Hao, Guo, Han, et al. (7) | 2023 | NeurIPS 2023 | 2310.19444 | Hao840/OFAKD (none) | Projects intermediate features of heterogeneous students into logit space and boosts target-class signal | ImageNet Swin-T→ResNet18 **71.85** (KD 71.14) (Table 1) |
| 7 | CORE | VkD (`miles2024vkd`) | VkD: Improving Knowledge Distillation using Orthogonal Projections | Miles, Elezi, Deng | 2024 | CVPR 2024 | 2403.06213 | roymiles/vkd (none) | Orthogonal projector plus task-specific normalisation | CIFAR-100 R32×4→ShuffleNetV2 **77.51** (Table 7) |
| 8 | CORE | Projector study (`miles2024projector`) | Understanding the Role of the Projector in Knowledge Distillation | Miles, Mikolajczyk | 2024 | AAAI 2024 | 2303.11098 / 10.1609/aaai.v38i5.28219 | roymiles/Simple-Recipe-Distillation (none) | Projector, normalisation and a LogSum loss are enough; relational-gradient view of the projector | ImageNet R34→R18 top-1 error **28.37%** (KD 29.34%) (Table 6) |
| 9 | CORE | TCS (`zhou2025tcs`) | All You Need in Knowledge Distillation Is a Tailored Coordinate System | Zhou, Zhu, Wu | 2025 | AAAI 2025 | 2412.09388 / 10.1609/aaai.v39i21.34457 | none found | PCA coordinate system from the teacher in one forward pass; student features aligned to it | CIFAR-100 ConvNeXt-T→ResNet18 **81.60** (OFA 80.91) (Table 1) |
| 10 | CORE | VRM (`zhang2025vrm`) | VRM: Knowledge Distillation via Virtual Relation Matching | Zhang, Xie, Cai, Ma | 2025 | ICCV 2025 (Highlight per arXiv) | 2502.20760 | none found | Affinity graphs over real and virtually augmented samples; unreliable edges pruned | R32×4→R8×4 **78.76** (Table 1) |
| 11 | CORE | RSD (`zhang2025rsd`) | Cross-Architecture Distillation Made Simple with Redundancy Suppression | Zhang, Liu, Ran, Ma | 2025 | ICCV 2025 | none (CVF only) | none found | Cross-architecture KD as redundancy suppression (invariance + decorrelation) | **not extracted** (abstract: beats OFA on CIFAR-100 and ImageNet-1k); RPKD Table 3 gives 72.18 (secondary) |
| 12 | CORE-A | RPKD (`etcibasi2026rpkd`) | You Don't Need Aligned Representations: Knowledge Distillation via Random Prototype Spaces | Etcibasi, Cinbis | 2026 | NeurIPS 2026 (author-stated) | 2610.37937 | HamzaEtcibasi/RPKD (MIT) | Matches similarity distributions over shared random prototypes; no representation alignment needed | ImageNet DeiT-T→MobileNetV2 **72.67** (OFA 71.39) (Table 3) |
| — | cross-ref | WKD-F (`lv2024wkd`), SPOFA (`yang2026spofa`, §5) | | | | | | | Feature and heterogeneous variants | WKD-F 76.77; SPOFA §5 |
| C1 | CLASSIC | FitNets (`romero2015fitnets`) | FitNets: Hints for Thin Deep Nets | Romero, Ballas, Kahou, et al. | 2014 | venue not verified | 1412.6550 | — | Feature hints | — |
| C2 | CLASSIC | AT (`zagoruyko2017at`) | Paying More Attention to Attention: … via Attention Transfer | Zagoruyko, Komodakis | 2016 | venue not verified | 1612.03928 | szagoruyko/attention-transfer | Attention maps | — |
| C3 | CLASSIC | RKD (`park2019rkd`) | Relational Knowledge Distillation | Park, Kim, Lu, Cho | 2019 | CVPR 2019 | 1904.05068 | — | Distance and angle relations | — |
| C4 | CLASSIC | CRD (`tian2020crd`) | Contrastive Representation Distillation | Tian, Krishnan, Isola | 2019 | ICLR 2020 (author-stated) | 1910.10699 | HobbitLong/RepDistiller | Contrastive features; defines the CIFAR-100 protocol | — |
| C5 | CLASSIC | ReviewKD (`chen2021reviewkd`) | Distilling Knowledge via Knowledge Review | Chen, Liu, Zhao, Jia | 2021 | CVPR 2021 | 2104.09044 | Jia-Research-Lab/ReviewKD | Cross-stage feature review | — |

*INTERPRETATION:* since 2023 the feature line has moved toward **heterogeneous / cross-architecture** KD
(OFA → TCS → RSD → RPKD, plus SPOFA in §5), because CNN-to-CNN CIFAR-100 gains have saturated (VkD).

## 3. Training schemes

| # | Tag | Scheme | Method (`id`) | Exact title | Authors | Year | Venue | arXiv / DOI | Code (licence) | Key idea | Headline number (source) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CORE | online / mutual | L-MCL (`yang2023lmcl`) | Online Knowledge Distillation via Mutual Contrastive Learning for Visual Recognition | Yang, An, Zhou, et al. (6) | 2023 | IEEE TPAMI 2023 | 2207.11518 / 10.1109/TPAMI.2023.3257878 | winycg/L-MCL (none) | Mutual contrastive learning between peers plus meta-optimised layer-wise transfer | ImageNet ResNet-18 **71.38** (DML 70.60) (Table 5) |
| 2 | CORE | online / mutual | SwitOKD (`qian2022switokd`) | Switchable Online Knowledge Distillation | Qian, Wang, Yin, Hong, Wang | 2022 | ECCV 2022 | 2209.04996 / 10.1007/978-3-031-20083-0_26 | hfutqian/SwitOKD (Apache-2.0) | Teacher pauses ("expert mode") when the gap grows; adaptive switching threshold | ImageNet R34/R18 pair, student **71.75** (DML 70.81) (Table 6) |
| 3 | CORE | self-distillation | DLB (`shen2022dlb`) | Self-Distillation from the Last Mini-Batch for Consistency Regularization | Shen, Xu, Yang, Li, Guo | 2022 | CVPR 2022 | 2203.16172 | Meta-knowledge-Lab/DLB (MIT) | Previous mini-batch's soft predictions are the targets; no extra network | CIFAR-100 ResNet-32 error **26.00** vs 28.26 (Table 2) |
| 4 | CORE | self-distillation | USKD (`yang2023nkd`) | see §1 #5 | | 2023 | ICCV 2023 | | | Teacher-free customised soft labels | §1 |
| 5 | CORE | self-distillation (theory) | Label-averaging view (`jeong2025selfdistill`) | Rethinking Self-Distillation: Label Averaging and Enhanced Soft Label Refinement with Partial Labels | Jeong, Chung | 2025 | ICLR 2025 | 2402.10482 | none found | Multi-round self-distillation as label averaging; one-round partial-label refinement | Theory: conditions for 100% population accuracy under label noise (abstract) |
| 6 | CORE | multi-teacher | MTKD-RL (`yang2025mtkdrl`) | Multi-Teacher Knowledge Distillation with Reinforcement Learning for Visual Recognition | Yang, Yu, Yang, et al. (7) | 2025 | AAAI 2025 | 2502.18510 / 10.1609/aaai.v39i9.32990 | winycg/MTKD-RL (none) | RL agent sets per-sample teacher weights | ImageNet ResNet-34 student **76.77** vs AE-KD 75.66 (Table 2) |
| 7 | CORE | capacity gap | ATS (`li2022ats`) | Asymmetric Temperature Scaling Makes Larger Networks Teach Well Again | Li, Fan, Song, et al. (7) | 2022 | NeurIPS 2022 | 2210.04427 | none found | Separate temperatures for target and non-target classes | CIFAR-100 WRN28-8→ShuffleNetV1 KD 70.87 → **73.58** (Table 2) |
| 8 | CORE | capacity gap | DPK (`qiu2023dpk`) | Better Teacher Better Student: Dynamic Prior Knowledge for Knowledge Distillation | Qiu, Ma, Yang, et al. (7) | 2023 | ICLR 2023 | 2206.06067 | none found | Teacher features fed as dynamic prior (masked mixing) | ImageNet R34→R18 **72.51** (Table 2) |
| 9 | CORE | capacity gap | AID (`qian2025aid`) | A Good Teacher Adapts Their Knowledge for Distillation | Qian, Le, Harandi | 2025 | ICCV 2025 | none (CVF only) | none found | Fine-tunes the teacher's intra-class distribution to suit the student | CIFAR-100 ResNet8 student, size ratio 340: **63.44** vs KD 61.47 (Table 1) |
| 10 | CORE | data-free | NAYER (`tran2024nayer`) | NAYER: Noisy Layer Data Generation for Efficient and Effective Data-free Knowledge Distillation | Tran, Le, Le, et al. (6) | 2024 | CVPR 2024 | 2310.00258 | tmtuan1307/NAYER (none) | Noisy layer replaces noisy input; label-text embedding as generator input | CIFAR-100 R34→R18 (data-free) **77.54** (Table 1) |
| 11 | CORE | data-free | SSD-KD (`liu2024ssdkd`) | Small Scale Data-Free Knowledge Distillation | Liu, Wang, Liu, Sun, Yao | 2024 | CVPR 2024 | 2406.07876 | OSVAI/SSD-KD (Apache-2.0) | Small synthetic set with difficulty/diversity priority sampling | CIFAR-100 R34→R18 **75.16 in 4.22 h** vs CMI 77.04 in 15.42 h (Table 2) |
| — | cross-ref | capacity gap | DIST (§1), TAID / AMiD (§6), AGRE-KD (§4, multi-teacher) | | | | | | | | |
| C1 | CLASSIC | online | DML (`zhang2018dml`) | Deep Mutual Learning | Zhang, Xiang, Hospedales, Lu | 2018 | CVPR 2018 | 1706.00384 | — | Peers teach each other | — |
| C2 | CLASSIC | self | BYOT (`zhang2019byot`) | Be Your Own Teacher: … via Self Distillation | Zhang, Song, Gao, et al. | 2019 | ICCV 2019 | 1905.08094 | — | Deep-to-shallow self-KD | — |
| C3 | CLASSIC | capacity gap | TAKD (`mirzadeh2020takd`) | Improved Knowledge Distillation via Teacher Assistant | Mirzadeh, Farajtabar, Li, et al. | 2019 | AAAI 2020 (author-stated) | 1902.03393 | — | Teacher-assistant chain | — |
| C4 | CLASSIC | data-free | DeepInversion (`yin2020deepinversion`) | Dreaming to Distill: Data-free Knowledge Transfer via DeepInversion | Yin, Molchanov, Li, et al. | 2020 | CVPR 2020 | 1912.08795 | NVlabs/DeepInversion | BatchNorm-statistics inversion | — |
| C5 | CLASSIC | multi-teacher | AE-KD (`du2020aekd`) | Agree to Disagree: Adaptive Ensemble Knowledge Distillation in Gradient Space | Du, You, Li, et al. (7) | 2020 | NeurIPS 2020 | — | — | MGDA-style teacher weighting (also §5) | — |

## 4. Teacher reliability and selective transfer

| # | Tag | Method (`id`) | Exact title | Authors | Year | Venue | arXiv / DOI | Code (licence) | Key idea | Headline number (source) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CORE | RLD (`sun2025rld`) | Knowledge Distillation with Refined Logits | Sun, Chen, Lyu, et al. (6) | 2025 | ICCV 2025 | 2408.07703 | zju-SWJ/RLD (none) | Label-refined teacher logits; fixes the KD/CE inconsistency when the teacher is wrong | R32×4→R8×4 **76.64** (Table 1) |
| 2 | CORE | TGeo-KD (`hu2024tgeokd`) | Less or More From Teacher: Exploiting Trilateral Geometry For Knowledge Distillation | Hu, Wu, Li, et al. (8) | 2024 | ICLR 2024 | 2312.15112 | none found | Learns a per-sample teacher-vs-label fusion ratio from student–teacher–label geometry | R32×4→R8×4 **77.27** (Table 1) |
| 3 | CORE | EA-KD (`su2025eakd`) | EA-KD: Entropy-based Adaptive Knowledge Distillation | Su, Tseng, Pu, et al. (7) | 2025 | ICCV 2025 | 2311.13621 | cpsu00/EA-KD (none) | Per-sample weights from teacher and student entropy; plug-in | ImageNet R34→R18 KD 71.03 → **71.79** (Table 4) |
| 4 | CORE | AGRE-KD (`kenfack2025agrekd`) | Adaptive Group Robust Ensemble Knowledge Distillation | Kenfack, Aïvodji, Kahou | 2025 | TMLR (11/2025) | 2411.14984 | patrikken/AGRE-KD (none) | Gradient-based teacher selection against a biased model, for worst-group robustness | Waterbirds worst-group accuracy **91.1** vs AE-KD 89.0 (Table 2) |
| 5 | CORE-A | CaRE-Div / selective LLM-KD (`sengupta2026casd`) | Distilling What Matters: Confidence-Aware Selective Distillation for Large Language Models | Sengupta, Seth, Chakraborty | 2026 | NeurIPS 2026 (author-stated) | 2609.36734 | none found | Confidence-aware selective divergence plus a "Revival" step for LLM KD | GPT2-XL→GPT2-base average ROUGE-L **19.6** vs FKL 17.0 (Table 1) |
| 6 | CORE-P | TPKD (`yuan2026tpkd`) | Learning Beyond Full Imitation: Task-Preserving Knowledge Distillation | Yuan, Tao | 2026 | arXiv preprint | 2609.39338 | none found | Projects teacher directions so task margins are preserved (also §5) | CIFAR-100 **88.05%**, +0.47 pp over standard KD, 3 seeds (abstract; setting not read) |
| — | cross-ref | SAAD (`lee2025saad`, §6 robust) | | | 2025 | TMLR | | | Sample-wise transfer-consistency weighting | §6 |
| S1 | SUPPORT | CHAD / EWAD (`sumit2026chad`) | When Does Knowledge Distillation Hurt? Reliability-Aware Distillation for Low-Resource Language Summarization | Sumit, Srizon, Rodela, et al. (7) | 2026 | arXiv preprint | 2607.19956 | none | Estimates per-sample harmful distillation; reliability-aware gating | **Contradicting evidence:** on BanSum, standard KD adds only +0.0003 ROUGE-L, and about 51.3% of samples harm validation loss (abstract) |
| S2 | SUPPORT | SCOPE (`chen2026scope`) | Selective Confidence-Guided Projection-Based Encoding for Medical Image Classification | Chen, Zhou, Wang, et al. | 2026 | Journal of Imaging (not a listed venue) | 10.3390/jimaging12090436 | — | Classification-priority conflict removal plus confidence-weighted relations | not re-checked in T4b |

## 5. KD with multi-objective optimisation (MOO)

| # | Tag | Method (`id`) | Exact title | Authors | Year | Venue | arXiv / DOI | Code (licence) | Key idea | Headline number (source) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CORE | DTO-KD (`hayder2026dtokd`) | DTO-KD: Dynamic Trade-off Optimization for Effective Knowledge Distillation | Hayder, Cheraghian, Petersson, Harandi, Hartley | 2026 | ICLR 2026 | — (proceedings page) | none on the proceedings page | FAMO-style min-norm convex combination of the log-loss gradients of task and distillation; closed-form weights | R32×4→R8×4 **76.40** (Table 2; that table lists DKD at 75.44) |
| 2 | CORE | DOT (`zhao2023dot`) | DOT: A Distillation-Oriented Trainer | Zhao, Cui, Song, Liang | 2023 | ICCV 2023 | 2307.08436 | megvii-research/mdistiller (MIT) | Separate, larger momentum for the KD gradient than for the task gradient | R32×4→R8×4 KD 73.33 → KD+DOT **75.12**; ImageNet R34→R18 **71.72** (mdistiller README) |
| 3 | CORE | MOO adversaries (`dong2025mooadv`) | Confound from All Sides, Distill with Resilience: Multi-Objective Adversarial Paths to Zero-Shot Robustness | Dong, Liu, Qu, Ong | 2025 | ICCV 2025 | none (CVF only) | none found | Tchebycheff/Riesz-energy MOO generates diverse targeted adversaries for robust VLM→small distillation | **not extracted** (tables not machine-readable) |
| 4 | CORE-P | SPOFA (MEMA scaler) (`yang2026spofa`) | Heterogeneous Knowledge Distillation via Geometry Decoupling and Momentum-Aware Gradient Regulation | Yang, Zhang, Zhao | 2026 | arXiv, under review | 2606.24557 | none found | LayerNorm projector plus momentum-EMA gradient-consistency baseline that damps conflicting KD signal | CIFAR-100 Swin-T→ResNet18 **82.39** vs OFA 80.54 (Table I) |
| 5 | CORE-P | TPKD (`yuan2026tpkd`) | see §4 #6 | | 2026 | preprint | 2609.39338 | | Asymmetric projection protecting task margins | §4 |
| 6 | CORE-P | UP-MOPD (`zhu2026upmopd`) | UP-MOPD: Update Projection in Multi-Teacher On-Policy Distillation | Zhu, Jin, Xia, et al. (11) | 2026 | arXiv preprint | 2610.08398 | none found | Projects conflicting per-teacher updates in multi-teacher on-policy LLM KD | IFEval-loose **+2.96** points over vanilla multi-teacher OPD (abstract) |
| 7 | CORE-A | DHO (`kang2025dho`) | Simple yet Effective Semi-supervised Knowledge Distillation from Vision-Language Models via Dual-Head Optimization | Kang, Lee, Jang, Hwang | 2025 | NeurIPS 2026 (author-stated) | 2505.07675 | erjui/DHO (none) | Separate CE and KD heads; *measures* the CE–KD gradient conflict (cos about −0.4 to −0.76) | ImageNet semi-supervised **+3% / +0.1%** at 1% / 10% labels (Sec. 1) |
| C1 | CLASSIC | AE-KD (`du2020aekd`) | Agree to Disagree: Adaptive Ensemble Knowledge Distillation in Gradient Space | Du, You, Li, et al. | 2020 | NeurIPS 2020 | — | — | Multi-teacher KD as MGDA with a disagreement tolerance | — |
| C2 | CLASSIC | SCKD (`zhu2021sckd`) | Student Customized Knowledge Distillation: Bridging the Gap Between Student and Teacher | Zhu, Wang | 2021 | ICCV 2021 | 10.1109/ICCV48922.2021.00501 | — | Gradient-similarity gating of KD terms | — |
| S1 | SUPPORT | CHAD (`sumit2026chad`) | see §4 S1 | | 2026 | preprint | | | | |
| S2 | SUPPORT | PCD (`varam2026pcd`) | Not All Objectives Are Born Equal: Priority-Constrained Descent for Hierarchical Multi-Objective Optimization | Varam, AlHajri | 2026 | TMLR | 2606.29521 | DaraVaram/priority-constrained-descent (MIT) | Prioritised (lexicographic) MOO update | A general MOO method with **no KD results** (pruning/sparsity only). Include as one MOO method, not as KD state of the art. |
| W1 | WITHDRAWN | MoKD (`hayder2025mokd`) | MoKD: Multi-Task Optimization for Knowledge Distillation | Hayder, Cheraghian, Petersson, Harandi | 2025 | withdrawn (arXiv v2) | 2505.08170 | — | — | Superseded by DTO-KD (*INTERPRETATION*: same first four authors plus Hartley) |

*INTERPRETATION:* only two peer-reviewed methods treat the task-vs-distillation trade-off itself as an
optimisation problem: DTO-KD (ICLR 2026, symmetric min-norm) and DOT (ICCV 2023, momentum separation).
The rest are 2026 preprints (SPOFA, TPKD, UP-MOPD) or use MOO elsewhere: for adversary generation (Dong et al.) or for teacher weighting (AE-KD).
This is a genuinely thin area. The survey should say so rather than pad it.

## 6. Emerging settings

### 6a. LLM distillation

| # | Tag | Method (`id`) | Exact title | Authors | Year | Venue | arXiv / DOI | Code (licence) | Key idea | Headline number (source) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CORE | MiniLLM (`gu2024minillm`) | MiniLLM: On-Policy Distillation of Large Language Models | Gu, Dong, Wei, Huang | 2024 | ICLR 2024 | 2306.08543 | microsoft/LMOps (MIT, archived) | Reverse KL optimised with policy gradient on student samples | LLaMA-13B→7B DollyEval GPT-4 score **76.4** vs KD 73.7 (Table 1) |
| 2 | CORE | GKD (`agarwal2024gkd`) | On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes | Agarwal, Vieillard, Zhou, et al. (7) | 2024 | ICLR 2024 | 2306.13649 | no official code | On-policy student samples, teacher feedback, generalised JSD | Relative gains of **2.1×** (summarisation) and **1.7×** (translation) over the initial T5 student (Sec. 1) |
| 3 | CORE | DistiLLM (`ko2024distillm`) | DistiLLM: Towards Streamlined Distillation for Large Language Models | Ko, Kim, Chen, Yun | 2024 | ICML 2024 | 2402.03898 | jongwooko/distillm (none) | Skew KL plus adaptive off-policy replay | Up to **4.3×** training speedup vs recent KD methods (abstract) |
| 4 | CORE | DistiLLM-2 (`ko2025distillm2`) | DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs | Ko, Chen, Kim, et al. (7) | 2025 | ICML 2025 | 2503.07067 | jongwooko/distillm-2 (none) | Contrastive objective: raise teacher-response, lower student-response likelihood | Qwen2-7B→1.5B average win rate **58.69** vs DistiLLM 56.35 (Table 2) |
| 5 | CORE | TAID (`shing2025taid`) | TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models | Shing, Misaki, Bao, Yokoi, Akiba | 2025 | ICLR 2025 | 2501.16937 | SakanaAI/TAID (Apache-2.0) | Target interpolated from student to teacher with an adaptive schedule (capacity gap) | Phi-3-mini→TinyLlama MT-Bench **4.05** vs KL 2.71 (Table 1) |
| 6 | CORE | ABKD (`wang2025abkd`) | ABKD: Pursuing a Proper Allocation of the Probability Mass in Knowledge Distillation via α-β-Divergence | Wang, Yang, Wang, et al. (6) | 2025 | ICML 2025 | 2505.04560 | ghwang-s/abkd (none) | α-β-divergence interpolating forward and reverse KL | GPT-2 XL→GPT-2 Dolly ROUGE-L **25.65** vs DistiLLM 25.32 (Table 2) |
| 7 | CORE | AMiD (`shin2026amid`) | AMiD: Knowledge Distillation for LLMs with α-mixture Assistant Distribution | Shin, Kim, Jo, Na, Moon | 2026 | ICLR 2026 | 2510.15982 | aailab-kaist/AMiD (Apache-2.0) | α-mixture family of assistant distributions | **not extracted** (PDF text unreadable) |
| — | cross-ref | CaRE-Div (§4), UP-MOPD (§5) | | | | | | | | | |

### 6b. VLM → small models

| # | Tag | Method (`id`) | Exact title | Authors | Year | Venue | arXiv / DOI | Code (licence) | Key idea | Headline number (source) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CORE | TinyCLIP (`wu2023tinyclip`) | TinyCLIP: CLIP Distillation via Affinity Mimicking and Weight Inheritance | Wu, Peng, Zhou, et al. (12) | 2023 | ICCV 2023 | 2309.12314 | wkcn/TinyCLIP (NOASSERTION) | Cross-modal affinity mimicking plus weight inheritance | ViT-8M/16 zero-shot ImageNet **41.1%** (abstract) |
| 2 | CORE | CLIP-KD (`yang2024clipkd`) | CLIP-KD: An Empirical Study of CLIP Model Distillation | Yang, An, Huang, et al. (8) | 2024 | CVPR 2024 | 2307.12732 | winycg/CLIP-KD (none) | Systematic study; simple feature mimicry works best | ViT-B/16 student **57.5%** zero-shot ImageNet with ViT-L/14 teacher (Sec. 1) |
| 3 | CORE | PromptKD (`li2024promptkd`) | PromptKD: Unsupervised Prompt Distillation for Vision-Language Models | Li, Li, Fu, et al. (7) | 2024 | CVPR 2024 | 2403.02781 | zhengli97/PromptKD (Apache-2.0) | Prompted large CLIP teacher distils into a lightweight student on unlabeled images | **+2.70 / +4.63** points (base / new classes) on 11 datasets (abstract) |
| 4 | CORE | VL2Lite (`jang2025vl2lite`) | VL2Lite: Task-Specific Knowledge Distillation from Large Vision-Language Models to Lightweight Networks | Jang, Ma, Lee | 2025 | CVPR 2025 | none (CVF only) | jsjangAI/VL2Lite (none) | VLM knowledge distilled into CNN classifiers at training time only | Up to **7%** classification improvement (abstract) |
| 5 | CORE-A | DHO (`kang2025dho`) | see §5 #7 | | 2025 | NeurIPS 2026 (author-stated) | 2505.07675 | erjui/DHO | Dual-head semi-supervised KD from VLMs | §5 |
| — | cross-ref | MOO adversaries (`dong2025mooadv`, §5) | | | | | | | Robust VLM→small | |

### 6c. Adversarially robust KD

| # | Tag | Method (`id`) | Exact title | Authors | Year | Venue | arXiv / DOI | Code (licence) | Key idea | Headline number (source) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CORE | AdaAD (`huang2023adaad`) | Boosting Accuracy and Robustness of Student Models via Adaptive Adversarial Distillation | Huang, Chen, Wang, et al. (6) | 2023 | CVPR 2023 | none (CVF only) | boyellow/AdaAD (MIT) | Teacher-guided adaptive inner maximisation | ResNet-18 **54.23%** AutoAttack (RobustBench) (abstract) |
| 2 | CORE | PeerAiD (`jung2024peeraid`) | PeerAiD: Improving Adversarial Distillation from a Specialized Peer Tutor | Jung, Jang, Song, Lee | 2024 | CVPR 2024 | 2403.06668 | jaewonalive/PeerAiD (GPL-3.0) | A peer trained on the student's adversaries acts as tutor | TinyImageNet ResNet-18: AA up to **+1.66 pp**, clean up to **+4.72 pp** (abstract) |
| 3 | CORE | IGDM (`lee2025igdm`) | Indirect Gradient Matching for Adversarial Robust Distillation | Lee, Cho, Kim | 2025 | ICLR 2025 | 2312.03286 | none found | Indirect input-gradient matching; plug-in | CIFAR-100 ResNet-18 AA 28.06 → **30.32** (abstract) |
| 4 | CORE | SAAD (`lee2025saad`) | Sample-wise Adaptive Weighting for Transfer Consistency in Adversarial Distillation | Lee, Chung | 2025 | TMLR | 2512.10275 | HongsinLee/saad (none) | Sample weights from teacher–student transfer consistency | CIFAR-10 ResNet-18 AA **50.34** vs RSLAD 44.42 (Table 4) |
| 5 | CORE | CIARD (`lu2025ciard`) | CIARD: Cyclic Iterative Adversarial Robustness Distillation | Lu, Pang, Zheng, et al. (7) | 2025 | **ICCV 2025** (registry corrected from "preprint") | 2509.12633 | eminentgu/CIARD (none) | Multi-teacher push-loss alignment of the conflicting clean and robust teachers; continual teacher retraining | CIFAR-10 ResNet-18 clean **88.87** / FGSM **61.88** (Table 3) |
| S1 | SUPPORT | Why robust teachers fail (`lee2026robustteachers`) | Toward Understanding Adversarial Distillation: Why Robust Teachers Fail | Lee, Chung | 2026 | ICML 2026 (author-stated) | 2605.21999 | HongsinLee/why-robust-teachers-fail (none) | Analysis; contradicting evidence for "stronger teacher → more robust student" | — |
| C1 | CLASSIC | ARD (`goldblum2020ard`) | Adversarially Robust Distillation | Goldblum, Fowl, Feizi, Goldstein | 2020 | AAAI 2020 | 1905.09747 / 10.1609/aaai.v34i04.5816 | — | First robust KD | — |
| C2 | CLASSIC | RSLAD (`zi2021rslad`) | Revisiting Adversarial Robustness Distillation: Robust Soft Labels Make Student Better | Zi, Zhao, Ma, Jiang | 2021 | ICCV 2021 | 2108.07969 | — | Robust soft labels | — |

### 6d. Federated KD

| # | Tag | Method (`id`) | Exact title | Authors | Year | Venue | arXiv / DOI | Code (licence) | Key idea | Headline number (source) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CORE | DFRD (`luo2023dfrd`) | DFRD: Data-Free Robustness Distillation for Heterogeneous Federated Learning | Luo, Wang, Fu, et al. (6) | 2023 | NeurIPS 2023 | 2309.13546 | none found | Server-side data-free distillation with a conditional generator plus EMA | CIFAR-100 (ω=1.0) FedAvg 57.31 → +DFRD **61.49** (Table 1) |
| 2 | CORE | HYDRA-FL (`khan2024hydrafl`) | HYDRA-FL: Hybrid Knowledge Distillation for Robust and Accurate Federated Learning | Khan, Chandio, Anwar | 2024 | NeurIPS 2024 | 2409.19912 | none found | Shallow-layer KD to stop KD-based FL from amplifying poisoning | MNIST under attack **76.67** vs FedNTD 58.09 (Table 1) |
| 3 | CORE | FedGO (`jang2025fedgo`) | Provably Near-Optimal Federated Ensemble Distillation with Negligible Overhead | Jang, Park, Lee | 2025 | ICML 2025 | 2502.06349 | none found | Discriminator-based per-sample client weighting, with near-optimality guarantees | CIFAR-10 (α=0.1) **79.62** vs FedDF 71.56 (Table 3) |
| 4 | CORE-A | FedRevive (`askin2026fedrevive`) | Reviving Stale Updates: Data-Free Knowledge Distillation for Asynchronous Federated Learning | Askin, Roth, Sun, et al. (6) | 2026 | NeurIPS 2026 (author-stated) | 2511.00655 | none found | Data-free KD refreshes stale asynchronous updates | Up to **+11.4 pp** final accuracy, **29.7%** faster (abstract) |
| C1 | CLASSIC | FedDF (`lin2020feddf`) | Ensemble Distillation for Robust Model Fusion in Federated Learning | Lin, Kong, Stich, Jaggi | 2020 | NeurIPS 2020 | 2006.07242 | — | Server ensemble distillation | — |
| C2 | CLASSIC | FedGen (`zhu2021fedgen`) | Data-Free Knowledge Distillation for Heterogeneous Federated Learning | Zhu, Hong, Zhou | 2021 | ICML 2021 | 2105.10056 | — | Generator-based data-free FL KD | — |

---

## Withdrawn, superseded and corrected entries
- **MoKD** (`hayder2025mokd`): arXiv v2 is a withdrawal notice ("Major changes to the paper and the authorship"). Cite DTO-KD instead.
- **CIARD** (`lu2025ciard`): the registry said "preprint", but the paper is in the ICCV 2025 open-access proceedings. The record is now corrected.
- **RLD** (`sun2025rld`): the registry said "accepted (per arXiv comment)". It is now confirmed published (CVF ICCV 2025).
- **AE-KD** (`du2020aekd`): the registry said "unverified" with one author. The NeurIPS 2020 page now confirms all 7 authors.
- **SDD**: the arXiv and repository title is "Scale Decoupled Distillation"; the CVF proceedings title is "Scaled Decoupled Distillation". Use the CVF title in the bibliography.
- **EKD** code: the URL printed in the paper (github.com/lyxiang-casia/EKD) now redirects to github.com/Liangyu-Xiang/EKD.

## Gaps and uncertain entries
1. **Headline number not extracted (4 entries).** RSD, the MOO-adversaries paper (Dong et al.) and AMiD have tables that pdftotext could not read. GKD gives only relative gains. A human should read these tables before Table II/IV is filled.
2. **Author-stated acceptance (CORE-A) only:** RPKD, CaRE-Div, DHO, FedRevive (NeurIPS 2026) and the robust-teacher analysis (ICML 2026). The NeurIPS/ICML 2026 proceedings pages were not checked. Cite these as "to appear".
3. **Preprints (CORE-P):** SPOFA, TPKD and UP-MOPD (2026). TPKD's 88.05% CIFAR-100 comes from the abstract, and the teacher/student setting was not read. That number is not comparable with the R32×4→R8×4 numbers.
4. **Venue not verified:** FitNets and AT (classics, no arXiv venue comment). CRD and TAKD venues are author-stated only.
5. **ICLR 2023** (FCFD, NORM, DPK): the proceedings listing was unreachable, so these are verified by the PDF header and the arXiv comment only.
6. **Licences:** more than half of the official repositories checked (27 of about 48) have **no LICENSE file**. TinyCLIP and Angular-KD report NOASSERTION. PeerAiD is GPL-3.0. Do not reuse code from these repositories without checking.
7. **Dropped candidates.** These were dropped either because their tables were not machine-readable, so I could not give a verified number, or because they are out of scope:
   - Dropped for unreadable tables: NC-KD (AAAI 2025, 2412.11788), MGD (ECCV 2022) and TaT (CVPR 2022).
   - Out of scope: UNIC (ECCV 2024, foundation-model multi-teacher), ATEsc (ICML 2025, data-free with non-transferable teachers), Angular-KD (NeurIPS 2025, 2510.22480) and FedSDR (ICML 2026, LLM federated self-distillation).
   - Unverified venue: "Can Students Beyond The Teacher?" (2412.09874).
   - The ICCV 2025 listing also has PAT (Perspective-Aware Teaching), Fuse-Before-Transfer, ACAM-KD and Competitive Distillation. I did not open these. They are candidates for a second pass.
8. **Recency limit:** searches covered the arXiv API (comment and title queries, up to 2026-11-03), the CVF listings up to ICCV 2025, and the official NeurIPS/ICLR/ICML/TMLR listings. **CVPR 2026, ECCV 2026 and NeurIPS 2026 proceedings were not searched** (CVPR 2026 KD papers seen on arXiv were application-specific). OpenReview was not used (it blocked bots in an earlier pass).
9. **Contradicting evidence for the survey's narrative:**
   - VkD: CIFAR-100 KD gains are saturated.
   - CHAD: standard KD barely helps in low-resource summarisation, and about half the samples are harmful.
   - "Why robust teachers fail": stronger robust teachers do not guarantee robust students.
   - Cross-paper reproductions of the same method differ by up to about 0.5 points (LSKD 76.62 vs 76.16; DKD 76.32 vs 75.44 in DTO-KD's table).
