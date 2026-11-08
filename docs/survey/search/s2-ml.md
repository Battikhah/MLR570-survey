# Systematic search S2: ML venues (NeurIPS, ICML, ICLR, TMLR), 2022–2026 (T12b)

Orca task `task_26dc300dedef`, Claude worker, 2026-11-08. Criteria: `tasks/plan.md` § "Scope decision" (I1–I3, E1–E7), applied as frozen. No snowballing (assigned to S3).

**Labels.** Every number below is **VERIFIED** against the full-text PDF named in the table (pdftotext, 2026-11-08); table numbers are the paper's own. Code and codings in the "AMBIGUOUS" notes are **INTERPRETATION** for the coordinator to decide.

## 1. Search log

Query: case-insensitive title match on `distill|knowledge transfer|teacher` over every accepted paper in each listing (the listings expose titles only; abstracts were read at screening for the 139 candidates). All queries run 2026-11-08.

| Source | Listing URL | Accepted papers in listing | Title hits |
|---|---|---:|---:|
| NeurIPS 2022 | https://papers.nips.cc/paper_files/paper/2022 | 2834 | 50 |
| NeurIPS 2023 | https://papers.nips.cc/paper_files/paper/2023 | 3540 | 57 |
| NeurIPS 2024 | https://papers.nips.cc/paper_files/paper/2024 | 4493 | 54 |
| NeurIPS 2025 | https://neurips.cc/virtual/2025/papers.html | 5858 | 85 |
| NeurIPS 2026 | https://neurips.cc/virtual/2026/papers.html | 9098 | 188 |
| ICLR 2022 | https://iclr.cc/virtual/2022/papers.html | 1095 | 18 |
| ICLR 2023 | https://iclr.cc/virtual/2023/papers.html | 1584 | 32 |
| ICLR 2024 | https://iclr.cc/virtual/2024/papers.html | 2296 | 41 |
| ICLR 2025 | https://iclr.cc/virtual/2025/papers.html | 3827 | 73 |
| ICLR 2026 | https://iclr.cc/virtual/2026/papers.html | 5468 | 93 |
| ICML 2022 | https://proceedings.mlr.press/v162/ | 1233 | 5 |
| ICML 2023 | https://proceedings.mlr.press/v202/ | 1828 | 23 |
| ICML 2024 | https://proceedings.mlr.press/v235/ | 2610 | 30 |
| ICML 2025 | https://proceedings.mlr.press/v267/ | 3330 | 43 |
| ICML 2026 | https://proceedings.mlr.press/v306/ | 6552 | 116 |
| TMLR | https://jmlr.org/tmlr/papers/ | 5056 | 77 |
| **Total** | | 60702 | 985 |

Notes on access:
- **OpenReview API and PDFs** (`api2.openreview.net`, `openreview.net/pdf`) return HTTP 403 "ChallengeRequiredError" to scripted access. Not bypassed. Accepted lists for ICLR, NeurIPS 2025–2026 and TMLR were therefore taken from the official conference virtual sites (`iclr.cc`/`neurips.cc` `/virtual/<year>/papers.html`, all accepted oral/spotlight/poster papers) and the TMLR accepted-papers page on jmlr.org.
- Cross-check: the official ICLR proceedings listings for 2024–2026 (`proceedings.iclr.cc/paper_files/paper/<year>`: 2260 / 3703 / 5351 papers) give the same keyword hits as the virtual sites (0 missing). `proceedings.iclr.cc` has no 2022 or 2023 volume (HTTP 404).
- `papers.nips.cc` lists only 64 NeurIPS 2025 papers so far, so NeurIPS 2025 used the virtual site. NeurIPS 2026 accepted papers are listed on `neurips.cc/virtual/2026`.
- Full texts came from the proceedings PDF (papers.nips.cc, PMLR, proceedings.iclr.cc) or, when the venue PDF is OpenReview-only, the arXiv version found by exact-title search of the arXiv API. 9 candidates had no accessible full text (§5).

## 2. PRISMA-style counts

| Stage | Count |
|---|---:|
| Identified (title hits, 16 listings) | 985 |
| Removed as duplicates (E7: same title in two venues) | 2 |
| Records screened (title; abstract for borderline) | 983 |
| Screened out | 844 |
| &nbsp;&nbsp;E1 | 91 |
| &nbsp;&nbsp;E2 | 641 |
| &nbsp;&nbsp;E3 | 0 |
| &nbsp;&nbsp;E5 | 2 |
| &nbsp;&nbsp;E6 | 101 |
| &nbsp;&nbsp;SUPPORT | 9 |
| Full text sought | 139 |
| Full text not accessible (§5) | 9 |
| Full text assessed | 130 |
| Excluded at full text | 94 |
| &nbsp;&nbsp;E1 | 6 |
| &nbsp;&nbsp;E2 | 9 |
| &nbsp;&nbsp;E4 | 54 |
| &nbsp;&nbsp;SUPPORT | 25 |
| **Included** | **36** (21 NEW, 15 existing registry ids) |

SUPPORT = analysis-only paper (I1): cited where relevant, not on the leaderboard. No E3 cases: every listing is inside 2022–2026 and TMLR began in 2022.

## 3. Inclusion table

Pairs: R32×4→R8×4, WRN-40-2→WRN-16-2, R56→R20, VGG13→VGG8, R32×4→ShuffleV1/V2, R50→MBV2 (CIFAR-100); IN = ImageNet-1K. Numbers are top-1 (%); "T2" = the paper's Table 2. Best stacked variant named where it is the best number. Protocol = mdistiller/CRD (240 epochs, CRD teachers e.g. R32×4 79.42, torchvision R34 73.31) unless the notes say otherwise. Licence from the repo's LICENSE via the GitHub API, 2026-11-08.

| Id | Reg. | Method | Venue | arXiv / DOI | Family | Pairs reported | CIFAR R32×4→R8×4 | IN R34→R18 | Notes | Code (licence) | Mechanism |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `wang2022checkpointkd` | NEW | CheckpointKD | NeurIPS 2022 | 2210.06458 | scheme | IN R34→R18 | n/r | 70.98 (T1, optimal intermediate teacher T*) | ImageNet teacher R34 73.86 (own); CIFAR pairs non-standard | https://github.com/LeapLabTHU/CheckpointKD (none found) | Distil from an intermediate teacher checkpoint (chosen by an information-bottleneck criterion) instead of the converged teacher. |
| `li2022shake` | NEW | SHAKE | NeurIPS 2022 | — | scheme | WRN-40-2→WRN-16-2, R56→R20, R32×4→R8×4, VGG13→VGG8, IN R34→R18, IN R50→MBV1 | 77.35 (T2) | 72.07 (T3); SHAKE† (multi-teacher) 72.53 | 240 epochs; CRD teachers | project page https://lilujunai.github.io/SHAKE/ (no repo URL in paper) (none found) | Shadow head on the frozen teacher trained online with the student; bridges offline and online KD with reversed distillation. |
| `chen2022pefd` | NEW | PEFD | NeurIPS 2022 | 2210.15274 | feature | WRN-40-2→WRN-16-2, VGG13→VGG8, R32×4→R8×4, R50→MBV2, IN R34→R18, IN R50→MBV1 | 76.08 (T5) | 71.94 (T7) | CRD teachers (79.42) | https://github.com/chenyd7/PEFD (MIT) | Feature distillation through an ensemble of randomly initialised projectors on the student feature. |
| `wang2022cutmixpick` | NEW | CutMixPick | NeurIPS 2022 | 2012.02909 | scheme | WRN-40-2→WRN-16-2, R56→R20, R32×4→R8×4, VGG13→VGG8, R50→MBV2, R32×4→ShuffleV2 | 76.11 (T1, CRD+CutMixPick, 240 ep); 75.96 at 960 ep | n/r (ImageNet used only for loss/stddev analysis, T7–T8) | arXiv first posted 2020-12 (2012.02909) | https://github.com/MingSun-Tse/Good-DA-in-KD (none found) | Statistical criterion for good KD augmentation (low teacher–student cross-entropy variance); picks high-entropy CutMix samples. |
| `niu2022ipwd` | NEW | IPWD | NeurIPS 2022 | 2210.12787 | logit | R56→R20, R32×4→R8×4, R32×4→ShuffleV1, R50→MBV2, IN R34→R18, IN R50→MBV1 | 76.03 (T2) | 71.88 (T4) | CRD teachers; student R8×4 72.50 | none found (none found) | Inverse-probability weighting of the distillation loss to correct the teacher–student transfer gap (under-represented samples). |
| `zhu2022tllm` | NEW | TLLM | NeurIPS 2022 | — | reliability | R32×4→R8×4, R50→MBV2, R32×4→ShuffleV1, IN R50→MBV1, IN R34→R18 | 77.83 (T2, SFTN+TLLM); KD+TLLM 75.53 | 72.6 (T3; teacher printed as 'ResNet32', acc 73.3 = torchvision R34) | plug-in on other KD methods | none found (none found) | Identifies 'undistillable classes' and drops their distillation signal (teach less, learn more). |
| `li2023kdzero` | NEW | KD-Zero | NeurIPS 2023 | — | hybrid | WRN-40-2→WRN-16-2, R32×4→R8×4, VGG13→VGG8, R32×4→ShuffleV2, R32×4→ShuffleV1, IN R34→R18, IN R50→MBV1 | 77.85 (T3) | 72.17 (T4) | 240 epochs after an evolutionary search per pair | none found (none found) | Evolutionary search over distiller design (knowledge transform, distance, loss) per teacher–student pair. |
| `saidutta2024cifd` | NEW | CIFD | NeurIPS 2024 | — | scheme | R32×4→R8×4, IN R34→R18, IN R50→MBV1 | 76.0 (T2/T10) | 72.32 (T3, 3 RDMs) | CIFAR result given to one decimal | none found (none found) | Rate-distortion modules act as cheap teacher assistants that control the information flow from teacher to student. |
| `yu2025angularkd` | NEW | Angular-KD | NeurIPS 2025 | 2510.22480 | scheme | R32×4→R8×4, VGG13→VGG8, WRN-40-2→WRN-16-2, IN R34→R18 | 77.28 (T2, MLKD+Angular-KD); KD+Angular-KD 76.08 (T1) | 71.07 (T3, KD+Angular-KD) |  | https://github.com/june6423/Angular-KD (MIT) | Single-teacher view augmentation: angularly diverse teacher views (feature/logit level) used as multiple teachers. |
| `huang2023maskd` | NEW | MasKD | ICLR 2023 | 2205.14589 | feature | IN R34→R18 | n/r | 71.26 (T6, appendix) | AMBIGUOUS: method targets detection/segmentation; image classification only in appendix T6 | https://github.com/hunto/MasKD (Apache-2.0) | Learnable receptive tokens produce masks that select the pixels used for feature distillation. |
| `dong2024soteacher` | NEW | SoTeacher | ICLR 2024 | 2206.06661 | reliability | WRN-40-2→WRN-16-2, R32×4→ShuffleV2 | n/r | n/r (R34→R18 only on Tiny-ImageNet) | teacher trained by SoTeacher (lower teacher acc.) | none found (none found) | Student-oriented teacher training (Lipschitz and consistency regularisation) so the teacher better approximates the true label distribution. |
| `ye2024mcmi` | NEW | MCMI teacher | ICLR 2024 | 2401.08732 | reliability | WRN-40-2→WRN-16-2, R56→R20, VGG13→VGG8, R50→MBV2, IN R34→R18 | n/r | 72.06 (T2, DKD with MCMI teacher); KD 71.54 | teacher re-trained (R34 71.62) | https://github.com/iclr2024mcmi/ICLRMCMI (none found) | Trains the teacher to maximise log-likelihood plus conditional mutual information, a better estimate of the Bayes conditional distribution. |
| `guo2025gpd` | NEW | GPD | ICLR 2025 | 2410.04140 | scheme | IN R34→R18, IN R50→MBV1 | n/r | 72.71 (T1, DKD+GPD) | ImageNet only | none found (none found) | Dynamic teacher trained alongside the student with bidirectional parameter mappings that preserve a fixed teacher–student gap. |
| `hossain2025tekap` | NEW | TeKAP | ICLR 2025 | — | scheme | R32×4→R8×4, WRN-40-2→WRN-16-2, VGG13→VGG8, R56→R20, R32×4→ShuffleV1, R32×4→ShuffleV2, IN R34→R18 | 77.36 (T2, MLKD+TeKAP); TeKAP(F+L) 75.98 (T1) | 70.67 (T3, KD+TeKAP(L); table gives top-1 error 29.33) |  | https://github.com/mdimtiazh/TeKAP (BSD-2-Clause) | Teacher knowledge augmentation: perturbed copies of one teacher's features/logits act as multiple teachers. |
| `chen2026djip` | NEW | DJIP | ICLR 2026 | — | reliability | WRN-40-2→WRN-16-2, R56→R20, VGG13→VGG8, R32×4→R8×4, IN R34→R18, IN R50→MBV1 | 76.61 (T1, WTTM+DJIP teacher) | 72.08 (T3, DKD+DJIP) | teacher retrained with DJIP; R32×4 79.41 | none found (none found) | Differentiable JPEG input perturbation during teacher training raises the teacher's conditional mutual information. |
| `morad2026bayesteacher` | NEW | Bayesian teachers | ICLR 2026 | 2601.01484 | reliability | WRN-40-2→WRN-16-2, VGG13→VGG8 | n/r | n/r (R34→R18 only on Tiny-ImageNet) | AMBIGUOUS: own protocol (WRN-16-2 no-KD 67.70, teachers retrained, 5 seeds), not mdistiller | none found (none found) | SGD analysis showing Bayes-class-probability teachers reduce student variance; uses Bayesian (VI/Laplace) teachers. |
| `kim2024topkd` | NEW | TopKD | ICML 2024 | — | feature | R56→R20, R32×4→R8×4, WRN-40-2→WRN-16-2, VGG13→VGG8, IN R34→R18, R50→MBV2 | 75.40 (T1) | 73.60 (T3; above the 73.31 teacher) |  | https://github.com/jekim5418/TopKD (cited in paper; repo not reachable 2026-11-08) (none found) | Distils global topology of the feature space via persistence diagrams (topological features). |
| `peng2024kdav` | NEW | KD with auxiliary variable | ICML 2024 | — | hybrid | WRN-40-2→WRN-16-2, R56→R20, R32×4→R8×4, VGG13→VGG8, R32×4→ShuffleV1, R50→MBV2, IN R34→R18, IN R50→MBV1 | 77.47 (T1) | 73.04 (T4) |  | none found (none found) | Probabilistic KD with an auxiliary variable (nonparametric) that aligns teacher and student representations and logits. |
| `chen2025adm` | NEW | ADM | ICML 2025 | — | scheme | R32×4→R8×4, R32×4→ShuffleV1, R32×4→ShuffleV2, IN R34→R18 | 74.63 (T1, SwitOKD+ADM; online KD, both trained) | 71.69 (T9, offline KD, best α/β) | AMBIGUOUS: online KD — the R8×4 number is not the offline mdistiller protocol | none found (none found) | Asymmetric decision-making in online KD: consensus on foreground features, divergence elsewhere. |
| `guan2025rankingkd` | NEW | Kendall-τ ranking loss | ICML 2025 | 2409.17823 | logit | R32×4→R8×4, VGG13→VGG8, WRN-40-2→WRN-16-2, R32×4→ShuffleV2, R50→MBV2, IN R34→R18 | 77.25 (T2, MLKD+ranking) | 72.06 (T13, NKD+ranking) | plug-in loss | https://github.com/OvernighTea/RankingLoss-KD (cited in paper; repo not reachable 2026-11-08) (none found) | Plug-and-play Kendall's τ ranking loss that aligns the order of teacher and student logits. |
| `do2022mad` | NEW | MAD | NeurIPS 2022 | 2209.10359 | scheme | WRN-40-2→WRN-16-2 | n/r | n/r (R34→R18 only on CIFAR/TinyImageNet; ImageNet uses other pairs) | AMBIGUOUS: data-free KD (no training data); CIFAR-100 W40-2→W16-2 64.05 (T1), not comparable to data-based KD | none found (none found) | Data-free KD with an EMA copy of the generator (momentum adversarial distillation) to handle generator distribution shift. |
| `huang2022dist` | existing | DIST | NeurIPS 2022 | 2205.10536 | logit | R56→R20, R32×4→R8×4, R50→MBV2, R32×4→ShuffleV1, R32×4→ShuffleV2, IN R34→R18, IN R50→MBV1 | 76.31 (T5) | 72.07 (T2) |  | see registry | Inter- and intra-class Pearson correlation matching. |
| `huang2023diffkd` | existing | DiffKD | NeurIPS 2023 | 2305.15712 | feature | R56→R20, R50→MBV2, IN R34→R18, IN R50→MBV1 | 76.72 (T9, appendix) | 72.22 (T2); DiffKD† 72.49 |  | see registry | Diffusion model denoises student features toward teacher features. |
| `hao2023ofakd` | existing | OFA-KD | NeurIPS 2023 | 2310.19444 | feature | R50→MBV2, IN R34→R18 | n/r | 72.10 (T5) | heterogeneous focus | see registry | Projects intermediate features to logit space for heterogeneous pairs. |
| `lv2024wkd` | existing | WKD | NeurIPS 2024 | 2412.08139 | logit | R32×4→R8×4, VGG13→VGG8, R32×4→ShuffleV1, R50→MBV2, IN R34→R18, IN R50→MBV1 | 76.53 WKD-L; 77.28 L+F (T11) | 72.49 WKD-L (T4) |  | see registry | Wasserstein distance over cross-category relations. |
| `bassam2025pld` | existing | PLD | NeurIPS 2025 | 2506.12542 | logit | R56→R20, R32×4→R8×4, R50→MBV2 | 73.97 (T1) | n/r | own protocol (R8×4 CE 71.56, DKD 73.08) | see registry | Plackett–Luce list-wise logit distillation. |
| `huang2025deepkd` | existing | DeepKD | NeurIPS 2025 | 2505.15133 | optimizer | R32×4→R8×4, VGG13→VGG8, WRN-40-2→WRN-16-2, R56→R20, R50→MBV2, IN R34→R18, IN R50→MBV1 | 79.25 (T1, CRLD+DeepKD top-k); MLKD+DeepKD 79.15 | 73.34 (T3, CRLD+DeepKD top-k; camera-ready, was 74.23 in arXiv v1); WRN-40-2→WRN-16-2 78.42; IN R50→MBV1 74.85 |  | see registry | Decoupled momentum per gradient component plus top-k denoising. |
| `etcibasi2026rpkd` | existing | RPKD | NeurIPS 2026 | 2610.37937 | feature | R50→MBV2, IN R34→R18, IN R50→MBV1 | n/r | 72.23 (T4) |  | see registry | Random frozen prototype space for heterogeneous KD. |
| `qiu2023dpk` | existing | DPK | ICLR 2023 | 2206.06067 | feature | WRN-40-2→WRN-16-2, R56→R20, VGG13→VGG8, R32×4→ShuffleV1, R50→MBV2, IN R34→R18, IN R50→MBV1 | n/r | 72.51 (T2) |  | see registry | Dynamic prior knowledge: teacher features mixed into student features. |
| `liu2023norm` | existing | NORM | ICLR 2023 | 2305.13803 | feature | R32×4→R8×4, WRN-40-2→WRN-16-2, R56→R20, VGG13→VGG8, R32×4→ShuffleV1, R50→MBV2, IN R34→R18, IN R50→MBV1 | 76.49 (T1); +KD 76.98 | 72.14 (T3) |  | see registry | N-to-one representation matching via feature expansion. |
| `liu2023fcfd` | existing | FCFD | ICLR 2023 | 2304.11832 | feature | R32×4→R8×4, WRN-40-2→WRN-16-2, R56→R20, VGG13→VGG8, R32×4→ShuffleV1, R50→MBV2, IN R34→R18, IN R50→MBV1 | 76.62 (T1) | 72.25 (T2, Ours*) |  | see registry | Function-consistent feature distillation. |
| `zheng2024wttm` | existing | WTTM | ICLR 2024 | 2402.11148 | logit | R32×4→R8×4, WRN-40-2→WRN-16-2, R56→R20, VGG13→VGG8, R32×4→ShuffleV1, R50→MBV2, IN R34→R18, IN R50→MBV1 | 76.06 (T2) | 72.19 (T5) |  | see registry | Transformed teacher matching with sample-adaptive weighting. |
| `hu2024tgeokd` | existing | TGeo-KD | ICLR 2024 | 2312.15112 | logit | R56→R20, R32×4→R8×4, R32×4→ShuffleV1, R32×4→ShuffleV2, IN R34→R18, IN R50→MBV1 | 77.27 (T1, per registry) | 72.89 (T2) |  | see registry | Trilateral geometry for sample-wise KD weighting. |
| `hayder2026dtokd` | existing | DTO-KD | ICLR 2026 | — | optimizer | R32×4→R8×4, R56→R20, R50→MBV2 | 76.40 (T2) | n/r (ImageNet only with DeiT students, T1) |  | see registry | Min-norm dynamic trade-off of distillation and task gradients. |
| `wang2025abkd` | existing | ABKD | ICML 2025 | 2505.04560 | logit | WRN-40-2→WRN-16-2, R56→R20, R32×4→R8×4, VGG13→VGG8 | figure only (Fig. 5), no table | n/r |  | see registry | α-β-divergence for probability-mass allocation. |
| `hossain2025luminet` | existing | LumiNet | TMLR | 2310.03669 | logit | R32×4→R8×4, WRN-40-2→WRN-16-2, R56→R20, VGG13→VGG8, R32×4→ShuffleV1, R50→MBV2, IN R34→R18 | 77.50 (T1) | 72.16 (T2) |  | see registry | Perception-driven statistical logit calibration. |

**Top CIFAR-100 R32×4→R8×4 results in this search** (best reported variant, any protocol):

- 79.25 — DeepKD (`huang2025deepkd`): 79.25 (T1, CRLD+DeepKD top-k); MLKD+DeepKD 79.15
- 77.85 — KD-Zero (`li2023kdzero`): 77.85 (T3)
- 77.83 — TLLM (`zhu2022tllm`): 77.83 (T2, SFTN+TLLM); KD+TLLM 75.53
- 77.50 — LumiNet (`hossain2025luminet`): 77.50 (T1)
- 77.47 — KD with auxiliary variable (`peng2024kdav`): 77.47 (T1)
- 77.36 — TeKAP (`hossain2025tekap`): 77.36 (T2, MLKD+TeKAP); TeKAP(F+L) 75.98 (T1)
- 77.35 — SHAKE (`li2022shake`): 77.35 (T2)
- 77.28 — Angular-KD (`yu2025angularkd`): 77.28 (T2, MLKD+Angular-KD); KD+Angular-KD 76.08 (T1)

**INTERPRETATION.** DeepKD (1st) and TLLM (3rd) are stacked on other methods (CRLD+DeepKD; SFTN+TLLM), and TeKAP and Angular-KD reach their best numbers on top of MLKD, so none of these four is like-for-like with a single-method row. Among stand-alone methods, KD-Zero 77.85 (distiller searched per pair), LumiNet 77.50, KD with auxiliary variable 77.47 and SHAKE 77.35 lead. Protocols differ (teachers, seeds), so these are reported numbers, not a controlled ranking.

## 4. Full-text exclusion table

| # | Paper | Venue | Code | Reason |
|---|---|---|---|---|
| 2 | Functional Ensemble Distillation | NeurIPS 2022 | E4 | Bayesian-ensemble distillation; no standard CRD pair |
| 3 | Discovering and Overcoming Limitations of Noise-engineered Data-free Knowledge Distillation | NeurIPS 2022 | E4 | data-free KD; CIFAR-100 only with R34→R18 (not a standard pair) |
| 4 | Weighted Distillation with Unlabeled Examples | NeurIPS 2022 | E4 | semi-supervised distillation with unlabelled data; no standard-pair result |
| 5 | Learning Efficient Vision Transformers via Fine-Grained Manifold Distillation | NeurIPS 2022 | E4 | ViT (DeiT/Swin) pairs only |
| 10 | Knowledge Distillation: Bad Models Can Be Good Role Models | NeurIPS 2022 | SUPPORT | analysis of teacher quality; no new method |
| 13 | On student-teacher deviations in distillation: does it pay to disobey? | NeurIPS 2023 | SUPPORT | analysis of student–teacher deviations |
| 14 | Revisit the Power of Vanilla Knowledge Distillation: from Small Scale to Large Scale | NeurIPS 2023 | SUPPORT | analysis of vanilla KD under stronger recipes (useful context numbers: R32×4→R8×4 KD 75.90, T1b) |
| 15 | Improving Adversarial Robustness via Information Bottleneck Distillation | NeurIPS 2023 | E4 | adversarial-robustness distillation; no standard clean-accuracy pair |
| 16 | What Knowledge Gets Distilled in Knowledge Distillation? | NeurIPS 2023 | SUPPORT | analysis of what knowledge is transferred |
| 17 | Revisiting Adversarial Robustness Distillation from the Perspective of Robust Fairness | NeurIPS 2023 | E4 | adversarial robust-fairness distillation |
| 18 | NEO-KD: Knowledge-Distillation-Based Adversarial Training for Robust Multi-Exit Neural Networks | NeurIPS 2023 | E4 | multi-exit adversarial training |
| 19 | Progressive Ensemble Distillation: Building Ensembles for Efficient Inference | NeurIPS 2023 | E4 | ensemble construction; no standard pair |
| 21 | SLaM: Student-Label Mixing for Distillation with Unlabeled Examples | NeurIPS 2023 | E4 | semi-supervised distillation; no standard pair |
| 23 | Knowledge Distillation Performs Partial Variance Reduction | NeurIPS 2023 | SUPPORT | theory (variance reduction) |
| 25 | Understanding the Gains from Repeated Self-Distillation | NeurIPS 2024 | SUPPORT | theory of repeated self-distillation |
| 26 | ScaleKD: Strong Vision Transformers Could Be Excellent Teachers | NeurIPS 2024 | E4 | large ViT teachers; no standard pair |
| 28 | Over-parameterized Student Model via Tensor Decomposition Boosted Knowledge Distillation | NeurIPS 2024 | E4 | ImageNet with non-standard pairs only |
| 29 | Improving Adversarial Robust Fairness via Anti-Bias Soft Label Distillation | NeurIPS 2024 | E4 | adversarial robust fairness |
| 32 | Synergy Between the Strong and the Weak: Spiking Neural Networks are Inherently Self-Distillers | NeurIPS 2025 | E4 | spiking-network students |
| 33 | Knowledge Distillation of Uncertainty using Deep Latent Factor Model | NeurIPS 2025 | E4 | uncertainty distillation; non-standard pairs |
| 34 | The Effect of Optimal Self-Distillation in Noisy Gaussian Mixture Model | NeurIPS 2025 | SUPPORT | theory (Gaussian mixture) |
| 35 | Neural Tangent Knowledge Distillation for Optical Convolutional Networks | NeurIPS 2025 | E4 | optical networks |
| 37 | Learning Task-Agnostic Representations through Multi-Teacher Distillation | NeurIPS 2025 | E1 | task-agnostic multi-teacher representation learning |
| 38 | Enhanced Self-Distillation Framework for Efficient Spiking Neural Network Training | NeurIPS 2025 | E4 | spiking-network self-distillation |
| 41 | Improving Self-Supervised Vision Transformers with Cross Distillation | NeurIPS 2026 | E1 | self-supervised ViT pre-training |
| 42 | Decoupled Optimization for Teacher-Student Semi-Supervised Learning via a Pioneer Student | NeurIPS 2026 | E1 | semi-supervised learning with EMA teachers |
| 44 | Data Density Scaling Laws for Image Self-Distillation | NeurIPS 2026 | SUPPORT | scaling laws for self-distillation |
| 46 | Learning Better Certified Models from Empirically-Robust Teachers | NeurIPS 2026 | E1 | certified-robustness training |
| 48 | AVSD: Adaptive-View Self-Distillation by Balancing Consensus and Teacher-Specific Privileged Signals | NeurIPS 2026 | E2 | LLM self-distillation |
| 50 | Reliable Adversarial Distillation with Unreliable Teachers | ICLR 2022 | E4 | adversarial distillation; no standard clean pair |
| 51 | Churn Reduction via Distillation | ICLR 2022 | E1 | churn reduction |
| 52 | The Augmented Image Prior: Distilling 1000 Classes by Extrapolating from a Single Image | ICLR 2023 | E4 | single-image distillation; non-standard protocol |
| 53 | Teacher Guided Training: An Efficient Framework for Knowledge Transfer | ICLR 2023 | E4 | no standard pair |
| 54 | Supervision Complexity and its Role in Knowledge Distillation | ICLR 2023 | SUPPORT | AMBIGUOUS: theory of supervision complexity; online KD on R56→R20 with own protocol (student 67.7); not a new KD method |
| 55 | Towards Understanding Ensemble, Knowledge Distillation and Self-Distillation in Deep Learning | ICLR 2023 | SUPPORT | theory of ensembles/KD |
| 59 | Robust Active Distillation | ICLR 2023 | E4 | active/semi-supervised distillation |
| 61 | Augmentation with Projection: Towards an Effective and Efficient Data Augmentation Paradigm for Distillation | ICLR 2023 | E2 | NLP (GLUE) |
| 65 | AuG-KD: Anchor-Based Mixup Generation for Out-of-Domain Knowledge Distillation | ICLR 2024 | E4 | out-of-domain KD on Office-31/Home |
| 66 | Annealing Self-Distillation Rectification Improves Adversarial Training | ICLR 2024 | E4 | adversarial training |
| 68 | Fantastic Gains and Where to Find Them: On the Existence and Prospect of General Knowledge Transfer between Any Pretrained Model | ICLR 2024 | SUPPORT | analysis of transfer between pretrained models |
| 69 | A Good Learner can Teach Better: Teacher-Student Collaborative Knowledge Distillation | ICLR 2024 | E2 | NLP (GLUE) |
| 70 | High-dimensional Analysis of Knowledge Distillation: Weak-to-Strong Generalization and Scaling Laws | ICLR 2025 | SUPPORT | high-dimensional theory |
| 71 | Rethinking Self-Distillation: Label Averaging and Enhanced Soft Label Refinement with Partial Labels | ICLR 2025 | E4 | [jeong2025selfdistill] self-distillation theory under label noise; no standard pair |
| 73 | Student-Informed Teacher Training | ICLR 2025 | E2 | robot RL (privileged teacher) |
| 74 | Progressive distillation induces an implicit curriculum | ICLR 2025 | SUPPORT | analysis of progressive distillation |
| 75 | SelKD: Selective Knowledge Distillation via Optimal Transport Perspective | ICLR 2025 | E4 | selective KD; CIFAR-10 / ImageNet subsets only |
| 76 | Indirect Gradient Matching for Adversarial Robust Distillation | ICLR 2025 | E4 | [lee2025igdm] adversarial distillation; no standard clean pair |
| 77 | Long-tailed Adversarial Training with Self-Distillation | ICLR 2025 | E4 | long-tailed adversarial training |
| 79 | Medium-Difficulty Samples Constitute Smoothed Decision Boundary for Knowledge Distillation on Pruned Datasets | ICLR 2025 | E4 | KD on pruned datasets only (r ≤ 70%) |
| 80 | In Good GRACES: Principled Teacher Selection for Knowledge Distillation | ICLR 2026 | E2 | teacher selection for LLM distillation |
| 81 | Contextual Similarity Distillation: Ensemble Uncertainties with a Single Model | ICLR 2026 | E4 | ensemble uncertainty |
| 82 | Knowledge Distillation as Decontamination? Revisiting the “Data Laundering” Concern in Classification Tasks | ICLR 2026 | E2 | LLM data-laundering analysis |
| 83 | SiNGER: A Clearer Voice Distills Vision Transformers Further | ICLR 2026 | E4 | ViT students only |
| 85 | FERD: Fairness-Enhanced Data-Free Adversarial Robustness Distillation | ICLR 2026 | E4 | data-free adversarial robustness |
| 88 | Biologically Plausible Learning via Bidirectional Spike-Based Distillation | ICLR 2026 | E4 | spiking networks |
| 89 | Many Eyes, One Mind: Temporal Multi-Perspective and Progressive Distillation for Spiking Neural Networks | ICLR 2026 | E4 | spiking networks |
| 90 | Revisiting Label Smoothing and Knowledge Distillation Compatibility: What was Missing? | ICML 2022 | SUPPORT | analysis of label smoothing and KD compatibility |
| 91 | Spatial-Channel Token Distillation for Vision MLPs | ICML 2022 | E4 | vision-MLP students |
| 92 | TSPipe: Learn from Teacher Faster with Pipelines | ICML 2022 | E4 | systems (pipelined KD); no standard pair |
| 93 | Improving Ensemble Distillation With Weight Averaging and Diversifying Perturbation | ICML 2022 | E4 | ensemble distillation; non-standard pairs |
| 94 | Understanding Self-Distillation in the Presence of Label Noise | ICML 2023 | SUPPORT | self-distillation theory |
| 95 | On the Impact of Knowledge Distillation for Model Interpretability | ICML 2023 | SUPPORT | interpretability analysis |
| 96 | Revisiting Data-Free Knowledge Distillation with Poisoned Teachers | ICML 2023 | E4 | data-free KD under poisoned teachers; CIFAR-10 WRN16-2→WRN16-1 |
| 97 | Are Large Kernels Better Teachers than Transformers for ConvNets? | ICML 2023 | SUPPORT | analysis of large-kernel teachers |
| 98 | Random Teachers are Good Teachers | ICML 2023 | SUPPORT | analysis (random teachers) |
| 99 | Revisit the Essence of Distilling Knowledge through Calibration | ICML 2024 | SUPPORT | analysis of teacher calibration |
| 100 | Bayesian Knowledge Distillation: A Bayesian Perspective of Distillation with Uncertainty Quantification | ICML 2024 | E4 | Bayesian KD; non-standard pairs |
| 102 | Enhancing Class-Imbalanced Learning with Pre-Trained Guidance through Class-Conditional Knowledge Distillation | ICML 2024 | E4 | class-imbalanced learning |
| 104 | Knowledge Transfer from Vision Foundation Models for Efficient Training of Small Task-specific Models | ICML 2024 | E4 | foundation-model teachers |
| 105 | Distilling the Knowledge in Data Pruning | ICML 2025 | E4 | data pruning; non-standard pairs |
| 108 | When Data-Free Knowledge Distillation Meets Non-Transferable Teacher: Escaping Out-of-Distribution Trap is All You Need | ICML 2025 | E4 | data-free KD; non-standard pairs |
| 109 | Ensemble Distribution Distillation via Flow Matching | ICML 2025 | E4 | ensemble distribution distillation |
| 110 | Right Time to Learn: Promoting Generalization via Bio-inspired Spacing Effect in Knowledge Distillation | ICML 2025 | E4 | spaced KD; ResNet-18 students only |
| 112 | Efficient Logit-based Knowledge Distillation of Deep Spiking Neural Networks for Full-Range Timestep Deployment | ICML 2025 | E4 | spiking networks |
| 113 | Toward Understanding Adversarial Distillation: Why Robust Teachers Fail | ICML 2026 | E4 | [lee2026robustteachers] adversarial distillation analysis |
| 114 | Quantifying Cross-Domain Knowledge Distillation in the Presence of Domain Shift | ICML 2026 | SUPPORT | cross-domain KD theory |
| 115 | DomED: Redesigning Ensemble Distillation for Domain Generalization | ICML 2026 | E4 | domain-generalisation ensemble distillation |
| 116 | From Per-Image Low-Rank to Encoding Mismatch: Rethinking Feature Distillation in Vision Transformers | ICML 2026 | E4 | ViT feature distillation; R34→R18 only as a FitNet control (T11) |
| 117 | Cross-Modal Knowledge Distillation without Paired Data: Theoretical Foundation and Algorithm | ICML 2026 | E2 | cross-modal KD |
| 118 | Trust Functions: Near-Lossless Weak-to-Strong Generalization by Learning When to Trust the Weak Teacher | ICML 2026 | E2 | weak-to-strong generalisation |
| 119 | Shortcut-Resistant CAM Distillation for Long-Tailed Recognition | ICML 2026 | E4 | long-tailed recognition |
| 120 | Why Self-Distillation Helps and Hurts: Denoising vs. Signal Forgetting | ICML 2026 | SUPPORT | self-distillation theory |
| 121 | What Makes a Strong Model? A Unified Spectral Analysis of Knowledge Transfer over High-dimensional Linear Regression | ICML 2026 | SUPPORT | theory of knowledge transfer |
| 123 | Sample-wise Adaptive Weighting for Transfer Consistency in Adversarial Distillation | TMLR | E4 | [lee2025saad] adversarial distillation |
| 124 | Distilled Circuits: A Mechanistic Study of Internal Restructuring in Knowledge Distillation | TMLR | E2 | mechanistic study of LM distillation |
| 126 | Preserving Angles Improves Feature Distillation | TMLR | E4 | no CNN standard pair |
| 127 | Adaptive Group Robust Ensemble Knowledge Distillation | TMLR | E4 | [kenfack2025agrekd] group-robustness ensemble KD |
| 128 | Simplifying Knowledge Transfer in Pretrained Models | TMLR | E4 | pretrained-model transfer |
| 131 | Towards Undistillable Models by Minimizing Conditional Mutual Information | TMLR | E1 | anti-distillation (protecting teachers) |
| 132 | ReDistill: Residual Encoded Distillation for Peak Memory Reduction of CNNs | TMLR | E4 | peak-memory reduction; non-standard pairs |
| 133 | What’s Left After Distillation? How Knowledge Transfer Impacts Fairness and Bias | TMLR | SUPPORT | fairness analysis |
| 134 | Rethinking Knowledge Transfer in Learning Using Privileged Information | TMLR | SUPPORT | privileged-information theory |
| 136 | On Good Practices for Task-Specific Distillation of Large Pretrained Visual Models | TMLR | E4 | task-specific distillation from large pretrained models |
| 138 | Teacher’s pet: understanding and mitigating biases in distillation | TMLR | SUPPORT | bias analysis (self-distillation R34→R34) |

## 5. Full text not accessible (not included; listed for the coordinator)

| # | Paper | Venue | Error |
|---|---|---|---|
| 36 | SDPGO: Efficient Self-Distillation Training Meets Proximal Gradient Optimization | NeurIPS 2025 | NeurIPS 2025: no arXiv version found; proceedings PDF not on papers.nips.cc 2025 listing; OpenReview PDF returned HTTP 403 (bot challenge) |
| 43 | Learning from Disagreement: Maximum Divergence Knowledge Distillation | NeurIPS 2026 | NeurIPS 2026: no arXiv version; only OpenReview (HTTP 403) |
| 47 | Prediction-only distillation with optimal mixing in ridge-regularized linear and logistic regression | NeurIPS 2026 | NeurIPS 2026: no arXiv version; only OpenReview (HTTP 403) |
| 49 | Feature Kernel Distillation | ICLR 2022 | ICLR 2022: no proceedings.iclr.cc volume for 2022 (HTTP 404), arXiv title search found only a different paper; OpenReview HTTP 403 |
| 122 | Breaking BatchNorm Barriers for Noise-driven Data Free Knowledge Distillation | TMLR | TMLR: OpenReview only (HTTP 403); no arXiv version found |
| 125 | Correctness-Aware Knowledge Distillation for Enhanced Student Learning | TMLR | TMLR: OpenReview only (HTTP 403); no arXiv version found |
| 130 | Unified Wisdom: Harnessing Collaborative Learning to Improve Efficacy of Knowledge Distillation | TMLR | TMLR: OpenReview only (HTTP 403); no arXiv version found |
| 135 | Feature Distillation Improves Zero-Shot Transfer from Synthetic Images | TMLR | TMLR: OpenReview only (HTTP 403); no arXiv version found |
| 137 | Layerwise Bregman Representation Learning of Neural Networks with Applications to Knowledge Distillation | TMLR | TMLR: OpenReview only (HTTP 403); no arXiv version found |

Of these, *Learning from Disagreement: Maximum Divergence Knowledge Distillation* (NeurIPS 2026), *Correctness-Aware Knowledge Distillation for Enhanced Student Learning* and *Unified Wisdom* (TMLR) are KD methods for classification by abstract and could meet I3. Their eligibility could not be checked.

## 6. AMBIGUOUS cases (coordinator to decide)

- `huang2023maskd` (MasKD): AMBIGUOUS: method targets detection/segmentation; image classification only in appendix T6
- `morad2026bayesteacher` (Bayesian teachers): AMBIGUOUS: own protocol (WRN-16-2 no-KD 67.70, teachers retrained, 5 seeds), not mdistiller
- `chen2025adm` (ADM): AMBIGUOUS: online KD — the R8×4 number is not the offline mdistiller protocol
- `do2022mad` (MAD): AMBIGUOUS: data-free KD (no training data); CIFAR-100 W40-2→W16-2 64.05 (T1), not comparable to data-based KD
- Supervision Complexity and its Role in Knowledge Distillation (#54, coded SUPPORT): AMBIGUOUS: theory of supervision complexity; online KD on R56→R20 with own protocol (student 67.7); not a new KD method
- `zhu2022tllm`: the ImageNet table labels the teacher "ResNet32" with accuracy 73.3; the value matches torchvision ResNet-34, so it is recorded as R34→R18.
- `kim2024topkd`: ImageNet R34→R18 73.60 is above the 73.31 teacher; recorded as printed.

## Appendix A. Title-screen decisions (all records not sent to full text)

<details><summary>846 records</summary>

| Source | Title | Code | Basis |
|---|---|---|---|
| NeurIPS 2022 | [Offline Multi-Agent Reinforcement Learning with Knowledge Distillation](https://papers.nips.cc/paper_files/paper/2022/hash/01d78b294d80491fecddea897cf03642-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [Dataset Distillation via Factorization](https://papers.nips.cc/paper_files/paper/2022/hash/07bc722f08f096e6ea7ee99349ff0a86-Abstract-Conference.html) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [Structural Knowledge Distillation for Object Detection](https://papers.nips.cc/paper_files/paper/2022/hash/18c0102cb7f1a02c14f0929089b2e576-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [Accelerating Certified Robustness Training via Knowledge Transfer](https://papers.nips.cc/paper_files/paper/2022/hash/22bf0634985f4e6dbb1fb40e247d1478-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2022 | [DTG-SSOD: Dense Teacher Guidance for Semi-Supervised Object Detection](https://papers.nips.cc/paper_files/paper/2022/hash/3a02b6df276223b68c69ca572cb3c4a8-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [Dataset Distillation using Neural Feature Regression](https://papers.nips.cc/paper_files/paper/2022/hash/3fe2a777282299ecb4f9e7ebb531f0ab-Abstract-Conference.html) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [Decomposed Knowledge Distillation for Class-Incremental Semantic Segmentation](https://papers.nips.cc/paper_files/paper/2022/hash/439bf902de1807088d8b731ca20b0777-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [Symbolic Distillation for Learned TCP Congestion Control](https://papers.nips.cc/paper_files/paper/2022/hash/4574ac9854d4defe3bf119d07b817084-Abstract-Conference.html) | E2 | title |
| NeurIPS 2022 | [SeqPATE: Differentially Private Text Generation via Knowledge Distillation](https://papers.nips.cc/paper_files/paper/2022/hash/480045ad846b44bf31441c1f1d9dd768-Abstract-Conference.html) | E2 | title |
| NeurIPS 2022 | [Hilbert Distillation for Cross-Dimensionality Networks](https://papers.nips.cc/paper_files/paper/2022/hash/4c9477b9e2c7ec0ad3f4f15077aaf85a-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2022 | [Knowledge Distillation Improves Graph Structure Augmentation for Graph Neural Networks](https://papers.nips.cc/paper_files/paper/2022/hash/4d4a3b6a34332d80349137bcc98164a5-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [Improving Policy Learning via Language Dynamics Distillation](https://papers.nips.cc/paper_files/paper/2022/hash/51053d7b8473df7d5a2165b2a8ee9629-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [Teacher Forcing Recovers Reward Functions for Text Generation](https://papers.nips.cc/paper_files/paper/2022/hash/51ae7d9db3423ae96cd6afeb01529819-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [Efficient Dataset Distillation using Random Feature Approximation](https://papers.nips.cc/paper_files/paper/2022/hash/5a28f46993c19f428f482cc59db40870-Abstract-Conference.html) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [BiT: Robustly Binarized Multi-distilled Transformer](https://papers.nips.cc/paper_files/paper/2022/hash/5c1863f711c721648387ac2ef745facb-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2022 | [Bi-directional Weakly Supervised Knowledge Distillation for Whole Slide Image Classification](https://papers.nips.cc/paper_files/paper/2022/hash/62c9aa4d48329a85d1e36d5b6d0a6a32-Abstract-Conference.html) | E2 | title: KD not the contribution / not classification KD (manual override) |
| NeurIPS 2022 | [PKD: General Distillation Framework for Object Detectors via Pearson Correlation Coefficient](https://papers.nips.cc/paper_files/paper/2022/hash/631ad9ae3174bf4d6c0f6fdca77335a4-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [Beyond Not-Forgetting: Continual Learning with Backward Knowledge Transfer](https://papers.nips.cc/paper_files/paper/2022/hash/6728fcf94660c59c938319a6833a6073-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2022 | [TOIST: Task Oriented Instance Segmentation Transformer with Noun-Pronoun Distillation](https://papers.nips.cc/paper_files/paper/2022/hash/70270a1bc28ecb2a2aefad566c5e556b-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [Fairness without Demographics through Knowledge Distillation](https://papers.nips.cc/paper_files/paper/2022/hash/79dc391a2c1067e9ac2b764e31a60377-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2022 | [MetaTeacher: Coordinating Multi-Model Domain Adaptation for Medical Image Classification](https://papers.nips.cc/paper_files/paper/2022/hash/8313b1920ee9c78d846c5798c1ce48be-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2022 | [An Analytical Theory of Curriculum Learning in Teacher-Student Networks](https://papers.nips.cc/paper_files/paper/2022/hash/84bad835faaf48f24d990072bb5b80ee-Abstract-Conference.html) | SUPPORT | title (manual override) |
| NeurIPS 2022 | [Towards Efficient 3D Object Detection with Knowledge Distillation](https://papers.nips.cc/paper_files/paper/2022/hash/8625a8c2be8ba5197b7a14833dbea8ac-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [Meta-DMoE: Adapting to Domain Shift by Meta-Distillation from Mixture-of-Experts](https://papers.nips.cc/paper_files/paper/2022/hash/8bd4f1dbc7a70c6b80ce81b8b4fdc0b2-Abstract-Conference.html) | E2 | title |
| NeurIPS 2022 | [Decomposing NeRF for Editing via Feature Field Distillation](https://papers.nips.cc/paper_files/paper/2022/hash/93f250215e4889119807b6fac3a57aec-Abstract-Conference.html) | E2 | title |
| NeurIPS 2022 | [Distilled Gradient Aggregation: Purify Features for Input Attribution in the Deep Neural Network](https://papers.nips.cc/paper_files/paper/2022/hash/a935ba2236c6ba0fb620f23354e789ff-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2022 | [Toward Understanding Privileged Features Distillation in Learning-to-Rank](https://papers.nips.cc/paper_files/paper/2022/hash/aa31dc84098add7dd2ffdd20646f2043-Abstract-Conference.html) | E2 | title |
| NeurIPS 2022 | [Zero-shot Transfer Learning within a Heterogeneous Graph via Knowledge Transfer Networks](https://papers.nips.cc/paper_files/paper/2022/hash/af2bb2b2280d36f8842e440b4e275152-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [Few-shot Task-agnostic Neural Architecture Search for Distilling Large Language Models](https://papers.nips.cc/paper_files/paper/2022/hash/b7c12689a89e98a61bcaa65285a41b7c-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [Geometric Knowledge Distillation: Topology Compression for Graph Neural Networks](https://papers.nips.cc/paper_files/paper/2022/hash/c06f788963f0ce069f5b2dbf83fe7822-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [Prune and distill: similar reformatting of image information along rat visual cortex and deep neural networks](https://papers.nips.cc/paper_files/paper/2022/hash/c2d82a425af4c18a35049899fea5ee82-Abstract-Conference.html) | E2 | title |
| NeurIPS 2022 | [Learning Generalizable Models for Vehicle Routing Problems via Knowledge Distillation](https://papers.nips.cc/paper_files/paper/2022/hash/ca70528fb11dc8086c6a623da9f3fee6-Abstract-Conference.html) | E2 | title |
| NeurIPS 2022 | [Distilling Representations from GAN Generator via Squeeze and Span](https://papers.nips.cc/paper_files/paper/2022/hash/dd0151081b1e80e93f1b8aaf0b684c18-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [Remember the Past: Distilling Datasets into Addressable Memories for Neural Networks](https://papers.nips.cc/paper_files/paper/2022/hash/de3d2bb604cfc43c81edd2a31b257f03-Abstract-Conference.html) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [PerfectDou: Dominating DouDizhu with Perfect Information Distillation](https://papers.nips.cc/paper_files/paper/2022/hash/e26f31de8b13ec569bf507e6ae2cd952-Abstract-Conference.html) | E2 | title |
| NeurIPS 2022 | [Look Around and Refer: 2D Synthetic Semantics Knowledge Distillation for 3D Visual Grounding](https://papers.nips.cc/paper_files/paper/2022/hash/f0b42291ddab77dcb2ef8a3488301b62-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2022 | [Preservation of the Global Knowledge by Not-True Distillation in Federated Learning](https://papers.nips.cc/paper_files/paper/2022/hash/fadec8f2e65f181d777507d1df69b92f-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [ProlificDreamer: High-Fidelity and Diverse Text-to-3D Generation with Variational Score Distillation](https://papers.nips.cc/paper_files/paper/2023/hash/1a87980b9853e84dfb295855b425c262-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Spectral Co-Distillation for Personalized Federated Learning](https://papers.nips.cc/paper_files/paper/2023/hash/1b86cf4b15cd83b6520d851eb7298228-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [MIM4DD: Mutual Information Maximization for Dataset Distillation](https://papers.nips.cc/paper_files/paper/2023/hash/24d36eee157559e0d2549455fba28f6a-Abstract-Conference.html) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Localized Symbolic Knowledge Distillation for Visual Commonsense Models](https://papers.nips.cc/paper_files/paper/2023/hash/257be12f31dfa7cc158dda99822c6fd1-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2023 | [Towards Efficient Pre-Trained Language Model via Feature Correlation Distillation](https://papers.nips.cc/paper_files/paper/2023/hash/34260a400e39a802961470b3d3de99cc-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Laughing Hyena Distillery: Extracting Compact Recurrences From Convolutions](https://papers.nips.cc/paper_files/paper/2023/hash/371355cd42caaf83412c3fbef4688979-Abstract-Conference.html) | E2 | title |
| NeurIPS 2023 | [DFRD: Data-Free Robustness Distillation for Heterogeneous Federated Learning](https://papers.nips.cc/paper_files/paper/2023/hash/39ca8893ea38905a9d2ffe786e85af0f-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Attacks on Online Learners: a Teacher-Student Analysis](https://papers.nips.cc/paper_files/paper/2023/hash/46e37aeccafc3b4b697b17b8a36f3b30-Abstract-Conference.html) | E1 | title (analysis-only) (manual override) |
| NeurIPS 2023 | [Accelerating Molecular Graph Neural Networks via Knowledge Distillation](https://papers.nips.cc/paper_files/paper/2023/hash/51ec452ca04d8ec7160e5bbaf76153f6-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [STXD: Structural and Temporal Cross-Modal Distillation for Multi-View 3D Object Detection](https://papers.nips.cc/paper_files/paper/2023/hash/5d8c01de2dc698c54201c1c7d0b86974-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Distilling Out-of-Distribution Robustness from Vision-Language Foundation Models](https://papers.nips.cc/paper_files/paper/2023/hash/67f30132d98e758f7b4e28c36091d86e-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Knowledge Distillation for High Dimensional Search Index](https://papers.nips.cc/paper_files/paper/2023/hash/6a15378acabd1aef017ec79a3ed744d2-Abstract-Conference.html) | E2 | title |
| NeurIPS 2023 | [EgoDistill: Egocentric Head Motion Distillation for Efficient Video Understanding](https://papers.nips.cc/paper_files/paper/2023/hash/6a412f0037b0df295a39a198666ea6a6-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [RD-Suite: A Benchmark for Ranking Distillation](https://papers.nips.cc/paper_files/paper/2023/hash/701eba0f98c6f28ffee0de5969d8d034-Abstract-Datasets_and_Benchmarks.html) | E2 | title |
| NeurIPS 2023 | [Segment Any Point Cloud Sequences by Distilling Vision Foundation Models](https://papers.nips.cc/paper_files/paper/2023/hash/753d9584b57ba01a10482f1ea7734a89-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Switching Temporary Teachers for Semi-Supervised Semantic Segmentation](https://papers.nips.cc/paper_files/paper/2023/hash/7eeb42802d3750ca59e8a0523068e9e6-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Cluster-aware Semi-supervised Learning: Relational Knowledge Distillation Provably Learns Clustering](https://papers.nips.cc/paper_files/paper/2023/hash/8037f47a6254eb60899a644bd90b4f6a-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2023 | [One-Step Diffusion Distillation via Deep Equilibrium Models](https://papers.nips.cc/paper_files/paper/2023/hash/82f05a105c928c10706213952bf0c8b7-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Token-Scaled Logit Distillation for Ternary Weight Generative Language Models](https://papers.nips.cc/paper_files/paper/2023/hash/8342218a4ec08b8c19661725e9cd6c0b-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Slimmed Asymmetrical Contrastive Learning and Cross Distillation for Lightweight Model Training](https://papers.nips.cc/paper_files/paper/2023/hash/8393d955a00c463a982cefe77d0404e1-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2023 | [Students Parrot Their Teachers: Membership Inference on Model Distillation](https://papers.nips.cc/paper_files/paper/2023/hash/8b07d224a643b02e7571e083578a86d2-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2023 | [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://papers.nips.cc/paper_files/paper/2023/hash/8c3c666820ea055a77726d66fc7d447f-Abstract-Datasets_and_Benchmarks.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Propagating Knowledge Updates to LMs Through Distillation](https://papers.nips.cc/paper_files/paper/2023/hash/932147114c48f8b04d41aebc0c631158-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Knowledge-Augmented Reasoning Distillation for Small Language Models in Knowledge-Intensive Tasks](https://papers.nips.cc/paper_files/paper/2023/hash/97faedc90260eae5c400f92d5831c3d7-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Dual Mean-Teacher: An Unbiased Semi-Supervised Framework for Audio-Visual Source Localization](https://papers.nips.cc/paper_files/paper/2023/hash/98143953a7fd1319175b491888fc8df5-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Sparse Parameterization for Epitomic Dataset Distillation](https://papers.nips.cc/paper_files/paper/2023/hash/9e8889198d16fb79926e71adbe38cae4-Abstract-Conference.html) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Augmentation-Free Dense Contrastive Knowledge Distillation for Efficient Semantic Segmentation](https://papers.nips.cc/paper_files/paper/2023/hash/a12779b5e802668df1cbc73fa00da62f-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Robust Knowledge Transfer in Tiered Reinforcement Learning](https://papers.nips.cc/paper_files/paper/2023/hash/a39ab46bf619ada0e90ceed846648a81-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Does Graph Distillation See Like Vision Dataset Counterpart?](https://papers.nips.cc/paper_files/paper/2023/hash/a6efa49c54bedf4411f1bcd32f15937a-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [MGDD: A Meta Generator for Fast Dataset Distillation](https://papers.nips.cc/paper_files/paper/2023/hash/b0506debbf49e31d25690fbd1e69cd2f-Abstract-Conference.html) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [DinoSR: Self-Distillation and Online Clustering for Self-supervised Speech Representation Learning](https://papers.nips.cc/paper_files/paper/2023/hash/b6404bf461c3c3186bdf5f55756af908-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [How a Student becomes a Teacher: learning and forgetting through Spectral methods](https://papers.nips.cc/paper_files/paper/2023/hash/bd9ea5d671ee761a69dba811348d78ba-Abstract-Conference.html) | SUPPORT | title (analysis-only) |
| NeurIPS 2023 | [FedFed: Feature Distillation against Data Heterogeneity in Federated Learning](https://papers.nips.cc/paper_files/paper/2023/hash/bdcdf38389d7fcefc73c4c3720217155-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [On the Size and Approximation Error of Distilled Datasets](https://papers.nips.cc/paper_files/paper/2023/hash/c03a9ccdb3e95f2c2dcfc3f4bc16bf42-Abstract-Conference.html) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Can Language Models Teach? Teacher Explanations Improve Student Performance via Personalization](https://papers.nips.cc/paper_files/paper/2023/hash/c6afe9a5d1e1068796d32613ddca1ab7-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Concept Distillation: Leveraging Human-Centered Explanations for Model Improvement](https://papers.nips.cc/paper_files/paper/2023/hash/c9450295fd667740a39a68148fc17f6e-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2023 | [Sequential Subset Matching for Dataset Distillation](https://papers.nips.cc/paper_files/paper/2023/hash/d553f0e0abb80e2a60328d634583bd2e-Abstract-Conference.html) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Enhancing Knowledge Transfer for Task Incremental Learning with Data-free Subnetwork](https://papers.nips.cc/paper_files/paper/2023/hash/d7b3cef7c31b94a4a533db83d01a8882-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2023 | [Label-Only Model Inversion Attacks via Knowledge Transfer](https://papers.nips.cc/paper_files/paper/2023/hash/d9827e811c5a205c1313fb950c072c7d-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2023 | [Module-wise Adaptive Distillation for Multimodality Foundation Models](https://papers.nips.cc/paper_files/paper/2023/hash/dc9544b26ad3579477e567588db18cfc-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Frequency Domain-Based Dataset Distillation](https://papers.nips.cc/paper_files/paper/2023/hash/ddbbcd937d63d5c6b935c07b1a8222ec-Abstract-Conference.html) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Collaborative Score Distillation for Consistent Visual Editing](https://papers.nips.cc/paper_files/paper/2023/hash/e7fd2c0a1a6f956c94024e955b34cc43-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Modality-Independent Teachers Meet Weakly-Supervised Audio-Visual Event Parser](https://papers.nips.cc/paper_files/paper/2023/hash/e95e9f0c127aa1cfa2628adb2f3cb107-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2023 | [Should Under-parameterized Student Networks Copy or Average Teacher Weights?](https://papers.nips.cc/paper_files/paper/2023/hash/f5ccb3ab757131a93586ef61ec701533-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2023 | [Fair Graph Distillation](https://papers.nips.cc/paper_files/paper/2023/hash/ff6540c54a847ef9114a332c101f5edc-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Invertible Consistency Distillation for Text-Guided Image Editing in Around 7 Steps](https://papers.nips.cc/paper_files/paper/2024/hash/1704fe7aaff33a54802b83a016050ab8-Abstract-Conference.html) | E2 | title |
| NeurIPS 2024 | [Variational Distillation of Diffusion Policies into Mixture of Experts](https://papers.nips.cc/paper_files/paper/2024/hash/175fa4fc8f275f877ec85340131c5d7a-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Are Large-scale Soft Labels Necessary for Large-scale Dataset Distillation?](https://papers.nips.cc/paper_files/paper/2024/hash/1da9ca7e9cef4b1af63913f05d1630a4-Abstract-Conference.html) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [PaGoDA: Progressive Growing of a One-Step Generator from a Low-Resolution Diffusion Teacher](https://papers.nips.cc/paper_files/paper/2024/hash/221ccaeaef4b9cc8f89b63d6fc98a271-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Score Distillation via Reparametrized DDIM](https://papers.nips.cc/paper_files/paper/2024/hash/2ded44d59f5094eed0d02132fe75b60d-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [FineCLIP: Self-distilled Region-based CLIP for Better Fine-grained Understanding](https://papers.nips.cc/paper_files/paper/2024/hash/3122aaa22b2fe83f9cead1a696f65ceb-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [LaKD: Length-agnostic Knowledge Distillation for Trajectory Prediction with Any Length Observations](https://papers.nips.cc/paper_files/paper/2024/hash/327b9b8d4e45c3f81568e11ffc505f77-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://papers.nips.cc/paper_files/paper/2024/hash/3848fef259495bfd04d60cdc5c1b4db7-Abstract-Conference.html) | E2 | title |
| NeurIPS 2024 | [Rethinking Score Distillation as a Bridge Between Image Distributions](https://papers.nips.cc/paper_files/paper/2024/hash/3b62bca132cf5c8973b09a2fc6dc8ca6-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Multistep Distillation of Diffusion Models via Moment Matching](https://papers.nips.cc/paper_files/paper/2024/hash/3f66d5cdbe032bb750f2dc523357b7a5-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Probabilistic Conformal Distillation for Enhancing Missing Modality Robustness](https://papers.nips.cc/paper_files/paper/2024/hash/3fb97beb678a1c46bf25f40b3a8c6f98-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2024 | [Simple and Fast Distillation of Diffusion Models](https://papers.nips.cc/paper_files/paper/2024/hash/47ee3941a6f1d23c39b788e0f450e2a7-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Semi-supervised Knowledge Transfer Across Multi-omic Single-cell Data](https://papers.nips.cc/paper_files/paper/2024/hash/47f30d67bce3e9824928267e9355420f-Abstract-Conference.html) | E2 | title |
| NeurIPS 2024 | [Compact Language Models via Pruning and Knowledge Distillation](https://papers.nips.cc/paper_files/paper/2024/hash/4822991365c962105b1b95b1107d30e5-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [EM Distillation for One-step Diffusion Models](https://papers.nips.cc/paper_files/paper/2024/hash/4fac0e32088db2fd2948cfaacc4fe108-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Reinforced Cross-Domain Knowledge Distillation on Time Series Data](https://papers.nips.cc/paper_files/paper/2024/hash/5424f6b74f475ad738b54888d609283a-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Improved Distribution Matching Distillation for Fast Image Synthesis](https://papers.nips.cc/paper_files/paper/2024/hash/54dcf25318f9de5a7a01f0a4125c541e-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2024 | [HYDRA-FL: Hybrid Knowledge Distillation for Robust and Accurate Federated Learning](https://papers.nips.cc/paper_files/paper/2024/hash/5a5ddf0ab751861025c00700093c5677-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Color-Oriented Redundancy Reduction in Dataset Distillation](https://papers.nips.cc/paper_files/paper/2024/hash/5f5f7b6080dcadced61cf5d96f7c6dde-Abstract-Conference.html) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [MoTE: Reconciling Generalization with Specialization for Visual-Language to Video Knowledge Transfer](https://papers.nips.cc/paper_files/paper/2024/hash/641ce6c0e22483f34cd58625fcc7630e-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Flipped Classroom: Aligning Teacher Attention with Student in Generalized Category Discovery](https://papers.nips.cc/paper_files/paper/2024/hash/70270a1bc28ecb2a2aefad566c5e556b-Abstract-Conference.html) | E2 | title |
| NeurIPS 2024 | [DistillNeRF: Perceiving 3D Scenes from Single-Glance Images by Distilling Neural Fields and Foundation Model Features](https://papers.nips.cc/paper_files/paper/2024/hash/720991812855c99df50bc8b36966cd81-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [The Mamba in the Llama: Distilling and Accelerating Hybrid Models](https://papers.nips.cc/paper_files/paper/2024/hash/723933067ad315269b620bc0d2c05cba-Abstract-Conference.html) | E2 | title |
| NeurIPS 2024 | [Self-Distilled Depth Refinement with Noisy Poisson Fusion](https://papers.nips.cc/paper_files/paper/2024/hash/81b8390039b7302c909cb769f8b6cd93-Abstract-Conference.html) | E2 | title |
| NeurIPS 2024 | [VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought](https://papers.nips.cc/paper_files/paper/2024/hash/8ac50fd0a4eeeb1f077b17bb7c5353c3-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Persistence Homology Distillation for Semi-supervised Continual Learning](https://papers.nips.cc/paper_files/paper/2024/hash/8bd31288ad8e9a31d519fdeede7ee47d-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2024 | [UDON: Universal Dynamic Online distillatioN for generic image representations](https://papers.nips.cc/paper_files/paper/2024/hash/9df6a759e01b871a009138bcc0471607-Abstract-Conference.html) | E2 | title |
| NeurIPS 2024 | [Provable and Efficient Dataset Distillation for Kernel Ridge Regression](https://papers.nips.cc/paper_files/paper/2024/hash/a1c716638d9b618a1a40a96f473c8250-Abstract-Conference.html) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [How JEPA Avoids Noisy Features: The Implicit Bias of Deep Linear Self Distillation Networks](https://papers.nips.cc/paper_files/paper/2024/hash/a600f0f740605205133553cb74a1c107-Abstract-Conference.html) | SUPPORT | title (analysis-only) |
| NeurIPS 2024 | [A Kernel Perspective on Distillation-based Collaborative Learning](https://papers.nips.cc/paper_files/paper/2024/hash/a71c1931d3fb8ba564f7458d0657d0b1-Abstract-Conference.html) | SUPPORT | title (analysis-only) |
| NeurIPS 2024 | [ID-to-3D: Expressive ID-guided 3D Heads via Score Distillation Sampling](https://papers.nips.cc/paper_files/paper/2024/hash/b0171a5965e0b58afcd4ce1adb0baa56-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [DDK: Distilling Domain Knowledge for Efficient Large Language Models](https://papers.nips.cc/paper_files/paper/2024/hash/b206d54ffbb803b5c51d85f405d422e4-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Voxel Proposal Network via Multi-Frame Knowledge Distillation for Semantic Scene Completion](https://papers.nips.cc/paper_files/paper/2024/hash/b734c30b9c955c535e333f0301f5e45c-Abstract-Conference.html) | E2 | title |
| NeurIPS 2024 | [One-shot Federated Learning via Synthetic Distiller-Distillate Communication](https://papers.nips.cc/paper_files/paper/2024/hash/ba0ad9d1e0c737800b2340b9cd68c208-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Motion Consistency Model: Accelerating Video Diffusion with Disentangled Motion-Appearance Distillation](https://papers.nips.cc/paper_files/paper/2024/hash/c859b99b5d717c9035e79d43dfd69435-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Adversarial Moment-Matching Distillation of Large Language Models](https://papers.nips.cc/paper_files/paper/2024/hash/cbae8efcc23a0cb6d15a20f245514020-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Offline Behavior Distillation](https://papers.nips.cc/paper_files/paper/2024/hash/d0724f5d6108517c3eab35f77f156967-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2024 | [One-Step Diffusion Distillation through Score Implicit Matching](https://papers.nips.cc/paper_files/paper/2024/hash/d107ca794d83c8242e357e6a43a068f4-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [A teacher-teacher framework for clinical language representation learning](https://papers.nips.cc/paper_files/paper/2024/hash/d1ebc73cd4c88866b97a6851ece739d1-Abstract-Conference.html) | E2 | title |
| NeurIPS 2024 | [S2HPruner: Soft-to-Hard Distillation Bridges the Discretization Gap in Pruning](https://papers.nips.cc/paper_files/paper/2024/hash/d368aba36f74776cc7a1079332a31973-Abstract-Conference.html) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2024 | [FedGMKD: An Efficient Prototype Federated Learning Framework through Knowledge Distillation and Discrepancy-Aware Aggregation](https://papers.nips.cc/paper_files/paper/2024/hash/d6520fa7f71dc8e09ed5939a60a64218-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Diversity-Driven Synthesis: Enhancing Dataset Distillation through Directed Weight Adjustment](https://papers.nips.cc/paper_files/paper/2024/hash/d80f533473c2dc8dd6984ceffc3ed3fd-Abstract-Conference.html) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [VeXKD: The Versatile Integration of Cross-Modal Fusion and Knowledge Distillation for 3D Perception](https://papers.nips.cc/paper_files/paper/2024/hash/e34d908241aef40440e61d2a27715424-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Depth Anywhere: Enhancing 360 Monocular Depth Estimation via Perspective Distillation and Unlabeled Data Augmentation](https://papers.nips.cc/paper_files/paper/2024/hash/e6c2e85db1f1039177c4495ccd399ac4-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [Fine-grained Image-to-LiDAR Contrastive Distillation with Visual Foundation Models](https://papers.nips.cc/paper_files/paper/2024/hash/e7e506bc5a94768243083216fe51d98b-Abstract-Conference.html) | E2 | title |
| NeurIPS 2024 | [A Label is Worth A Thousand Images in Dataset Distillation](https://papers.nips.cc/paper_files/paper/2024/hash/ee45939f4403e8abd63a15a29a9c055b-Abstract-Conference.html) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [SeeClear: Semantic Distillation Enhances Pixel Condensation for Video Super-Resolution](https://papers.nips.cc/paper_files/paper/2024/hash/f358b2a880adf34939d2d6f926e54d2a-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2024 | [End-to-End Video Semantic Segmentation in Adverse Weather using Fusion Blocks and Temporal-Spatial Teacher-Student Learning](https://papers.nips.cc/paper_files/paper/2024/hash/fed6d142d12b2f8c031615cc8fd50893-Abstract-Conference.html) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Hawaii: Hierarchical Visual Knowledge Transfer for Efficient Vision-Language Models](https://neurips.cc/virtual/2025/poster/118565) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Efficient Knowledge Transfer in Federated Recommendation for Joint Venture Ecosystem](https://neurips.cc/virtual/2025/poster/117351) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Rectifying Soft-Label Entangled Bias in Long-Tailed Dataset Distillation](https://neurips.cc/virtual/2025/poster/115270) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Feature Distillation is the Better Choice for Model-Heterogeneous Federated Learning](https://neurips.cc/virtual/2025/poster/115230) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Dual-Space Semantic Synergy Distillation for Continual Learning of Unlabeled Streams](https://neurips.cc/virtual/2025/poster/120294) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2025 | [CovMatch: Cross-Covariance Guided Multimodal Dataset Distillation with Trainable Text Encoder](https://neurips.cc/virtual/2025/poster/120122) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Preference-driven Knowledge Distillation for Few-shot Node Classification](https://neurips.cc/virtual/2025/poster/119820) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Degrees of Freedom for Linear Attention: Distilling Softmax Attention with Optimal Feature Efficiency](https://neurips.cc/virtual/2025/poster/119670) | E2 | title |
| NeurIPS 2025 | [When Models Know More Than They Can Explain: Quantifying Knowledge Transfer in Human-AI Collaboration](https://neurips.cc/virtual/2025/poster/119536) | E1 | title (analysis-only) (manual override) |
| NeurIPS 2025 | [Elevating Visual Perception in Multimodal LLMs with Visual Embedding Distillation](https://neurips.cc/virtual/2025/poster/119448) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Universal Cross-Tokenizer Distillation via Approximate Likelihood Matching](https://neurips.cc/virtual/2025/poster/119176) | E2 | title |
| NeurIPS 2025 | [Efficient Data Selection at Scale via Influence Distillation](https://neurips.cc/virtual/2025/poster/119164) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2025 | [SpectraLDS: Provable Distillation for Linear Dynamical Systems](https://neurips.cc/virtual/2025/poster/119041) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2025 | [FairDD: Fair Dataset Distillation](https://neurips.cc/virtual/2025/poster/118865) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Cross-Modal Representational Knowledge Distillation for Enhanced Spike-informed LFP Modeling](https://neurips.cc/virtual/2025/poster/116652) | E2 | title |
| NeurIPS 2025 | [Knowledge Distillation Detection for Open-weights Models](https://neurips.cc/virtual/2025/poster/118076) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [One-Step Offline Distillation of Diffusion-based Models via Koopman Modeling](https://neurips.cc/virtual/2025/poster/118022) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [MOSDT: Self-Distillation-Based Decision Transformer for Multi-Agent Offline Safe Reinforcement Learning](https://neurips.cc/virtual/2025/poster/117926) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [DKDR: Dynamic Knowledge Distillation for Reliability in Federated Learning](https://neurips.cc/virtual/2025/poster/117817) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Antidistillation Sampling](https://neurips.cc/virtual/2025/poster/117654) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2025 | [Distilling LLM Prior to Flow Model for Generalizable Agent’s Imagination in Object Goal Navigation](https://neurips.cc/virtual/2025/poster/117630) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Dataset Distillation of 3D Point Clouds via Distribution Matching](https://neurips.cc/virtual/2025/poster/117394) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Unlocking Dataset Distillation with Diffusion Models](https://neurips.cc/virtual/2025/poster/117126) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Beyond Random: Automatic Inner-loop Optimization in Dataset Distillation](https://neurips.cc/virtual/2025/poster/116998) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Vision‑Language‑Vision Auto‑Encoder: Scalable Knowledge Distillation from Diffusion Models](https://neurips.cc/virtual/2025/poster/116899) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Efficient Multi-modal Large Language Models via Progressive Consistency Distillation](https://neurips.cc/virtual/2025/poster/116731) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Why Knowledge Distillation Works in Generative Models: A Minimal Working Explanation](https://neurips.cc/virtual/2025/poster/116625) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [To Distill or Decide? Understanding the Algorithmic Trade-off in Partially Observable RL](https://neurips.cc/virtual/2025/poster/116574) | E2 | title |
| NeurIPS 2025 | [Optimizing Distributional Geometry Alignment with Optimal Transport for Generative Dataset Distillation](https://neurips.cc/virtual/2025/poster/116446) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [VarFlow: Proper Scoring-Rule Diffusion Distillation via Energy Matching](https://neurips.cc/virtual/2025/poster/116135) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Improving Target Sound Extraction via Disentangled Codec Representations with Privileged Knowledge Distillation](https://neurips.cc/virtual/2025/poster/115752) | E2 | title |
| NeurIPS 2025 | [MTL-KD: Multi-Task Learning Via Knowledge Distillation for Generalizable Neural Vehicle Routing Solver](https://neurips.cc/virtual/2025/poster/115747) | E2 | title |
| NeurIPS 2025 | [Bi-Level Knowledge Transfer for Multi-Task Multi-Agent Reinforcement Learning](https://neurips.cc/virtual/2025/poster/119769) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Vision Transformers with Self-Distilled Registers](https://neurips.cc/virtual/2025/poster/117648) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2025 | [K-DeCore: Facilitating Knowledge Transfer in Continual Structured Knowledge Reasoning via Knowledge Decoupling](https://neurips.cc/virtual/2025/poster/115651) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Hyperbolic Dataset Distillation](https://neurips.cc/virtual/2025/poster/115610) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [MonoLift: Learning 3D Manipulation Policies from Monocular RGB via Distillation](https://neurips.cc/virtual/2025/poster/115316) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders](https://neurips.cc/virtual/2025/poster/115055) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [A Dataset for Distilling Knowledge Priors from Literature for Therapeutic Design](https://neurips.cc/virtual/2025/poster/121470) | E6 | title |
| NeurIPS 2025 | [SeerAttention: Self-distilled Attention Gating for Efficient Long-context Prefilling](https://neurips.cc/virtual/2025/poster/118344) | E2 | title |
| NeurIPS 2025 | [Distilling LLM Agent into Small Models with Retrieval and Code Tools](https://neurips.cc/virtual/2025/poster/117657) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [$\text{S}^2$Q-VDiT: Accurate Quantized Video Diffusion Transformer with Salient Data and Sparse Token Distillation](https://neurips.cc/virtual/2025/poster/116949) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [ELDET: Early-Learning Distillation with Noisy Labels for Object Detection](https://neurips.cc/virtual/2025/poster/118794) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Multi-order Orchestrated Curriculum Distillation for Model-Heterogeneous Federated Graph Learning](https://neurips.cc/virtual/2025/poster/119316) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Distillation Robustifies Unlearning](https://neurips.cc/virtual/2025/poster/117762) | E2 | title |
| NeurIPS 2025 | [How Ensembles of Distilled Policies Improve Generalisation in Reinforcement Learning](https://neurips.cc/virtual/2025/poster/119498) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Generative Data Augmentation via Diffusion Distillation, Adversarial Alignment, and Importance Reweighting](https://neurips.cc/virtual/2025/poster/116854) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Efficient Multimodal Dataset Distillation via Generative Models](https://neurips.cc/virtual/2025/poster/119089) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Preference Distillation via Value based Reinforcement Learning](https://neurips.cc/virtual/2025/poster/116869) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Asymmetric Dual Self-Distillation for 3D Self-Supervised Representation Learning](https://neurips.cc/virtual/2025/poster/119465) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Distilled Decoding 2: One-step Sampling of Image Auto-regressive Models with Conditional Score Distillation](https://neurips.cc/virtual/2025/poster/119746) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Co-Regularization Enhances Knowledge Transfer in High Dimensions](https://neurips.cc/virtual/2025/poster/118265) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2025 | [Dataset Distillation for Pre-Trained Self-Supervised Vision Models](https://neurips.cc/virtual/2025/poster/118957) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Reinforcement Learning Teachers of Test Time Scaling](https://neurips.cc/virtual/2025/poster/115573) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [How to build a consistency model: Learning flow maps via self-distillation](https://neurips.cc/virtual/2025/poster/119201) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [InfiGFusion: Graph-on-Logits Distillation via Efficient Gromov-Wasserstein for Model Fusion](https://neurips.cc/virtual/2025/poster/115895) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Fin3R: Fine-tuning Feed-forward 3D Reconstruction Models via Monocular Knowledge Distillation](https://neurips.cc/virtual/2025/poster/115951) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Efficient Verified Unlearning For Distillation](https://neurips.cc/virtual/2025/poster/116015) | E2 | title |
| NeurIPS 2025 | [KINDLE: Knowledge-Guided Distillation for Prior-Free Gene Regulatory Network Inference](https://neurips.cc/virtual/2025/poster/119666) | E2 | title |
| NeurIPS 2025 | [Learning to Focus: Causal Attention Distillation via Gradient‐Guided Token Pruning](https://neurips.cc/virtual/2025/poster/115296) | E2 | title |
| NeurIPS 2025 | [Unlocking SLM Potential for Data Analysis Code Generation via Non-Parametric Knowledge Distillation](https://neurips.cc/virtual/2025/poster/115197) | E2 | title |
| NeurIPS 2025 | [Self-Refining Language Model Anonymizers via Adversarial Distillation](https://neurips.cc/virtual/2025/poster/117971) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Few-Shot Knowledge Distillation of LLMs With Counterfactual Explanations](https://neurips.cc/virtual/2025/poster/119420) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Distil-E2D: Distilling Image-to-Depth Priors for Event-Based Monocular Depth Estimation](https://neurips.cc/virtual/2025/poster/115168) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [A Token is Worth over 1,000 Tokens: Efficient Knowledge Distillation through Low-Rank Clone](https://neurips.cc/virtual/2025/poster/118551) | E2 | title |
| NeurIPS 2025 | [Self-supervised Learning of Echocardiographic Video Representations via Online Cluster Distillation](https://neurips.cc/virtual/2025/poster/120161) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Simple Distillation for One-Step Diffusion Models](https://neurips.cc/virtual/2025/poster/118385) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Taught Well Learned Ill: Towards Distillation-conditional Backdoor Attack](https://neurips.cc/virtual/2025/poster/118829) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2025 | [Democratizing Clinical Risk Prediction with Cross-Cohort Cross-Modal Knowledge Transfer](https://neurips.cc/virtual/2025/poster/119681) | E2 | title |
| NeurIPS 2025 | [FADRM: Fast and Accurate Data Residual Matching for Dataset Distillation](https://neurips.cc/virtual/2025/poster/117777) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Align Your Flow: Scaling Continuous-Time Flow Map Distillation](https://neurips.cc/virtual/2025/poster/115909) | E2 | title |
| NeurIPS 2025 | [Learnable Sampler Distillation for Discrete Diffusion Models](https://neurips.cc/virtual/2025/poster/116751) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [What Makes a Reward Model a Good Teacher? An Optimization Perspective](https://neurips.cc/virtual/2025/poster/119671) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [Beyond Modality Collapse: Representation Blending for Multimodal Dataset Distillation](https://neurips.cc/virtual/2025/poster/117473) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2025 | [One-Step Diffusion-Based Image Compression with Semantic Distillation](https://neurips.cc/virtual/2025/poster/117982) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Don't Discard Your Rollouts: Reusing Teacher RL Traces for Student Distillation](https://neurips.cc/virtual/2026/poster/153136) | E2 | title |
| NeurIPS 2026 | [SODA: Selective Optimization with Deferred BN Alignment for Efficient Dataset Distillation](https://neurips.cc/virtual/2026/poster/150571) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Reinforcement Learning for View-Adaptive Distillation in 3D Gaussian Compression](https://neurips.cc/virtual/2026/poster/154966) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Multi-Agent Coordination via Support-Preserving Distillation](https://neurips.cc/virtual/2026/poster/152690) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Rebellious Student: Reversing Teacher Signals for Reasoning Exploration with Self-Distilled RLVR](https://neurips.cc/virtual/2026/poster/150786) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Solver-as-Teacher: Solver-Guided On-Policy Post-Training Framework for PDE Foundation Models](https://neurips.cc/virtual/2026/poster/151443) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Truncate Bad, Upweight Good: BoN-Style Distillation via Rank-Based Classification](https://neurips.cc/virtual/2026/poster/152325) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2026 | [COMET: Decoupled Distillation, Routing, and Capacity Control for Task-Agnostic Continual Vision--Language Learning](https://neurips.cc/virtual/2026/poster/152607) | E2 | title |
| NeurIPS 2026 | [EditDistill: Is It Possible to Guide Video Editing with Image Editing](https://neurips.cc/virtual/2026/poster/154635) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Failure Profiling and Reachable Trajectory Selection for Reasoning Distillation](https://neurips.cc/virtual/2026/poster/149263) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Trajectory as the Teacher: Few-Step Discrete Flow Matching via Energy-Navigated Distillation](https://neurips.cc/virtual/2026/poster/155603) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Trust Region Policy Distillation](https://neurips.cc/virtual/2026/poster/150346) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Anchoring Reasoning Distillation via Syntactic Constraints](https://neurips.cc/virtual/2026/poster/154471) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [VC-OPD: Visual Counterfactual On-Policy Distillation for Grounded Vision-Language Reasoning](https://neurips.cc/virtual/2026/poster/152275) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [DiffRatio: Training One-Step Diffusion Models Without Teacher Supervision](https://neurips.cc/virtual/2026/poster/155104) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [It Takes Two: Complementary Self-Distillation for Contextual Integrity in LLMs](https://neurips.cc/virtual/2026/poster/149725) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [The Shape of Events: Edge-Based Inductive Biases via Cross-Domain Distillation](https://neurips.cc/virtual/2026/poster/148705) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2026 | [Simple yet Effective Semi-supervised Knowledge Distillation from Vision-Language Models via Dual-Head Optimization](https://neurips.cc/virtual/2026/poster/151357) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Learning to Foresee: Unveiling the Unlocking Efficiency of On-Policy Distillation](https://neurips.cc/virtual/2026/poster/154435) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Rethinking Knowledge Distillation for Diffusion Language Models](https://neurips.cc/virtual/2026/poster/152596) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Circuit-Level Knowledge Distillation for Large Language Models](https://neurips.cc/virtual/2026/poster/153589) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [GenEvolve: Self-Evolving Image Generation Agents via Tool-Orchestrated Visual Experience Distillation](https://neurips.cc/virtual/2026/poster/155907) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [HandXFM: Semantic-Structural Distillation for Hand Radiograph Foundation Models](https://neurips.cc/virtual/2026/poster/150797) | E2 | title |
| NeurIPS 2026 | [SD-LoRA: Training-Time Structural Distillation into LoRA for Few-Shot Vision-Language Adaptation](https://neurips.cc/virtual/2026/poster/153156) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [CAST: Certifiable Aggregation of Smoothed Teachers for Robust Policy Adaptation](https://neurips.cc/virtual/2026/poster/151249) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Co-Evolving Policy Distillation](https://neurips.cc/virtual/2026/poster/152206) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [LinearARD: Linear-Memory Attention Distillation for RoPE Restoration](https://neurips.cc/virtual/2026/poster/148387) | E2 | title |
| NeurIPS 2026 | [Power Distribution Bridges Sampling, Self-Reward RL, and Self-Distillation](https://neurips.cc/virtual/2026/poster/154816) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [S2D: Sparse-To-Dense Keymask Distillation for Unsupervised Video Instance Segmentation](https://neurips.cc/virtual/2026/poster/153406) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Model Distribution-Aware Multimodal Dataset Distillation](https://neurips.cc/virtual/2026/poster/148787) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Beyond Outcome Rewards: Step-Level Self-Distilled Policy Optimization for Deep Search Agents](https://neurips.cc/virtual/2026/poster/154780) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [RAIL: Representation-Aligned Imitation Learning for Student-Compatible Teacher Policies](https://neurips.cc/virtual/2026/poster/154487) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [WASD: Wasserstein-based Knowledge Distillation for Large Language Models](https://neurips.cc/virtual/2026/poster/154228) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Knowledge Transfer Scaling Laws for 3D Medical Imaging](https://neurips.cc/virtual/2026/poster/149904) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Variance Reduction for Expectations with Diffusion Teachers](https://neurips.cc/virtual/2026/poster/153246) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [VISD: Enhancing Video Reasoning via Structured Self-Distillation](https://neurips.cc/virtual/2026/poster/154414) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Beyond Stabilization: Dual-EMA Teachers for Global–Local Semantic Learning in Semi-Supervised Medical Image Segmentation](https://neurips.cc/virtual/2026/poster/153534) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [D-OPSD: On-Policy Self-Distillation for Continuously Tuning Step-Distilled Diffusion Models](https://neurips.cc/virtual/2026/poster/153949) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Training with Harnesses: On-Policy Harness Self-Distillation for Complex Reasoning](https://neurips.cc/virtual/2026/poster/149380) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Fewer Tokens, Fewer Layers: Efficient Vision Token Pruning and On-Policy Distillation to Accelerate VLMs](https://neurips.cc/virtual/2026/poster/152441) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [DDMS: Discriminative Distillation of Multi-view Foundational Features into Single-view Models](https://neurips.cc/virtual/2026/poster/148341) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2026 | [CoDMD: Copula-aware Distribution Matching Distillation for Fast Video Generation](https://neurips.cc/virtual/2026/poster/154796) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [$\boldsymbol{f}$-OPD: Stabilizing Long-Horizon On-Policy Distillation with Freshness-Aware Control](https://neurips.cc/virtual/2026/poster/150017) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Teach-to-Reason: Competition-Guided Reasoning with a Self-Improving Teacher](https://neurips.cc/virtual/2026/poster/150121) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Visual-Advantage On-Policy Distillation for Vision-Language Models](https://neurips.cc/virtual/2026/poster/149701) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [From Solver Trajectories to Teaching Trajectories: Cognition-Aligned Reasoning Distillation](https://neurips.cc/virtual/2026/poster/148685) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [FreDRec: Frequency-Decoupled Knowledge Distillation for Multimodal Recommendation in Missing Modalities Scenarios](https://neurips.cc/virtual/2026/poster/154805) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Learn where to Click from Yourself: On-Policy Self-Distillation for GUI Grounding](https://neurips.cc/virtual/2026/poster/155839) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Temporal Prototype Alignment for Frozen-Feature Dataset Distillation](https://neurips.cc/virtual/2026/poster/149275) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Distill to Think, Foresee to Act: Cognitive-Physical Reinforcement Learning for Autonomous Driving](https://neurips.cc/virtual/2026/poster/153115) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Phase-wise Velocity Distillation: Towards Effective Image Generation with A Single NFE](https://neurips.cc/virtual/2026/poster/150700) | E2 | title |
| NeurIPS 2026 | [Efficient Hybrid Distillation: Synergizing Score and Adversarial Objectives for One-Step Diffusion](https://neurips.cc/virtual/2026/poster/153904) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Path-Guided Flow Matching for Dataset Distillation](https://neurips.cc/virtual/2026/poster/149871) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Rethinking Dataset Distillation for Classification: Do Distilled Sets Outperform Coresets?](https://neurips.cc/virtual/2026/poster/139495) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Multi-view Relational Distillation for Spatial Reasoning with Vision-Language Models](https://neurips.cc/virtual/2026/poster/152091) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Behavior Cloning is Not All You Need: The Optimality of On-Policy Distillation for Noisy Expert Feedback](https://neurips.cc/virtual/2026/poster/150673) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Beyond SFT-to-RL: Pre-alignment via Black-box On-policy Distillation for Multimodal RL](https://neurips.cc/virtual/2026/poster/153111) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [The Kernel Reality Check: Benchmarking and Distilling Efficient Attention at Scale](https://neurips.cc/virtual/2026/poster/149008) | E2 | title |
| NeurIPS 2026 | [Value-Rectified Distillation for Flow-based Offline Reinforcement Learning](https://neurips.cc/virtual/2026/poster/149851) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [DetailAnywhere: Fashion Detail Generation via Cross-Modal Feature Alignment Distillation](https://neurips.cc/virtual/2026/poster/151134) | E2 | title |
| NeurIPS 2026 | [Minimax Rates and Spectral Distillation for Tree Ensembles](https://neurips.cc/virtual/2026/poster/155405) | E2 | title |
| NeurIPS 2026 | [Efficient Dataset Distillation for Pre-Trained Self-Supervised Models via Statistical Flow Matching](https://neurips.cc/virtual/2026/poster/155616) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information](https://neurips.cc/virtual/2026/poster/149938) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [FlashControl: One-Step Controllable Generator via Distillation-Friendly Single-Stream Teachers.](https://neurips.cc/virtual/2026/poster/154256) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Distribution Matching Distillation without Fake Score Network](https://neurips.cc/virtual/2026/poster/151363) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2026 | [Pruning and Distilling Mixture-of-Experts into Dense Language Models](https://neurips.cc/virtual/2026/poster/150472) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Teacher-Aware Evolution of Heuristic Programs from Learned Optimization Policies](https://neurips.cc/virtual/2026/poster/151024) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Improving Generative Adversarial Networks with Self-Distillation](https://neurips.cc/virtual/2026/poster/151051) | E2 | title |
| NeurIPS 2026 | [ByteDistill: Cross-Tokenizer Distillation via Chunk-wise Byte-Level Distribution Alignment](https://neurips.cc/virtual/2026/poster/149633) | E2 | title |
| NeurIPS 2026 | [The Voice-Native Classroom: Multilingual AI Co-Teachers for Global ML Education](https://neurips.cc/virtual/2026/poster/137880) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2026 | [Vision-OPD: Learning to See Fine Details for Multimodal LLMs via On-Policy Self-Distillation](https://neurips.cc/virtual/2026/poster/151295) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Hide to See: Reasoning-prefix Masking for Visual-anchored Thinking in VLM Distillation](https://neurips.cc/virtual/2026/poster/149574) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [RelaVPR: Relation-Based Knowledge Distillation for Efficient Visual Place Recognition](https://neurips.cc/virtual/2026/poster/151495) | E2 | title |
| NeurIPS 2026 | [Self-Distilled RLVR](https://neurips.cc/virtual/2026/poster/152431) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2026 | [SimCT: Recovering Lost Supervision for Cross-Tokenizer On-Policy Distillation](https://neurips.cc/virtual/2026/poster/153233) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [The Locality Cost of Semantic Patch Self-Distillation](https://neurips.cc/virtual/2026/poster/150207) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2026 | [Trainable Sparse Attention via Hybrid Top-k+Top-p Masking and Distillation Fine-Tuning](https://neurips.cc/virtual/2026/poster/154615) | E2 | title |
| NeurIPS 2026 | [Revisiting On-policy Adversarial Black-Box Distillation: Calibrating Groupwise Reward Geometry for Effective Advantage Construction](https://neurips.cc/virtual/2026/poster/155928) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Heterogeneous Graph Federated Learning with Structure-Aware Data-Free Distillation](https://neurips.cc/virtual/2026/poster/148359) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Learning from Disagreement: Multi-Teacher Distillation for Chinese Spelling Correction](https://neurips.cc/virtual/2026/poster/151148) | E2 | title |
| NeurIPS 2026 | [Multilingual Safety Alignment via Self-Distillation](https://neurips.cc/virtual/2026/poster/151163) | E2 | title |
| NeurIPS 2026 | [Contractive Restoring Flows: Robust Reasoning Distillation via Orbital Stability](https://neurips.cc/virtual/2026/poster/152740) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Your Teacher Can’t Help You Here: Combating Supervision Fidelity Decay in On-Policy Distillation](https://neurips.cc/virtual/2026/poster/154216) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Med-Agentic: Distilling Agentic Medical Reasoning with Internalized Meta-Capabilities](https://neurips.cc/virtual/2026/poster/153012) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [NNCoxKL: Risk-Set Distillation from Probability-Free Prognostic Teachers for Deep Cox Models](https://neurips.cc/virtual/2026/poster/154182) | E2 | title |
| NeurIPS 2026 | [Subliminal Learning as Trait-Direction Drift: A Mechanism and Targeted Control under SFT Distillation](https://neurips.cc/virtual/2026/poster/154775) | E2 | title |
| NeurIPS 2026 | [Joint Sequence--Vocabulary Selection for Efficient LLM Distillation](https://neurips.cc/virtual/2026/poster/152047) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Speculative Self-Distillation enables Efficient Knowledge Internalization](https://neurips.cc/virtual/2026/poster/155356) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [DinoComplete: 3D Shape Completion with Distilled Semantic Priors and State Space Models](https://neurips.cc/virtual/2026/poster/155664) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [AsyncOPD: How Stale Can On-Policy Distillation Be?](https://neurips.cc/virtual/2026/poster/156136) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Latent Spatial Reasoning: Building Innate 3D Awareness via Latent-Space Distillation](https://neurips.cc/virtual/2026/poster/154054) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Facts Don't Speak Louder than Words: The Behavioral Essence of Long-CoT Distillation](https://neurips.cc/virtual/2026/poster/153530) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2026 | [BayesAT: Bayes-Guided Progressive Distillation for Semi-Supervised Adversarial Training](https://neurips.cc/virtual/2026/poster/150593) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2026 | [Distillation of Foundation Models for Time-dependent PDEs](https://neurips.cc/virtual/2026/poster/155669) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Closed-Form Linear-Probe Dataset Distillation for Pre-trained Vision Models](https://neurips.cc/virtual/2026/poster/153458) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Collaborative Reasoning Distillation via Cross-Feedback and Coherent Curation](https://neurips.cc/virtual/2026/poster/152076) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [High Performance Differentially Private Fine-Tuning using Dataset Distillation](https://neurips.cc/virtual/2026/poster/153009) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Spatial Representation Distillation and Knowledge Routing for Vision-Language-Action Models](https://neurips.cc/virtual/2026/poster/154721) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [X-AVDD: Cross-Attentive Audio-Visual Dataset Distillation](https://neurips.cc/virtual/2026/poster/153215) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Distilling Conditional Image Generators into Spatial Effect Maps](https://neurips.cc/virtual/2026/poster/148655) | E2 | title |
| NeurIPS 2026 | [On-Policy Distillation with Open Property-Equivalence Reward for LLM-Based NL-to-SVA Generation](https://neurips.cc/virtual/2026/poster/149770) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [SEAD: Competence-Aware On-Policy Distillation via Entropy-Guided Supervision](https://neurips.cc/virtual/2026/poster/155569) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Conflict-Aware Logit Adapters for Utility-Preserving Anti-Distillation](https://neurips.cc/virtual/2026/poster/152508) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2026 | [Distilling What Matters: Confidence-Aware Selective Distillation for Large Language Models](https://neurips.cc/virtual/2026/poster/149862) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Reason in the Words You Speak: Idiolectal Paraphrasing Off-Policy Traces for Reasoning Distillation in VideoLLMs](https://neurips.cc/virtual/2026/poster/149165) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Learning from the Self-future: On-policy Self-distillation for dLLMs](https://neurips.cc/virtual/2026/poster/153722) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Improving Neural Processes in the Low-Data Regime via Context-Subset Training and Self-Distillation](https://neurips.cc/virtual/2026/poster/148845) | E2 | title |
| NeurIPS 2026 | [Matched-Control Tests of Partition-Source Claims in One Routed Distillation Family](https://neurips.cc/virtual/2026/poster/152841) | E2 | title |
| NeurIPS 2026 | [Distilling Multi-Teacher Scoring Principles for Unsupervised Time Series Anomaly Detection](https://neurips.cc/virtual/2026/poster/151289) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Distilling Graph Geometry: Knowledge Gap from GNNs to MLPs](https://neurips.cc/virtual/2026/poster/150714) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Towards Precise Knowledge Distillation for Large Language Models via Knowledge Probing](https://neurips.cc/virtual/2026/poster/151591) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Codebook-Guided Cross-Modal Knowledge Distillation for Structurally Heterogeneous Features](https://neurips.cc/virtual/2026/poster/155243) | E2 | title |
| NeurIPS 2026 | [Standing on the Shoulders of Giants: Rethinking EEG Foundation Model Pretraining via Multi-Teacher Distillation](https://neurips.cc/virtual/2026/poster/150310) | E2 | title |
| NeurIPS 2026 | [RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models](https://neurips.cc/virtual/2026/poster/150692) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [S$^2$-RL: Sample-Set Dual Reinforcement Learning for Generative Semantic Segmentation Dataset Distillation](https://neurips.cc/virtual/2026/poster/155529) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Dataset Distillation via Drifting](https://neurips.cc/virtual/2026/poster/155633) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [TriTD: Tri-Partite Trajectory–Distribution Distillation for Real-Time Autoregressive Video Generation](https://neurips.cc/virtual/2026/poster/154734) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [KL for a KL: On-Policy Distillation with Control Variate Baseline](https://neurips.cc/virtual/2026/poster/149290) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Subliminal Learning Is Steering Vector Distillation](https://neurips.cc/virtual/2026/poster/153935) | E2 | title |
| NeurIPS 2026 | [On the Memorization of Consistency Distillation for Diffusion Models](https://neurips.cc/virtual/2026/poster/152743) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Learning Visual Speech Representations via Cross-Modal Distillation and Joint Face-Lip Modeling](https://neurips.cc/virtual/2026/poster/149522) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Locking Pretrained Weights via Deep Low-Rank Residual Distillation](https://neurips.cc/virtual/2026/poster/149948) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2026 | [Decomposing SGD Dynamics in Neural Networks: Teacher-Induced Spikes and Variance Inflation](https://neurips.cc/virtual/2026/poster/149560) | SUPPORT | title (manual override) |
| NeurIPS 2026 | [Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents](https://neurips.cc/virtual/2026/poster/151567) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Beyond Raw Observations: Distilling and Storing Invariant Driving Memories for Generalizable Autonomous Driving](https://neurips.cc/virtual/2026/poster/152198) | E2 | title |
| NeurIPS 2026 | [ControlFlow3D: Distilling Multi-View Knowledge into Latent Flow Matching for Point Cloud Upsampling](https://neurips.cc/virtual/2026/poster/151092) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [$\mathbf{D^{3}S^{2}}$: Diffusion-Guided Dataset Distillation for Semantic Segmentation](https://neurips.cc/virtual/2026/poster/155224) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [FlashSSM-3D: A Distilled State Space Model for Lightning-Fast Dense 3D Reconstruction](https://neurips.cc/virtual/2026/poster/149335) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [VoluCore: Spanning Teacher Representations with Volumetric Coresets for Data-Efficient LLM Distillation](https://neurips.cc/virtual/2026/poster/155942) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [FedProG: Federated Graph Learning via Server-Side LLM Semantic Bridging and Uncertainty-Aware Distillation](https://neurips.cc/virtual/2026/poster/155040) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Continuous-Time Distribution Matching for Few-Step Diffusion Distillation](https://neurips.cc/virtual/2026/poster/150079) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Beyond the Golden Teacher: Enhancing Graph Learning through LLM-GNN Co-teaching](https://neurips.cc/virtual/2026/poster/150344) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Logical Distillation of Transformer Encoders](https://neurips.cc/virtual/2026/poster/148712) | E2 | title |
| NeurIPS 2026 | [Diffusion fine-tuning with Rewarded Moment Matching Distillation](https://neurips.cc/virtual/2026/poster/150176) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [TextSeal: A Localized LLM Watermark for Provenance & Distillation Protection](https://neurips.cc/virtual/2026/poster/152304) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [DiLaDiff: Distilled Latent-augmented Diffusion for Language Modeling](https://neurips.cc/virtual/2026/poster/150062) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Learning Transferable Representations from Operating System Entities via Provenance Graph Distillation](https://neurips.cc/virtual/2026/poster/151915) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Distilling LLM Feedback for Lean Theorem Proving](https://neurips.cc/virtual/2026/poster/154163) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [GDSD: Reinforcement Learning as Guided Denoiser Self-Distillation for Diffusion Language Models](https://neurips.cc/virtual/2026/poster/151913) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [OneSearch-V2: The Latent Reasoning Enhanced Self-distillation Generative Search Framework](https://neurips.cc/virtual/2026/poster/152224) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [GDMD: Guiding Distribution Matching Distillation with Gradient-Based Reinforcement Learning](https://neurips.cc/virtual/2026/poster/152678) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Dense Cross-Tokenizer Distillation via Semantic Optimal Local Alignment](https://neurips.cc/virtual/2026/poster/153427) | E2 | title |
| NeurIPS 2026 | [Efficient Knowledge Transfer in Federated Bayesian Optimization through Neural Network Surrogates](https://neurips.cc/virtual/2026/poster/151479) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [SD-Search: Hindsight Self-Distillation for Search-Augmented Reasoning](https://neurips.cc/virtual/2026/poster/155518) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Self-Distillation of Hidden Layers for Masked Self-Supervised Representation Learning](https://neurips.cc/virtual/2026/poster/150397) | E1 | title: KD not the contribution / not classification KD |
| NeurIPS 2026 | [Heterogeneity-aware Distillation for Federated Continual Learning](https://neurips.cc/virtual/2026/poster/155355) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [DD-Ranking: Rethinking the Evaluation of Dataset Distillation](https://neurips.cc/virtual/2026/poster/139355) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [CoTrek: Toward Scalable On-Policy Distillation for Long Chain-of-Thought Reasoning](https://neurips.cc/virtual/2026/poster/154397) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Learning What to Remember: Test-Time Training via Context Distillation](https://neurips.cc/virtual/2026/poster/153696) | E2 | title |
| NeurIPS 2026 | [HEED: Density-Weighted Residual Alignment for Hybrid Vision-Language Model Distillation](https://neurips.cc/virtual/2026/poster/150667) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [A Few Teacher Steps Go a Long Way: Cost-Efficient On-Policy Data Augmentation for Agent Post-Training](https://neurips.cc/virtual/2026/poster/150832) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [DeltaPrompts: Escaping the Zero-Delta Trap in Multimodal Distillation](https://neurips.cc/virtual/2026/poster/153494) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Align and Distill: Unifying and Improving Domain Adaptive Object Detection](https://neurips.cc/virtual/2026/poster/156740) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [AgentArk: Distilling Multi-Agent Intelligence into a Single LLM Agent](https://neurips.cc/virtual/2026/poster/149790) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [PatternBloom: Empowering Agentic RAG with Externalized RL-Distilled Graph Patterns](https://neurips.cc/virtual/2026/poster/152560) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Scaling Multi-Teacher Distillation for Digital Pathology](https://neurips.cc/virtual/2026/poster/148948) | E2 | title |
| NeurIPS 2026 | [SHRED: Retain-Set-Free Unlearning via Self-Distillation with Logit Demotion](https://neurips.cc/virtual/2026/poster/151972) | E2 | title |
| NeurIPS 2026 | [LARK: Learnability-Grounded Trajectory Selection for Efficient Reasoning Distillation](https://neurips.cc/virtual/2026/poster/149142) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Procedural Memory Distillation: Online Reflection for Self-Improving Language Models](https://neurips.cc/virtual/2026/poster/148323) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Relational Feature Distillation for Lightweight 3D Point Cloud Segmentation](https://neurips.cc/virtual/2026/poster/148750) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Decompose the Distillation: Interpretable Single-Pass Guidance for Diffusion Models](https://neurips.cc/virtual/2026/poster/152875) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Progress-Aware Distillation for Mitigating Stagnation in Small Language Model Agents](https://neurips.cc/virtual/2026/poster/149176) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Relaxed On-Policy Distillation: Selective Credit Allocation for Scaling Reasoning Efficiently](https://neurips.cc/virtual/2026/poster/150064) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Learning to Follow In-Context Watermark Instructions via Self-Distillation](https://neurips.cc/virtual/2026/poster/150382) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Proposing Better Rollouts for On-Policy Distillation](https://neurips.cc/virtual/2026/poster/155190) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Rethinking On-Policy Self-Distillation for Thinking Models](https://neurips.cc/virtual/2026/poster/152392) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Counterfactual Distillation: Internalizing Reflective Experience into LLM Agent](https://neurips.cc/virtual/2026/poster/154297) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Reviving Stale Updates: Data-Free Knowledge Distillation for Asynchronous Federated Learning](https://neurips.cc/virtual/2026/poster/152286) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Cornerstones or Stumbling Blocks? Deciphering the Rock Tokens in On-Policy Distillation](https://neurips.cc/virtual/2026/poster/152055) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Structural Rationale Distillation via Reasoning Space Compression](https://neurips.cc/virtual/2026/poster/152271) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Distilling Sequential Computation in Transformer Language Models](https://neurips.cc/virtual/2026/poster/150342) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Strong Teacher Not Needed? On Distillation in LLM Pretraining](https://neurips.cc/virtual/2026/poster/153838) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Few-Step Diffusion Language Models via Trajectory Self-Distillation](https://neurips.cc/virtual/2026/poster/151333) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [The Many Faces of On-Policy Distillation: Pitfalls, Mechanisms, and Fixes](https://neurips.cc/virtual/2026/poster/153073) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Learning from Language Feedback via Variational Policy Distillation](https://neurips.cc/virtual/2026/poster/152357) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation](https://neurips.cc/virtual/2026/poster/153652) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [On-Policy Hindsight Distillation for Early Risk Prediction](https://neurips.cc/virtual/2026/poster/153484) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [LCD$^3$: Layout-Conditioned Diffusion for Dataset Distillation in Object Detection](https://neurips.cc/virtual/2026/poster/150456) | E6 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [Enabling Preference-driven Unlearning in Few-step Distilled Text-to-Image Diffusion Models](https://neurips.cc/virtual/2026/poster/154856) | E2 | title (auto keyword, checked by hand) |
| NeurIPS 2026 | [When Are Teacher Tokens Reliable? Position-Weighted On-Policy Self-Distillation for Reasoning](https://neurips.cc/virtual/2026/poster/148618) | E2 | title (auto keyword, checked by hand) |
| ICLR 2022 | [Cold Brew: Distilling Graph Node Representations with Incomplete or Missing Neighborhoods](https://iclr.cc/virtual/2022/poster/7094) | E2 | title (auto keyword, checked by hand) |
| ICLR 2022 | [OBJECT DYNAMICS DISTILLATION FOR SCENE DECOMPOSITION AND REPRESENTATION](https://iclr.cc/virtual/2022/poster/6826) | E2 | title |
| ICLR 2022 | [Open-vocabulary Object Detection via Vision and Language Knowledge Distillation](https://iclr.cc/virtual/2022/poster/6372) | E2 | title (auto keyword, checked by hand) |
| ICLR 2022 | [Unsupervised Semantic Segmentation by Distilling Feature Correspondences](https://iclr.cc/virtual/2022/poster/6068) | E2 | title (auto keyword, checked by hand) |
| ICLR 2022 | [Towards Model Agnostic Federated Learning Using Knowledge Distillation](https://iclr.cc/virtual/2022/poster/6644) | E2 | title (auto keyword, checked by hand) |
| ICLR 2022 | [Bag of Instances Aggregation Boosts Self-supervised Distillation](https://iclr.cc/virtual/2022/poster/5909) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2022 | [Data Efficient Language-Supervised Zero-Shot Recognition with Optimal Transport Distillation](https://iclr.cc/virtual/2022/poster/6582) | E2 | title |
| ICLR 2022 | [Learning curves for continual learning in neural networks: Self-knowledge transfer and forgetting](https://iclr.cc/virtual/2022/poster/6690) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2022 | [Progressive Distillation for Fast Sampling of Diffusion Models](https://iclr.cc/virtual/2022/poster/6537) | E2 | title (auto keyword, checked by hand) |
| ICLR 2022 | [Trans-Encoder: Unsupervised sentence-pair modelling through self- and mutual-distillations](https://iclr.cc/virtual/2022/poster/6242) | E2 | title |
| ICLR 2022 | [MonoDistill: Learning Spatial Features for Monocular 3D Object Detection](https://iclr.cc/virtual/2022/poster/6677) | E2 | title (auto keyword, checked by hand) |
| ICLR 2022 | [Distilling GANs with Style-Mixed Triplets for X2I Translation with Limited Data](https://iclr.cc/virtual/2022/poster/6708) | E2 | title (auto keyword, checked by hand) |
| ICLR 2022 | [Improving Non-Autoregressive Translation Models Without Distillation](https://iclr.cc/virtual/2022/poster/7197) | E2 | title |
| ICLR 2022 | [Graph-less Neural Networks: Teaching Old MLPs New Tricks Via Distillation](https://iclr.cc/virtual/2022/poster/6711) | E2 | title (auto keyword, checked by hand) |
| ICLR 2022 | [Online Hyperparameter Meta-Learning with Hypergradient Distillation](https://iclr.cc/virtual/2022/poster/6204) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2023 | [Distilling Model Failures as Directions in Latent Space](https://iclr.cc/virtual/2023/poster/11743) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2023 | [Cross-Level Distillation and Feature Denoising for Cross-Domain Few-Shot Classification](https://iclr.cc/virtual/2023/poster/12203) | E2 | title (auto keyword, checked by hand) |
| ICLR 2023 | [Meta-prediction Model for Distillation-Aware NAS on Unseen Datasets](https://iclr.cc/virtual/2023/poster/12067) | E1 | title (manual override) |
| ICLR 2023 | [Autoencoders as Cross-Modal Teachers: Can Pretrained 2D Image Transformers Help 3D Representation Learning?](https://iclr.cc/virtual/2023/poster/11988) | E2 | title (auto keyword, checked by hand) |
| ICLR 2023 | [Knowledge Distillation based Degradation Estimation for Blind Super-Resolution](https://iclr.cc/virtual/2023/poster/12136) | E2 | title |
| ICLR 2023 | [The Modality Focusing Hypothesis: Towards Understanding Crossmodal Knowledge Distillation](https://iclr.cc/virtual/2023/poster/11737) | E2 | title |
| ICLR 2023 | [A System for Morphology-Task Generalization via Unified Representation and Behavior Distillation](https://iclr.cc/virtual/2023/poster/11363) | E2 | title |
| ICLR 2023 | [Exploring The Role of Mean Teachers in Self-supervised Masked Auto-Encoders](https://iclr.cc/virtual/2023/poster/11930) | E2 | title |
| ICLR 2023 | [Distilling Cognitive Backdoor Patterns within an Image](https://iclr.cc/virtual/2023/poster/12155) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2023 | [3D Segmenter: 3D Transformer based Semantic Segmentation via 2D Panoramic Distillation](https://iclr.cc/virtual/2023/poster/11824) | E2 | title (auto keyword, checked by hand) |
| ICLR 2023 | [Effective Self-supervised Pre-training on Low-compute Networks without Distillation](https://iclr.cc/virtual/2023/poster/12108) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2023 | [HomoDistil: Homotopic Task-Agnostic Distillation of Pre-trained Transformers](https://iclr.cc/virtual/2023/poster/10956) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2023 | [AutoTransfer: AutoML with Knowledge Transfer - An Application to Graph Neural Networks](https://iclr.cc/virtual/2023/poster/11462) | E2 | title (auto keyword, checked by hand) |
| ICLR 2023 | [In-context Reinforcement Learning with Algorithm Distillation](https://iclr.cc/virtual/2023/poster/11148) | E2 | title (auto keyword, checked by hand) |
| ICLR 2023 | [Self-Distillation for Further Pre-training of Transformers](https://iclr.cc/virtual/2023/poster/12123) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2023 | [BEVDistill: Cross-Modal BEV Distillation for Multi-View 3D Object Detection](https://iclr.cc/virtual/2023/poster/12222) | E2 | title (auto keyword, checked by hand) |
| ICLR 2023 | [Model ensemble instead of prompt fusion: a sample-specific knowledge transfer method for few-shot prompt tuning](https://iclr.cc/virtual/2023/poster/11794) | E2 | title (auto keyword, checked by hand) |
| ICLR 2023 | [Scaling Up Probabilistic Circuits by Latent Variable Distillation](https://iclr.cc/virtual/2023/poster/10744) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2023 | [Weakly Supervised Knowledge Transfer with Probabilistic Logical Reasoning for Object Detection](https://iclr.cc/virtual/2023/poster/11578) | E2 | title (auto keyword, checked by hand) |
| ICLR 2023 | [Excess Risk of Two-Layer ReLU Neural Networks in Teacher-Student Settings and its Superiority to Kernel Methods](https://iclr.cc/virtual/2023/poster/10813) | SUPPORT | title (manual override) |
| ICLR 2023 | [The Best of Both Worlds: Accurate Global and Personalized Models through Federated Learning with Data-Free Hyper-Knowledge Distillation](https://iclr.cc/virtual/2023/poster/10802) | E2 | title (auto keyword, checked by hand) |
| ICLR 2023 | [Wasserstein Auto-encoded MDPs: Formal Verification of Efficiently Distilled RL Policies with Many-sided Guarantees](https://iclr.cc/virtual/2023/poster/11247) | E2 | title (auto keyword, checked by hand) |
| ICLR 2024 | [Towards Lossless Dataset Distillation via Difficulty-Aligned Trajectory Matching](https://iclr.cc/virtual/2024/poster/17692) | E6 | title (auto keyword, checked by hand) |
| ICLR 2024 | [Training Graph Transformers via Curriculum-Enhanced Attention Distillation](https://iclr.cc/virtual/2024/poster/18040) | E2 | title (auto keyword, checked by hand) |
| ICLR 2024 | [Noise-free Score Distillation](https://iclr.cc/virtual/2024/poster/18247) | E2 | title (auto keyword, checked by hand) |
| ICLR 2024 | [ZeroFlow: Scalable Scene Flow via Distillation](https://iclr.cc/virtual/2024/poster/19064) | E2 | title |
| ICLR 2024 | [Self-Supervised Dataset Distillation for Transfer Learning](https://iclr.cc/virtual/2024/poster/18115) | E6 | title (auto keyword, checked by hand) |
| ICLR 2024 | [Mirage: Model-agnostic Graph Distillation for Graph Classification](https://iclr.cc/virtual/2024/poster/19373) | E2 | title (auto keyword, checked by hand) |
| ICLR 2024 | [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://iclr.cc/virtual/2024/poster/19484) | E2 | title (auto keyword, checked by hand) |
| ICLR 2024 | [Behaviour Distillation](https://iclr.cc/virtual/2024/poster/17711) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2024 | [SparseDFF: Sparse-View Feature Distillation for One-Shot Dexterous Manipulation](https://iclr.cc/virtual/2024/poster/19000) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2024 | [Masked Distillation Advances Self-Supervised Transformer Architecture Search](https://iclr.cc/virtual/2024/poster/18864) | E2 | title |
| ICLR 2024 | [Toward effective protection against diffusion-based mimicry through score distillation](https://iclr.cc/virtual/2024/poster/18759) | E2 | title (auto keyword, checked by hand) |
| ICLR 2024 | [Hybrid Distillation: Connecting Masked Autoencoders with Contrastive Learners](https://iclr.cc/virtual/2024/poster/18021) | E2 | title |
| ICLR 2024 | [CLIPSelf: Vision Transformer Distills Itself for Open-Vocabulary Dense Prediction](https://iclr.cc/virtual/2024/poster/19128) | E2 | title |
| ICLR 2024 | [Embarrassingly Simple Dataset Distillation](https://iclr.cc/virtual/2024/poster/18710) | E6 | title (auto keyword, checked by hand) |
| ICLR 2024 | [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://iclr.cc/virtual/2024/poster/17899) | E2 | title (auto keyword, checked by hand) |
| ICLR 2024 | [FROSTER: Frozen CLIP is A Strong Teacher for Open-Vocabulary Action Recognition](https://iclr.cc/virtual/2024/poster/17380) | E2 | title (auto keyword, checked by hand) |
| ICLR 2024 | [UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition](https://iclr.cc/virtual/2024/poster/17704) | E2 | title (auto keyword, checked by hand) |
| ICLR 2024 | [Unsupervised Pretraining for Fact Verification by Language Model Distillation](https://iclr.cc/virtual/2024/poster/19573) | E2 | title (auto keyword, checked by hand) |
| ICLR 2024 | [Tailoring Self-Rationalizers with Multi-Reward Distillation](https://iclr.cc/virtual/2024/poster/17624) | E2 | title (auto keyword, checked by hand) |
| ICLR 2024 | [Text-to-3D with Classifier Score Distillation](https://iclr.cc/virtual/2024/poster/17961) | E2 | title (auto keyword, checked by hand) |
| ICLR 2024 | [DistillSpec: Improving Speculative Decoding via Knowledge Distillation](https://iclr.cc/virtual/2024/poster/17680) | E2 | title (auto keyword, checked by hand) |
| ICLR 2024 | [Rethinking Backdoor Attacks on Dataset Distillation: A Kernel Method Perspective](https://iclr.cc/virtual/2024/poster/18070) | E6 | title (auto keyword, checked by hand) |
| ICLR 2024 | [Towards Robust and Efficient Cloud-Edge Elastic Model Adaptation via Selective Entropy Distillation](https://iclr.cc/virtual/2024/poster/17525) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2024 | [P2Seg: Pointly-supervised Segmentation via Mutual Distillation](https://iclr.cc/virtual/2024/poster/19231) | E2 | title (auto keyword, checked by hand) |
| ICLR 2024 | [MEND: Meta Demonstration Distillation for Efficient and Effective In-Context Learning](https://iclr.cc/virtual/2024/poster/19544) | E2 | title |
| ICLR 2024 | [MBR and QE Finetuning: Training-time Distillation of the Best and Most Expensive Decoding Methods](https://iclr.cc/virtual/2024/poster/18325) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2024 | [Ensemble Distillation for Unsupervised Constituency Parsing](https://iclr.cc/virtual/2024/poster/18643) | E2 | title |
| ICLR 2024 | [Understanding Reconstruction Attacks with the Neural Tangent Kernel and Dataset Distillation](https://iclr.cc/virtual/2024/poster/18493) | E6 | title (auto keyword, checked by hand) |
| ICLR 2024 | [MiniLLM: Knowledge Distillation of Large Language Models](https://iclr.cc/virtual/2024/poster/19420) | E2 | title (auto keyword, checked by hand) |
| ICLR 2024 | [Data Distillation Can Be Like Vodka: Distilling More Times For Better Quality](https://iclr.cc/virtual/2024/poster/19592) | E6 | title |
| ICLR 2024 | [LightHGNN: Distilling Hypergraph Neural Networks into MLPs for 100x Faster Inference](https://iclr.cc/virtual/2024/poster/17940) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2024 | [Towards the Fundamental Limits of Knowledge Transfer over Finite Domains](https://iclr.cc/virtual/2024/poster/18387) | SUPPORT | title (analysis-only) |
| ICLR 2024 | [RLCD: Reinforcement Learning from Contrastive Distillation for LM Alignment](https://iclr.cc/virtual/2024/poster/17552) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [MiniPLM: Knowledge Distillation for Pre-training Language Models](https://iclr.cc/virtual/2025/poster/28062) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Elucidating the Preconditioning in Consistency Distillation](https://iclr.cc/virtual/2025/poster/30971) | E2 | title |
| ICLR 2025 | [InstantPortrait: One-Step Portrait Editing via Diffusion Multi-Objective Distillation](https://iclr.cc/virtual/2025/poster/29200) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Beyond Autoregression: Fast LLMs via Self-Distillation Through Time](https://iclr.cc/virtual/2025/poster/27972) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Dataset Distillation via Knowledge Distillation: Towards Efficient Self-Supervised Pre-training of Deep Networks](https://iclr.cc/virtual/2025/poster/29070) | E6 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://iclr.cc/virtual/2025/poster/27759) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models](https://iclr.cc/virtual/2025/poster/29025) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Knowledge Distillation with Multi-granularity Mixture of Priors for Image Super-Resolution](https://iclr.cc/virtual/2025/poster/29042) | E2 | title |
| ICLR 2025 | [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://iclr.cc/virtual/2025/poster/27754) | E2 | title |
| ICLR 2025 | [Distilling Reinforcement Learning Algorithms for In-Context Model-Based Planning](https://iclr.cc/virtual/2025/poster/30559) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Adaptive teachers for amortized samplers](https://iclr.cc/virtual/2025/poster/30561) | E2 | title |
| ICLR 2025 | [UniDetox: Universal Detoxification of Large Language Models via Dataset Distillation](https://iclr.cc/virtual/2025/poster/28932) | E6 | title (auto keyword, checked by hand) |
| ICLR 2025 | [ToVE: Efficient Vision-Language Learning via Knowledge Transfer from Vision Experts](https://iclr.cc/virtual/2025/poster/30410) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Going Beyond Feature Similarity: Effective Dataset distillation based on Class-aware Conditional Mutual Information](https://iclr.cc/virtual/2025/poster/31237) | E6 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Data Distillation for extrapolative protein design through exact preference optimization](https://iclr.cc/virtual/2025/poster/27969) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Score Forgetting Distillation: A Swift, Data-Free Method for Machine Unlearning in Diffusion Models](https://iclr.cc/virtual/2025/poster/28804) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [SLMRec: Distilling Large Language Models into Small for Sequential Recommendation](https://iclr.cc/virtual/2025/poster/30304) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [GIFT: Unlocking Full Potential of Labels in Distilled Dataset at Near-zero Cost](https://iclr.cc/virtual/2025/poster/30327) | E6 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Distilled Decoding 1: One-step Sampling of Image Auto-regressive Models with Flow Matching](https://iclr.cc/virtual/2025/poster/27673) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Breaking Class Barriers: Efficient Dataset Distillation via Inter-Class Feature Compensator](https://iclr.cc/virtual/2025/poster/29331) | E6 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Towards Fast, Specialized Machine Learning Force Fields: Distilling Foundation Models via Energy Hessians](https://iclr.cc/virtual/2025/poster/31192) | E2 | title |
| ICLR 2025 | [Distilling Structural Representations into Protein Sequence Models](https://iclr.cc/virtual/2025/poster/30051) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback](https://iclr.cc/virtual/2025/poster/28093) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Weighted Multi-Prompt Learning with Description-free Large Language Model Distillation](https://iclr.cc/virtual/2025/poster/29892) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [MAESTRO: Masked Encoding Set Transformer with Self-Distillation](https://iclr.cc/virtual/2025/poster/30353) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2025 | [DataEnvGym: Data Generation Agents in Teacher Environments with Student Feedback](https://iclr.cc/virtual/2025/poster/31276) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [RecDreamer: Consistent Text-to-3D Generation via Uniform Score Distillation](https://iclr.cc/virtual/2025/poster/29139) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [BOND: Aligning LLMs with Best-of-N Distillation](https://iclr.cc/virtual/2025/poster/31233) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [ADAPT: Attentive Self-Distillation and Dual-Decoder Prediction Fusion for Continual Panoptic Segmentation](https://iclr.cc/virtual/2025/poster/30235) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [SuperCorrect: Advancing Small LLM Reasoning with Thought Template Distillation and Self-Correction](https://iclr.cc/virtual/2025/poster/29720) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Presto! Distilling Steps and Layers for Accelerating Music Generation](https://iclr.cc/virtual/2025/poster/30264) | E2 | title |
| ICLR 2025 | [Improving Language Model Distillation through Hidden State Matching](https://iclr.cc/virtual/2025/poster/30163) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Chunk-Distilled Language Modeling](https://iclr.cc/virtual/2025/poster/28391) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Efficient Active Imitation Learning with Random Network Distillation](https://iclr.cc/virtual/2025/poster/30291) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Boost Self-Supervised Dataset Distillation via Parameterization, Predefined Augmentation, and Approximation](https://iclr.cc/virtual/2025/poster/31137) | E6 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Influence-Guided Diffusion for Dataset Distillation](https://iclr.cc/virtual/2025/poster/31231) | E6 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Distribution Backtracking Builds A Faster Convergence Trajectory for Diffusion Distillation](https://iclr.cc/virtual/2025/poster/31101) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Distilling Dataset into Neural Field](https://iclr.cc/virtual/2025/poster/28420) | E6 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Guided Score identity Distillation for Data-Free One-Step Text-to-Image Generation](https://iclr.cc/virtual/2025/poster/30232) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Adversarial Score identity Distillation: Rapidly Surpassing the Teacher in One Step](https://iclr.cc/virtual/2025/poster/28519) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2025 | [Repulsive Latent Score Distillation for Solving Inverse Problems](https://iclr.cc/virtual/2025/poster/29081) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Diversity-Rewarded CFG Distillation](https://iclr.cc/virtual/2025/poster/32061) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [DistillHGNN: A Knowledge Distillation Approach for High-Speed Hypergraph Neural Networks](https://iclr.cc/virtual/2025/poster/27878) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2025 | [From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://iclr.cc/virtual/2025/poster/30107) | E2 | title |
| ICLR 2025 | [Flow Distillation Sampling: Regularizing 3D Gaussians with Pre-trained Matching Priors](https://iclr.cc/virtual/2025/poster/30536) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://iclr.cc/virtual/2025/poster/31068) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [AugKD: Ingenious Augmentations Empower Knowledge Distillation for Image Super-Resolution](https://iclr.cc/virtual/2025/poster/30646) | E2 | title |
| ICLR 2025 | [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://iclr.cc/virtual/2025/poster/28137) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Reward Guided Latent Consistency Distillation](https://iclr.cc/virtual/2025/poster/31456) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Linear Multistep Solver Distillation for Fast Sampling of Diffusion Models](https://iclr.cc/virtual/2025/poster/27893) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [BLEND: Behavior-guided Neural Population Dynamics Modeling via Privileged Knowledge Distillation](https://iclr.cc/virtual/2025/poster/28643) | E2 | title |
| ICLR 2025 | [On LLM Knowledge Distillation - A Comparison between Forward KL and Reverse KL](https://iclr.cc/virtual/2025/poster/31335) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Scale-Aware Contrastive Reverse Distillation for Unsupervised Medical Anomaly Detection](https://iclr.cc/virtual/2025/poster/30228) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Consistent Flow Distillation for Text-to-3D Generation](https://iclr.cc/virtual/2025/poster/30650) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Group Distributionally Robust Dataset Distillation with Risk Minimization](https://iclr.cc/virtual/2025/poster/31083) | E6 | title (auto keyword, checked by hand) |
| ICLR 2025 | [LLaVA-MoD: Making LLaVA Tiny via MoE-Knowledge Distillation](https://iclr.cc/virtual/2025/poster/27973) | E2 | title |
| ICLR 2025 | [Tuning Timestep-Distilled Diffusion Model Using Pairwise Sample Optimization](https://iclr.cc/virtual/2025/poster/28873) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://iclr.cc/virtual/2025/poster/30392) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [On the Byzantine-Resilience of Distillation-Based Federated Learning](https://iclr.cc/virtual/2025/poster/28341) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Query-based Knowledge Transfer for Heterogeneous Learning Environments](https://iclr.cc/virtual/2025/poster/29312) | E2 | title |
| ICLR 2025 | [Open-Vocabulary Customization from CLIP via Data-Free Knowledge Distillation](https://iclr.cc/virtual/2025/poster/31193) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [EG4D: Explicit Generation of 4D Object without Score Distillation](https://iclr.cc/virtual/2025/poster/27956) | E2 | title (auto keyword, checked by hand) |
| ICLR 2025 | [Cyclic Contrastive Knowledge Transfer for Open-Vocabulary Object Detection](https://iclr.cc/virtual/2025/poster/30109) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Reasoning Scaffolding: Distilling the Flow of Thought from LLMs](https://iclr.cc/virtual/2026/poster/10010581) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [SkillFactory: Self-Distillation for Learning Cognitive Behaviors](https://iclr.cc/virtual/2026/poster/10006943) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2026 | [Entropy-Monitored Kernelized Token Distillation for Audio-Visual Compression](https://iclr.cc/virtual/2026/poster/10007450) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Distilling Causal Signals for One-Shot Directed Evolution of Antibodies](https://iclr.cc/virtual/2026/poster/10009973) | E2 | title |
| ICLR 2026 | [VARestorer: One-Step VAR Distillation for Real-World Image Super-Resolution](https://iclr.cc/virtual/2026/poster/10009357) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Transformers Trained via Gradient Descent Can Provably Learn a Class of Teacher Models](https://iclr.cc/virtual/2026/poster/10006870) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2026 | [Distillation of Large Language Models via Concrete Score Matching](https://iclr.cc/virtual/2026/poster/10008599) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Streaming Autoregressive Video Generation via Diagonal Distillation](https://iclr.cc/virtual/2026/poster/10009003) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Universal Inverse Distillation for Matching Models with Real-Data Supervision (No GANs)](https://iclr.cc/virtual/2026/poster/10011203) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Scale-wise Distillation of Diffusion Models](https://iclr.cc/virtual/2026/poster/10008849) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Asymmetric Synthetic Data Update for Domain Incremental Dataset Distillation](https://iclr.cc/virtual/2026/poster/10008953) | E6 | title (auto keyword, checked by hand) |
| ICLR 2026 | [DistillKac: Few-Step Image Generation via Damped Wave Equations](https://iclr.cc/virtual/2026/poster/10006712) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation](https://iclr.cc/virtual/2026/poster/10010734) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Accelerating Diffusion Planners in Offline RL via Reward-Aware Consistency Trajectory Distillation](https://iclr.cc/virtual/2026/poster/10008059) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [STAR: Similarity-guided Teacher-Assisted Refinement for Super-Tiny Function Calling Models](https://iclr.cc/virtual/2026/poster/10006893) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2026 | [Cross-Tokenizer Likelihood Scoring Algorithms for Language Model Distillation](https://iclr.cc/virtual/2026/poster/10008081) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Distilling the Thought, Watermarking the Answer: A Principle Semantic Guided Watermark for Reasoning Large Language Models](https://iclr.cc/virtual/2026/poster/10009350) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Meta-Adaptive Prompt Distillation for Few-Shot Visual Question Answering](https://iclr.cc/virtual/2026/poster/10006606) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Boomerang Distillation Enables Zero-Shot Model Size Interpolation](https://iclr.cc/virtual/2026/poster/10011542) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2026 | [DisTaC: Conditioning Task Vectors via Distillation for Robust Model Merging](https://iclr.cc/virtual/2026/poster/10009077) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2026 | [Spectral-guided Physical Dynamics Distillation](https://iclr.cc/virtual/2026/poster/10009710) | E2 | title |
| ICLR 2026 | [CompoDistill: Attention Distillation for Compositional Reasoning in Multimodal LLMs](https://iclr.cc/virtual/2026/poster/10009041) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Motion Prior Distillation in Time Reversal Sampling for Generative Inbetweening](https://iclr.cc/virtual/2026/poster/10010490) | E2 | title |
| ICLR 2026 | [Dataset Distillation as Pushforward Optimal Quantization](https://iclr.cc/virtual/2026/poster/10010609) | E6 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Diffusion Models as Dataset Distillation Priors](https://iclr.cc/virtual/2026/poster/10010354) | E6 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Brain-Semantoks: Learning Semantic Tokens of Brain Dynamics with a Self-Distilled Foundation Model](https://iclr.cc/virtual/2026/poster/10011042) | E2 | title |
| ICLR 2026 | [Splat and Distill: Augmenting Teachers with Feed-Forward 3D Reconstruction For 3D-Aware Distillation](https://iclr.cc/virtual/2026/poster/10011094) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Pedagogically-Inspired Data Synthesis for Language Model Knowledge Distillation](https://iclr.cc/virtual/2026/poster/10010897) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Reverse Distillation: Consistently Scaling Protein Language Model Representations](https://iclr.cc/virtual/2026/poster/10008273) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [FutureMind: Equipping Small Language Models with Strategic Thinking-Pattern Priors via Adaptive Knowledge Distillation](https://iclr.cc/virtual/2026/poster/10008144) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Dataset Distillation for Memorized Data: Soft Labels can Leak Held-Out Teacher Knowledge](https://iclr.cc/virtual/2026/poster/10007648) | E6 | title (auto keyword, checked by hand) |
| ICLR 2026 | [KaVa: Latent Reasoning via Compressed KV-Cache Distillation](https://iclr.cc/virtual/2026/poster/10008323) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [AMiD: Knowledge Distillation for LLMs with $\alpha$-mixture Assistant Distribution](https://iclr.cc/virtual/2026/poster/10011293) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Lightweight Spatio-Temporal Modeling via Temporally Shifted Distillation for Real-Time Accident Anticipation](https://iclr.cc/virtual/2026/poster/10011157) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2026 | [Language Confusion Gate: Language-Aware Decoding Through Model Self-Distillation](https://iclr.cc/virtual/2026/poster/10010179) | E2 | title |
| ICLR 2026 | [CoT-Evo: Evolutionary Distillation of Chain-of-Thought for Scientific Reasoning](https://iclr.cc/virtual/2026/poster/10009790) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Parameterization-Based Dataset Distillation of 3D Point Clouds through Learnable Shape Morphing](https://iclr.cc/virtual/2026/poster/10009568) | E6 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Gumbel Distillation for Parallel Text Generation](https://iclr.cc/virtual/2026/poster/10008724) | E2 | title |
| ICLR 2026 | [Catching the Details: Self-Distilled RoI Predictors for Fine-Grained MLLM Perception](https://iclr.cc/virtual/2026/poster/10010825) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2026 | [DUET: Distilled LLM Unlearning from an Efficiently Contextualized Teacher](https://iclr.cc/virtual/2026/poster/10008958) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Rethinking JEPA: Compute‑Efficient Video Self-Supervised Learning with Frozen Teachers](https://iclr.cc/virtual/2026/poster/10011627) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [VER: Vision Expert Transformer for Robot Learning via Foundation Distillation and Dynamic Routing](https://iclr.cc/virtual/2026/poster/10008667) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Distilling and Adapting: A Topology-Aware Framework for Zero-Shot Interaction Prediction in Multiplex Biological Networks](https://iclr.cc/virtual/2026/poster/10010448) | E2 | title |
| ICLR 2026 | [Token Distillation: Attention-Aware Input Embeddings for New Tokens](https://iclr.cc/virtual/2026/poster/10007514) | E2 | title |
| ICLR 2026 | [Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model Self-Distillation](https://iclr.cc/virtual/2026/poster/10006990) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Algorithmic Guarantees for Distilling Supervised and Offline RL Datasets](https://iclr.cc/virtual/2026/poster/10006407) | E6 | title |
| ICLR 2026 | [Explain in Your Own Words: Improving Reasoning via Token-Selective Dual Knowledge Distillation](https://iclr.cc/virtual/2026/poster/10006422) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Generative Diffusion Prior Distillation for Long-Context Knowledge Transfer](https://iclr.cc/virtual/2026/poster/10008356) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Iterative Distillation for Reward-Guided Fine-Tuning of Diffusion Models in Biomolecular Design](https://iclr.cc/virtual/2026/poster/10009874) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Scaling Knowledge Graph Construction through Synthetic Data Generation and Distillation](https://iclr.cc/virtual/2026/poster/10009128) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Vivid-VR: Distilling Concepts from Text-to-Video Diffusion Transformer for Photorealistic Video Restoration](https://iclr.cc/virtual/2026/poster/10008888) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [GoldenStart: Q-Guided Priors and Entropy Control for Distilling Flow Policies](https://iclr.cc/virtual/2026/poster/10009193) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Exploring Knowledge Purification in Multi-Teacher Knowledge Distillation for LLMs](https://iclr.cc/virtual/2026/poster/10011259) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Incomplete Multi-View Multi-Label Classification via Shared Codebook and Fused-Teacher Self-Distillation](https://iclr.cc/virtual/2026/poster/10010056) | E2 | title |
| ICLR 2026 | [SenseFlow: Scaling Distribution Matching for Flow-based Text-to-Image Distillation](https://iclr.cc/virtual/2026/poster/10008590) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Multimodal Dataset Distillation Made Simple by Prototype-Guided Data Synthesis](https://iclr.cc/virtual/2026/poster/10008585) | E6 | title (auto keyword, checked by hand) |
| ICLR 2026 | [OD$^3$: Optimization-free Dataset Distillation for Object Detection](https://iclr.cc/virtual/2026/poster/10009078) | E6 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Large Scale Diffusion Distillation via Score-Regularized Continuous-Time Consistency](https://iclr.cc/virtual/2026/poster/10011694) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [pi-Flow: Policy-Based Few-Step Generation via Imitation Distillation](https://iclr.cc/virtual/2026/poster/10011793) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [SPECS: Decoupling Multimodal Learning via Self-distilled Preference-based Cold Start](https://iclr.cc/virtual/2026/poster/10007417) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Joint Distillation for Fast Likelihood Evaluation and Sampling in Flow-based Models](https://iclr.cc/virtual/2026/poster/10011167) | E2 | title |
| ICLR 2026 | [Thinking as Society: Multi-Social-Agent Self-Distillation for Multimodal Misinformation Detection](https://iclr.cc/virtual/2026/poster/10007488) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [CoDA: From Text-to-Image Diffusion Models to Training-Free Dataset Distillation](https://iclr.cc/virtual/2026/poster/10011340) | E6 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Probing to Refine: Reinforcement Distillation of LLM Reasoners via Explanatory Inversion](https://iclr.cc/virtual/2026/poster/10007123) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [BIRD: Behavior Induction via Representation-structure Distillation](https://iclr.cc/virtual/2026/poster/10007865) | E1 | title: KD not the contribution / not classification KD |
| ICLR 2026 | [GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation](https://iclr.cc/virtual/2026/poster/10007584) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [BOLT: Decision‑Aligned Distillation and Budget-Aware Routing for Constrained Multimodal QA on Robots](https://iclr.cc/virtual/2026/poster/10009092) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Grounding and Enhancing Informativeness and Utility in Dataset Distillation](https://iclr.cc/virtual/2026/poster/10009293) | E6 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Rejuvenating Cross-Entropy Loss in Knowledge Distillation for Recommender Systems](https://iclr.cc/virtual/2026/poster/10009344) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Distilling to Hybrid Attention Models via KL-Guided Layer Selection](https://iclr.cc/virtual/2026/poster/10009449) | E2 | title |
| ICLR 2026 | [Score Distillation Beyond Acceleration: Generative Modeling from Corrupted Data](https://iclr.cc/virtual/2026/poster/10009500) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Thinking-Free Policy Initialization Makes Distilled Reasoning Models More Effective and Efficient Reasoners](https://iclr.cc/virtual/2026/poster/10009507) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Multimodal Dataset Distillation via Phased Teacher Models](https://iclr.cc/virtual/2026/poster/10009933) | E6 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Distilled Pretraining: A modern lens of Data, In-Context Learning and Test-Time Scaling](https://iclr.cc/virtual/2026/poster/10009683) | E2 | title |
| ICLR 2026 | [Towards One-step Causal Video Generation via Adversarial Self-Distillation](https://iclr.cc/virtual/2026/poster/10009718) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [BLADE: Block-Sparse Attention Meets Step Distillation for Efficient Video Generation](https://iclr.cc/virtual/2026/poster/10009809) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Where Did This Sentence Come From? Tracing Provenance in LLM Reasoning Distillation](https://iclr.cc/virtual/2026/poster/10010657) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Knowledge Distillation for Large Language Models through Residual Learning](https://iclr.cc/virtual/2026/poster/10010753) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Asynchronous Matching with Dynamic Sampling for Multimodal Dataset Distillation](https://iclr.cc/virtual/2026/poster/10011298) | E6 | title (auto keyword, checked by hand) |
| ICLR 2026 | [BioX-Bridge: Model Bridging for Unsupervised Cross-Modal Knowledge Transfer across Biosignals](https://iclr.cc/virtual/2026/poster/10011868) | E2 | title |
| ICLR 2026 | [Understanding Dataset Distillation via Spectral Filtering](https://iclr.cc/virtual/2026/poster/10011909) | E6 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Dual Distillation for Few-Shot Anomaly Detection](https://iclr.cc/virtual/2026/poster/10006980) | E2 | title (auto keyword, checked by hand) |
| ICLR 2026 | [Rectified Decoupled Dataset Distillation: A Closer Look for Fair and Comprehensive Evaluation](https://iclr.cc/virtual/2026/poster/10009039) | E6 | title (auto keyword, checked by hand) |
| ICML 2022 | [Learning Domain Adaptive Object Detection with Probabilistic Teacher](https://proceedings.mlr.press/v162/chen22b.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2023 | [Atari-5: Distilling the Arcade Learning Environment down to Five Games](https://proceedings.mlr.press/v202/aitchison23a.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2023 | [Prototype-Sample Relation Distillation: Towards Replay-Free Continual Learning](https://proceedings.mlr.press/v202/asadi23a.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2023 | [Learning Lightweight Object Detectors via Multi-Teacher Progressive Distillation](https://proceedings.mlr.press/v202/cao23c.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2023 | [Scaling Up Dataset Distillation to ImageNet-1K with Constant Memory](https://proceedings.mlr.press/v202/cui23e.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2023 | [NerfDiff: Single-image View Synthesis with NeRF-guided Distillation from 3D-aware Diffusion](https://proceedings.mlr.press/v202/gu23a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2023 | [Linkless Link Prediction via Relational Distillation](https://proceedings.mlr.press/v202/guo23f.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2023 | [Generalized Teacher Forcing for Learning Chaotic Dynamics](https://proceedings.mlr.press/v202/hess23a.html) | E2 | title |
| ICML 2023 | [Less is More: Task-aware Layer-wise Distillation for Language Model Compression](https://proceedings.mlr.press/v202/liang23j.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2023 | [Understanding the Distillation Process from Deep Generative Models to Tractable Probabilistic Circuits](https://proceedings.mlr.press/v202/liu23x.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2023 | [Dataset Distillation with Convexified Implicit Gradients](https://proceedings.mlr.press/v202/loo23a.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2023 | [Anti-Exploration by Random Network Distillation](https://proceedings.mlr.press/v202/nikulin23a.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2023 | [Towards Understanding Ensemble Distillation in Federated Learning](https://proceedings.mlr.press/v202/park23e.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2023 | [Auxiliary Modality Learning with Generalized Curriculum Distillation](https://proceedings.mlr.press/v202/shen23f.html) | E2 | title |
| ICML 2023 | [TGRL: An Algorithm for Teacher Guided Reinforcement Learning](https://proceedings.mlr.press/v202/shenfeld23a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2023 | [MetricGAN-OKD: Multi-Metric Optimization of MetricGAN via Online Knowledge Distillation for Speech Enhancement](https://proceedings.mlr.press/v202/shin23b.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2023 | [Distilling Internet-Scale Vision-Language Models into Embodied Agents](https://proceedings.mlr.press/v202/sumers23a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2023 | [Quantifying the Knowledge in GNNs for Reliable Distillation into MLPs](https://proceedings.mlr.press/v202/wu23m.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2023 | [EM-Network: Oracle Guided Self-distillation for Sequence Learning](https://proceedings.mlr.press/v202/yoon23a.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2024 | [How Uniform Random Weights Induce Non-uniform Bias: Typical Interpolating Neural Networks Generalize with Narrow Teachers](https://proceedings.mlr.press/v235/buzaglo24a.html) | SUPPORT | title (manual override) |
| ICML 2024 | [MAGDi: Structured Distillation of Multi-Agent Interaction Graphs Improves Reasoning in Smaller Language Models](https://proceedings.mlr.press/v235/chen24ah.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2024 | [Embodied CoT Distillation From LLM To Off-the-shelf Agents](https://proceedings.mlr.press/v235/choi24d.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2024 | [DSD-DA: Distillation-based Source Debiasing for Domain Adaptive Object Detection](https://proceedings.mlr.press/v235/feng24d.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2024 | [Keypoint-based Progressive Chain-of-Thought Distillation for LLMs](https://proceedings.mlr.press/v235/feng24e.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2024 | [Data-free Distillation of Diffusion Models with Bootstrapping](https://proceedings.mlr.press/v235/gu24d.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2024 | [DistiLLM: Towards Streamlined Distillation for Large Language Models](https://proceedings.mlr.press/v235/ko24c.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2024 | [SelMatch: Effectively Scaling Up Dataset Distillation via Selection-Based Initialization and Partial Updates by Trajectory Matching](https://proceedings.mlr.press/v235/lee24g.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2024 | [DetKDS: Knowledge Distillation Search for Object Detectors](https://proceedings.mlr.press/v235/li24c.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2024 | [Graph Distillation with Eigenbasis Matching](https://proceedings.mlr.press/v235/liu24d.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2024 | [DFD: Distilling the Feature Disparity Differently for Detectors](https://proceedings.mlr.press/v235/liu24cd.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2024 | [Large Scale Dataset Distillation with Domain Shift](https://proceedings.mlr.press/v235/loo24a.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2024 | [Rethinking Momentum Knowledge Distillation in Online Continual Learning](https://proceedings.mlr.press/v235/michel24a.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2024 | [Federated Continual Learning via Prompt-based Dual Knowledge Transfer](https://proceedings.mlr.press/v235/piao24a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2024 | [Retrieval-Augmented Score Distillation for Text-to-3D Generation](https://proceedings.mlr.press/v235/seo24a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2024 | [InterpreTabNet: Distilling Predictive Signals from Tabular Data by Salient Feature Interpretation](https://proceedings.mlr.press/v235/si24a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2024 | [MH-pFLID: Model Heterogeneous personalized Federated Learning via Injection and Distillation for Medical Data Analysis](https://proceedings.mlr.press/v235/xie24h.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2024 | [Distilling Morphology-Conditioned Hypernetworks for Efficient Universal Morphology Control](https://proceedings.mlr.press/v235/xiong24c.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2024 | [Low-Rank Similarity Mining for Multimodal Dataset Distillation](https://proceedings.mlr.press/v235/xu24q.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2024 | [Exploration and Anti-Exploration with Distributional Random Network Distillation](https://proceedings.mlr.press/v235/yang24w.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2024 | [What is Dataset Distillation Learning?](https://proceedings.mlr.press/v235/yang24am.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2024 | [SF-DQN: Provable Knowledge Transfer using Successor Feature for Deep Reinforcement Learning](https://proceedings.mlr.press/v235/zhang24q.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2024 | [Score identity Distillation: Exponentially Fast Distillation of Pretrained Diffusion Models for One-Step Generation](https://proceedings.mlr.press/v235/zhou24x.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2024 | [Emergence of In-Context Reinforcement Learning from Noise Distillation](https://proceedings.mlr.press/v235/zisman24a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [A Cross Modal Knowledge Distillation & Data Augmentation Recipe for Improving Transcriptomics Representations through Morphological Features](https://proceedings.mlr.press/v267/bendidi25a.html) | E2 | title |
| ICML 2025 | [Puzzle: Distillation-Based NAS for Inference-Optimized LLMs](https://proceedings.mlr.press/v267/bercovich25a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [Point Cloud Dataset Distillation](https://proceedings.mlr.press/v267/bo25a.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2025 | [Distillation Scaling Laws](https://proceedings.mlr.press/v267/busbridge25a.html) | E2 | title (analysis-only) (manual override) |
| ICML 2025 | [From Thousands to Billions: 3D Visual Language Grounding via Render-Supervised Distillation from 2D VLMs](https://proceedings.mlr.press/v267/cao25a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://proceedings.mlr.press/v267/cheng25b.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [OmiAD: One-Step Adaptive Masked Diffusion Model for Multi-class Anomaly Detection via Adversarial Distillation](https://proceedings.mlr.press/v267/feng25b.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [Q-VDiT: Towards Accurate Quantization and Distillation of Video-Generation Diffusion Transformers](https://proceedings.mlr.press/v267/feng25q.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [FEAT-KD: Learning Concise Representations for Single and Multi-Target Regression via TabNet Knowledge Distillation](https://proceedings.mlr.press/v267/fong25a.html) | E2 | title |
| ICML 2025 | [SHARP-Distill: A 68$\times$ Faster Recommender System with Hypergraph Neural Networks and Language Models](https://proceedings.mlr.press/v267/forouzandeh25a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [Inverse Bridge Matching Distillation](https://proceedings.mlr.press/v267/gushchin25b.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2025 | [Distillation of Discrete Diffusion through Dimensional Correlations](https://proceedings.mlr.press/v267/hayakawa25a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [DA-KD: Difficulty-Aware Knowledge Distillation for Efficient Large Language Models](https://proceedings.mlr.press/v267/he25c.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [Provably Near-Optimal Federated Ensemble Distillation with Negligible Overhead](https://proceedings.mlr.press/v267/jang25b.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [Metastable Dynamics of Chain-of-Thought Reasoning: Provable Benefits of Search, RL and Distillation](https://proceedings.mlr.press/v267/kim25aj.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs](https://proceedings.mlr.press/v267/ko25a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [One Diffusion Step to Real-World Super-Resolution via Flow Trajectory Distillation](https://proceedings.mlr.press/v267/li25a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [DMOSpeech: Direct Metric Optimization via Distilled Diffusion Model in Zero-Shot Speech Synthesis](https://proceedings.mlr.press/v267/li25ay.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [Rethinking Score Distilling Sampling for 3D Editing and Generation](https://proceedings.mlr.press/v267/miao25a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [Noise Conditional Variational Score Distillation](https://proceedings.mlr.press/v267/peng25g.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [Rethinking the Temperature for Federated Heterogeneous Distillation](https://proceedings.mlr.press/v267/qi25a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [Efficient Graph Continual Learning via Lightweight Graph Neural Tangent Kernels-based Dataset Distillation](https://proceedings.mlr.press/v267/qiu25f.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2025 | [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://proceedings.mlr.press/v267/ro25a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [MGD$^3$ : Mode-Guided Dataset Distillation using Diffusion Models](https://proceedings.mlr.press/v267/santiago25a.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2025 | [Overcoming Vocabulary Mismatch: Vocabulary-agnostic Teacher Guided Language Modeling](https://proceedings.mlr.press/v267/shin25a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [On Teacher Hacking in Language Model Distillation](https://proceedings.mlr.press/v267/tiapkin25a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [One-Step Diffusion Policy: Fast Visuomotor Policies via Diffusion Distillation](https://proceedings.mlr.press/v267/wang25ba.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [Multi-Domain Graph Foundation Models: Robust Knowledge Transfer via Topology Alignment](https://proceedings.mlr.press/v267/wang25dj.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [Bridging Layout and RTL: Knowledge Distillation based Timing Prediction](https://proceedings.mlr.press/v267/wang25dn.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2025 | [Pre-Training Graph Contrastive Masked Autoencoders are Strong Distillers for EEG](https://proceedings.mlr.press/v267/wei25q.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [Scalable Model Merging with Progressive Layer-wise Distillation](https://proceedings.mlr.press/v267/xu25r.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2025 | [Strengthen Out-of-Distribution Detection Capability with Progressive Self-Knowledge Distillation](https://proceedings.mlr.press/v267/yang25ap.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [Taming Diffusion for Dataset Distillation with High Representativeness](https://proceedings.mlr.press/v267/zhao25x.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2025 | [TINED: GNNs-to-MLPs by Teacher Injection and Dirichlet Energy Distillation](https://proceedings.mlr.press/v267/zhou25a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2025 | [ROME is Forged in Adversity: Robust Distilled Datasets via Information Bottleneck](https://proceedings.mlr.press/v267/zhou25d.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2026 | [Hyper-ICL: Attention Calibration with Hyperbolic Anchor Distillation for Multimodal In-Context Learning](https://proceedings.mlr.press/v306/alipour-talemi26a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Optimizing Few-Step Generation with Adaptive Matching Distillation](https://proceedings.mlr.press/v306/bai26n.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Retrieval-Aware Distillation for Transformer-SSM Hybrids](https://proceedings.mlr.press/v306/bick26a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Efficient Multi-modal Dataset Distillation via Analytic Parameter Matching](https://proceedings.mlr.press/v306/bo26b.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2026 | [NanoFLUX: Distillation-Driven Compression of Large Text-to-Image Generation Models for Mobile Devices](https://proceedings.mlr.press/v306/chavhan26a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Gated Relational Alignment via Confidence-based Distillation for Efficient VLMs](https://proceedings.mlr.press/v306/chen26am.html) | E2 | title |
| ICML 2026 | [Beyond the Proxy: Trajectory-Distilled Guidance for Offline GFlowNet Training](https://proceedings.mlr.press/v306/chen26ej.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Beyond Next-Token Alignment: Distilling Multimodal Large Language Models via Token Interactions](https://proceedings.mlr.press/v306/chen26gr.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Learn from A Rationalist: Distilling Intermediate Interpretable Rationales](https://proceedings.mlr.press/v306/dai26e.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2026 | [Optimal Unconstrained Self-Distillation in Ridge Regression: Strict Improvements, Precise Asymptotics, and One-Shot Tuning](https://proceedings.mlr.press/v306/dang26b.html) | E2 | title |
| ICML 2026 | [Don’t Ignore the Tail: Decoupled Distillation Produces Top Maths Students on an Academic Budget](https://proceedings.mlr.press/v306/dasgupta26a.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2026 | [Discrete Survival Knowledge Distillation for Competing Risks Analysis](https://proceedings.mlr.press/v306/deng26o.html) | E2 | title |
| ICML 2026 | [Component-Wise Composite Likelihood Distillation for Censored Time-to-Event Data](https://proceedings.mlr.press/v306/deng26p.html) | E2 | title |
| ICML 2026 | [VideoGPA: Distilling Geometry Priors for 3D-Consistent Video Generation](https://proceedings.mlr.press/v306/du26q.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Uncovering the Gradient Geometry of Long CoT: A Spectral-guided Approach to Reasoning Distillation](https://proceedings.mlr.press/v306/fan26e.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Set-Coupled Guidance: Set-Level Coordination in Diffusion-Based Dataset Distillation](https://proceedings.mlr.press/v306/gan26d.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2026 | [GKD-Recruiter: Jointly Modeling Social and Task Heterogeneity for Spatial Crowdsourcing via Graph Knowledge Distillation](https://proceedings.mlr.press/v306/gao26ai.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [$\textttMetaDistill$: Unlocking the Performance Ceiling for Pretrained Optimizers](https://proceedings.mlr.press/v306/han26x.html) | E2 | title |
| ICML 2026 | [Veda: Scalable Video Diffusion via Distilled Sparse Attention](https://proceedings.mlr.press/v306/han26y.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Effective Distillation to Hybrid xLSTM Architectures](https://proceedings.mlr.press/v306/hauzenberger26a.html) | E2 | title |
| ICML 2026 | [Newton-coupled Dual-Teacher Semi-supervised Learning Framework](https://proceedings.mlr.press/v306/he26ad.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2026 | [Reasoning-preserved Efficient Distillation of Large Language Models via Activation-aware Initialization](https://proceedings.mlr.press/v306/he26aj.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Beyond Point Predictions: Manifold Expansion and Dual Alignment for Robust Time Series Distillation](https://proceedings.mlr.press/v306/hong26e.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [PADA-Coder: Improving Plan-Following Code Generation via Perturbation-Verified Attention Distillation and Dynamic Alignment](https://proceedings.mlr.press/v306/huang26ar.html) | E2 | title |
| ICML 2026 | [Restoring Initial Noise Sensitivity in Text-to-Image Distillation via Geometric Alignment](https://proceedings.mlr.press/v306/huang26bj.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [How to Fine-Tune a Reasoning Model? A Teacher–Student Cooperation Framework to Synthesize Student-Consistent SFT Data](https://proceedings.mlr.press/v306/huang26bq.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Reinforcement Learning via Self-Distillation](https://proceedings.mlr.press/v306/hubotter26a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Compute as Teacher: Turning Inference Compute Into Reference-Free Supervision](https://proceedings.mlr.press/v306/jayalath26a.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2026 | [Entropy-Aware On-Policy Distillation of Language Models](https://proceedings.mlr.press/v306/jin26e.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Federated Distillation for Whole Slide Image via Gaussian-Mixture Feature Alignment and Curriculum Integration](https://proceedings.mlr.press/v306/jing26b.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Critique-Guided Distillation for Robust Reasoning via Refinement](https://proceedings.mlr.press/v306/kapusuzoglu26a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Dataset Distillation Efficiently Encodes Low-Dimensional Representations from Gradient-Based Learning of Non-Linear Tasks](https://proceedings.mlr.press/v306/kinoshita26a.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2026 | [Positive–Unlabeled Reinforcement Learning Distillation for On-Premise Small Models](https://proceedings.mlr.press/v306/kou26a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Towards Resource-Efficient LLMs: End-to-End Energy Accounting of Distillation Pipelines](https://proceedings.mlr.press/v306/lambert26a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [HieRD: Hierarchical Relational Distillation for Vision-Language Embedding Models](https://proceedings.mlr.press/v306/le26b.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Improving Topic Modeling by Distilling Soft Labels from Language Models](https://proceedings.mlr.press/v306/li26a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [IDLM: Inverse-distilled Diffusion Language Models](https://proceedings.mlr.press/v306/li26az.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Shuffle the Context: RoPE-Perturbed Self-Distillation for Long-Context Adaptation](https://proceedings.mlr.press/v306/li26cs.html) | E2 | title |
| ICML 2026 | [High-Fidelity ANN-to-SNN Conversion via Closed-Loop CKA Distillation](https://proceedings.mlr.press/v306/li26db.html) | E2 | title |
| ICML 2026 | [GeoDM: Geometry-aware Distribution Matching for Dataset Distillation](https://proceedings.mlr.press/v306/li26ea.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2026 | [Mind Your Margin and Boundary: Are Your Distilled Datasets Truly Robust?](https://proceedings.mlr.press/v306/li26ec.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2026 | [Object-level Semantic and Spatial Distillation for Open Vocabulary Detection](https://proceedings.mlr.press/v306/li26hp.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Video-OPD: Efficient Post-Training of Multimodal Large Language Models for Temporal Video Grounding via On-Policy Distillation](https://proceedings.mlr.press/v306/li26im.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [AAD-1: Asymmetric Adversarial Distillation for One-Step Autoregressive Video Generation](https://proceedings.mlr.press/v306/li26iw.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [FedCDWA: Decoupled Federated Prototype Distillation with Hierarchical Wasserstein Aggregation](https://proceedings.mlr.press/v306/liu26af.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [TopoDistill: Distilling Global System Topology for Causal Discovery in Multivariate Time Series](https://proceedings.mlr.press/v306/liu26bp.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Entropy-aware Span-Constrained Optimal Transport for Robust Cross-Tokenizer Knowledge Distillation](https://proceedings.mlr.press/v306/liu26bw.html) | E2 | title |
| ICML 2026 | [XPERT: Expert Knowledge Transfer for Effective Training of Language Models](https://proceedings.mlr.press/v306/liu26dr.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [HVAE: Hyperbolic Variational Autoencoder For Flexible Knowledge Transfer Across Multiple Domains](https://proceedings.mlr.press/v306/liu26eg.html) | E2 | title |
| ICML 2026 | [Distillation Models are Good Samplers for Diffusion Reinforcement Learning](https://proceedings.mlr.press/v306/liu26ev.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Utility Boundary of Dataset Distillation: Scaling and Coverage Laws](https://proceedings.mlr.press/v306/luo26aa.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2026 | [Student-Centered Distillation Narrows the Agentic Gap Between Small and Large LLMs](https://proceedings.mlr.press/v306/lyu26j.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Semantic Cache Distillation: Efficient State Transfer via Reuse and Selective Patching](https://proceedings.mlr.press/v306/ma26ag.html) | E2 | title |
| ICML 2026 | [Making Expert Reasoning Learnable with Self-Distillation](https://proceedings.mlr.press/v306/mendes26b.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Distilling Neuro-Symbolic Programs into 3D Multi-modal LLMs](https://proceedings.mlr.press/v306/mo26c.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Fair Dataset Distillation via Cross-Group Barycenter Alignment](https://proceedings.mlr.press/v306/moslemi26a.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2026 | [Federated Manifold Learning (FML): Tackling Domain Heterogeneity with Structural Knowledge Transfer](https://proceedings.mlr.press/v306/mu26c.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [DocVAL: Validated Chain-of-Thought Distillation for Grounded Document VQA](https://proceedings.mlr.press/v306/neogi26a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Updating Parametric Knowledge with Context Distillation Retains Post-Training Capabilities](https://proceedings.mlr.press/v306/padmanabhan26a.html) | E2 | title |
| ICML 2026 | [Privileged Information Distillation for Language Models](https://proceedings.mlr.press/v306/penaloza26a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [PADD: Path-Aligned Decompression Distillation for Non-Router Teacher to Guide MoE Student Learning](https://proceedings.mlr.press/v306/peng26l.html) | E2 | title |
| ICML 2026 | [d3LLM: Ultra-Fast Diffusion LLM using Pseudo-Trajectory Distillation](https://proceedings.mlr.press/v306/qian26g.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [One-step Optimal Transport via Regularized Distribution Matching Distillation](https://proceedings.mlr.press/v306/rakitin26a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [FedSDR: Federated Self-Distillation with Rectification](https://proceedings.mlr.press/v306/ren26n.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Attention Hijacking: Backdooring Text Dataset Distillation via Semantic Anchors](https://proceedings.mlr.press/v306/ren26q.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2026 | [Memory-Distilled Selection for Noise-Robust Anomaly Detection](https://proceedings.mlr.press/v306/safarov26a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [One-Step Residual Shifting Diffusion for Image Super-Resolution via Distillation](https://proceedings.mlr.press/v306/selikhanovych26a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [TMS: Trajectory-Mixed Supervision for On-Policy Self Distillation](https://proceedings.mlr.press/v306/shahroz26a.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Breaking the Scale Barrier: One-Shot Knowledge Transfer via Frequency Transform](https://proceedings.mlr.press/v306/shen26f.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2026 | [SPEED: Sharpened-Teacher Distillation for Parallel Decoding of Diffusion Language Models](https://proceedings.mlr.press/v306/shen26z.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Self-Distillation Enables Continual Learning](https://proceedings.mlr.press/v306/shenfeld26a.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2026 | [Distilling Linearized Behavior into Non-linear Fine-Tuning for Effective Task Arithmetic](https://proceedings.mlr.press/v306/sommariva26a.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2026 | [Unified Time Series Explanations via Amortized Optimization and Instance-level Multi-Expert Knowledge Distillation](https://proceedings.mlr.press/v306/tran26h.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Adversarial Dual On-Policy Distillation from Expressive Teacher](https://proceedings.mlr.press/v306/wan26n.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [StyleDistillation: A New Insight of Image Style Enables Personalized Aesthetic Manipulation](https://proceedings.mlr.press/v306/wang26bi.html) | E2 | title (analysis-only) (manual override) |
| ICML 2026 | [ProtoVAR: Efficient Dataset Distillation via Prototype-Guided Visual Autoregressive Modeling](https://proceedings.mlr.press/v306/wang26co.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2026 | [The Bridge-Garden Dilemma in LLM Distillation: Why Mixing Hard and Soft Labels Works](https://proceedings.mlr.press/v306/wang26cw.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [CodeChemist: Test-Time Scaling for Low-Resource Code Generation via Functional Knowledge Transfer](https://proceedings.mlr.press/v306/wang26dw.html) | E2 | title |
| ICML 2026 | [A Unified Approach to Interpreting Knowledge Distillation for Large Language Models via Interactions](https://proceedings.mlr.press/v306/wang26gj.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [REST: Diffusion-based Real-time End-to-end Streaming Talking Head Generation via ID-Context Caching and Asynchronous Streaming Distillation](https://proceedings.mlr.press/v306/wang26iv.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Zooming without Zooming: Region-to-Image Distillation for Fine-Grained Multimodal Perception](https://proceedings.mlr.press/v306/wei26j.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [SGMD: Score Gradient Matching Distillation for Few-Step Video Diffusion Distillation](https://proceedings.mlr.press/v306/wu26q.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Diversity-Preserved Distribution Matching Distillation for Fast Visual Synthesis](https://proceedings.mlr.press/v306/wu26ag.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2026 | [Native Parallel Reasoner: Reasoning in Parallelism via Self-Distilled Reinforcement Learning](https://proceedings.mlr.press/v306/wu26ai.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [From Interactions to Principles: Experience-Driven Self-Distillation for Evolving LLM Agents](https://proceedings.mlr.press/v306/wu26bf.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [DIVER: Diving Deeper into Distilled Data via Expressive Semantic Recovery](https://proceedings.mlr.press/v306/xia26g.html) | E6 | title (auto keyword, checked by hand) |
| ICML 2026 | [Unifying Dataset Pruning and Distillation for Efficient Large-scale Compression](https://proceedings.mlr.press/v306/xiao26k.html) | E6 | title |
| ICML 2026 | [Generalist Graph Anomaly Detection via Prototype-Based Distillation](https://proceedings.mlr.press/v306/xu26g.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Antidistillation Fingerprinting](https://proceedings.mlr.press/v306/xu26y.html) | E2 | title |
| ICML 2026 | [DGS-Net: Distillation-Guided Gradient Surgery for CLIP Fine-Tuning in AI-Generated Image Detection](https://proceedings.mlr.press/v306/yan26h.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Infinite Mask Diffusion for Few-Step Distillation](https://proceedings.mlr.press/v306/yoo26b.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Decomposed On-Policy Distillation for Vision-Language Reasoning: Steering Gradients for Visual Grounding](https://proceedings.mlr.press/v306/yoon26f.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [CORRECT: COndensed eRror RECognition via knowledge Transfer in multi-agent systems](https://proceedings.mlr.press/v306/yu26x.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Symbiosis-Inspired Knowledge Distillation for Incremental Object Detection](https://proceedings.mlr.press/v306/zeng26c.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Large Language Models Explore by Latent Distilling](https://proceedings.mlr.press/v306/zeng26m.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Distilling Task-Level Coordination Policies for Generalizable Multi-Agent Cooperation](https://proceedings.mlr.press/v306/zhai26c.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Reinforcement-aware Knowledge Distillation for LLM Reasoning](https://proceedings.mlr.press/v306/zhang26bw.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Learning Adaptive Topology with FiLM-Guided Distillation for Tertiary Structure-Based RNA Design](https://proceedings.mlr.press/v306/zhang26bx.html) | E2 | title |
| ICML 2026 | [From Teacher Pathways to Invariant Manifolds: Consensus Subspace Distillation for TSFMs](https://proceedings.mlr.press/v306/zhang26cf.html) | E1 | title: KD not the contribution / not classification KD |
| ICML 2026 | [Physics-Informed Distillation of Diffusion Models for PDE-Constrained Generation](https://proceedings.mlr.press/v306/zhang26gl.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Experience is the Best Teacher: Motivating Effective Exploration in Reinforcement Learning for LLMs](https://proceedings.mlr.press/v306/zhang26io.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Rh-3DGS: Robust Open-Vocabulary Scene Understanding via Riemannian Huber Distillation and Manifold-Aware Sampling](https://proceedings.mlr.press/v306/zhao26s.html) | E2 | title |
| ICML 2026 | [Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models](https://proceedings.mlr.press/v306/zhao26be.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Mean Flow Distillation: Robust and Stable Distillation for Flow Matching Models](https://proceedings.mlr.press/v306/zhao26bx.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Making Learner Weakness Actionable for Learning from Demonstration with Novice Teachers](https://proceedings.mlr.press/v306/zhu26s.html) | E2 | title |
| ICML 2026 | [Hybrid Policy Distillation for LLMs](https://proceedings.mlr.press/v306/zhu26av.html) | E2 | title (auto keyword, checked by hand) |
| ICML 2026 | [Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation](https://proceedings.mlr.press/v306/zhu26bf.html) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Stabilizing Consistency Training: A Flow Map Analysis and Self-Distillation](https://openreview.net/pdf?id=Qx2FrHDVzp) | E2 | title |
| TMLR | [SPID: Distilled Protein Backbone Generation](https://openreview.net/pdf?id=l1fS626LVB) | E2 | title (auto keyword, checked by hand) |
| TMLR | [From Deferral to Learning: Online In-Context Knowledge Distillation for LLM Cascades](https://openreview.net/pdf?id=KUcCF5qqFL) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Do MLPs Inherit GNN Knowledge Uniformly? Class-Conditional Transfer Equity in Graph-Free Distillation](https://openreview.net/pdf?id=GDOC2rR4wv) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Collaborative Synthetic Data Generation for Knowledge Transfer in One-Shot Federated Learning](https://openreview.net/pdf?id=9H3b5MX87m) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Stable Continuous-Time Consistency Distillation: An Empirical Study with a Multistep Extension](https://openreview.net/pdf?id=di6ofoWEU8) | E2 | title |
| TMLR | [When Perplexity Lies: Generation-Focused Distillation of Hybrid Sequence Models](https://openreview.net/pdf?id=u4sfTcn6Tx) | E2 | title |
| TMLR | [Towards Bridging the Gap Between Offline and Iterative Alignment via Preference Distillation](https://openreview.net/pdf?id=X6r1bU1m6x) | E2 | title (auto keyword, checked by hand) |
| TMLR | [EdgeCrafter: Compact ViTs for Edge Dense Prediction via Task-Specialized Distillation](https://openreview.net/pdf?id=yoSD5BRFkV) | E1 | title: KD not the contribution / not classification KD |
| TMLR | [Analysis of an Idealized Stochastic Polyak Method and its Application to Black-Box Model Distillation](https://openreview.net/pdf?id=lNRBJekTFX) | SUPPORT | title (analysis-only) |
| TMLR | [EFFEKT: Efficient Federated Knowledge Transfer to Foundation Models](https://openreview.net/pdf?id=jpUDUJfE1K) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Automaton Distillation: Neuro-Symbolic Transfer Learning for Deep Reinforcement Learning](https://openreview.net/pdf?id=Tyxmx2vNDb) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Multimodal Masked Point Distillation for 3D Representation Learning](https://openreview.net/pdf?id=Gxb3z4VlM7) | E2 | title (auto keyword, checked by hand) |
| TMLR | [TextTeacher: What Can Language Teach About Images?](https://openreview.net/pdf?id=Xwb0aEUwKh) | E2 | title |
| TMLR | [Topology- and Gradient-Guided Knowledge Distillation for Point Cloud Semantic Segmentation](https://openreview.net/pdf?id=lP2phGa5af) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Active Teacher Selection for Reward Learning](https://openreview.net/pdf?id=9OEy68av40) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Towards Customized Knowledge Distillation for Efficient Dense Image Predictions](https://openreview.net/pdf?id=4verIe3tE4) | E2 | title: KD not the contribution / not classification KD (manual override) |
| TMLR | [Distilled Thompson Sampling: Practical and Efficient Thompson Sampling via Imitation Learning](https://openreview.net/pdf?id=J8PrWwvYX2) | E2 | title (auto keyword, checked by hand) |
| TMLR | [GraphMERT: Efficient and Scalable Distillation of Reliable Knowledge Graphs from Unstructured Data](https://openreview.net/pdf?id=tnXSdDhvqc) | E2 | title (auto keyword, checked by hand) |
| TMLR | [SpikingMamba: Towards Energy-Efficient Large Language Models via Knowledge Distillation from Mamba](https://openreview.net/pdf?id=uxb2jcCLxt) | E2 | title (auto keyword, checked by hand) |
| TMLR | [PRISM: Diversifying Dataset Distillation by Decoupling Architectural Priors](https://openreview.net/pdf?id=xN58FtB1Gq) | E6 | title (auto keyword, checked by hand) |
| TMLR | [InfGraND: An Influence-Guided GNN-to-MLP Knowledge Distillation](https://openreview.net/pdf?id=lfzHR3YwlD) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Dive3D: Diverse Distillation-based Text-to-3D Generation via Score Implicit Matching](https://openreview.net/pdf?id=OUYMueHLMf) | E2 | title (auto keyword, checked by hand) |
| TMLR | [SPONGE: Competing Sparse Language Representations for Effective Knowledge Transfer](https://openreview.net/pdf?id=OevFdPgk3h) | E2 | title |
| TMLR | [Learning few-step posterior samplers by unfolding and distillation of diffusion models](https://openreview.net/pdf?id=oGCfD8YKN2) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Privacy-Aware Time Series Synthesis via Public Knowledge Distillation](https://openreview.net/pdf?id=TC6ihoRw0c) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Efficient Distillation of Classifier-Free Guidance using Adapters](https://openreview.net/pdf?id=uMz8FiiW01) | E1 | title: KD not the contribution / not classification KD |
| TMLR | [From Novelty to Imitation: Self-Distilled Rewards for Offline Reinforcement Learning](https://openreview.net/pdf?id=F5K94JI2Jb) | E2 | title (auto keyword, checked by hand) |
| TMLR | [A Comprehensive Survey on Knowledge Distillation](https://openreview.net/pdf?id=3cbJzdR78B) | E5 | title |
| TMLR | [One-Shot Federated Distillation Using Monoclass Teachers: A Study of Knowledge Fragmentation and Out-of-Distribution Supervision](https://openreview.net/pdf?id=ENdm5BM7aF) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Efficient Knowledge Injection in LLMs via Self-Distillation](https://openreview.net/pdf?id=drYpdSnRJk) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Scaling and Distilling Transformer Models for sEMG](https://openreview.net/pdf?id=hFPWThwUiZ) | E2 | title |
| TMLR | [Proximal Policy Distillation](https://openreview.net/pdf?id=WfVXe88oMh) | E2 | title (auto keyword, checked by hand) |
| TMLR | [On Learning Representations for Tabular Data Distillation](https://openreview.net/pdf?id=GXlsrvOGIK) | E2 | title (auto keyword, checked by hand) |
| TMLR | [FedDr+: Stabilizing Dot-regression with Global Feature Distillation for Federated Learning](https://openreview.net/pdf?id=a6WthNFhL2) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Distilling Datasets Into Less Than One Image](https://openreview.net/pdf?id=qsipSdfWeV) | E6 | title (auto keyword, checked by hand) |
| TMLR | [Align and Distill: Unifying and Improving Domain Adaptive Object Detection](https://openreview.net/pdf?id=ssXSrZ94sR) | E7 | duplicate title (listed in two venues) |
| TMLR | [Robust Preference Optimization through Reward Model Distillation](https://openreview.net/pdf?id=E2zKNuwNDc) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Global Safe Sequential Learning via Efficient Knowledge Transfer](https://openreview.net/pdf?id=PtD2gVmb3J) | E2 | title |
| TMLR | [Federated Learning on Virtual Heterogeneous Data with Local-Global Dataset Distillation](https://openreview.net/pdf?id=QplBL2pV4Z) | E6 | title (auto keyword, checked by hand) |
| TMLR | [MIND: Modality-Informed Knowledge Distillation Framework for Multimodal Clinical Prediction Tasks](https://openreview.net/pdf?id=BhOJreYmur) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Towards Cross-Tokenizer Distillation: the Universal Logit Distillation Loss for LLMs](https://openreview.net/pdf?id=bwRxXiGO9A) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Teacher-Guided Graph Contrastive Learning](https://openreview.net/pdf?id=15tjpSHI15) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Adaptive Self-Distillation for Minimizing Client Drift in Heterogeneous Federated Learning](https://openreview.net/pdf?id=K58n87DE4s) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Dataset Distillation via Curriculum Data Synthesis in Large Data Era](https://openreview.net/pdf?id=PlaZD2nGCl) | E6 | title (auto keyword, checked by hand) |
| TMLR | [Audio-Visual Dataset Distillation](https://openreview.net/pdf?id=IJlbuSrXmk) | E6 | title (auto keyword, checked by hand) |
| TMLR | [Deep Tabular Learning via Distillation and Language Guidance](https://openreview.net/pdf?id=p6KIteShzf) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Graph Knowledge Distillation to Mixture of Experts](https://openreview.net/pdf?id=vzZ3pbNRvh) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Reward Guided Latent Consistency Distillation](https://openreview.net/pdf?id=z116TO4LDT) | E7 | duplicate title (listed in two venues) |
| TMLR | [SA-MLP: Distilling Graph Knowledge from GNNs into Structure-Aware MLP](https://openreview.net/pdf?id=MZ2kKZc8m7) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Rethinking Teacher-Student Curriculum Learning through the Cooperative Mechanics of Experience](https://openreview.net/pdf?id=qWh82br6KT) | E1 | title: KD not the contribution / not classification KD |
| TMLR | [Vision-Language Dataset Distillation](https://openreview.net/pdf?id=6L6cD65pot) | E6 | title (auto keyword, checked by hand) |
| TMLR | [Homogenizing Non-IID Datasets via In-Distribution Knowledge Distillation for Decentralized Learning](https://openreview.net/pdf?id=CuyJkNjIVd) | E1 | title (manual override) |
| TMLR | [TAP: The Attention Patch for Cross-Modal Knowledge Transfer from Unlabeled Modality](https://openreview.net/pdf?id=73uyerai53) | E2 | title |
| TMLR | [Physics Informed Distillation for Diffusion Models](https://openreview.net/pdf?id=rOvaUsF996) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Differentially Private Kernel Inducing Points using features from ScatterNets (DP-KIP-ScatterNet) for Privacy Preserving Data Distillation](https://openreview.net/pdf?id=84M8xwNxrc) | E6 | title |
| TMLR | [Choosing Wisely and Learning Deeply: Selective Cross-Modality Distillation via CLIP for Domain Generalization](https://openreview.net/pdf?id=4KLwep6mA1) | E2 | title (auto keyword, checked by hand) |
| TMLR | [Two-Level Actor-Critic Using Multiple Teachers](https://openreview.net/pdf?id=LfQ6uAVAEo) | E2 | title |
| TMLR | [Data Distillation: A Survey](https://openreview.net/pdf?id=lmXMXP74TO) | E5 | title |
| TMLR | [PCPs: Patient Cardiac Prototypes to Probe AI-based Medical Diagnoses, Distill Datasets, and Retrieve Patients](https://openreview.net/pdf?id=X1pjWMCMB0) | E2 | title (auto keyword, checked by hand) |

</details>

Title-screen basis: "auto keyword" = title names a non-classification task (LLM, diffusion, detection, segmentation, RL, graphs, 3D, speech, federated) or dataset distillation; every such title was read by hand and mis-flags were moved to full text (e.g. DiffKD, DeepKD, Shadow KD). The remaining titles were coded by hand.
