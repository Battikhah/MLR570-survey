# Manually retrieved full texts (2026-11-08)

A team member downloaded 15 of the 17 previously inaccessible papers (plus OpenReview-only TMLR/ICLR papers) by browser
and AUS IEEE Xplore access. PDFs: `literature/pdfs/access/` (git-ignored). Assessed by the coordinator against the
frozen I1–I3; numbers read from the cited table (TPAMI tables read from rendered pages).

## Included (6): 106 → 112 methods

| Paper | Venue | Std pair → top-1 (source) | Flags |
|---|---|---|---|
| MCD, Correctness-Aware KD | TMLR | R32x4→R8x4 76.81; +MLLD 77.45; +LS 77.11 (T2). ImageNet R34→R18 72.08, R50→MBV1 see T4 | 3 trials |
| MC-Distil, Unified Wisdom | TMLR 08/2025 | R32x4→R8x4 75.38 (T1) | multi-student; own teacher 80.10; not mdistiller protocol |
| DiSK, Scaffolding a Student | ICLR 2023 | R32x4→R8x4 76.92, R32x4→SV2 80.23 (T4); ImageNet R50→R18 72.35 (T7, not an I3 pair) | own KD baseline 76.25 (strong) |
| DIST+ (journal ext. of `huang2022dist`) | TPAMI 47(7) 2025 | R32x4→R8x4 76.19 (T6); ImageNet R34→R18 72.39, R50→MBV1 73.47 (T3) | separate row from DIST (adds feature losses) |
| LB, Receptive-Field Alignment | TPAMI 48(10) 2026 | ImageNet R34→R18 72.30, R50→MobileNet 73.25 (T1) | ImageNet only |
| GapSSG, Unpacking the Gap Box | TPAMI 46(9) 2024 | WRN40-2→WRN16-2 68.88 (data-free, T1) | data-free sub-table |

## Excluded (9)

| Paper | Code | Reason |
|---|---|---|
| Feature Distillation Improves Zero-Shot Transfer from Synthetic Images (TMLR) | E4 | CLIP zero-shot; no I3 pair |
| Layerwise Bregman Representation Learning (TMLR) | E4 | ImageNet R50→R18 (PreAct) only; not an I3 pair |
| Breaking BatchNorm Barriers (TMLR) | E4 | data-free; WRN28-10→WRN16-8/RN18 only |
| Prediction-only distillation, optimal mixing (NeurIPS 2026) | E4 | linear/logistic regression on frozen features |
| Allies Teach Better Than Enemies (TPAMI) | E4 | adversarially robust KD; WRN28-10→R18/MNV2 on CIFAR-10 |
| Pixel Distillation (TPAMI) | E4 | cross-resolution; R50→R18 only |
| Selecting and Distilling Cross-Label Models (TPAMI) | E4 | teacher selection / cross-label reuse; no I3 pair |
| Toward Effective KD: Small-Data Pitfall (TPAMI) | SUPPORT | mainly analysis of KD across data scale; R34→R18 on CIFAR, R50 student on ImageNet |
| Learning from Interaction (Gao et al., ICCV 2025) | E2 | VLM→vision-foundation-model transfer |

## Still not assessable (2)

Maximum Divergence KD (NeurIPS 2026) and Feature Kernel Distillation (ICLR 2022): no full text found.
SDPGO (NeurIPS 2025) was not among the downloaded files.

MCD's ImageNet column order was read from flattened text (15 methods, MCD 12th = 72.08); recheck against the PDF before
it enters the leaderboard.
