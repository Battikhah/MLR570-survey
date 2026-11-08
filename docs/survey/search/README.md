# Systematic search (T12b): consolidated record

The criteria I1–I3 and exclusion codes E1–E7 were frozen in `tasks/plan.md` (commit 22c7492) before the search started.
Three Claude searches ran in parallel on 2026-11-08:

| Search | Sources | Identified | Full text assessed | Included | File |
|---|---|---|---|---|---|
| S1 | CVPR 2022–26, ICCV 2023/25, ECCV 2022/24 (ECCV 2026 not yet online) | 656 | 96 | 37 (18 new) | `s1-cvf.md` |
| S2 | NeurIPS, ICML, ICLR 2022–26, TMLR | 985 | 130 | 36 (21 new) | `s2-ml.md` |
| S3 | AAAI 2022–26, TPAMI, IJCV, arXiv 2025+, snowballing | 552 | 84 | 39 (all new) | `s3-aaai-journals-arxiv-snowball.md` |

Union after de-duplication: **106 distinct included methods** (6 found by two searches). The merged registry has 228 records.
On the merge, line-level conflict resolution had spliced fields between adjacent records; the registry was rebuilt from
whole records (commit 65b48d6). Snowball duplicates: see the note at the end of `s3-…md`.

## Coordinator rulings on AMBIGUOUS cases (applying I1–I3 literally)

Comparability is handled in the §VIII leaderboard (separate sub-tables and protocol flags), not by exclusion.

| Case | Ruling | Reason |
|---|---|---|
| Data-free KD: `wang2024kdci`, `tran2024nayer`, `chen2025cpnet`, `yu2023spaceshipnet`, `liu2024ssdkd`, `do2022mad` | **Include**; separate data-free sub-table | I1 (a KD training scheme for classification) and I3 (WRN-40-2→WRN-16-2) are met. E6 covers dataset distillation and teacher-free compression, which these are not. |
| `tang2023kd3` (web data) | **Include**, flag "non-standard training data" | I1–I3 met |
| `kim2026ltkd` (CIFAR-100-LT only) | **Exclude from the leaderboard (E4)**; it stays cited in §V as reliability/group-bias work | CIFAR-100-LT is not one of the I3 datasets |
| `deng2022pebkd` | **SUPPORT** (not on the leaderboard) | Mainly analysis; its only gain over KD is an oracle simulation (I1) |
| Supervision Complexity (S2 #54) | **SUPPORT** | Theory, not a new KD method (I1) |
| `miles2024vkd` | **Include pending verification**: the Codex spot-check must confirm the Table 7 value in the arXiv version | The CVF PDF has no standard-pair table |
| `huang2023maskd` | **Include**, flag "detection-first; classification in appendix" | It reports the I3 ImageNet pair |
| `morad2026bayesteacher`, `chen2025adm` | **Include**, flag "own protocol" / "online KD" | I3 met; their protocol differs |
| `jeong2026skd` | **Include**; note that its KD baseline is 74.75 | I1–I3 met |
| 2025+ preprints later published at venues outside the list (ERA/GDKD in TNNLS, AR-KD at CIKM, Sort-KD in SPL, FiGKD in ESWA) | **Include as CORE-P**, stating the actual venue | I2's preprint clause is date-based ("first posted from 2025, no listed venue") |
| KD-AIF (teacher updated to 86.56) | **Include**, flag "non-standard teacher" | I3 met |
| HiDFD (ShuffleNet version unstated) | **Include** | I3 accepts both ShuffleNetV1 and V2 |
| TeKAP / TopoKD (OpenReview 403) | **Resolved**: S2 read both full texts (`hossain2025tekap` via arXiv, `kim2024topkd` via PMLR) | — |
| TLLM teacher label; TopKD ImageNet above its teacher | Recorded as printed; noted in the leaderboard | — |

## Not assessable (full text inaccessible): 17 papers

These are 9 from S2 (OpenReview bot challenge, no arXiv copy), 7 TPAMI papers from S3 (paywalled, no arXiv copy, including DIST+)
and 1 from S1 (an ICCV 2025 PDF that timed out). They are listed in each search file and stay unassessed unless a team member downloads
the PDFs by hand (a browser passes the OpenReview challenge; AUS library access covers IEEE Xplore). Three of the S2 papers are KD
methods by their abstracts and could meet I3: Maximum Divergence KD (NeurIPS 2026), Correctness-Aware KD (TMLR) and Unified Wisdom (TMLR).

## Recall gaps found by the coordinator (closed by the gap pass, T12b-G)

1. S3 matched 15 papers to existing registry ids and dropped them from assessment, including `li2023ctkd`, `miles2024projector`,
   `zhou2025tcs`, `yang2025mtkdrl` and `yang2023lmcl`. They need an eligibility decision like any other paper.
2. The title keyword filters missed titles that say "teach", "mimic" or "student" without "distill". For example, ATS (*Asymmetric
   Temperature Scaling Makes Larger Networks Teach Well Again*, NeurIPS 2022), which the survey already cites, was not identified by S2.
3. 2022+ classification works already cited in §III–§VI that no search included need an explicit decision (e.g. `li2022ats`,
   `sengupta2026casd`).

## Gap pass outcome and final rulings (2026-11-08)

The gap pass (`g-gap.md`, merge of commit d483a59) assessed:
- S3's 15 dropped registry matches;
- 445 new titles found with the broader terms (teach / student / mimic / soft label / dark knowledge / logit / temperature scaling) across all listings;
- the 29 cited-but-unincluded works;
- one more round of snowballing from the 2026 inclusions.

It added **2 methods**:
- **CTKD** (AAAI 2023; ImageNet R34→R18 only);
- **SRD / projector study** (`miles2024projector`, AAAI 2024; 76.44 with RandAugment, 78.37 with SSKD teachers, the latter flagged as not protocol-comparable).

ATS (NeurIPS 2022) is E4: its CIFAR teachers (ResNet110, WRN28-8, ResNeXt29) are not CRD pairs. It stays cited in §III.

Coordinator rulings on the residual items:
- **InherNet (ICLR 2026): SUPPORT.** It builds the student by decomposing the teacher's weights, which is weight inheritance rather than training a given student with a teacher signal (I1). It is cited in §VIII/§IX as a related alternative, not ranked.
- **CVPR 2023 listing residual: closed by the coordinator.** I re-fetched the CVF CVPR 2023 listing (2,353 papers) and found 80 titles matching S1's regex. Title-screening them leaves 4 possibly eligible: OKDPH, DisWOT and Learning-to-Retain (all assessed and excluded in `s1-cvf.md`), plus "Data-Free KD via Feature Exchange and Activation Region Constraint", which is SpaceshipNet (`yu2023spaceshipnet`), already included. No new inclusions.
- *Scaffolding a Student to Instill Knowledge* (ICLR 2023) joins the not-assessable list (18 papers in total).

**Final included set: 106 methods.** That is the 106-method union, plus CTKD and SRD, minus LTKD (E4 by ruling; cited in §V) and PE-BKD (SUPPORT). The Codex spot-check (`spotcheck-codex.md`) found 0/20 inclusion errors and 0/20 exclusion errors on accessible papers after adjudication.
