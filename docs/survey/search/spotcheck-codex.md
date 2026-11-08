# Codex independent spot-check — T12b-V (PDF text audit)

The checks below use the supplied `literature/pdfs/spotcheck/*.txt` and `INDEX.json`. Code URL/licence checks were omitted as authorized. “AGREE” means the inclusion criteria and the reported available values/table references are supported; “DISAGREE” records a factual/table-reference discrepancy; unavailable texts remain unsupported.

## Inclusion sample

| ID | Verdict | Primary-text check |
|---|---|---|
| `cui2024dkl` | **AGREE** | I1 IKL-KD is proposed for KD; I2 NeurIPS 2024; I3 CIFAR100 standard R32x4→R8x4. Table 13: 76.59; ImageNet R34→R18 Table 4: 71.91. Text lines 539-550, 906-926, 463-474. |
| `hossain2025tekap` | **AGREE** | I1 teacher augmentation for KD; I2 ICLR 2025 printed on PDF; I3 CIFAR pair in Table 2: MLKD+TeKAP 77.36; ImageNet Table 3 prints top-1 error 29.33 (=70.67 accuracy). Text lines 399-419, 435-454. |
| `chae2025kdas` | **AGREE** | I1 adaptive sampling/weighting for KD; I2 ICCV 2025 proceedings PDF; I3 standard R56→R20 / other CRD pairs in CIFAR Table 2 (e.g. 71.81 DKD+Ours for R110→R20); ImageNet R34→R18 71.81 in Table 3. Text lines 434-465. |
| `li2023kdzero` | **AGREE** | I1 automated KD design search; I2 NeurIPS 2023; I3 R32x4→R8x4 77.85 Table 3 and ImageNet R34→R18 72.17 Table 4. Text lines 447-480. |
| `chen2026djip` | **AGREE** | I1 teacher-training method to improve KD; I2 ICLR 2026 printed on PDF; I3 CIFAR R32x4→R8x4 WTTM+DJIP-teacher 76.61 Table 1; ImageNet R34→R18 DKD+DJIP 72.08 Table 3. Text lines 399-408, 474-479. |
| `bassam2025pld` | **AGREE** | I1 PLD is a proposed classification KD loss; I2 NeurIPS 2025 official proceedings; I3 CIFAR R32x4→R8x4 PLD 73.97 Table 1; no ImageNet R34→R18 result in that table. Accessible official proceedings: https://proceedings.neurips.cc/paper_files/paper/2025/hash/c6b2921f24f82dc05cda53bbe50bab90-Abstract-Conference.html; arXiv text lines 420-460. |
| `jeong2026skd` | **AGREE** | I1 streamlined KD method; I2 CVPR 2026 proceedings PDF; I3 CIFAR R32x4→R8x4 78.33 Table 1; ImageNet R34→R18 71.13 Table 3. Text lines 328-350, 396-403. |
| `zhao2023dot` | **AGREE** | I1 optimizer/training rule for KD; I2 ICCV 2023; I3 CIFAR 75.12 KD+DOT and ImageNet 71.72 KD+DOT, both Table 3 (CIFAR section a, ImageNet section c). Text lines 375-406. |
| `sun2025rld` | **AGREE** | I1 teacher reliability KD method; I2 ICCV 2025; I3 CIFAR R32x4→R8x4 76.64 Table 1; ImageNet R34→R18 71.91 Table 3. Text lines 281-285, 367-370. |
| `wang2022cutmixpick` | **AGREE** | I1 KD augmentation selection method; I2 NeurIPS 2022; I3 R32x4→R8x4 CIFAR Table 1 includes KD+CutMixPick 76.11 (the table also reports separate 960-epoch results); no ImageNet R34→R18 result is claimed. Text lines 620-645. |
| `huang2023maskd` | **AGREE** | I1 KD method applied to image classification as well as dense prediction; I2 ICLR 2023; I3 ImageNet R34→R18 71.26 Table 6 (appendix). Paper explicitly calls this classification experiment. Text lines 785-826. |
| `huang2023diffkd` | **AGREE** | I1 diffusion feature KD method; I2 NeurIPS 2023; I3 CIFAR R32x4→R8x4 76.72 Table 9 (appendix); ImageNet R34→R18 72.22 Table 2. Text lines 327-332, 817-832. |
| `limantoro2025sortkd` | **AGREE** | I1 label-aware logit KD method; I2 arXiv first posted 2025 (2508.16544), eligible under CORE-P; I3 CIFAR standard pairs reported in Table I and ImageNet R34→R18 Sort-DKD 71.84 Table II. The record correctly says no R32x4→R8x4 CIFAR value; text lines 216-259. |
| `liao2026dskd` | **UNSUPPORTED** | AAAI PDF retrieval was blocked by the bot challenge (per coordinator). |
| `chen2022pefd` | **AGREE** | I1 projector-ensemble feature KD; I2 NeurIPS 2022; I3 CIFAR R32x4→R8x4 76.08 Table 5; ImageNet R34→R18 71.94 Table 7. Text lines 343-371, 398-401. |
| `liu2023norm` | **AGREE** | I1 many-to-one feature KD method; I2 ICLR 2023; I3 CIFAR R32x4→R8x4 76.49 Table 1; ImageNet R34→R18 72.14 Table 3. Text lines 346-380, 457-487. |
| `zhu2022tllm` | **AGREE** | I1 reliability-based KD method; I2 NeurIPS 2022; I3 CIFAR R32x4→R8x4 TLLM 77.83 Table 2; ImageNet R34→R18 TLLM 72.6 Table 3. Text lines 428-446, 489-495. |
| `li2023autokd` | **AGREE** | I1 automated distiller-search method; I2 ICCV 2023; I3 CIFAR R32x4→R8x4 77.61 Table 3 (with logits KD); ImageNet R34→R18 72.45 Table 4. Text lines 354-383. |
| `jiang2026arkd` | **AGREE** | I1 category-correlation KD method; I2 arXiv 2026, CORE-P (its stated CIKM venue is outside the frozen list); I3 CIFAR R32x4→R8x4 77.29 Table 1; ImageNet R34→R18 72.13 Table 2. Text lines 392-417, 423-450. |
| `zheng2024wttm` | **DISAGREE** | I1/I2/I3 hold; CIFAR R32x4→R8x4 value 76.06 is in Table 1, not Table 2 as recorded. ImageNet R34→R18 72.19 is Table 5 and matches. Text lines 455-490, 558. |
| `niu2022ipwd` | **AGREE** | I1 inverse-propensity KD method; I2 NeurIPS 2022; I3 CIFAR R32x4→R8x4 76.03 Table 2; ImageNet R34→R18 71.88 Table 4. Text lines 417-445, 520-535. |
| `li2025adgkd` | **UNSUPPORTED** | AAAI PDF retrieval was blocked by the bot challenge (per coordinator). |

**Inclusion error rate (accessible sampled rows):** 2/20 = 10.0%. Two sampled rows are inaccessible (`liao2026dskd`, `li2025adgkd`); both remain outside the denominator.

**VkD mandatory check:** **AGREE** — arXiv text Table 7 explicitly reports ResNet32x4→ShuffleNetV2 = **77.51** (text lines 773–795).

**Inclusion DISAGREE list:** `zheng2024wttm` — CIFAR value 76.06 is Table 1, not Table 2; `niu2022ipwd` — ImageNet 71.88 is Table 4, not Table 5. Both values match; only the table identifiers differ.

## Full-text exclusion sample

| Source row | Code | Verdict | Evidence / note |
|---|---|---|---|
| `s2-ml.md:25` | SUPPORT | **AGREE** | Theoretical analysis of repeated self-distillation; analysis-only, so SUPPORT is appropriate. excl_s2_ml_md_25.txt abstract, lines 12-25. |
| `s2-ml.md:66` | E4 | **AGREE** | Adversarial-training-focused KD; no standard clean CIFAR-100/ImageNet teacher→student result in the cited full text. |
| `s2-ml.md:138` | SUPPORT | **UNSUPPORTED** | NO ARXIV MATCH in INDEX.json. |
| `s3-aaai-journals-arxiv-snowball.md:238` | E2 | **UNSUPPORTED** | NO ARXIV MATCH in INDEX.json. |
| `s2-ml.md:117` | E2 | **AGREE** | Cross-modal transfer experiments are AVE/RAVDESS/CREMA-D/VGGSound, not image classification; text/audio modality. excl_s2_ml_md_117.txt lines 1-28, 450-463. |
| `s2-ml.md:16` | SUPPORT | **AGREE** | Analysis of what knowledge transfers; no proposed distillation algorithm. excl_s2_ml_md_16.txt abstract, lines 17-38. |
| `s2-ml.md:118` | E2 | **AGREE** | Weak-to-strong language-model learning; tasks are knowledge/reasoning and games, not image classification. excl_s2_ml_md_118.txt lines 13-25, 224-240. |
| `s2-ml.md:33` | E4 | **AGREE** | Gaussian distillation transfers ensemble uncertainty; CIFAR-100 evaluation is model-level/ensemble setup and no listed standard pair. excl_s2_ml_md_33.txt lines 21-30, 421-433. |
| `s3-aaai-journals-arxiv-snowball.md:529` | E4 | **AGREE** | CIFAR-100 table uses large teachers (ConvNeXt-L/ViT-B/ResNet152V2) and MobileNetV2 student, not an accepted pair; table 3. excl_s3...529.txt lines 727-741. |
| `s2-ml.md:3` | E4 | **UNSUPPORTED** | NO ARXIV MATCH in INDEX.json. |
| `s2-ml.md:34` | SUPPORT | **AGREE** | Theoretical self-distillation analysis on Gaussian mixtures; CIFAR-10 is an illustration, not a new KD method. excl_s2_ml_md_34.txt abstract lines 30-44. |
| `s2-ml.md:91` | E4 | **UNSUPPORTED** | NO ARXIV MATCH in INDEX.json. |
| `s2-ml.md:108` | E4 | **AGREE** | Data-free KD is evaluated for OOD/backdoor transfer with VGG13→VGG11 and ResNet34→ResNet18, not an I3 CIFAR-100 or ImageNet standard result. excl_s2_ml_md_108.txt lines 501-536. |
| `s2-ml.md:68` | SUPPORT | **AGREE** | Study/analysis of general teacher-student transfer, not a proposed KD method. excl_s2_ml_md_68.txt abstract and lines 58-76. |
| `s2-ml.md:98` | SUPPORT | **AGREE** | Empirical analysis of randomly initialized teachers; no distinct KD method contribution. excl_s2_ml_md_98.txt abstract lines 7-22. |
| `s2-ml.md:126` | E4 | **AGREE** | No listed CNN standard pair; ImageNet results use ViT/linear-evaluation style. excl_s2_ml_md_126.txt lines 423-450. |
| `s3-aaai-journals-arxiv-snowball.md:482` | E4 | **UNSUPPORTED** | NO ARXIV MATCH in INDEX.json. |
| `s2-ml.md:112` | E4 | **AGREE; NUANCE** | SNN students make E2 (non-image-classification student/task) a better conceptual code; E4 is still defensible because paper reports CIFAR/ImageNet image-classification data but only SNN students. excl_s2_ml_md_112.txt abstract lines 13-27, table 1 lines 347+. |
| `s3-aaai-journals-arxiv-snowball.md:360` | E4 | **AGREE** | Robustness distillation uses CIFAR robustness settings and non-standard teachers/students (ResNet56, WRN-34-10, WRN-22-6; students ResNet18/MobileNetV2); no I3 pair. excl_s3...360.txt lines 530-547. |
| `s2-ml.md:19` | E4 | **AGREE; NUANCE** | Progressive ensemble distillation deliberately produces multiple student models/ensembles, not an accepted single teacher→student result. Ensemble-student task could also be coded E2 under broad scope wording; recorded E4 is understandable. excl_s2_ml_md_19.txt abstract lines 16-22. |
| `s3-aaai-journals-arxiv-snowball.md:461` | E4 | **UNSUPPORTED** | NO ARXIV MATCH in INDEX.json. |
| `s2-ml.md:28` | E4 | **AGREE** | CIFAR/ImageNet experiments use student variants not in standard CRD pair list; the listed ImageNet result is nonstandard. excl_s2_ml_md_28.txt full text. |
| `s2-ml.md:109` | E4 | **UNSUPPORTED** | NO ARXIV MATCH in INDEX.json. |
| `s3-aaai-journals-arxiv-snowball.md:524` | E4 | **UNSUPPORTED** | NO ARXIV MATCH in INDEX.json. |
| `s2-ml.md:38` | E4 | **AGREE; NUANCE** | Self-distillation is among SNNs, including CIFAR/ImageNet; E2 is arguably the more direct task/student-family code, but E4 captures absence of an accepted standard pair. excl_s2_ml_md_38.txt abstract lines 16-31. |
| `s2-ml.md:4` | E4 | **AGREE** | CIFAR-100 uses ResNet110→ResNet56, not an I3 pair; CIFAR-10 uses MobileNet variants. excl_s2_ml_md_4.txt lines 376-381. |
| `s3-aaai-journals-arxiv-snowball.md:170` | E4 | **UNSUPPORTED** | NO ARXIV MATCH in INDEX.json; if verified, the endoscopy/medical-only setting is an E2 nuance rather than a standard image-classification scope. |
| `s3-aaai-journals-arxiv-snowball.md:467` | E4 | **AGREE** | Foundation teachers (DINOv2/OpenCLIP) to MobileNetV3 in semi-supervised CIFAR/ImageNet; no standard pair. excl_s3...467.txt lines 305-314. |
| `s3-aaai-journals-arxiv-snowball.md:462` | E4 | **UNSUPPORTED** | NO ARXIV MATCH in INDEX.json. |
| `s3-aaai-journals-arxiv-snowball.md:232` | E2 | **AGREE** | Text classification/GLUE embedding self-distillation; not image classification. excl_s3...232.txt abstract lines 12-26. |

**Exclusion error rate (accessible sampled rows):** 0/20 = 0.0%; inaccessible rows are excluded. SUPPORT is treated as correct when analysis-only.

**Exclusion DISAGREE list:** none.

## Coding nuances / denominator

E4 is plausible but E2 may better describe SNN/student-family cases (`112`, `38`) and ensemble-student work (`19`); these are nuances rather than counted errors. The medical/endoscopy row `170` is inaccessible; E2 would likely be the more direct code if its stated endoscopy-only scope is confirmed.

The stored deterministic inclusion draw contains 22 IDs; the text inventory has 20 accessible IDs plus the two blocked IDs, despite the coordinator note saying 21/22 are accessible. The stored exclusion draw contains 30 rows (including SUPPORT rows); the note describes 28 sampled exclusions with 18 texts available. This report uses the exact stored draw and inventories the files: 20/30 exclusion rows have text, 10 are NO ARXIV MATCH. Error rates use accessible rows in those stored samples; denominator discrepancies are surfaced rather than silently changing the draw.

## Coordinator adjudication (2026-11-08)

- `zheng2024wttm`: **the recorded "T2" is correct.** In `literature/pdfs/spotcheck/zheng2024wttm.txt`, the WTTM row with 76.06 for R32x4→R8x4 appears in both Table 1 (caption line 455, row line 478) and Table 2 (caption line 482, row line 490). This finding is withdrawn.
- `niu2022ipwd`: **the recorded "T4" is correct.** Both `s2-ml.md:73` and `s3-…md:109` record ImageNet 71.88 as T4, and the per-row verdict above (AGREE, Table 4) agrees. The summary line's "Table 4 rather than Table 5" refers to no recorded error. This finding is withdrawn.
- **Adjudicated rates:** inclusions 0/20 errors (2 inaccessible); exclusions 0/20 errors (10 inaccessible). VkD Table 7 (77.51) is confirmed.
