# Survey benchmark NE and code availability audit

Observation date: 2026-11-14. Scope is the 112 included records parsed from `scripts/build_supplement.py` and `docs/survey/included-methods.md`, plus the method rows in the selected CIFAR and ImageNet comparison tables in `paper/survey/sections/08_benchmarks.tex`. No bibliography keys or source-registry records were added or changed for this audit.

## Scope and status

The inclusion inventory has **112 records and 281 `--` benchmark cells**: 40 CIFAR ResNet32x4→ResNet8x4, 101 CIFAR WRN-40-2→WRN-16-2, 32 ImageNet ResNet34→ResNet18, and 108 ImageNet ResNet50→MobileNetV1. The complete cell inventory, each current official source URL, and whether a cell was actually reviewed is in [survey-source-audit-ne-cells.csv](survey-source-audit-ne-cells.csv). This is the pre-integration inventory. The final merged CSV records 13 supported fills, inspected mismatches, and retrieval/full-text limitations; it is not evidence that all 112 papers were re-read.

Before this audit, the five entirely empty records were HiDFD, VkD, SoTeacher, Bayesian teacher, and ABKD. Exact source locations reviewed and recommendations are listed below. The subsequent batch checks are documented in survey-ne-batch-a.md and survey-ne-batch-b.md; many retrieval attempts did not yield inspected full text, and those cells remain NE. The CSV's source URL is for the existing included record only, and an empty URL means the source registry has no corresponding official URL.

## Candidate fills from visually checked primary tables and figure

These are recommendations for the parent to integrate; this audit did not edit manuscript or source files. Values are top-1 accuracy (%) and match the stated dataset, student/teacher architecture, and variant.

| Record and target cell | Candidate | Primary source evidence | Notes |
|---|---:|---|---|
| MLKD, CIFAR WRN-40-2→WRN-16-2 | 76.63 | [CVPR 2023 paper, Table 2, printed p. 24281](https://openaccess.thecvf.com/content/CVPR2023/papers/Jin_Multi-Level_Logit_Distillation_CVPR_2023_paper.pdf) | MLKD row, exact WRN pair. Render `/private/tmp/aml-source-audit/mlkd-page-06.png`; visually checked. |
| MLKD, ImageNet R34→R18 | 71.90 | [CVPR 2023 paper, Table 4, printed p. 24281](https://openaccess.thecvf.com/content/CVPR2023/papers/Jin_Multi-Level_Logit_Distillation_CVPR_2023_paper.pdf) | MLKD row, ResNet34 teacher / ResNet18 student. Render `/private/tmp/aml-source-audit/mlkd-page-06.png`; visually checked. |
| MLKD, ImageNet R50→MobileNetV1 | — | Same Table 4 | No compatible candidate: paper pair is ResNet50→MobileNetV2. Do not fill this cell. Render `/private/tmp/aml-source-audit/mlkd-page-06.png`; visually checked. |
| LSKD, CIFAR WRN-40-2→WRN-16-2 | 76.95 | [CVPR 2024 paper, Table 2, printed p. 15737](https://openaccess.thecvf.com/content/CVPR2024/papers/Sun_Logit_Standardization_in_Knowledge_Distillation_CVPR_2024_paper.pdf) | Correct variant is MLKD+Ours (logit standardization). Render `/private/tmp/aml-source-audit/lskd-page-07.png`; visually checked. |
| LSKD, ImageNet R34→R18 | 72.08 | [CVPR 2024 paper, Table 3, printed p. 15737](https://openaccess.thecvf.com/content/CVPR2024/papers/Sun_Logit_Standardization_in_Knowledge_Distillation_CVPR_2024_paper.pdf) | Correct reported variant is MLKD+Ours (logit standardization), same stacked variant used in the CIFAR row. Rendered table visually checked (`/private/tmp/aml-source-audit/lskd-page-07.png`). |
| LSKD, ImageNet R50→MobileNetV1 | 73.22 | Same Table 3 | MLKD+Ours row, paper labels pair ResNet50/MN-V1. The printed red +0.18 and +0.21 are gains over MLKD, not uncertainty intervals. Render `/private/tmp/aml-source-audit/lskd-page-07.png`; visually checked. |
| RLD, ImageNet R34→R18 | 71.91 | [ICCV 2025 paper, Table 3, printed p. 1115](https://openaccess.thecvf.com/content/ICCV2025/papers/Sun_Knowledge_Distillation_with_Refined_Logits_ICCV_2025_paper.pdf) | Mean of three trials; rendered table `/private/tmp/aml-source-audit/rld-page-06.png` visually checked. |
| RLD, ImageNet R50→MobileNetV1 | 72.75 | Same Table 3 | Mean of three trials; rendered table `/private/tmp/aml-source-audit/rld-page-06.png` visually checked. |
| SoTeacher, CIFAR WRN-40-2→WRN-16-2 | 75.39 ± 0.23 | [ICLR 2024 paper, Table 1, p. 7](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1263ffa557506ea29c54481788d518f-Paper-Conference.pdf) | SoTeacher student / own teacher row; distinct from Standard 74.87 ± 0.45. Rendered table visually checked. |
| ABKD, CIFAR R32x4→R8x4 | 76.82 (ABTTM stacked; standalone ABKD 75.62) | [PMLR proceedings page](https://proceedings.mlr.press/v267/wang25dz.html), [official PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dz/wang25dz.pdf), Figure 5(f), p. 8 | Best stacked ABTTM label; standalone ABKD label is 75.62. Exact printed label above ABKD bar for the captioned CIFAR-100 ResNet32x4→ResNet8x4 pair, not estimated from the bar. Render `/private/tmp/aml-source-audit/abkd-page-hi-08.png`; visually checked at high resolution. |
| Bayesian teacher, CIFAR WRN-40-2→WRN-16-2 | 72.94 | [ICLR 2026 paper, Table 1, p. 9](https://proceedings.iclr.cc/paper_files/paper/2026/file/0bdbfac7d9df70021d694e5ac795bf9d-Paper-Conference.pdf) | Bayesian (Ours) student accuracy: mean over five repetitions of the best result among six temperature/λ configurations. Preserve the existing own-teacher setting note. Render `/private/tmp/aml-source-audit/bay-page-09.png`; visually checked. |

**Architecture check:** MLKD reports ResNet50→MobileNetV2 (73.01), which does not match the survey's MobileNetV1 column. Leave that cell NE. There are ten recommended fills in the table above. No value is recommended for the mismatched MobileNetV2 pair.

### Five wholly empty records

- **SoTeacher** and **Bayesian teacher:** CIFAR WRN pair cells above are verified candidates.
- **HiDFD:** the existing notes identify an alternative DF ResNet32x4→ShuffleNet result (version unspecified), not the standard R32x4→R8x4 comparison. Preserve all standard-pair NE cells. Official paper: [AAAI 2025 paper](https://ojs.aaai.org/index.php/AAAI/article/download/34293/36448).
- **VkD:** its checked official paper/supplement reports an alternative ResNet32x4→ShuffleNetV2 pair, not the standard R32x4→R8x4 pair. Preserve standard-pair NE cells. [CVPR 2024 paper](https://openaccess.thecvf.com/content/CVPR2024/html/Miles_VkD_Improving_Knowledge_Distillation_using_Orthogonal_Projections_CVPR_2024_paper.html); [official supplement](https://openaccess.thecvf.com/content/CVPR2024/supplemental/Miles_VkD_Improving_Knowledge_CVPR_2024_supplemental.pdf).
- **ABKD:** Figure 5(f) of the official PMLR PDF explicitly labels the exact CIFAR-100 ResNet32x4→ResNet8x4 bar as 75.62. This candidate is now included above; the original paper row is figure-based, not table-based.

### Other priority checks

- **DTO-KD:** existing CIFAR R32x4→R8x4 result is 76.40 (ICLR 2026 Table 2; existing extracted value). Table 2 has WRN-40-2→WRN-40-1 (75.68), not the survey's WRN-40-2→WRN-16-2 pair. Its ImageNet Table 1 uses RegNetY-160 teachers and DeiT students, so it does not supply the survey's ResNet34→ResNet18 or ResNet50→MobileNetV1 cells. These are mismatches in reviewed tables, not a whole-paper claim that the results are never reported. Official [ICLR 2026 paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/e546ce4230c15bc422a500bb47b341ea-Paper-Conference.pdf); relevant existing page renders are in `/private/tmp/aml-source-audit/dtokd-page-05.png` through `-07.png`.
- **VRM:** the checked ImageNet table uses ResNet101→ResNet18 and ResNet50→MobileNetV2, not either selected standard pair. Do not transfer those figures to the survey cells. Official [ICCV 2025 paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_VRM_Knowledge_Distillation_via_Virtual_Relation_Matching_ICCV_2025_paper.pdf).
- **SimKD:** Table 2 has a WRN-16-2 student with a ResNet32x4 teacher (77.17 ± 0.32), not the required WRN40-2 teacher; keep that W16 cell NE. ImageNet Table 3 gives SimKD 71.66 with ResNet-18 student but omits the teacher in its caption. The official supplement Table S.3 (PDF p. 2) shows the ImageNet SimKD teacher pair ResNet-50→ResNet-34 has teacher accuracy 76.26; this matches Table 3's 76.26 teacher and establishes ResNet50→ResNet18, not the survey R34→R18 pair. Keep the R18 cell NE. Renders: `/private/tmp/aml-source-audit/simkd-page-05.png`, `simkd-page-06.png`, and `simkd-supp-page-2.png`. Official [CVPR 2022 paper](https://openaccess.thecvf.com/content/CVPR2022/papers/Chen_Knowledge_Distillation_With_the_Reused_Teacher_Classifier_CVPR_2022_paper.pdf) and [official supplement](https://openaccess.thecvf.com/content/CVPR2022/supplemental/Chen_Knowledge_Distillation_With_CVPR_2022_supplemental.pdf).

## Code availability for comparison-table rows

Status is a current observation on 2026-11-14, based on existing registry links and checked official paper/project links. “Linked, accessible” means an author/paper-linked implementation page loaded; it does not certify code completeness, reproducibility, or license. “No author link located” means the reviewed official paper/proceedings page and current registry had no implementation URL; it is not a claim that code cannot exist elsewhere. The code URL is shown for every linked row.

| Main-table row | Current observation |
|---|---|
| KD baseline | Linked, accessible: [mdistiller](https://github.com/megvii-research/mdistiller) |
| DKD | Linked, accessible: [mdistiller](https://github.com/megvii-research/mdistiller) |
| Student alone | Not applicable; no distillation implementation |
| VRM | Linked, accessible: [VISION-SJTU/VRM](https://github.com/VISION-SJTU/VRM), linked by author/paper page |
| SimKD | Linked, accessible: [DefangChen/SimKD](https://github.com/DefangChen/SimKD) |
| GDKD | Linked, accessible: [ZaberKo/GDKD](https://github.com/ZaberKo/GDKD) |
| LumiNet | Linked, accessible: [ismail31416/LumiNet](https://github.com/ismail31416/LumiNet) |
| MLKD | Linked, accessible: [Jin-Ying/Multi-Level-Logit-Distillation](https://github.com/Jin-Ying/Multi-Level-Logit-Distillation) |
| MCD | No author implementation link located on reviewed [OpenReview paper](https://openreview.net/forum?id=XpRXmzd2sF); registry code field is empty |
| RLD | Linked, accessible: [zju-SWJ/RLD](https://github.com/zju-SWJ/RLD) |
| DTO-KD | No author implementation link located on reviewed [ICLR paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/e546ce4230c15bc422a500bb47b341ea-Paper-Conference.pdf); registry code field is empty |
| DIST | Linked, accessible: [hunto/DIST_KD](https://github.com/hunto/DIST_KD) |
| DIST+ | Linked, accessible: [hunto/DIST_KD](https://github.com/hunto/DIST_KD) (shared project URL in registry) |
| TopoKD | Linked, accessible now: [jekim5418/TopKD](https://github.com/jekim5418/TopKD). Existing `unreachable` display status is stale. |
| DOT | Linked, accessible: [mdistiller](https://github.com/megvii-research/mdistiller) |
| KD-AIF | No author implementation link located on reviewed [arXiv paper](https://arxiv.org/abs/2501.02705); registry code field is empty |
| DeepKD | No author implementation link located on reviewed [NeurIPS proceedings page](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2756ffa0487af8d276a0b1baf78732f4-Abstract-Conference.html); registry code field is empty |
| EA-KD | Linked, accessible: [cpsu00/EA-KD](https://github.com/cpsu00/EA-KD) |
| SKD | No author implementation link located on reviewed [CVPR paper page](https://openaccess.thecvf.com/content/CVPR2026/html/Jeong_Streamlined_Knowledge_Distillation_CVPR_2026_paper.html); registry code field is empty |
| LSKD | Linked, accessible: [sunshangquan/logit-standardization-KD](https://github.com/sunshangquan/logit-standardization-KD) |
| SRD | Linked, accessible: [roymiles/Simple-Recipe-Distillation](https://github.com/roymiles/Simple-Recipe-Distillation) |
| LB | No author implementation link located on reviewed [TPAMI journal DOI page](https://doi.org/10.1109/TPAMI.2026.3704741); registry code field is empty |
| DistPro | Linked, accessible: [xdeng7/DistPro](https://github.com/xdeng7/DistPro) |
| CTKD | Linked, accessible: [zhengli97/CTKD](https://github.com/zhengli97/CTKD) |

**Counts:** 17 method rows have an author-linked accessible implementation; 6 method rows have no author link located on the checked official source; Student alone is not applicable. The TopoKD link currently loads and should no longer be labeled “unreachable.” The integrated main-table caption now records the 2026-11-14 check.

## Additional reviewed-cell count

The final integration fills 13 of the original 281 NE cells, leaving 268 NE cells. Batch A added PEFD W16-2 76.02 and DJIP+KD W16-2 75.64; the main session also extracted ABKD Figure 5(a), ABTTM W16-2 76.67 (standalone ABKD 76.11). ABKD uses the best stacked variant, explicitly flagged, consistently with the existing Table S2 policy. Most remaining cells lack full-text verification: an access failure or a mismatching inspected table is not a paper-wide absence finding. See the merged CSV and linked upload list.

## Reproducibility trail

- Inventory parsed with `scripts.build_supplement.rows` from `docs/survey/included-methods.md`; source URLs looked up in the existing `literature/sources.yaml`.
- Official PDF originals and rendered screenshots used for visual checks were stored outside the repository under `/private/tmp/aml-source-audit/`. They are not project inputs and are not committed.
- No new bibliography entries or keys were created. No NE cell was labeled “not reported” merely because text search failed.

## Main-session integration checks

The main session inspected the primary MLKD, LSKD, RLD, SoTeacher, Bayesian-teacher and ABKD figure/table renders before integration. LSKD’s red +0.18/+0.21 annotations are improvements over MLKD, not standard deviations. MLKD’s official implementation repository also lists `configs/imagenet/r50_mv2`, consistent with the paper’s V2 label; this does not establish an MN-V1 result. [Author repository configuration directory](https://github.com/Jin-Ying/Multi-Level-Logit-Distillation/tree/main/configs/imagenet).

Final ABKD selection supersedes the earlier standalone-only candidate discussion: R8x4 76.82 and W16-2 76.67 are the printed ABTTM bars in Figure 5(f)/(a); standalone ABKD values remain explicitly recorded in the notes.
