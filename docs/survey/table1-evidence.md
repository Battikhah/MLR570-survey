# Table I evidence: comparison with existing surveys (survey Task 4)

This file justifies every cell of Table I (`paper/survey/sections/01_intro.tex`, `\label{tab:surveys}`).
Compiled 2026-11-03 by the Claude T4 worker (Orca task `task_1aba4b8161fe`).
Each survey has a record in `literature/sources.yaml` under the id shown. The metadata is **VERIFIED** against
Crossref, the TMLR listing or bib, and the arXiv API, as recorded in each record's `verified_by` field.

## Method

- **Section lists:** read from the arXiv PDFs with `pdftotext` (the latest arXiv version, listed per survey).
  Section numbers below follow those PDFs. The published versions may number sections differently.
- **Keyword checks:** each full text was also searched with regexes, counting matches. The patterns were:
  - MOO: `multi-objective|Pareto|gradient conflict|conflicting gradient|MGDA|PCGrad|multi-task optimi`
  - teacher reliability: `noisy teacher|unreliable|incorrect (teacher|prediction)|teacher…(mistake|error)|reliab`
  - LLM: `large language model|LLM`
  - VLM: `CLIP|vision-language`
  - benchmarks: `CIFAR-100|ImageNet`
  - years cited (2024–2026)

  A zero count is used only as *supporting* evidence for a ✗. Every ✗ also rests on the section list.
- **Legend:**
  - ✓ means a dedicated section or subsection covers the topic.
  - partial (○) means the topic is covered only in passing, only inside another topic, or only in a narrower
    setting (for example LLM-only).
  - ✗ means the topic is not covered.
  - ? means the cell could not be determined because the full text was not accessible.
- **"MOO in KD"** means that the KD and task objectives (or several teachers) are treated with multi-objective
  optimisation: Pareto optimality, gradient balancing, or conflict handling. A survey that discusses only loss
  *weighting* between CE and KD terms gets partial.
- **"2024–26 methods"** means the survey discusses KD *methods* published in 2024–2026.
  - partial: it reaches 2024 or 2025 but stops before the 2025–2026 state of the art.
  - The cut-off we compare against is the inventory in `docs/survey/sota-inventory.md`, which includes ICCV 2025
    and ICLR 2026 methods such as DTO-KD.
- **Labels:** cells are *INTERPRETATION* of the section content (my judgement), backed by the **VERIFIED** section
  titles quoted below.

## Table I

| Survey (id) | Venue | Year | Logit | Feat./relation | Schemes | Teacher reliab. | MOO in KD | Bench./results | LLM/VLM | 2024–26 methods |
|---|---|---|---|---|---|---|---|---|---|---|
| Gou et al. (`gou2021kdsurvey`) | IJCV | 2021 | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ |
| Wang & Yoon (`wang2022kdreview`) | TPAMI | 2022 | ✓ | ✓ | ✓ | partial | ✗ | ✗ | ✗ | ✗ |
| Hu et al. (`hu2023tsasurvey`) | arXiv | 2023 | ✓ | ✓ | ✓ | ✗ | partial | ✗ | ✗ | ✗ |
| Moslemi et al. (`moslemi2024kdsurvey`) | MLWA | 2024 | ✓ | ✓ | partial | ? | ? | ? | partial | ? |
| Xu et al. (`xu2024llmkdsurvey`) | arXiv | 2024 | partial | partial | partial | ✗ | ✗ | ✗ | ✓ | partial |
| Mansourian et al. (`mansourian2025kdsurvey`) | TMLR | 2025 | ✓ | ✓ | ✓ | partial | partial | ✓ | ✓ | partial |
| Yang et al. (`yang2025llmkdsurvey`) | ACM TIST | 2025 | partial | partial | ✗ | ✗ | ✗ | partial | ✓ | partial |
| Chen et al. (`chen2026gradmoo`) | TMLR | 2026 (arXiv 2025) | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **This survey** | — | 2026 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | partial | ✓ |

**Gap shown (INTERPRETATION):** no existing survey is both
1. a KD survey that reaches the 2025–2026 state of the art, and
2. one that treats KD as a multi-objective problem.

The closest general survey, Mansourian et al. (TMLR 2025), touches loss weighting only inside "Adaptive
Distillation" (§4.6). Its full text has zero MOO-keyword hits, and its coverage ends before its 09/2025
publication. The one MOO survey, Chen et al. (TMLR 2026), never uses the word "distill". The KD × MOO column is
therefore empty outside this survey, apart from the loss-weighting partials. That is the gap §VI targets.

## Per-survey justifications

### Gou, Yu, Maybank, Tao, "Knowledge Distillation: A Survey", IJCV 2021 (arXiv 2006.05525v7)

Sections: 1 Introduction; 2 Knowledge (2.1 Response-Based, 2.2 Feature-Based, 2.3 Relation-Based); 3 Distillation
Schemes (3.1 Offline, 3.2 Online, 3.3 Self-Distillation); 4 Teacher-Student Architecture; 5 Distillation Algorithms
(5.1 Adversarial … 5.2 Multi-Teacher … 5.6 Data-Free … 5.9 NAS-Based); 6 Performance Comparison; 7 Applications
(7.1 Visual Recognition, 7.2 NLP, 7.3 Speech, 7.4 Other); 8 Conclusion and Discussion (8.1 Challenges, 8.2 Future
Directions).

- Logit ✓: §2.1. Feature/relation ✓: §2.2 and §2.3.
- Schemes ✓: §3.1–3.3, §5.2 (multi-teacher) and §5.6 (data-free).
- Teacher reliability ✗:
  - §4 discusses the teacher–student *capacity gap*, not per-sample teacher error.
  - The only reliability-keyword hit is in a reference title.
- MOO in KD ✗: no section on it, and 0 MOO-keyword hits.
- Bench ✓: §6 "Performance Comparison".
- LLM/VLM ✗: §7.2 covers pre-LLM NLP KD, with 0 LLM or CLIP hits.
- 2024–26 ✗: published 2021, and the latest cited year is 2021.

### Wang & Yoon, "Knowledge Distillation and Student-Teacher Learning for Visual Intelligence", TPAMI 2022 (arXiv 2004.05937v7)

Sections:
- 1 Introduction
- 3 A Theoretical Analysis of KD
- 4 KD Based on the Number of Teachers: 4.1 One Teacher (4.1.1 Knowledge from logits, 4.1.2 Knowledge from the
  intermediate layers); 4.2 Multiple Teachers
- 5 Distillation Based on Data Format: 5.1 Data-free; 5.2 Few data samples; 5.3 Cross-modal
- 6: 6.1 Online distillation; 6.2 Teacher-free distillation
- 7: 7.1 Label-required; 7.2 Label-free
- 8 KD with Novel Learning Metrics: 8.1 Adversarial; 8.2 Graph representations; 8.3 Semi-/self-supervised;
  8.4 Few-shot; 8.5 Incremental; 8.6 Reinforcement learning
- 9 Applications for Visual Intelligence
- 10 Discussions
- 11 New Outlooks and Perspectives
- 12 Conclusion

Cells:
- Logit ✓: §4.1.1.
- Feature/relation ✓: §4.1.2 and §8.2.
- Schemes ✓: §4.2, §5.1, §6.1 and §6.2.
- Teacher reliability partial: §4.1.1 discusses methods that "fix the incorrect predictions" of the teacher, and
  §10 discusses whether teacher outputs are reliable. Neither is a dedicated section.
- MOO ✗: 0 MOO-keyword hits.
- Bench ✗: Tables 1–9 are method taxonomies and notation summaries. There is no accuracy comparison.
- LLM/VLM ✗: §5.3 cross-modal KD predates CLIP, and there are 0 LLM or CLIP hits.
- 2024–26 ✗: the latest cited year is 2021.

### Hu et al., "Teacher-Student Architecture for Knowledge Distillation: A Survey", arXiv 2023 (2308.04268v1; preprint)

Sections:
- 2 Purposes: 2.1 Compression; 2.2 Expansion; 2.3 Adaptation; 2.4 Enhancement; 2.5 Comparison
- 3: 3.1 Knowledge Construction (3.1.1 Response-Based, 3.1.2 Intermediate, 3.1.3 Relation-Based); 3.2 Knowledge
  Optimization
- 4: 4.1 Multi-Teacher; 4.3 Federated; 4.4 Cross-Modal
- 5: 5.1 Online; 5.2 Self-Distillation
- 6 Applications
- 7 Future directions: 7.1 Architecture Design; 7.2 Knowledge Quality; 7.3 Theoretical Understandings …

Cells:
- Logit ✓: §3.1.1.
- Feature/relation ✓: §3.1.2 and §3.1.3.
- Schemes ✓: §4.1, §5.1 and §5.2.
- Teacher reliability ✗: §7.2 "Knowledge Quality" is about quantifying the knowledge a teacher encodes, not about
  teacher errors.
- MOO in KD partial: §3.2 "Knowledge Optimization" writes the KD objective as a fixed-weight sum
  λ1·CE + λ2·KL + λ3·L_D (Eq. 14). It uses no Pareto or gradient methods, with 0 MOO-keyword hits.
- Bench ✗: the arXiv main text has no result tables; its comparisons are qualitative (Table 2).
- LLM/VLM ✗: 0 hits.
- 2024–26 ✗: posted 2023.

### Moslemi, Briskina, Dang, Li, "A survey on knowledge distillation: Recent advancements", MLWA 18:100605, 2024

**Full text not read.** ScienceDirect returned HTTP 403 to both curl and WebFetch. OpenAlex lists it as gold open
access, but there is no repository copy. Every cell below comes from the **abstract** (OpenAlex), so this row has
no section numbers.
- Logit ✓ and feature/relation ✓: the abstract says "response-based, feature-based, and relation-based knowledge
  distillation".
- Schemes partial: the abstract names self-distillation, cross-modal and adversarial distillation, and
  limited-data KD. It does not mention online or multi-teacher distillation.
- LLM/VLM partial: "applications across … natural language processing, and multimodal tasks".
- Teacher reliability, MOO, benchmarks and 2024–26 coverage: **?** (not determinable from the abstract).
  Published 12/2024, so it cannot cover 2025–2026.

**RECOMMENDATION:** a team member with institutional access (or a browser) should read the paper's table of
contents and replace the four ? cells before Checkpoint A.

### Xu et al., "A Survey on Knowledge Distillation of Large Language Models", arXiv 2024 (2402.13116v4; preprint)

Sections:
- 2 Overview: 2.1–2.4
- 3 KD Algorithms: 3.1 Knowledge (3.1.1 Labeling, 3.1.2 Expansion, 3.1.3 Data Curation, 3.1.4 Feature,
  3.1.5 Feedback, 3.1.6 Self-Knowledge); 3.2 Distillation (3.2.1 SFT, 3.2.2 Divergence and Similarity,
  3.2.3 Reinforcement Learning, 3.2.4 Ranking Optimization)
- 4 Skill Distillation: … 4.5 Multi-Modality
- 5 Domain-specified Vertical Distillation
- 6 Open Problems
- 7 Conclusion

Cells:
- Logit partial: §3.2.2 covers token-level divergences (forward/reverse KL, MiniLLM, GKD) for LLMs only. It has no
  vision logit methods.
- Feature/relation partial: §3.1.4 "Feature" knowledge, for white-box LLMs only.
- Schemes partial: §3.1.6 covers self-knowledge. Multi-teacher distillation appears only as an open problem (§6).
  There is no online/offline taxonomy.
- Teacher reliability ✗: §6 "Trustworthy Knowledge Distillation" is about truthfulness, safety and privacy of LLM
  outputs, not the reliability of the teacher signal.
- MOO ✗: 0 hits.
- Bench ✗: Tables 1–3 summarise divergences and works. It reports no results.
- LLM/VLM ✓: the whole survey is about LLMs, with §4.5 on multi-modality.
- 2024–26 partial: v4 dates from 10/2024, so it covers up to 2024 (e.g. MiniLLM and GKD at ICLR 2024).

### Mansourian et al., "A Comprehensive Survey on Knowledge Distillation", TMLR 09/2025 (arXiv 2503.12067v2)

Sections:
- 2 Sources: 2.1 Logit-based; 2.2 Feature-based; 2.3 Similarity-based
- 3 Schemes: 3.1 Offline; 3.2 Online; 3.3 Self-distillation
- 4 Algorithms: 4.1 Attention; 4.2 Adversarial (4.2.1 Adversarial Data-Free, 4.2.2 Discriminator in the Loop,
  4.2.3 Adversarial Robust KD); 4.3 Multi-teacher; 4.4 Cross-modal; 4.5 Graph-based; 4.6 Adaptive Distillation
- 5 Modalities
- 6 Applications: 6.1 Distillation in LLMs; 6.2 Foundation Model Distillation (6.2.1 Vision-language Models …);
  6.3–6.5
- 7 Performance Comparison
- 8 Discussion: 8.1–8.4 (8.3 Quantitative Comparison); 8.5 Challenges; 8.6 Future Directions
- 9 Conclusion

Cells:
- Logit ✓: §2.1.
- Feature/relation ✓: §2.2 and §2.3.
- Schemes ✓: §3.1–3.3, §4.3 and §4.2.1.
- Teacher reliability partial:
  - §4.6 addresses teachers that "may produce incorrect outputs" through adaptive losses and per-sample weighting.
  - §4.2.3 covers robust KD, including refining the reliability of teacher predictions.
  - There is no dedicated taxonomy of reliability signals.
- MOO in KD partial: §4.6 lists "adaptive loss weighting". The full text has **0 MOO-keyword hits** (no Pareto,
  MGDA or gradient conflict).
- Bench ✓: §7 and §8.3.
- LLM/VLM ✓: §6.1 and §6.2.1.
- 2024–26 partial:
  - It covers 2024 methods, e.g. logit standardisation (CVPR 2024) and CLIP-KD (CVPR 2024).
  - It cites many works from 2024 and 2025.
  - Nothing after its 09/2025 publication appears: none of the ICCV 2025 or ICLR 2026 methods in our inventory
    (e.g. RLD, DTO-KD) occur in the text.

### Yang et al., "Survey on Knowledge Distillation for Large Language Models: Methods, Evaluation, and Application", ACM TIST 16(6), 2025 (arXiv 2407.01885v1)

Sections:
- 2: 2.1 Logits-based KD; 2.2 Hint-based KD; 2.3 In-Context Learning; 2.4 Chain-of-Thought
- 3: 3.1 White-box KD; 3.2 Robustness Evaluation of White-box KD; 3.3 Discussion; 3.4 Black-box KD; 3.5 Robustness
  Evaluation of Black-box KD; 3.6 Discussion; 3.7 Others
- 4 Applications: 4.1 Healthcare; 4.2 Education; 4.3 Law
- 5 Challenges and Future Directions

Cells:
- Logit partial and feature partial: §2.1 and §2.2 present them as background for LLMs.
- Schemes ✗: the paper is organised by white-box vs black-box access (§3.1 and §3.4). It covers no online,
  self-distillation or multi-teacher schemes.
- Teacher reliability ✗ and MOO ✗: 0 hits.
- Bench partial: the paper runs its own evaluation of KD methods on GPT-2, OPT and LLaMA (Tables 2–4 and 6–8),
  for LLMs only.
- LLM/VLM ✓: LLMs throughout, with multimodal transfer in §3.7.
- 2024–26 partial: arXiv v1 dates from 07/2024. A reference-list search finds only 3 entries dated 2024, one of them a KD method (Kang et al. 2024, knowledge-augmented reasoning distillation), so coverage stops in early 2024.

### Chen et al., "Gradient-Based Multi-Objective Deep Learning: Algorithms, Theories, Applications, and Beyond", TMLR 08/2026 (arXiv 2501.10945v3)

Sections:
- 1 Introduction: 1.1 Comparison with Related Surveys on MOO
- 2 Preliminary MOO: 2.1 Key Concepts; 2.2 Scalarization
- 3 Single Pareto-Optimal Solution: 3.1 Loss Balancing; 3.2 Gradient Balancing; 3.3 Discussions
- 4 Finite Set of Solutions
- 5 Infinite Set of Solutions
- 6 Theories
- 7 Applications: … 7.3 Computer Vision; 7.4 NAS; 7.5 Recommendation; 7.6 LLMs; 7.7 Misc.
- 8 Resources: 8.1 Datasets; 8.2 Libraries

The MOO side is covered in depth (§2–§6). The string "distill" **does not occur** in the PDF text, so every KD
column is ✗, including "MOO in KD". §7.6 applies MOO to LLM alignment and fine-tuning, not to distillation.
The plan calls it "Chen et al. 2025" after its arXiv year; the TMLR bib gives 2026, which is the year used in
Table I.

### This survey

The last row states the coverage **planned** in `tasks/plan.md`. Sections 3–10 are still placeholders, so the
row must be re-checked at Task 16 (final audit).

| Column | Section of this survey |
|---|---|
| Logit | `sec:logit` |
| Feature/relation | `sec:feature` |
| Schemes | `sec:schemes` |
| Teacher reliability | `sec:reliability` |
| MOO in KD | `sec:moo` and `sec:kd_moo` |
| Bench./results | `sec:benchmarks` |
| LLM/VLM | `sec:emerging` |
| 2024–26 methods | the core methods of `docs/survey/sota-inventory.md` (2022–2026, including ICCV 2025 and ICLR 2026) |

## Considered but not added
- **Yang, Yu, An, Xu, "Categories of Response-Based, Feature-Based, and Relation-Based Knowledge Distillation"**
  (arXiv 2306.10687). It is a chapter in a Springer book, not a survey article, and is narrower than Gou et al.
  Not registered.
- **Mansourian et al.'s own Table 1** compares earlier KD surveys and was used as a cross-check for coverage.
  No surveys beyond those above were added from it.

## Fig. 1 (`paper/survey/figures/taxonomy.tex`)
- **Branches:** six section groups, referenced by `\ref` so the numbers follow the manuscript:
  1. What is transferred (`sec:logit`, `sec:feature`)
  2. Distillation schemes
  3. Teacher reliability
  4. KD as multi-objective optimisation (`sec:moo`, `sec:kd_moo`)
  5. Emerging settings
  6. Benchmarks
- **Leaves and methods:** 19 leaves, each with 2–4 methods. Every method is CORE, CORE-A or CORE-P in
  `docs/survey/sota-inventory.md`. The registry ids per leaf are listed in the header comment of the `.tex` file.
- **Marking:** CORE-A and CORE-P methods carry an asterisk: RPKD, CaRE-Div, TPKD, SPOFA, UP-MOPD and DHO.
- **Excluded:** classics (Hinton KD, FitNets, CRD, DML, AE-KD, SCKD …), SUPPORT entries (CHAD, PCD, SCOPE) and the
  withdrawn MoKD.

**Update 2026-11-08 (T15, Codex review M1):** "This survey" LLM/VLM set to partial. After the scope change to image
classification, §VII only points to LLM/VLM distillation work (E2 excludes it from the leaderboard).
