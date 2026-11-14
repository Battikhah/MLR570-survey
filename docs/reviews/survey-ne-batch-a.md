# Existing-source NE audit — batch A

Scope: 135 missing cells across 54 already cited records. No new papers, bibliography keys, manuscript edits, or source registry edits.

## Results

- 2 exact candidate values found in canonical PDFs:
  - PEFD, CIFAR-100 WRN-40-2 → WRN-16-2: 76.02 (Table 5, PDF p. 6; Ours).
  - DJIP + vanilla KD, CIFAR-100 WRN-40-2 → WRN-16-2: 75.64 (Table 5, PDF p. 7; DJIP row, KD column).
- 5 other cells had inspected table evidence that rules out direct filling: 3 PLD pair mismatches, PEFD ImageNet MobileNet variant unresolved, and DJIP ImageNet MobileNetV2 vs requested MobileNetV1.
- 125 cells have an explicit canonical existing-source URL attempt recorded, but the full paper/table was not inspected in this batch. These remain unverified; they are not evidence that the paper lacks the result.
- 3 cells belong to kag2023disk, whose existing record supplies no official or arXiv URL. No source search was performed; the CSV requests the already-cited source URL.

## Canonical PDF evidence checked

- [PLD NeurIPS 2025 PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/c6b2921f24f82dc05cda53bbe50bab90-Paper-Conference.pdf): Table 1 (p. 6) uses WRN-40-2 → WRN-40-1, not WRN-16-2. Table 2 (p. 7) does not include R34 → R18 or R50 → MobileNetV1.
- [PEFD NeurIPS 2022 PDF](https://papers.nips.cc/paper_files/paper/2022/file/4ec0b6648bdf487a2f1c815924339022-Paper-Conference.pdf): Table 5 (p. 6) gives Ours 76.02±0.10 for the exact CIFAR-100 pair. Table 7(b) lists ResNet-50 → MobileNet but does not establish MobileNetV1, so no ImageNet candidate was accepted.
- [DJIP ICLR 2026 PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/f7d3cef7ff579f2f903c8f458e730cae-Paper-Conference.pdf): Table 5 (p. 7) gives DJIP + KD 75.64 for exact CIFAR-100 pair. Table 2 uses MobileNetV2, not requested MobileNetV1.
- ADM's PMLR page was reachable, but its linked PDF was not extracted by the browser tool (unsupported content type). Its cells remain pending full-text table inspection.

All exact per-cell statuses, source URLs, page/table pointers, evidence, and needed-user inputs are in [survey-ne-batch-a.csv](survey-ne-batch-a.csv). Preserve existing manuscript values until the integrator reviews the two candidates and the unresolved variant warnings. Do not convert the remaining NE cells to NR from these checks.
