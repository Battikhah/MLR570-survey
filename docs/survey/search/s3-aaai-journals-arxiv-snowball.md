# T12b-S3: systematic search of AAAI, TPAMI, IJCV and arXiv (2025+), with snowballing

Orca task `task_db81966516f2`, run on 2026-11-08 by the Claude worker. The criteria are the frozen I1–I3 and
E1–E7 in `tasks/plan.md` § "Scope decision". Every included paper has a `literature/sources.yaml` record. The
record's `verified_by` field names the source table for each number.

**Evidence labels.** Numbers and table references are **VERIFIED**: I read them from each paper's own PDF
(pdftotext) on 2026-11-08. Remarks on comparability are **INTERPRETATION**. Each number is the paper's own claim.
The papers use different reproductions and baselines, so these numbers are not a leaderboard as they stand
(see the caution in `docs/survey/sota-inventory.md`).

## 1. Search log

| # | Source | Query / URL | Date | Hits |
|---|---|---|---|---|
| Q1 | AAAI via Crossref REST API (`filter=prefix:10.1609,from-pub-date:2022-01-01,until-pub-date:2026-11-08`) | `query.title=` distillation / distill / distilling / distilled / "teacher student" / "knowledge transfer" | 2026-11-08 | 250 / 0 / 32 / 10 / 651 / 787 raw; **338** after title regex `distil\|knowledge transfer\|teacher` and union |
| Q2 | TPAMI via Crossref (`filter=issn:0162-8828,issn:1939-3539,issn:2160-9292`, same dates) | same six title queries | 2026-11-08 | 66 / 2 / 8 / 1 / 9 / 125 raw; **81** after regex and union |
| Q3 | IJCV via Crossref (`filter=issn:0920-5691,issn:1573-1405`, same dates) | same six title queries | 2026-11-08 | 24 / 1 / 1 / 0 / 8 / 40 raw; **35** after regex and union |
| Q4 | arXiv API `export.arxiv.org/api/query` | `(cat:cs.CV OR cat:cs.LG) AND abs:"knowledge distillation" AND (abs:"CIFAR-100" OR abs:CIFAR100 OR abs:ImageNet) AND submittedDate:[202501010000 TO 202611082359]` | 2026-11-08 | **98** |
| Q5 | arXiv API title search (`ti:` words) | to find an arXiv full text for each venue hit that passed screening | 2026-11-08 | 13 of 33 venue candidates matched |
| Q6 | Crossref `link` (text-mining URLs) | full text for AAAI (OJS download), IJCV (Springer) and TPAMI | 2026-11-08 | 18 AAAI/IJCV/TPAMI PDFs retrieved; 7 TPAMI not retrievable |
| Q7 | Snowballing: competitor rows in the CIFAR-100 tables of 10 registry papers (EKD, LDRLD, RLD, LumiNet, VRM, RSD, RPKD, LTKD, DeepKD, PLD) and 14 new inclusions (AR-KD, SAKD, REDistill, FiGKD, TopKD, HCD, ADG-KD, RCKD, IKD, NCKD, GenDD, BTKD++, KD-AIF, ASD) | competitor names resolved through each citing paper's reference list, then the arXiv API, the NeurIPS proceedings listings (2022, 2024) and the OpenReview API | 2026-11-08 | 26 competitors new to the registry checked (§6) |

**Access problems, recorded exactly as they happened:**
- `dblp.org`, `dblp.uni-trier.de` and `dblp.dagstuhl.de` all returned an HTML page "Making sure you're not a bot!"
  (Anubis challenge) to the search API. `ojs.aaai.org/index.php/AAAI/search` returned the same challenge. I did not
  try to get past either, so Crossref is the listing source for Q1–Q3.
- `link.springer.com` article pages returned a JS challenge. The Crossref text-mining PDF links did work for the three
  IJCV papers without an arXiv version.
- IEEE Xplore (TPAMI): the Crossref `xplorestaging` links returned HTML, not a PDF, for 7 papers. No arXiv
  version was found for them (§5, "not retrievable").
- OpenReview PDFs: `openreview.net/pdf` and `api2.openreview.net/attachment` both returned
  `ChallengeRequiredError` (403) for TeKAP and TopKD-topology. Only their metadata (from `notes/search`) is verified.
- `proceedings.neurips.cc/paper_files/paper/2025` returned 54 KB, not the full listing, so Angular-KD's NeurIPS 2025
  status rests on the authors' statement.

**Search limitation (INTERPRETATION).** Q1–Q3 match titles only. A venue paper whose title does not contain the
keywords is missed. For example, *Generalized Kullback–Leibler Divergence Loss* (TPAMI 2026) was found only through
arXiv (Q4) and then confirmed in Crossref with a separate title query. Crossref's AAAI 2022–2023 counts (26 and 39
title matches) are lower than I expected; an independent count from OpenAlex was not possible (it needs an API key
tied to an email address). S1/S2 or the coordinator may want to cross-check AAAI against the OJS issue tables of
contents when they are reachable.

## 2. PRISMA-style flow

| Stage | Count |
|---|---|
| Identified (Q1 338 + Q2 81 + Q3 35 + Q4 98) | **552** |
| Duplicates within this search (HCD: AAAI 2026 and arXiv 2511.10942) | −1 → 551 |
| Already in `literature/sources.yaml` (matched by DOI, arXiv id or normalised title): `li2023ctkd`, `miles2024projector`, `zhou2025tcs`, `yang2025mtkdrl`, `wang2022kdreview`, `yang2023lmcl`, `zhang2025vrm`, `kang2025dho`, `hayder2025mokd`, `huang2025deepkd`, `bassam2025pld`, `kim2026ltkd`, `zhang2025rsd`, `yuan2026tpkd`, `etcibasi2026rpkd` | −15 → **536 new records screened** |
| Screened out by title/abstract | **445**: E1 44 · E2 365 · E3 5 (AAAI symposium/other proceedings under prefix 10.1609) · E5 6 · E6 25 |
| Full text sought | **91** |
| Full text not retrievable (TPAMI paywall, no arXiv copy) → tagged AMBIGUOUS | 7 |
| Full text assessed | 84 |
| Excluded at full text | **52**: E4 41 · E2 5 · E1 1 · analysis-only (SUPPORT, not leaderboard) 5 |
| **Included from Q1–Q4** | **32** (25 clean, 7 AMBIGUOUS) |
| **Included via snowballing (Q7)** | **7** (5 clean, 2 AMBIGUOUS) |
| **Total new registry records** | **39** |

How screening codes were assigned (INTERPRETATION): titles were first flagged by a keyword rule
(detection / segmentation / LLM / speech / graph / video / 3D / … → E2; quantisation / pruning / federated / continual
/ NAS / watermark / unlearning / education → E1; dataset distillation / condensation → E6; survey → E5). I then read
every unflagged title and every flagged title containing generic KD wording by hand. Image-classification papers
that cannot be judged from the title alone were sent to full text, not coded. For example, two papers first coded E2
(food recognition, endoscopy) were moved to full text and excluded there as E4.

## 3. Inclusion table (all NEW registry ids)

Columns: **Tag** = CORE (listed venue, verified), CORE-P (2025+ arXiv preprint with no listed venue), or AMBIGUOUS.
**R8x4** = CIFAR-100 ResNet32x4→ResNet8x4 top-1 (best variant named). **IN** = ImageNet ResNet34→ResNet18 top-1.
`n/r` = not reported. Unless noted, teachers follow the CRD/mdistiller protocol (ResNet32x4 79.42, 240 epochs).
Family codes: L = logit/target/loss, F = feature/relation, S = training scheme, R = reliability,
C = combination/optimiser, H = hybrid.

| id | Method | Title | Venue | arXiv / DOI | Tag | Fam. | Pairs reported (CIFAR-100 / IN) | R8x4 (table) | IN R34→R18 (table) | Code (licence) | Mechanism | Found via |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `lu2024uniads` | UniADS | UniADS: Universal Architecture-Distiller Search for Distillation Gap | AAAI 2024 | 10.1609/aaai.v38i13.29327 | CORE | C | W40-2/16-2, R110/20, R110/32, R32x4/8x4, VGG13/8, VGG13/MV2, R32x4/SV2, W40-2/SV1 / R34-R18, R50-R18 | 76.65 (T3) | 72.25 (T4; teacher 73.40) | none found | joint student-architecture + distiller search | Q1 |
| `wang2025ikd` | IKD | Debiased Distillation for Consistency Regularization | AAAI 2025 | 10.1609/aaai.v39i8.32840 | CORE | L | 10 CRD pairs / R34-R18, R50-MV1 | 77.10, NKD+IKD (T2) | 72.20, NKD+IKD (T3) | yema-web/IKD (BSD-2-Clause) | debiased batch-level consistency regulariser, plug-in | Q1 |
| `li2025adgkd` | ADG-KD | Adaptive Dual Guidance Knowledge Distillation | AAAI 2025 | 10.1609/aaai.v39i17.34031 | CORE | L | 10 CRD pairs / R34-R18, R50-MV2 | 77.51, MLKD+ADG (T1; plain 77.44) | 72.22 (T2) | none found | fuses teacher + instance guidance via learned factors | Q1 |
| `zhang2025nckd` | NCKD | Neural Collapse Inspired Knowledge Distillation | AAAI 2025 | 2412.11788 / 10.1609/aaai.v39i21.34412 | CORE | F | R56/20, W40-2/40-1, R32x4/8x4, R50/MV2, R32x4/SV1, R32x4/SV2 / R34-R18, R50-MV1 | 78.18, SimKD+NCKD (T1; plain 77.23) | 72.44 (T2) | none found | aligns features to the teacher's simplex-ETF structure | Q1, Q4 |
| `liao2026dskd` | DSKD | Direction Sensitivity–Based Knowledge Distillation: Optimization-Aware Low-Rank Knowledge Transfer | AAAI 2026 | 10.1609/aaai.v40i28.39520 | CORE | F | R56/20, R110/32, R32x4/8x4, W40-2/16-2 / — | 75.9, ReviewKD+DSKD (T2; one decimal) | n/r | theChoseno/DSKD (none) | direction-sensitivity low-rank transfer (also GLUE) | Q1 |
| `wang2026rckd` | RCKD | Rethinking the Dark Knowledge and Kullback-Leibler Divergence Loss in Knowledge Distillation Under Capacity Mismatching | AAAI 2026 | 10.1609/aaai.v40i31.39878 | CORE | L | 12 CRD pairs / R34-R18, R50-MV1 | 76.89 (T1) | 72.02 (T3) | yingchao-wang/RCKD (none) | cosine-type loss for capacity mismatch | Q1 |
| `fang2022fastdfkd` | FastDFKD | Up to 100x Faster Data-Free Knowledge Distillation | AAAI 2022 | 10.1609/aaai.v36i6.20613 | CORE | S (data-free) | W40-2/16-2 (data-free) / — | n/r (W40-2→W16-2 65.12, T1) | n/r | zju-vipa/Fast-Datafree (none) | meta-learned shared features for fast synthesis | Q1 |
| `tang2025hidfd` | HiDFD | Hybrid Data-Free Knowledge Distillation | AAAI 2025 | 2412.13525 / 10.1609/aaai.v39i19.34293 | **AMBIGUOUS** | S (data-free) | R32x4→"ShuffleNet" / — | n/r (R32x4→ShuffleNet 75.03) | n/r | tangjialiang97/HiDFD (none) | collected + GAN-generated hybrid data | Q1 |
| `xu2026hcd` | HCD | Heterogeneous Complementary Distillation | AAAI 2026 | 2511.10942 / 10.1609/aaai.v40i13.38112 | CORE | F (heterog.) | ViT/Swin/Mixer→R18/MV2 only / R34-R18, R50-MV1 | n/r | 72.18 (T3) | yema-web/HCD (none) | complementary feature mapper for ViT→CNN | Q1, Q4 |
| `zhang2025btkd` | BTKD | Can Students Beyond the Teacher? Distilling Knowledge from Teacher's Bias | AAAI 2025 | 2412.09874 / 10.1609/aaai.v39i21.34400 | CORE | R | VGG13/8, R50/MV2 (+ non-standard) / R34-R18, R50-MV1 | n/r (VGG13→VGG8 78.03; R50→MV2 80.45, T1) | 73.38 (T2) | none found | separates correct and biased teacher knowledge | Q1 |
| `chen2026pefd` | PEFD | Understanding the Effects of Projectors in Knowledge Distillation | IEEE TPAMI 2026 | 2310.17183 / 10.1109/tpami.2026.3677028 | CORE | F | VGG13/8, R32x4/8x4, R50/VGG8, R50/MV2 / R34-R18, R50-MV1 | 76.08 (T8) | 71.94 (T9) | chenyd7/PEFD (MIT) | projector-ensemble feature distillation | Q2 |
| `cui2026gkl` | GKL-KD | Generalized Kullback–Leibler Divergence Loss | IEEE TPAMI 2026 | 2503.08038 / 10.1109/TPAMI.2026.3703828 | CORE | L | 11 CRD pairs / R34-R18, R50-MV1 | 76.83 (T17) | 71.91 (T5) | jiequancui/DKL (none) | weighted-MSE + soft-label CE decomposition of KL | Q4 → Crossref |
| `yang2024srd` | SRD | Knowledge Distillation Meets Open-Set Semi-supervised Learning | IJCV 2024 | 2205.06701 / 10.1007/s11263-024-02192-7 | CORE | F | non-standard CIFAR pairs / R34-R18, R50-MV1 | n/r | 71.73 (T8) | jingyang2017/SRD_ossl (MIT) | teacher-classifier representation matching, uses unlabeled data | Q3 |
| `qu2026rekd` | ReKD | Relaxed Knowledge Distillation | IJCV 2026 | 10.1007/s11263-025-02705-y | CORE | F | 10 CRD pairs / R34-R18, R50-MV1 | 76.94 (T1) | 71.72 (T3) | none found | VAE-based relaxed feature matching | Q3 |
| `zhang2026btkdpp` | BTKD++ | BTKD++: Beyond Teachers by Critically Distilling Knowledge from Teacher's Bias | IJCV 2026 | 10.1007/s11263-026-02924-x | CORE | R | as BTKD / R34-R18, R50-MV1 | n/r (same CIFAR values as BTKD, T2) | 73.38 (T3) | smartyige/BTKD (none) | journal extension of BTKD | Q3 |
| `liang2024rgal` | RGAL | Relation-Guided Adversarial Learning for Data-Free Knowledge Transfer | IJCV 2024 | 2412.11380 / 10.1007/s11263-024-02303-4 | CORE | S (data-free) | W40-2/16-2 (data-free) / — | n/r (W40-2→W16-2 69.71, T1) | n/r | none found | relation-guided adversarial synthesis | Q3 |
| `qi2025bdd` | BDD | Balance Divergence for Knowledge Distillation | arXiv | 2501.07804 | CORE-P | L | 11 CRD pairs / R34-R18, R50-MV2 | 77.22, MLD+BDD (T1; plain 76.21) | 71.97, MLD+BDD (T3) | none found | adds reverse KL for small teacher probabilities | Q4 |
| `kim2025figkd` | FiGKD | FiGKD: Fine-Grained Knowledge Distillation via High-Frequency Detail Transfer | arXiv (journal_ref ESWA 2026) | 2505.11897 | **AMBIGUOUS** | F | 10 CRD pairs / — | 78.05 (T1) | n/r | none found | distils high-frequency wavelet detail only | Q4 |
| `cui2025gendd` | GenDD | Generative Distribution Distillation | arXiv (technique report) | 2507.14503 | CORE-P | L | 11 CRD pairs / R34-R18, R50-MV1 | 77.47 (T5) | 72.38 (T2) | jiequancui/Generative-Distribution-Distillation (MIT) | KD as conditional generative distribution matching | Q4 |
| `wang2025topkd` | TopKD | TopKD: Top-scaled Knowledge Distillation | arXiv | 2508.04539 | CORE-P | L | 14 CRD pairs / R34-R18, R50-MV1 | 78.18 (T2) | 71.52 (T3) | none found | scales/decouples top-K teacher logits | Q4 |
| `tybl2026redistill` | REDistill | REDistill: Robust Estimator Distillation for Balancing Robustness and Efficiency | arXiv | 2602.04677 | CORE-P | R | R32x4/SV2, R50/MV2, VGG13/MV2 (+ others) / R34-R18, R50-MV1 | n/r | 72.00 (T III) | none found | power-divergence loss down-weights unreliable samples | Q4 |
| `yu2026sakd` | SAKD | Single-Teacher View Augmentation: Enhancing Knowledge Distillation with Student-Guided Perturbations | arXiv | 2607.11557 | CORE-P | S | R32x4/8x4, VGG13/8 (+ others) / R34-R18 | 77.31, MLKD+SAKD (T IV) | 71.12 (T V) | none found | learnable student-guided teacher-view augmentation | Q4 |
| `raza2026asd` | ASD | Anti-Shortcut Distillation via Temporal Negative Knowledge Transfer | arXiv | 2608.11789 | CORE-P | S | R32x4/8x4, W40-2/16-2, VGG13/8 (own teachers) / — | 73.13 (T1; teacher 79.72, student 71.90) | n/r | none found | temporal negative transfer against shortcuts | Q4 |
| `mugisha2026rdd` | RDD | Representational Difference Distillation | arXiv | 2610.15997 | CORE-P | F | R32x4/8x4 only / — | 75.58 (T1; single run, final epoch) | n/r | none found | representational-difference curriculum/supervision | Q4 |
| `islam2025dts` | DTS | Dynamic Temperature Scheduler for Knowledge Distillation | arXiv | 2511.13767 | CORE-P | L | 6 homog. + 4 heterog. CRD pairs / — | 75.25, MLKD+DTS (T II; MLKD here 75.03) | n/r | Sibgat-Ul/DTS (none) | loss-gap-driven temperature schedule | Q4 |
| `yu2025uhkd` | UHKD | UHKD: A Unified Framework for Heterogeneous Knowledge Distillation via Frequency-Domain Representations | arXiv | 2510.24116 | CORE-P | F (heterog.) | heterogeneous only / R34-R18, R50-MV2 | n/r | 72.71 (T3) | none found | frequency-domain intermediate features | Q4 |
| `yu2026cocars` | CoCaRS | CoCaRS: Correlation Calibration-Based Redundancy Suppression for Heterogeneous Knowledge Distillation | arXiv | 2607.27054 | CORE-P | F (heterog.) | heterogeneous only / R34-R18, R50-MV1 | n/r | 72.58 (T7) | none found | correlation-calibrated redundancy suppression | Q4 |
| `wu2025kdaif` | KD-AIF | Knowledge Distillation with Adapted Weight | arXiv | 2501.02705 | **AMBIGUOUS** | R | 12 CRD pairs / — | 82.20 (T2/T3; teacher updated to 86.56) | n/r | none found | influence-function sample weights; teacher updated | Q4 |
| `yan2025era` | ERA | Expandable Residual Approximation for Knowledge Distillation | arXiv (author-stated TNNLS 2025) | 2508.16050 | **AMBIGUOUS** | F | 6 CRD pairs / R34-R18, R50-MV1 | 76.89, Ours-ST (CIFAR table) | 72.49 (T III) | Zhaoyi-Yan/ERA (MIT) | multi-branch residual approximation of teacher features | Q4 |
| `zheng2025gdkd` | GDKD | Rethinking Decoupled Knowledge Distillation: A Predictive Distribution Perspective | arXiv (author-stated TNNLS) | 2512.04625 | **AMBIGUOUS** | L | 11 CRD pairs / R34-R18, R50-MV1 | 77.76 (T I; own DKD 76.64) | 72.26 (T III) | ZaberKo/GDKD (NOASSERTION) | generalised top/other partition of DKD | Q4 |
| `jiang2026arkd` | AR-KD | Discovering and Preserving Category Correlation Knowledge via Adaptive Reciprocal Knowledge Distillation | arXiv (author-stated CIKM 2026) | 2609.13199 | **AMBIGUOUS** | L | 10 CRD pairs / R34-R18, R50-MV2 | 77.29 (T1) | 72.13 (T2) | none found | adaptive reciprocal learning of class correlations | Q4 |
| `limantoro2025sortkd` | Sort-KD | Parameter-Free Logit Distillation via Sorting Mechanism | arXiv (author-stated IEEE SPL 2025) | 2508.16544 | **AMBIGUOUS** | L | 11 CRD pairs (no R32x4/8x4) / R34-R18, R50-MV1 | n/r | 71.84, Sort-DKD (T II) | none found | sorts logits to fix teacher mispredictions | Q4 |
| `niu2022ipwd` | IPWD | Respecting Transfer Gap in Knowledge Distillation | NeurIPS 2022 | 2210.12787 | CORE | R | 8 CRD pairs / R34-R18, R50-MV1 | 76.03 (T2; SSKD+IPWD 76.74, own teacher, T3) | 71.88 (T4) | none found | inverse-propensity sample weighting | `found via: HCD T3` |
| `cui2024dkl` | DKL / IKL-KD | Decoupled Kullback-Leibler Divergence Loss | NeurIPS 2024 | 2305.13948 | CORE | L | 11 CRD pairs / R34-R18, R50-MV1 | 76.59 (T13) | 71.91 (T4) | jiequancui/DKL (none) | KL = weighted MSE + soft-label CE, symmetrised | `found via: GenDD T5` |
| `yu2025angularkd` | Angular-KD | Single-Teacher View Augmentation: Boosting Knowledge Distillation via Angular Diversity | NeurIPS 2025 (author-stated) | 2510.22480 | CORE | S | R32x4/8x4, VGG13/8, W40-2/40-1 (+ cross) / R34-R18 | 77.28, MLKD+Angular (T2; KD+ 76.08) | 71.07 (T3) | june6423/Angular-KD (NOASSERTION) | angular-diversity teacher-view augmentation | `found via: SAKD T IV` |
| `wang2022cutmixpick` | CutMixPick | What Makes a "Good" Data Augmentation in Knowledge Distillation - A Statistical Perspective | NeurIPS 2022 | 2012.02909 | CORE | S | 7 CRD pairs / — | 76.11, CRD+CutMixPick (T1) | n/r | MingSun-Tse/Good-DA-in-KD (none) | entropy-picked CutMix samples for KD | `found via: KD-AIF T2` |
| `wang2022checkpointkd` | CkptKD | Efficient Knowledge Distillation from Model Checkpoints | NeurIPS 2022 | 2210.06458 | CORE | S | non-standard CIFAR pairs / R34-R18 | n/r | 70.98 (T1; teacher 73.86) | LeapLabTHU/CheckpointKD (none) | intermediate-checkpoint teachers | `found via: ASD T1` |
| `hossain2025tekap` | TeKAP | Single Teacher, Multiple Perspectives: Teacher Knowledge Augmentation for Enhanced Knowledge Distillation | ICLR 2025 | OpenReview DmEHmZ89iB | **AMBIGUOUS** | S | (secondary: R32x4/8x4) | 74.79 *secondary* (LDRLD T1) | 70.67 *secondary* (Angular-KD T3) | none checked | noise-perturbed teacher views | `found via: LDRLD T1` |
| `kim2024topkd` | TopKD (topology) | Do Topological Characteristics Help in Knowledge Distillation? | ICML 2024 | OpenReview 2dEH0u8w0b | **AMBIGUOUS** | F | (secondary: R32x4/8x4) | 75.40 *secondary* (EKD T1) | n/r | none checked | topological (persistent-homology) feature relations | `found via: EKD T1` |

**AMBIGUOUS cases (the coordinator decides):**
1. **Published at a venue outside I2, arXiv v1 ≥ 2025: `yan2025era` (TNNLS), `zheng2025gdkd` (TNNLS), `jiang2026arkd`
   (CIKM), `limantoro2025sortkd` (IEEE SPL), `kim2025figkd` (Expert Systems with Applications).** I2 read
   literally allows "an arXiv preprint first posted from 2025-01-01 with no such venue", and these preprints have no
   *listed* venue. But the registry's convention so far tags non-listed-venue papers as SUPPORT/E3. Read either way, the
   numbers are recorded.
2. **`wu2025kdaif`**: its 82.20 on R32x4→R8x4 comes with the teacher retrained to 86.56. It is a standard pair, but not
   the standard fixed-teacher protocol, so it should not go on the leaderboard as is.
3. **`tang2025hidfd`**: data-free; the student is "ShuffleNet" with no version given, and its baseline accuracy (72.60)
   matches neither ShuffleNetV1 (70.50) nor V2 (71.82), so whether the pair is standard is unclear.
4. **`hossain2025tekap`, `kim2024topkd`**: the venue is verified (OpenReview metadata), but the full text is blocked.
   I3 is supported only by other papers' tables. These are ICLR/ICML papers, so S1/S2 may already hold the full text.
5. **Seven TPAMI papers with no full text** (§5): left unassessed for I3.

**Notes for de-duplication / other workers (INTERPRETATION):**
- `chen2026pefd` extends NeurIPS 2022 *Improved Feature Distillation via Projector Ensemble* (arXiv 2210.15274). The
  NeurIPS version is not in the registry and belongs to S1/S2's listing.
- `cui2026gkl` extends `cui2024dkl`, and `zhang2026btkdpp` extends `zhang2025btkd`. Each pair should count as one
  method family on the leaderboard.
- The BTKD/BTKD++ CIFAR numbers exceed their own teachers by up to 6 points (Adam optimiser, own teachers, e.g.
  WRN-40-2 73.57). These are the papers' claims, and their comparability is doubtful.
- arXiv 2511.15572 (*From Per-Image Low-Rank to Encoding Mismatch*, ICML 2026 author-stated) came up in Q4. It is
  ViT feature distillation and fails I3 (E4), and it falls under S1/S2's ICML listing.

## 4. Top CIFAR-100 ResNet32x4→ResNet8x4 results among the new inclusions

Each value is the paper's own claim (VERIFIED from its PDF). KD-AIF (82.20) is left out because its teacher is updated
(AMBIGUOUS #2).

| Rank | Method (id) | Top-1 | Source | Note |
|---|---|---|---|---|
| 1= | TopKD (`wang2025topkd`) | 78.18 | arXiv 2508.04539 T2 | CORE-P |
| 1= | SimKD+NCKD (`zhang2025nckd`) | 78.18 | AAAI 2025, T1 | NCKD alone 77.23 |
| 3 | FiGKD (`kim2025figkd`) | 78.05 | arXiv 2505.11897 T1 | AMBIGUOUS (ESWA) |
| 4 | GDKD (`zheng2025gdkd`) | 77.76 | arXiv 2512.04625 T I | AMBIGUOUS (TNNLS); its DKD baseline is 76.64 |
| 5 | MLKD+ADG-KD (`li2025adgkd`) | 77.51 | AAAI 2025, T1 | ADG-KD alone 77.44 |

For comparison, existing registry entries already report higher values, e.g. DeepKD (CRLD+DeepKD, NeurIPS 2025) at
79.25 in its own Table 1. So this search adds no new top-1 above the known best.

## 5. Full-text exclusion table

| Source row | Paper | Venue | Code | Reason |
|---|---|---|---|---|
| 9 | Boosting Contrastive Learning with Relation Knowledge Distillation | AAAI 2022 | E1 | KD for self-supervised pretraining; linear-probe evaluation only |
| 10 | Knowledge Distillation via Constrained Variational Inference | AAAI 2022 | E2 | distils into probabilistic graphical/topic models, not image classification |
| 20 | Robust and Resource-Efficient Data-Free KD by Generative Pseudo Replay | AAAI 2022 | E4 | CIFAR-100 only with ResNet34→ResNet18 (not a CRD pair) |
| 36 | Learn More for Food Recognition via Progressive Self-Distillation | AAAI 2023 | E4 | food datasets only |
| 41 | Adaptive Hierarchy-Branch Fusion for Online KD | AAAI 2023 | E4 | online KD, peer ResNets; no teacher→student CRD pair |
| 62 | Cooperative Knowledge Distillation: A Learner Agnostic Approach | AAAI 2024 | E4 | MNIST-scale experiments only |
| 74 | Impartial Adversarial Distillation (data-free) | AAAI 2024 | E4 | imbalanced CIFAR-100 (r = 0.01) teachers only |
| 78 | Out of Thin Air: Data-Free Adversarial Robustness Distillation | AAAI 2024 | E4 | robustness pairs, not CRD pairs |
| 98 | Teacher as a Lenient Expert (TA-DFKD) | AAAI 2024 | E4 | CIFAR-100 ResNet34→ResNet18 only |
| 104 | How to Trade Off the Quantity and Capacity of Teacher Ensemble | AAAI 2024 | E2 | NLP (TinyBERT/GLUE) |
| 131 | KDAT: Inherent Adversarial Robustness via KD with Adversarial Tuning | AAAI 2025 | E2 | object detection (COCO) |
| 149 | Multi-label Self Knowledge Distillation | AAAI 2025 | E4 | multi-label VOC/COCO |
| 166 | A Closer Look at KD in Spiking Neural Network Training | AAAI 2026 | E4 | SNN students |
| 170 | Pairing-free Group-level KD for Gastrointestinal Lesion Classification | AAAI 2026 | E4 | endoscopy data only |
| 177 | Revisiting Cross-Architecture Distillation: Adaptive Dual-Teacher Transfer | AAAI 2026 | E4 | no CIFAR-100; non-standard ImageNet pairs |
| 179 | Distillation Dynamics: Feature-Based Distillation in ViTs | AAAI 2026 | SUPPORT | analysis paper; ViT only |
| 208 | Condensed Data Expansion Using Model Inversion for KD | AAAI 2026 | E4 | non-standard pairs (ResNet-34→MobileNetV2 etc.) |
| 224 | Credal Ensemble Distillation for Uncertainty Quantification | AAAI 2026 | E4 | CIFAR-10 only |
| 228 | Bi-Spectrum Distillation (ANN→SNN) | AAAI 2026 | E4 | SNN students |
| 232 | MoSE: Hierarchical Self-Distillation Enhances Early Layer Embeddings | AAAI 2026 | E2 | text (GLUE) |
| 238 | ASKD: RL-Style KD with Quality-Adaptive Skewness | AAAI 2026 | E2 | LLM (Alpaca/GSM8K) |
| 248 | C2R-KD: Complex to Real KD (student abstract) | AAAI 2026 | E4 | no CIFAR-100/ImageNet |
| 342 | Generalized KD via Relationship Matching | TPAMI 2023 | E4 | CIFAR-100 with non-CRD pairs |
| 344 | Quantifying the Knowledge in a DNN to Explain KD | TPAMI 2022 | SUPPORT | analysis paper |
| 357 | Learning From Human Educational Wisdom: Student-Centered KD | TPAMI 2024 | E4 | no CRD/ImageNet standard pair found |
| 360 | Balanced Multi-Teacher Adversarial Distillation | TPAMI 2024 | E4 | robustness pairs only |
| 375 | Aligning Logits Generatively for Black-Box KD | TPAMI 2025 | E4 | ResNet56→MobileNet etc.; no standard pair |
| 379 | Forget Me Not: Knowledge Fusion and Distillation | TPAMI 2026 | E4 | self-ensemble; no teacher→student CRD pair |
| 420 | Multi-target KD via Student Self-reflection | IJCV 2023 | E4 | CIFAR-100 with ResNet34→18 (ImageNet-style) only |
| 424 | Cross-Architecture Knowledge Distillation | IJCV 2024 | E4 | ViT→CNN pairs only |
| 458 | Perspective-Aware Teaching (heterogeneous) | arXiv 2025 | E4 | heterogeneous pairs only |
| 460 | Multi-Level Decoupled Relational Distillation (heterogeneous) | arXiv 2025 | E4 | heterogeneous pairs only |
| 461 | Right Time to Learn: Spacing Effect in KD | arXiv 2025 | E4 | non-standard pairs |
| 462 | Transformer-in-Transformer Network Utilizing KD | arXiv 2025 | E4 | non-standard student (TITN) |
| 467 | CustomKD: Customizing Large Vision Foundation | arXiv 2025 | E4 | foundation-model teachers; no CRD pair |
| 476 | Improving KD Under Unknown Covariate Shift | arXiv 2025 | E4 | no CIFAR-100 CRD pair / ImageNet standard pair |
| 482 | Model compression using KD with integrated gradients | arXiv 2025 | E4 | CIFAR-10 main results; CIFAR-100 only in a literature-summary table |
| 485 | Fine-Grained Image Recognition from Scratch with Teacher-Guided DA | arXiv 2025 | E4 | fine-grained datasets |
| 498 | Dynamic KD Based on the Gompertz Curve | arXiv 2025 | E4 | ImageNet-style ResNet50→MobileNet_v2 on CIFAR, not the CRD networks |
| 504 | From Per-Image Low-Rank to Encoding Mismatch (ViT feature KD) | arXiv / ICML 2026 | E4 | ViT pairs; R34→R18 only as a FitNet control |
| 507 | Uncertainty-Aware Dual-Student KD | arXiv 2025 | E4 | no CIFAR-100 |
| 509 | HPM-KD: Hierarchical Progressive Multi-Teacher | arXiv 2025 | E4 | non-standard pairs |
| 512 | Distilling Lightweight Domain Experts (subspaces) | arXiv 2026 | E4 | non-standard pairs |
| 523 | Weak-to-Strong KD Accelerates Visual Learning | arXiv 2026 | E4 | weak→strong speed-up study; no CRD pair |
| 524 | STARS: ANN-to-SNN Data-Free KD | arXiv 2026 | E4 | SNN students |
| 527 | What Do Students Learn? Feature-Level Analysis of Dark Knowledge | arXiv / ICPR 2026 | SUPPORT | analysis paper |
| 529 | Beyond Dark Knowledge: Mixup-Based Distillation | arXiv 2026 | E4 | non-standard pairs |
| 530 | Dyna-DINO: Efficient ViT Distillation | arXiv 2026 | E4 | no CIFAR-100; ViT/DINO |
| 531 | Distill on a Diet: Learnable Data Pruning | arXiv 2026 | E4 | non-standard pairs |
| 536 | SPRKD: Saddle Region Approximation | arXiv 2026 | E4 | no CRD pair found |
| 540 | A Controlled Study of Feature-Based KD Across Student Designs | arXiv 2026 | SUPPORT | analysis (course project); MobileNetV2 variants |
| 545 | Transferring Visual Explanations (cross-architecture KD) | arXiv 2026 | SUPPORT | analysis of interpretability |

**Full text not retrievable (AMBIGUOUS, I3 unassessed).** TPAMI, IEEE Xplore returned HTML, and no arXiv version was
found. *Unpacking the Gap Box Against Data-Free KD* (2024) · *Pixel Distillation* (2024) · **DIST+: KD From a Stronger
Adaptive Teacher** (2025; extension of the registry's `huang2022dist`) · *Toward Effective KD: Navigating Beyond
Small-Data Pitfall* (2026) · *Allies Teach Better Than Enemies: Inverse Adversaries for Robust KD* (2026) · *Looking
Broader for KD via Receptive-Field Alignment* (2026) · *Selecting and Distilling Cross-Label Models* (2026). Their DOIs
are in the Crossref TPAMI hits (Q2).

## 6. Snowballing log

I read the CIFAR-100 comparison tables of 10 registry papers (EKD, LDRLD, RLD, LumiNet, VRM, RSD, RPKD, LTKD,
DeepKD, PLD) and the 14 new inclusions named in Q7. RSD and RPKD compare only cross-architecture baselines (OFA etc.,
already registered), and LTKD compares only on CIFAR-100-LT. Competitors already in the registry are not listed here.
These include KD, FitNet, AT, CRD, ReviewKD, DKD, CTKD, MLKD, NKD, LSKD, SDD, DOT, WTTM, NORM, SimKD, CAT-KD, FCFD,
DiffKD, DIST, OFA, RLD, LDRLD, EKD, RSD, WKD and the CLASSIC entries.

| Competitor | Seen in (table) | Resolution | Decision |
|---|---|---|---|
| IPWD (NeurIPS 2022) | HCD T3 | NeurIPS 2022 listing + arXiv 2210.12787 | **included** `niu2022ipwd` |
| DKL / IKL-KD (NeurIPS 2024) | GenDD T5, GKL T5 | NeurIPS 2024 listing + arXiv 2305.13948 | **included** `cui2024dkl` |
| Angular-KD (NeurIPS 2025) | SAKD T III/IV | arXiv 2510.22480 (author-stated NeurIPS 2025) | **included** `yu2025angularkd` |
| CutMixPick (NeurIPS 2022) | KD-AIF T2 | NeurIPS 2022 listing + arXiv 2012.02909 | **included** `wang2022cutmixpick` |
| CkptKD (NeurIPS 2022) | ASD T1 | NeurIPS 2022 listing + arXiv 2210.06458 | **included** `wang2022checkpointkd` |
| TeKAP (ICLR 2025) | LDRLD T1, FiGKD T1, AR-KD T1, HCD T3 | OpenReview metadata; PDF blocked | **AMBIGUOUS** `hossain2025tekap` |
| TopKD (topology, ICML 2024) | EKD T1, NCKD T1 | OpenReview metadata; PDF blocked | **AMBIGUOUS** `kim2024topkd` |
| CRLD | DeepKD T1 | ref: ACM MM 2024 | E3 |
| BDCKD | LumiNet T1 | ref: ICASSP 2025 | E3 |
| LA | RLD, REDistill | ref: Neurocomputing 2021 | E3 |
| RC | RLD, REDistill | ref: IEEE SPL 2023 | E3 |
| SAKD (spot-adaptive) | LDRLD appendix | ref: TIP 2022 | E3 |
| RCKA | AR-KD T1 | IJCAI 2024 (as labelled in the AR-KD table) | E3 |
| WCoRD, SRRL, SemCKD, SSKD, WSLD, TAKD, DML, ESKD, ONE | ADG-KD, AR-KD, UniADS, IPWD | pre-2022 | E3 |
| DisWOT (CVPR 2023) | UniADS T4, NCKD T2 | arXiv 2303.15678 | E4 (searched students; no CRD pair) |
| DIST+ (TPAMI 2025) | — | from Q2 | AMBIGUOUS (no full text, §5) |
| LR (label revision, Lan et al.) | RLD, REDistill | venue not given in the citing reference text | **unresolved** |
| RKKD (2025) | RCKD T1, HCD T1 | author-year citation; not resolved to a title in this pass | **unresolved** |
| URPKD | BTKD++ T3 | not resolved | **unresolved** |
| CID | PEFD T9 | not resolved | **unresolved** |
| FBT | UHKD T3 | not resolved | **unresolved** |
| InDistill (Sarridis et al. 2022) | BTKD T1 | venue not checked | **unresolved** |

The six unresolved competitors are left for the coordinator or S1/S2, where their venues may already be listed.


## Coordinator de-duplication (2026-11-08)

During the merge, the snowball records `wang2022ckptkd`, `wang2022gooddakd` and `kim2024topokd` turned out to duplicate the S2 records `wang2022checkpointkd`, `wang2022cutmixpick` and `kim2024topkd` (same paper). The S2 records are kept and the references above now point to them. `niu2022ipwd`, `yu2025angularkd` and `hossain2025tekap` were created by both S2 and S3 under the same id; the S2 version is kept.
