# Existing-source NE audit: batch B

- Assigned cells: **132** across 54 cited papers.
- Attempted each paper’s canonical official URL (and listed arXiv alternate where present); DNS resolution failed for all remote retrievals in this environment.
- Existing official PDFs were available and table-checked for SimKD and Bayesian teacher: **4 cells checked**, all lacked the exact requested pair/benchmark.
- Access blocked: **128 cells**; no number was estimated, and no `NR` was assigned.
- Accepted positive fills: **0**. Existing numeric values were not modified.

## Locally checked papers

- `chen2022simkd`, ImageNet R50→MobileNetV1: no exact pair; Table 3 reports ResNet-18 student (PDF p. 6).
- `morad2026bayesteacher`, CIFAR-100 R32x4→R8x4: no exact pair in Table 1 (PDF p. 9); supplemental tables reviewed.
- `morad2026bayesteacher`, ImageNet R34→R18 and R50→MobileNetV1: paper tables report CIFAR-100 and Tiny ImageNet experiments, not standard ImageNet (Table 1, Appendix G/Table 4; PDF pp. 9, 30-31).

## Retrieval blockers

The canonical/alternate URLs below were actually attempted. Requests failed before HTTP response with `DNS resolution error: [Errno 8] nodename nor servname provided, or not known`. Please provide the official PDF or restore network/DNS access to continue these per-cell checks. The CSV contains an individual row and exact attempted URL(s) for every affected cell.

- `chae2025kdas` — [CIFAR-100 R32x4→R8x4](https://openaccess.thecvf.com/content/ICCV2025/html/Chae_What_to_Distill_Fast_Knowledge_Distillation_with_Adaptive_Sampling_ICCV_2025_paper.html)
- `chen2025cpnet` — [CIFAR-100 R32x4→R8x4](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Coupling_the_Generator_with_Teacher_for_Effective_Data-Free_Knowledge_Distillation_ICCV_2025_paper.html)
- `chen2026pefd` — [CIFAR-100 WRN40-2→WRN16-2](https://doi.org/10.1109/tpami.2026.3677028); alternate: [arXiv](https://arxiv.org/abs/2310.17183)
- `cui2024dkl` — [CIFAR-100 WRN40-2→WRN16-2](https://proceedings.neurips.cc/paper_files/paper/2024/hash/87ee1bbac4635e7c948f3eea83c1f262-Abstract-Conference.html); alternate: [arXiv](https://arxiv.org/abs/2305.13948)
- `cui2026gkl` — [CIFAR-100 WRN40-2→WRN16-2](https://doi.org/10.1109/TPAMI.2026.3703828); alternate: [arXiv](https://arxiv.org/abs/2503.08038)
- `do2022mad` — [CIFAR-100 R32x4→R8x4](https://papers.nips.cc/paper_files/paper/2022/hash/41128e5b3a7622da5b17588757599077-Abstract-Conference.html); alternate: [arXiv](https://arxiv.org/abs/2209.10359)
- `etcibasi2026rpkd` — [CIFAR-100 R32x4→R8x4](https://arxiv.org/abs/2610.37937)
- `guan2025rankingkd` — [CIFAR-100 WRN40-2→WRN16-2](https://proceedings.mlr.press/v267/guan25a.html); alternate: [arXiv](https://arxiv.org/abs/2409.17823)
- `guo2025gpd` — [CIFAR-100 R32x4→R8x4](https://proceedings.iclr.cc/paper_files/paper/2025/hash/9a379c1b05793d1c42dc832269834515-Abstract-Conference.html); alternate: [arXiv](https://arxiv.org/abs/2410.04140)
- `hao2023ofakd` — [CIFAR-100 R32x4→R8x4](https://proceedings.neurips.cc/paper_files/paper/2023/hash/fb8e5f198c7a5dcd48860354e38c0edc-Abstract-Conference.html); alternate: [arXiv](https://arxiv.org/abs/2310.19444)
- `hossain2025luminet` — [CIFAR-100 WRN40-2→WRN16-2](https://openreview.net/forum?id=3rU1lp9w2l); alternate: [arXiv](https://arxiv.org/abs/2310.03669)
- `hu2024tgeokd` — [CIFAR-100 WRN40-2→WRN16-2](https://proceedings.iclr.cc/paper_files/paper/2024/hash/6aa4967920e495e90aeeaa3acf18d019-Abstract-Conference.html); alternate: [arXiv](https://arxiv.org/abs/2312.15112)
- `huang2023diffkd` — [CIFAR-100 WRN40-2→WRN16-2](https://proceedings.neurips.cc/paper_files/paper/2023/hash/cdddf13f06182063c4dbde8cbd5a5c21-Abstract-Conference.html); alternate: [arXiv](https://arxiv.org/abs/2305.15712)
- `huang2024unikd` — [CIFAR-100 WRN40-2→WRN16-2](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4805_ECCV_2024_paper.php); alternate: [arXiv](https://arxiv.org/abs/2409.18565)
- `islam2025dts` — [CIFAR-100 WRN40-2→WRN16-2](https://arxiv.org/abs/2511.13767)
- `jiang2026arkd` — [CIFAR-100 WRN40-2→WRN16-2](https://arxiv.org/abs/2609.13199)
- `kim2024topkd` — [CIFAR-100 WRN40-2→WRN16-2](https://proceedings.mlr.press/v235/kim24aj.html)
- `li2022kcd` — [CIFAR-100 WRN40-2→WRN16-2](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/75_ECCV_2022_paper.php); alternate: [arXiv](https://arxiv.org/abs/2207.05409)
- `li2023autokd` — [CIFAR-100 WRN40-2→WRN16-2](https://openaccess.thecvf.com/content/ICCV2023/html/Li_Automated_Knowledge_Distillation_via_Monte_Carlo_Tree_Search_ICCV_2023_paper.html)
- `li2023kdzero` — [CIFAR-100 WRN40-2→WRN16-2](https://papers.nips.cc/paper_files/paper/2023/hash/dbc8ce0fdfcd55172d73fb05dbae07fc-Abstract-Conference.html)
- `li2025fbt` — [CIFAR-100 R32x4→R8x4](https://openaccess.thecvf.com/content/ICCV2025/html/Li_Fuse_Before_Transfer_Knowledge_Fusion_for_Heterogeneous_Distillation_ICCV_2025_paper.html); alternate: [arXiv](https://arxiv.org/abs/2410.12342)
- `liao2026dskd` — [CIFAR-100 WRN40-2→WRN16-2](https://doi.org/10.1609/aaai.v40i28.39520)
- `lin2022tat` — [CIFAR-100 WRN40-2→WRN16-2](https://openaccess.thecvf.com/content/CVPR2022/html/Lin_Knowledge_Distillation_via_the_Target-Aware_Transformer_CVPR_2022_paper.html); alternate: [arXiv](https://arxiv.org/abs/2205.10793)
- `liu2023fcfd` — [CIFAR-100 WRN40-2→WRN16-2](https://arxiv.org/abs/2304.11832)
- `liu2024ssdkd` — [CIFAR-100 R32x4→R8x4](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Small_Scale_Data-Free_Knowledge_Distillation_CVPR_2024_paper.html); alternate: [arXiv](https://arxiv.org/abs/2406.07876)
- `lv2024wkd` — [CIFAR-100 WRN40-2→WRN16-2](https://proceedings.neurips.cc/paper_files/paper/2024/hash/78526d7ad4a2532bd91416e948b9644c-Abstract-Conference.html); alternate: [arXiv](https://arxiv.org/abs/2412.08139)
- `miles2024vkd` — [CIFAR-100 R32x4→R8x4](https://openaccess.thecvf.com/content/CVPR2024/html/Miles_VkD_Improving_Knowledge_Distillation_using_Orthogonal_Projections_CVPR_2024_paper.html); alternate: [arXiv](https://arxiv.org/abs/2403.06213)
- `niu2022ipwd` — [CIFAR-100 WRN40-2→WRN16-2](https://papers.nips.cc/paper_files/paper/2022/hash/89b0e466b46292ce0bfe53618aadd3de-Abstract-Conference.html); alternate: [arXiv](https://arxiv.org/abs/2210.12787)
- `peng2024kdav` — [CIFAR-100 WRN40-2→WRN16-2](https://proceedings.mlr.press/v235/peng24a.html)
- `qian2022switokd` — [CIFAR-100 R32x4→R8x4](https://link.springer.com/chapter/10.1007/978-3-031-20083-0_26); alternate: [arXiv](https://arxiv.org/abs/2209.04996)
- `qiu2023dpk` — [CIFAR-100 R32x4→R8x4](https://arxiv.org/abs/2206.06067)
- `raza2026asd` — [CIFAR-100 WRN40-2→WRN16-2](https://arxiv.org/abs/2608.11789)
- `su2025eakd` — [CIFAR-100 WRN40-2→WRN16-2](https://openaccess.thecvf.com/content/ICCV2025/html/Su_EA-KD_Entropy-based_Adaptive_Knowledge_Distillation_ICCV_2025_paper.html); alternate: [arXiv](https://arxiv.org/abs/2311.13621)
- `tang2023kd3` — [CIFAR-100 WRN40-2→WRN16-2](https://openaccess.thecvf.com/content/ICCV2023/html/Tang_Distribution_Shift_Matters_for_Knowledge_Distillation_with_Webly_Collected_Images_ICCV_2023_paper.html); alternate: [arXiv](https://arxiv.org/abs/2307.11469)
- `tran2024nayer` — [CIFAR-100 R32x4→R8x4](https://openaccess.thecvf.com/content/CVPR2024/html/Tran_NAYER_Noisy_Layer_Data_Generation_for_Efficient_and_Effective_Data-free_CVPR_2024_paper.html); alternate: [arXiv](https://arxiv.org/abs/2310.00258)
- `wang2022checkpointkd` — [CIFAR-100 R32x4→R8x4](https://papers.nips.cc/paper_files/paper/2022/hash/03e0712bf85ebe7cec4f1a7fc53216c9-Abstract-Conference.html); alternate: [arXiv](https://arxiv.org/abs/2210.06458)
- `wang2024gapssg` — [CIFAR-100 R32x4→R8x4](https://doi.org/10.1109/TPAMI.2024.3379505)
- `wang2024nd` — [CIFAR-100 WRN40-2→WRN16-2](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3432_ECCV_2024_paper.php)
- `wang2025ikd` — [CIFAR-100 WRN40-2→WRN16-2](https://doi.org/10.1609/aaai.v39i8.32840)
- `wang2026rckd` — [CIFAR-100 WRN40-2→WRN16-2](https://doi.org/10.1609/aaai.v40i31.39878)
- `wu2025kdaif` — [CIFAR-100 WRN40-2→WRN16-2](https://arxiv.org/abs/2501.02705)
- `xu2025ldrld` — [CIFAR-100 WRN40-2→WRN16-2](https://openaccess.thecvf.com/content/ICCV2025/html/Xu_Local_Dense_Logit_Relations_for_Enhanced_Knowledge_Distillation_ICCV_2025_paper.html); alternate: [arXiv](https://arxiv.org/abs/2507.15911)
- `yan2025era` — [CIFAR-100 WRN40-2→WRN16-2](https://arxiv.org/abs/2508.16050)
- `yang2023nkd` — [CIFAR-100 WRN40-2→WRN16-2](https://openaccess.thecvf.com/content/ICCV2023/html/Yang_From_Knowledge_Distillation_to_Self-Knowledge_Distillation_A_Unified_Approach_with_ICCV_2023_paper.html); alternate: [arXiv](https://arxiv.org/abs/2303.13005)
- `ye2024mcmi` — [CIFAR-100 R32x4→R8x4](https://proceedings.iclr.cc/paper_files/paper/2024/hash/718a3c5cf135894db6e718725f52ef9a-Abstract-Conference.html); alternate: [arXiv](https://arxiv.org/abs/2401.08732)
- `yu2025angularkd` — [CIFAR-100 WRN40-2→WRN16-2](https://neurips.cc/virtual/2025/poster/118239); alternate: [arXiv](https://arxiv.org/abs/2510.22480)
- `yu2026cocars` — [CIFAR-100 R32x4→R8x4](https://arxiv.org/abs/2607.27054)
- `zhang2025btkd` — [CIFAR-100 R32x4→R8x4](https://doi.org/10.1609/aaai.v39i21.34400); alternate: [arXiv](https://arxiv.org/abs/2412.09874)
- `zhang2025vrm` — [CIFAR-100 WRN40-2→WRN16-2](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_VRM_Knowledge_Distillation_via_Virtual_Relation_Matching_ICCV_2025_paper.html); alternate: [arXiv](https://arxiv.org/abs/2502.20760)
- `zhao2022dkd` — [CIFAR-100 WRN40-2→WRN16-2](https://openaccess.thecvf.com/content/CVPR2022/html/Zhao_Decoupled_Knowledge_Distillation_CVPR_2022_paper.html); alternate: [arXiv](https://arxiv.org/abs/2203.08679)
- `zheng2024wttm` — [CIFAR-100 WRN40-2→WRN16-2](https://proceedings.iclr.cc/paper_files/paper/2024/hash/c3d6bb5723b015b20c7333d5c8273027-Abstract-Conference.html); alternate: [arXiv](https://arxiv.org/abs/2402.11148)
- `zhu2022tllm` — [CIFAR-100 WRN40-2→WRN16-2](https://papers.nips.cc/paper_files/paper/2022/hash/cf5c369c1bc070361477008e3f5210ed-Abstract-Conference.html)
