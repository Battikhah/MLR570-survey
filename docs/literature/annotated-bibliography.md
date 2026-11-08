# Annotated bibliography

## auxiliary-learning

- [du2018auxgradsim] Yunshu Du et al., ‘Adapting Auxiliary Losses Using Gradient Similarity,’ , 2018-12-05. Status: preprint. Main-task-anchored gating of auxiliary losses by gradient cosine; asymmetric precedent.

## calibration

- [guo2017calibration] Chuan Guo et al., ‘On Calibration of Modern Neural Networks,’ ICML 2017, PMLR 70, 2017. Status: published. Foundational evidence that modern classifiers can be miscalibrated and that temperature scaling is a post-hoc calibration method. It motivates keeping calibration temperature distinct from KD temperature.

- [ovadia2019shiftuncertainty] Yaniv Ovadia et al., ‘Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift,’ NeurIPS 2019, 2019. Status: published. Large-scale comparison shows uncertainty methods and calibration behavior can change under dataset shift. It bounds claims that in-distribution confidence alone is a reliable gate.

## cifar10

- [cifar10] Alex Krizhevsky et al., ‘The CIFAR-10 dataset,’ University of Toronto dataset page, 2009. Status: published. PCD and FedPCD classification benchmark; 50,000 train and 10,000 test 32x32 color images, 10 classes; cite Krizhevsky's tech report when used.

## cifar100

- [cifar100] Alex Krizhevsky et al., ‘The CIFAR-100 dataset,’ University of Toronto dataset page, 2009. Status: published. PCD pruning and FedPCD classification benchmark; 50,000 train and 10,000 test 32x32 color images, 100 classes; cite Krizhevsky's tech report when used.

## constrained-learning

- [chamon2020pacc] Luiz F. O. Chamon et al., ‘Probably Approximately Correct Constrained Learning,’ , 2020-06-09. Status: unverified. Primal-dual constrained learning theory: the standard alternative to PCD when a secondary must meet a level (constraint) rather than make per-step progress.

- [cotter2019twoplayer] Andrew Cotter et al., ‘Two-Player Games for Efficient Non-Convex Constrained Optimization,’ , 2018-04-17. Status: unverified. Lagrangian/proxy-Lagrangian constrained training for non-convex models (fairness-rate constraints).

- [gallegoposada2025cooper] Jose Gallego-Posada et al., ‘Cooper: A Library for Constrained Optimization in Deep Learning,’ , 2025-04-01. Status: preprint. Lagrangian constrained-optimization baseline/tool; PCD compared against it.

## continual-learning

- [chaudhry2019agem] Arslan Chaudhry et al., ‘Efficient Lifelong Learning with A-GEM,’ ICLR 2019, 2018-12-02. Status: published. Single-constraint (averaged memory gradient) variant of GEM = K=2 projection with τ=0 and no normalization.

- [chaudhry2019tiny] Arslan Chaudhry et al., ‘On Tiny Episodic Memories in Continual Learning,’ , 2019-02-27. Status: unverified. Potential contradicting evidence for projection-based CL: plain experience replay (a weighted sum) as a cheap strong baseline. Must be re-read before citing any result.

- [farajtabar2019ogd] Mehrdad Farajtabar et al., ‘Orthogonal Gradient Descent for Continual Learning,’ , 2019-10-15. Status: unverified. Projection-based continual learning (orthogonal to past-task gradient subspace); related to the CL candidate.

- [hu2020softgem] Guannan Hu et al., ‘Gradient Episodic Memory with a Soft Constraint for Continual Learning,’ arXiv, 2020-11-16. Status: preprint. Closest prior art to PCD-for-continual-learning: GEM plus a normalized positive margin (essentially K=2 PCD with instantaneous normalization).

- [lopezpaz2017gem] David Lopez-Paz et al., ‘Gradient Episodic Memory for Continual Learning,’ NIPS 2017, 2017-06-26. Status: published. Closest prior work for any PCD continual-learning direction: the same minimal-Euclidean-deviation projection of the current-task gradient onto half-spaces defined by memory gradients.

## dataset

- [krizhevsky2009cifar] Alex Krizhevsky, ‘Learning Multiple Layers of Features from Tiny Images,’ Technical report, University of Toronto, 2009. Status: published. Source of the CIFAR-100 dataset, the main small-scale KD benchmark (survey T5, Sec. II).

- [lin2014coco] Tsung-Yi Lin et al., ‘Microsoft COCO: Common Objects in Context,’ ECCV 2014 (LNCS), 2014. Status: published. Reference for MS-COCO, the detection benchmark used to test logit KD beyond classification (survey T5, Sec. II).

- [russakovsky2015imagenet] Olga Russakovsky et al., ‘ImageNet Large Scale Visual Recognition Challenge,’ International Journal of Computer Vision (IJCV), 2015-04-11. Status: published. Reference for ImageNet-1K (ILSVRC-2012), the large-scale KD classification benchmark (survey T5, Sec. II).

## fairness

- [agarwal2018reductions] Alekh Agarwal et al., ‘A Reductions Approach to Fair Classification,’ , 2018-03-06. Status: unverified. Standard fairness-constrained baseline (exponentiated-gradient reduction).

## fashion-mnist

- [fashion_mnist] Han Xiao et al., ‘Fashion-MNIST,’ GitHub / arXiv, 2017. Status: published. FedPCD low-cost federated image classification benchmark; 60,000 train and 10,000 test 28x28 grayscale images, 10 classes.

## federated

- [acar2021feddyn] Durmus Alp Emre Acar et al., ‘Federated Learning Based on Dynamic Regularization,’ ICLR 2021, 2021-11-08. Status: published. Source of the Dirichlet non-IID partition protocol FedPCD follows.

- [hu2022fedmgda] Zeou Hu et al., ‘Federated Learning Meets Multi-objective Optimization,’ IEEE Transactions on Network Science and Engineering (2022), 2020-06-20. Status: published. FedMGDA+: symmetric MOO aggregation; FedPCD's main conceptual foil.

- [karimireddy2020scaffold] Sai Praneeth Karimireddy et al., ‘SCAFFOLD: Stochastic Controlled Averaging for Federated Learning,’ ICML 2020, 2019-10-14. Status: published. Client-drift correction baseline; cited but NOT compared in FedPCD.

- [li2020fedprox] Tian Li et al., ‘Federated Optimization in Heterogeneous Networks,’ MLSys 2020, 2018-12-14. Status: published. FedProx; drift-control baseline NOT included in FedPCD's evaluation.

- [li2020qffl] Tian Li et al., ‘Fair Resource Allocation in Federated Learning,’ ICLR 2020, 2019-05-25. Status: published. q-FFL fairness baseline (in FedPCD).

- [li2021ditto] Tian Li et al., ‘Ditto: Fair and Robust Federated Learning Through Personalization,’ ICML 2021, 2020-12-08. Status: published. Personalization-based fairness baseline (in FedPCD).

- [mcmahan2017fedavg] H. Brendan McMahan et al., ‘Communication-Efficient Learning of Deep Networks from Decentralized Data,’ AISTATS 2017, 2016-02-17. Status: published. FedAvg; FedPCD's primary direction.

- [mohri2019afl] Mehryar Mohri et al., ‘Agnostic Federated Learning,’ , 2019-02-01. Status: unverified. AFL minimax fairness baseline (in FedPCD).

- [wang2020fednova] Jianyu Wang et al., ‘Tackling the Objective Inconsistency Problem in Heterogeneous Federated Optimization,’ , 2020-07-15. Status: unverified. FedNova normalized averaging; relevant because FedPCD also normalizes client directions — a normalization-only control.

- [wang2021fedfv] Zheng Wang et al., ‘Federated Learning with Fair Averaging,’ IJCAI 2021, 2021-04-30. Status: published. FedFV: PCGrad-style projection of conflicting client gradients with history; strongest CIFAR-10 competitor in FedPCD.

## fedpcd

- [irshaid2026fedpcdcode] Yousef Irshaid et al., ‘FedPCD code (not released as of 2026-11-02),’ GitHub project page, 2026. Status: unverified. The authors' project repository documents that FedPCD implementation is not publicly released; there is no source code license or implementation to reproduce at this date.

## gradient-conflict

- [liu2021cagrad] Bo Liu et al., ‘Conflict-Averse Gradient Descent for Multi-task Learning,’ NeurIPS 2021, 2021-10-26. Status: published. CAGrad baseline; average-anchored, worst-case-improving direction.

- [yu2020pcgrad] Tianhe Yu et al., ‘Gradient Surgery for Multi-Task Learning,’ NeurIPS 2020, 2020-01-19. Status: published. PCGrad; symmetric projection baseline used by PCD and the KD proposal.

## kd

- [agarwal2024gkd] Rishabh Agarwal et al., ‘On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes,’ ICLR 2024, 2023-06-23. Status: published. GKD: trains the student on its own samples with teacher feedback under a chosen divergence (generalised JSD); the reference on-policy LLM-KD method.

- [askin2026fedrevive] Baris Askin et al., ‘Reviving Stale Updates: Data-Free Knowledge Distillation for Asynchronous Federated Learning,’ NeurIPS 2026, 2025-11-01. Status: accepted. FedRevive: server-side data-free KD refreshes stale client updates in asynchronous FL.

- [bassam2025pld] Ejafa Bassam et al., ‘PLD: A Choice-Theoretic List-Wise Knowledge Distillation,’ NeurIPS 2025, 2025. Status: published. Logit KD as a Plackett-Luce list-wise ranking loss (true label first, then teacher-ordered classes); a convex, translation-invariant surrogate that subsumes weighted cross-entropy and removes the separate KD weight.

- [beyer2022patientkd] Lucas Beyer et al., ‘Knowledge Distillation: A Good Teacher Is Patient and Consistent,’ CVPR 2022, 2022. Status: published. Demonstrates that distillation outcomes depend strongly on long training and consistent teacher/student image views. It underscores the need to hold recipes fixed when comparing optimization rules.

- [chen2021reviewkd] Pengguang Chen et al., ‘Distilling Knowledge via Knowledge Review,’ CVPR 2021, 2021. Status: published. CLASSIC/lineage: cross-stage feature review; the reference feature baseline in 2022-2025 tables.

- [chen2022simkd] Defang Chen et al., ‘Knowledge Distillation with the Reused Teacher Classifier,’ CVPR 2022, 2022-03-26. Status: published. SimKD: aligns the penultimate feature through a projector and reuses the frozen teacher classifier at inference; strong feature baseline but adds projector cost.

- [chen2026scope] Tao Chen et al., ‘Selective Confidence-Guided Projection-Based Encoding for Medical Image Classification,’ Journal of Imaging, 2026-09-11. Status: published. Classification-priority gradient-conflict removal for KD plus confidence-weighted relations: very close to the KD proposal.

- [cho2019efficacy] Jang Hyun Cho et al., ‘On the Efficacy of Knowledge Distillation,’ ICCV 2019, 2019. Status: published. Classic empirical analysis showing teacher accuracy alone does not predict distillation utility and that teacher-student capacity mismatch can limit transfer. It anchors discussion of teacher-student compatibility.

- [dong2025mooadv] Junhao Dong et al., ‘Confound from All Sides, Distill with Resilience: Multi-Objective Adversarial Paths to Zero-Shot Robustness,’ ICCV 2025, 2025. Status: published. Uses multi-objective optimisation to generate diverse targeted adversaries (one per preference vector) for robust distillation from VLMs to small models; MOO used for data generation, not loss balancing.

- [du2020aekd] Shangchen Du et al., ‘Agree to Disagree: Adaptive Ensemble Knowledge Distillation in Gradient Space,’ NeurIPS 2020, 2020. Status: published. Multi-teacher KD as MGDA with a disagreement tolerance: the earliest symmetric MOO formulation of KD (CLASSIC lineage for the KD x MOO section).

- [etcibasi2026rpkd] Hamza Etcibasi et al., ‘You Don't Need Aligned Representations: Knowledge Distillation via Random Prototype Spaces,’ NeurIPS 2026, 2026-10-27. Status: accepted. RPKD: distils by matching teacher and student similarity distributions over a shared set of random prototypes, so representations need not be aligned; newest cross-architecture method found.

- [furlanello2018bornagain] Tommaso Furlanello et al., ‘Born Again Neural Networks,’ ICML 2018, 2018. Status: published. CLASSIC: sequential same-architecture student training from a previous model's soft outputs.

- [goldblum2020ard] Micah Goldblum et al., ‘Adversarially Robust Distillation,’ AAAI 2020, 2019-05-23. Status: published. CLASSIC: first adversarially robust distillation (ARD).

- [gou2021kdsurvey] Jianping Gou et al., ‘Knowledge Distillation: A Survey,’ International Journal of Computer Vision (IJCV), 129(6):1789-1819, 2021-03-22. Status: published. The most-cited general KD survey (knowledge types, schemes, algorithms, performance comparison); row of Table I. Pre-2021 coverage only.

- [gu2024minillm] Yuxian Gu et al., ‘MiniLLM: On-Policy Distillation of Large Language Models,’ ICLR 2024, 2023-06-14. Status: published. MiniLLM: reverse-KL objective optimised with policy gradient on student-generated text (on-policy), avoiding the mode-covering of forward KL for generative LMs.

- [guo2023catkd] Ziyao Guo et al., ‘Class Attention Transfer Based Knowledge Distillation,’ CVPR 2023, 2023-04-25. Status: published. CAT-KD: transfers class activation maps (class attention) rather than raw features; links interpretability and distillation.

- [hao2023ofakd] Zhiwei Hao et al., ‘One-for-All: Bridge the Gap Between Heterogeneous Architectures in Knowledge Distillation,’ NeurIPS 2023, 2023-10-30. Status: published. OFA-KD: projects intermediate features of heterogeneous students into the logit space and adaptively enhances target-class information; reference method for cross-architecture KD.

- [hayder2025mokd] Zeeshan Hayder et al., ‘MoKD: Multi-Task Optimization for Knowledge Distillation,’ , 2025-05-13. Status: preprint. Framed KD as multi-objective optimisation against gradient conflict and dominance; withdrawn. INTERPRETATION: likely superseded by DTO-KD (hayder2026dtokd; same first four authors plus Richard Hartley, matching the withdrawal note 'major changes to the paper and the authorship'). Cite DTO-KD, not MoKD.

- [hayder2026dtokd] Zeeshan Hayder et al., ‘DTO-KD: Dynamic Trade-off Optimization for Effective Knowledge Distillation,’ ICLR 2026, 2026. Status: published. Direct optimizer-side KD comparator. FAMO-style (Liu et al. 2023) min-norm convex combination of grad log L_distill and grad log L_task with closed-form weights pi* (Eqs. 11-12); equal contribution to both losses (Cor. 3.3), i.e. SYMMETRIC, versus PCD's fixed priority. Amortized variant avoids the second backprop (Eq. 18). CIFAR-100 ResNet32x4->ResNet8x4: 76.40 (Table 2; that table lists DKD 75.44 vs 76.32 in mdistiller -- cross-paper numbers differ). Same first four authors as the withdrawn MoKD (hayder2025mokd).

- [hinton2015kd] Geoffrey Hinton et al., ‘Distilling the Knowledge in a Neural Network,’ NIPS 2014 Deep Learning Workshop, 2015-03-09. Status: published. Standard KD loss used as the secondary in the current proposal.

- [hossain2025luminet] Md. Ismail Hossain et al., ‘LumiNet: Perception-Driven Knowledge Distillation via Statistical Logit Calibration,’ TMLR (August 2025), 2023-10-05. Status: published. LumiNet: recalibrates each logit against intra-batch class statistics ('perception') before distillation; logit-only method competitive with feature KD.

- [hu2023tsasurvey] Chengming Hu et al., ‘Teacher-Student Architecture for Knowledge Distillation: A Survey,’ arXiv, 2023-08-08. Status: preprint. 2023 KD survey organised by teacher-student architecture and purpose (compression, expansion, adaptation, enhancement); extra row of Table I.

- [hu2024tgeokd] Chengming Hu et al., ‘Less or More From Teacher: Exploiting Trilateral Geometry For Knowledge Distillation,’ ICLR 2024, 2023-12-22. Status: published. TGeo-KD: learns a per-sample fusion ratio between teacher and ground-truth supervision from the student-teacher-label geometry; principled 'how much to trust the teacher'.

- [huang2022dist] Tao Huang et al., ‘Knowledge Distillation from A Stronger Teacher,’ NeurIPS 2022, 2022-05-21. Status: published. DIST: replaces exact KL matching with Pearson-correlation (inter- and intra-class relation) matching so a much stronger teacher still helps; core logit/relation method.

- [huang2023adaad] Bo Huang et al., ‘Boosting Accuracy and Robustness of Student Models via Adaptive Adversarial Distillation,’ CVPR 2023, 2023. Status: published. AdaAD: the teacher adaptively searches for inner-max adversarial examples where student and teacher disagree most, within a min-max distillation game.

- [huang2023diffkd] Tao Huang et al., ‘Knowledge Diffusion for Distillation,’ NeurIPS 2023, 2023-05-25. Status: published. DiffKD: treats student features as noisy teacher features and denoises them with a lightweight diffusion model before matching; also detection/segmentation.

- [huang2025deepkd] Haiduo Huang et al., ‘DeepKD: A Deeply Decoupled and Denoised Knowledge Distillation Trainer,’ NeurIPS 2025, 2025. Status: published. Optimizer-side KD trainer: separate momentum updaters for the task, target-class and non-target-class gradients (extending DOT) with GSNR-guided momentum, plus a dynamic top-k denoising mask. Belongs in the KD x MOO section next to DOT and DTO-KD.

- [jang2025fedgo] Won-Jun Jang et al., ‘Provably Near-Optimal Federated Ensemble Distillation with Negligible Overhead,’ ICML 2025, 2025-02-10. Status: published. FedGO: weights client logits with GAN-discriminator-based per-sample estimates, with a near-optimality guarantee for federated ensemble distillation.

- [jang2025vl2lite] Jinseong Jang et al., ‘VL2Lite: Task-Specific Knowledge Distillation from Large Vision-Language Models to Lightweight Networks,’ CVPR 2025, 2025. Status: published. VL2Lite: distils VLM (CLIP-like) visual and text-aligned knowledge into lightweight CNN classifiers during training only.

- [jeong2025selfdistill] Hyeonsu Jeong et al., ‘Rethinking Self-Distillation: Label Averaging and Enhanced Soft Label Refinement with Partial Labels,’ ICLR 2025, 2024-02-16. Status: published. Theory of why self-distillation helps: multi-round SD acts as label averaging among correlated samples; proposes one-round partial-label refinement. Use for the 'why' of self-KD, not as a benchmark method.

- [jin2023mlkd] Ying Jin et al., ‘Multi-Level Logit Distillation,’ CVPR 2023, 2023. Status: published. MLKD: aligns predictions at instance, batch and class level with multiple temperatures and strong augmentation; frequent strong logit baseline (LSKD builds on it).

- [jung2024peeraid] Jaewon Jung et al., ‘PeerAiD: Improving Adversarial Distillation from a Specialized Peer Tutor,’ CVPR 2024, 2024-03-11. Status: published. PeerAiD: a peer network trained on the student's adversarial examples serves as tutor, instead of a fixed robust teacher.

- [kang2025dho] Seongjae Kang et al., ‘Simple yet Effective Semi-supervised Knowledge Distillation from Vision-Language Models via Dual-Head Optimization,’ NeurIPS 2026, 2025-05-12. Status: accepted. Only source found with MEASURED CE–KD gradient cosine: single-head CE+KD baseline final-epoch cos(∇CE, ∇KD) ≈ −0.39 to −0.45 across ResNet-18 stages and −0.76 at the classifier head (8-dataset mean, 16-shot, CLIP RN50 zero-shot teacher). Prop. 1 proves head-level conflict whenever the student prediction lies in the ball with diameter [y, p].

- [kenfack2025agrekd] Patrik Kenfack et al., ‘Adaptive Group Robust Ensemble Knowledge Distillation,’ TMLR (11/2025), 2024-11-22. Status: published. AGRE-KD: selects/weights ensemble teachers by gradient direction relative to a biased model so the student inherits worst-group robustness; teacher selection under spurious correlation.

- [khan2024hydrafl] Momin Ahmad Khan et al., ‘HYDRA-FL: Hybrid Knowledge Distillation for Robust and Accurate Federated Learning,’ NeurIPS 2024, 2024-09-30. Status: published. Shows KD-based FL amplifies poisoning; adds shallow-layer distillation to keep KD benefits without amplifying attacks. Robust x federated KD.

- [kim2026ltkd] Seonghak Kim, ‘Distilling Balanced Knowledge from a Biased Teacher,’ CVPR 2026, 2026. Status: published. Long-tailed KD (LTKD): decomposes the KL objective into cross-group and within-group terms, rebalancing the first and reweighting the second so tail classes are not dominated by a head-biased teacher; reliability under class imbalance.

- [ko2024distillm] Jongwoo Ko et al., ‘DistiLLM: Towards Streamlined Distillation for Large Language Models,’ ICML 2024, 2024-02-06. Status: published. DistiLLM: skew KL divergence plus an adaptive off-policy replay of student-generated outputs; efficient alternative to fully on-policy KD.

- [ko2025distillm2] Jongwoo Ko et al., ‘DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs,’ ICML 2025 (Spotlight per arXiv comment), 2025-03-10. Status: published. DistiLLM-2: contrastive objective that raises likelihood of teacher responses and lowers that of student responses, with curriculum on the skew parameter.

- [lan2025labelrevision] Weichao Lan et al., ‘Improve Knowledge Distillation via Label Revision and Data Selection,’ IEEE Transactions on Cognitive and Developmental Systems, 2025-04-11. Status: published. Combines teacher-label revision with sample selection to reduce harmful supervision. It is a repair-and-select alternative to hard rejection of unreliable teacher outputs.

- [lee2022hardgatekd] Dongkyu Lee et al., ‘Hard Gate Knowledge Distillation - Leverage Calibration for Robust and Reliable Language Model,’ EMNLP 2022, 2022. Status: published. Applies a hard gate based on calibration to select between teacher guidance and ground-truth training in language-model distillation. It is a selective-transfer method and a calibration-based comparator.

- [lee2025igdm] Hongsin Lee et al., ‘Indirect Gradient Matching for Adversarial Robust Distillation,’ ICLR 2025, 2023-12-06. Status: published. IGDM: matches the student's input gradients to the teacher's indirectly via output differences on perturbed inputs; plug-in for adversarial distillation.

- [lee2025saad] Hongsin Lee et al., ‘Sample-wise Adaptive Weighting for Transfer Consistency in Adversarial Distillation,’ TMLR, 2025-12-11. Status: published. SAAD: robust teachers do not always transfer robustness; re-weights samples by 'transfer consistency' between teacher and student adversarial behaviour.

- [lee2026robustteachers] Hongsin Lee et al., ‘Toward Understanding Adversarial Distillation: Why Robust Teachers Fail,’ ICML 2026 (PMLR 306), 2026-05-21. Status: published. Analysis of when stronger robust teachers fail to produce robust students; CONTRADICTING-EVIDENCE source for 'better teacher = better robust student'.

- [li2022ats] Xin-Chun Li et al., ‘Asymmetric Temperature Scaling Makes Larger Networks Teach Well Again,’ NeurIPS 2022, 2022-10-10. Status: published. ATS: different temperatures for the target and non-target classes restore the discriminability of a large teacher's wrong-class logits; explains the capacity gap.

- [li2023ctkd] Zheng Li et al., ‘Curriculum Temperature for Knowledge Distillation,’ AAAI 2023, 2022-11-29. Status: published. CTKD: learnable, adversarially scheduled (easy-to-hard curriculum) temperature; plug-in for KD/DKD/CRD; small but consistent gains.

- [li2024promptkd] Zheng Li et al., ‘PromptKD: Unsupervised Prompt Distillation for Vision-Language Models,’ CVPR 2024, 2024-03-05. Status: published. PromptKD: a large CLIP teacher with learned prompts distils into a lightweight student via unlabeled images; the teacher's text features are pre-stored and shared.

- [lin2020feddf] Tao Lin et al., ‘Ensemble Distillation for Robust Model Fusion in Federated Learning,’ NeurIPS 2020, 2020. Status: published. CLASSIC: FedDF, server-side ensemble distillation in FL.

- [liu2023fcfd] Dongyang Liu et al., ‘Function-Consistent Feature Distillation,’ ICLR 2023, 2023-04-24. Status: published. FCFD: makes student features functionally consistent with the teacher by passing them through the teacher's later layers (and vice versa).

- [liu2023norm] Xiaolong Liu et al., ‘NORM: Knowledge Distillation via N-to-One Representation Matching,’ ICLR 2023, 2023-05-23. Status: published. NORM: expands the student feature N-fold with a linear transform and matches each slice to the teacher feature (N-to-one); no inference overhead after merging.

- [liu2024ssdkd] He Liu et al., ‘Small Scale Data-Free Knowledge Distillation,’ CVPR 2024, 2024-06-12. Status: published. SSD-KD: data-free KD with a small synthetic set chosen by difficulty/diversity-aware priority sampling; targets training efficiency.

- [lu2025ciard] Liming Lu et al., ‘CIARD: Cyclic Iterative Adversarial Robustness Distillation,’ ICCV 2025, 2025-09-16. Status: published. Attributes clean-accuracy loss in robust distillation to divergent clean/robust teacher objectives; robust-KD comparator for idea I2.

- [luo2023dfrd] Kangyang Luo et al., ‘DFRD: Data-Free Robustness Distillation for Heterogeneous Federated Learning,’ NeurIPS 2023, 2023-09-24. Status: published. DFRD: server-side data-free distillation with a conditional generator and EMA of the global model to resist heterogeneity-induced forgetting.

- [lv2024wkd] Jiaming Lv et al., ‘Wasserstein Distance Rivals Kullback-Leibler Divergence for Knowledge Distillation,’ NeurIPS 2024, 2024-12-11. Status: published. WKD: Wasserstein distance replaces KL, using cross-category relations (WKD-L, logits) and Gaussian feature distributions (WKD-F, features).

- [mansourian2025kdsurvey] Amir M. Mansourian et al., ‘A Comprehensive Survey on Knowledge Distillation,’ Transactions on Machine Learning Research (TMLR), 2025-09. Status: published. Closest and most recent general KD survey (sources, schemes, algorithms, modalities, LLM/foundation-model KD, performance comparison); row of Table I and the main survey this one must differentiate from.

- [meng2019conditionalts] Zhong Meng et al., ‘Conditional Teacher-Student Learning,’ ICASSP 2019, 2019. Status: published. Early correctness-conditioned teacher-student scheme that chooses teacher guidance only when its prediction matches the label. It is a direct antecedent for selective transfer by correctness.

- [miles2024projector] Roy Miles et al., ‘Understanding the Role of the Projector in Knowledge Distillation,’ AAAI 2024, 2023-03-20. Status: published. Shows that a projector, normalisation and a simple LogSum feature loss suffice; analyses the projector as encoding relational gradients.

- [miles2024vkd] Roy Miles et al., ‘VkD: Improving Knowledge Distillation using Orthogonal Projections,’ CVPR 2024, 2024-03-10. Status: published. VkD: orthogonal projector plus task-specific normalisation for feature KD; argues CIFAR-100 KD gains are saturated and partly regularisation.

- [mirzadeh2020takd] Seyed-Iman Mirzadeh et al., ‘Improved Knowledge Distillation via Teacher Assistant,’ AAAI 2020 (per arXiv comment), 2019-02-09. Status: accepted. CLASSIC: teacher-assistant chain for the capacity gap.

- [mishra2021cckd] Sourav Mishra et al., ‘Confidence Conditioned Knowledge Distillation,’ arXiv, 2021-07-06. Status: preprint. Uses teacher probability assigned to the ground-truth class to condition sample-specific distillation, distinguishing correctness-aware confidence from maximum softmax confidence.

- [moslemi2024kdsurvey] Amir Moslemi et al., ‘A survey on knowledge distillation: Recent advancements,’ Machine Learning with Applications, 18:100605, 2024-12. Status: published. 2024 general KD survey (response/feature/relation KD, self-/cross-modal/adversarial distillation, limited-data and privacy-preserving KD); row of Table I.

- [park2019rkd] Wonpyo Park et al., ‘Relational Knowledge Distillation,’ CVPR 2019, 2019. Status: published. CLASSIC: transfers distance and angle relations among samples; origin of relation-based KD.

- [qian2022switokd] Biao Qian et al., ‘Switchable Online Knowledge Distillation,’ ECCV 2022, 2022-09-12. Status: published. SwitOKD: switches the teacher between 'expert' (paused) and 'learning' modes via an adaptive gap threshold so the online teacher does not outrun the student.

- [qian2025aid] Chengyao Qian et al., ‘A Good Teacher Adapts Their Knowledge for Distillation,’ ICCV 2025, 2025. Status: published. AID: attributes the capacity gap to mismatched intra-class output distributions and fine-tunes the teacher to adapt them before distillation.

- [qiu2023dpk] Zengyu Qiu et al., ‘Better Teacher Better Student: Dynamic Prior Knowledge for Knowledge Distillation,’ ICLR 2023, 2022-06-13. Status: published. DPK: feeds part of the teacher's features to the student as dynamic prior knowledge (masked feature mixing) so larger teachers yield better students.

- [romero2015fitnets] Adriana Romero et al., ‘FitNets: Hints for Thin Deep Nets,’ ICLR 2015, 2014-12-19. Status: published. CLASSIC: origin of feature-based KD (intermediate 'hints' with a learned regressor).

- [sengupta2026casd] Ayan Sengupta et al., ‘Distilling What Matters: Confidence-Aware Selective Distillation for Large Language Models,’ NeurIPS 2026, 2026-09-29. Status: accepted. Confidence-aware selective distillation for LLMs (CaRE-Divergence plus a 'Revival' step): distil where the teacher is confident and correct; recent selective-transfer method beyond vision.

- [shen2022dlb] Yiqing Shen et al., ‘Self-Distillation from the Last Mini-Batch for Consistency Regularization,’ CVPR 2022, 2022-03-30. Status: published. DLB: teacher-free self-distillation that reuses the previous mini-batch's soft predictions on overlapping samples as targets; no extra network.

- [shin2026amid] Donghyeok Shin et al., ‘AMiD: Knowledge Distillation for LLMs with {\ensuremath{\alpha}}-mixture Assistant Distribution,’ ICLR 2026, 2025-10-13. Status: published. AMiD: generalises teacher-student 'assistant' (interpolated) distributions with an alpha-mixture family and divergence; latest assistant-distribution LLM-KD method.

- [shing2025taid] Makoto Shing et al., ‘TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models,’ ICLR 2025 (Spotlight per arXiv comment), 2025-01-28. Status: published. TAID: interpolates the target from student to teacher over training with an adaptive schedule; addresses the capacity gap and mode collapse in LLM KD.

- [stanton2021kdwork] Samuel Stanton et al., ‘Does Knowledge Distillation Really Work?,’ NeurIPS 2021, 2021. Status: published. Separates student-teacher fidelity from generalization and reports that closer imitation does not always improve generalization. It cautions against using KD loss as a proxy for student utility.

- [su2025eakd] Chi-Ping Su et al., ‘EA-KD: Entropy-based Adaptive Knowledge Distillation,’ ICCV 2025, 2023-11-22. Status: published. EA-KD: re-weights each sample's distillation loss by teacher and student entropy so valuable, high-entropy samples get more weight; plug-in for logit and feature KD.

- [sumit2026chad] Dipto Sumit et al., ‘When Does Knowledge Distillation Hurt? Reliability-Aware Distillation for Low-Resource Language Summarization,’ arXiv, 2026-07-22. Status: preprint. Reliability-aware KD reporting that teacher-confidence-only gates offered little benefit (per survey draft).

- [sun2024lskd] Shangquan Sun et al., ‘Logit Standardization in Knowledge Distillation,’ CVPR 2024 (Highlight), 2024-03-03. Status: published. Loss-side state of the art; standardisation also addresses logit scale, overlapping PCD's scale-invariance argument. Supplies MLKD+LS 78.28 (ResNet32x4->ResNet8x4) as the reference ceiling.

- [sun2025rld] Wujie Sun et al., ‘Knowledge Distillation with Refined Logits,’ ICCV 2025, 2024-08-14. Status: published. Refines teacher logits with label information so wrong teacher predictions do not make KD and CE inconsistent while class correlations are kept; state-of-the-art logit and reliability method.

- [tian2020crd] Yonglong Tian et al., ‘Contrastive Representation Distillation,’ ICLR 2020 (per arXiv comment), 2019-10-23. Status: accepted. CLASSIC: contrastive feature distillation; its RepDistiller codebase defines the CIFAR-100 protocol most later papers use.

- [tran2024nayer] Minh-Tuan Tran et al., ‘NAYER: Noisy Layer Data Generation for Efficient and Effective Data-free Knowledge Distillation,’ CVPR 2024, 2023-09-30. Status: published. NAYER: moves randomness from the generator input to a noisy layer and uses label-text embeddings as input, speeding up data-free KD while improving accuracy.

- [wang2022kdreview] Lin Wang et al., ‘Knowledge Distillation and Student-Teacher Learning for Visual Intelligence: A Review and New Outlooks,’ IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), 44(6):3048-3068, 2022-06-01. Status: published. TPAMI review of KD / student-teacher learning for vision, organised by number of teachers, data format and learning setting; row of Table I.

- [wang2025abkd] Guanghui Wang et al., ‘ABKD: Pursuing a Proper Allocation of the Probability Mass in Knowledge Distillation via α-β-Divergence,’ ICML 2025 (Spotlight per arXiv comment), 2025-05-07. Status: published. ABKD: alpha-beta divergence family that interpolates forward and reverse KL to balance 'hardness concentration' and 'confidence concentration'; applies to LLM and vision KD.

- [wei2024sdd] Shicai Wei et al., ‘Scale Decoupled Distillation,’ CVPR 2024, 2024-03-20. Status: published. SDD: multi-scale pooling of logits decouples global logits into local, scale-specific ones (consistent vs complementary terms); plug-in for KD/DKD/NKD.

- [wu2023tinyclip] Kan Wu et al., ‘TinyCLIP: CLIP Distillation via Affinity Mimicking and Weight Inheritance,’ ICCV 2023, 2023-09-21. Status: published. TinyCLIP: cross-modal affinity mimicking plus weight inheritance from the teacher for compact CLIP models.

- [xiang2025ekd] Liangyu Xiang et al., ‘Evidential Knowledge Distillation,’ ICCV 2025, 2025. Status: published. EKD: models the categorical prediction as a random variable (evidential second-order Dirichlet) and distils both its expectation and the distribution; claims a risk upper bound.

- [xu2024llmkdsurvey] Xiaohan Xu et al., ‘A Survey on Knowledge Distillation of Large Language Models,’ arXiv, 2024-02-20. Status: preprint. Main survey of LLM distillation (knowledge elicitation, distillation algorithms, skill and domain distillation); row of Table I.

- [xu2025ldrld] Liuchi Xu et al., ‘Local Dense Logit Relations for Enhanced Knowledge Distillation,’ ICCV 2025, 2025-07-21. Status: published. LDRLD: recursively decouples logits into local class pairs and distils their dense relations, with adaptive decay weights for key pairs; 2025 logit state of the art.

- [yang2023lmcl] Chuanguang Yang et al., ‘Online Knowledge Distillation via Mutual Contrastive Learning for Visual Recognition,’ IEEE TPAMI 2023, 2022-07-23. Status: published. L-MCL: online/mutual KD with mutual contrastive learning between peers' embeddings plus layer-wise meta-optimised transfer.

- [yang2023nkd] Zhendong Yang et al., ‘From Knowledge Distillation to Self-Knowledge Distillation: A Unified Approach with Normalized Loss and Customized Soft Labels,’ ICCV 2023, 2023-03-23. Status: published. NKD normalises the non-target logit distribution; USKD builds customised soft labels for teacher-free self-KD. Bridges logit KD and self-distillation.

- [yang2024clipkd] Chuanguang Yang et al., ‘CLIP-KD: An Empirical Study of CLIP Model Distillation,’ CVPR 2024, 2023-07-24. Status: published. Systematic study of CLIP-to-CLIP distillation objectives; finds simple feature mimicry (MSE) works surprisingly well.

- [yang2025llmkdsurvey] Chuanpeng Yang et al., ‘Survey on Knowledge Distillation for Large Language Models: Methods, Evaluation, and Application,’ ACM Transactions on Intelligent Systems and Technology (TIST), 16(6):1-27, 2025-11-24. Status: published. LLM-KD survey with its own evaluation of white-box and black-box KD on GPT-2/OPT/LLaMA; extra row of Table I.

- [yang2025mtkdrl] Chuanguang Yang et al., ‘Multi-Teacher Knowledge Distillation with Reinforcement Learning for Visual Recognition,’ AAAI 2025, 2025-02-22. Status: published. MTKD-RL: an RL agent assigns per-sample teacher weights from teacher performance and teacher-student gaps; strongest recent multi-teacher weighting baseline.

- [yang2026spofa] Wuming Yang et al., ‘Heterogeneous Knowledge Distillation via Geometry Decoupling and Momentum-Aware Gradient Regulation,’ , 2026-06-23. Status: under-review. MEMA: EMA-baseline test of task-vs-distillation gradient conflict that penalises harmful distillation signals (task-first, opposite of PCD's guaranteed KD progress); closest 2026 optimizer-side neighbour.

- [yin2020deepinversion] Hongxu Yin et al., ‘Dreaming to Distill: Data-free Knowledge Transfer via DeepInversion,’ CVPR 2020, 2020. Status: published. CLASSIC: data-free KD by inverting BatchNorm statistics.

- [yuan2020labelkd] Li Yuan et al., ‘Revisiting Knowledge Distillation via Label Smoothing Regularization,’ CVPR 2020, 2020. Status: published. Shows that weak teachers can still help and analyzes KD as learned label smoothing, including teacher-free KD. It provides a counterexample to equating teacher weakness with useless supervision.

- [yuan2026tpkd] Qianfeng Yuan et al., ‘Learning Beyond Full Imitation: Task-Preserving Knowledge Distillation,’ arXiv, 2026-09-30. Status: preprint. Asymmetric KD that projects teacher directions to protect task margins: close to PCD-KD.

- [zagoruyko2017at] Sergey Zagoruyko et al., ‘Paying More Attention to Attention: Improving the Performance of Convolutional Neural Networks via Attention Transfer,’ ICLR 2017, 2017. Status: published. CLASSIC: attention-map transfer.

- [zhang2018dml] Ying Zhang et al., ‘Deep Mutual Learning,’ CVPR 2018, 2018. Status: published. CLASSIC: online mutual learning between peers.

- [zhang2019byot] Linfeng Zhang et al., ‘Be Your Own Teacher: Improve the Performance of Convolutional Neural Networks via Self Distillation,’ ICCV 2019, 2019. Status: published. CLASSIC: self-distillation from deep to shallow sections of one network.

- [zhang2022camkd] Hailin Zhang et al., ‘Confidence-Aware Multi-Teacher Knowledge Distillation,’ ICASSP 2022, 2021-12-30. Status: accepted. Assigns sample-wise reliability to multiple teachers using ground-truth labels and intermediate features. It extends reliability-aware selection to multi-teacher KD.

- [zhang2025rsd] Weijia Zhang et al., ‘Cross-Architecture Distillation Made Simple with Redundancy Suppression,’ ICCV 2025, 2025. Status: published. RSD: cross-architecture KD as redundancy suppression (invariance maximisation + feature decorrelation) with a lightweight decoupling module; simpler alternative to OFA.

- [zhang2025vrm] Weijia Zhang et al., ‘VRM: Knowledge Distillation via Virtual Relation Matching,’ ICCV 2025 (Highlight per arXiv comment), 2025-02-28. Status: published. VRM: builds affinity graphs over real and virtually augmented samples and matches inter-sample/inter-class relations, pruning unreliable edges; strongest CIFAR-100 relation result found.

- [zhao2022dkd] Borui Zhao et al., ‘Decoupled Knowledge Distillation,’ CVPR 2022, 2022. Status: published. Splits KD into TCKD and NCKD with hand-set weights alpha/beta; natural K=3 test case for PCD (CE | TCKD, NCKD) and a loss-side state-of-the-art baseline.

- [zhao2023dot] Borui Zhao et al., ‘DOT: A Distillation-Oriented Trainer,’ ICCV 2023, 2023-07-17. Status: published. Closest optimizer-side state of the art for the task-vs-distillation trade-off (separate, larger momentum for the KD gradient); mandatory baseline for PCD-in-KD.

- [zheng2024wttm] Kaixiang Zheng et al., ‘Knowledge Distillation Based on Transformed Teacher Matching,’ ICLR 2024, 2024-02-17. Status: published. TTM drops temperature from the student side (power-transformed teacher only), interpreted as an extra Renyi-entropy regulariser; WTTM adds sample-adaptive weights.

- [zhou2025tcs] Junjie Zhou et al., ‘All You Need in Knowledge Distillation Is a Tailored Coordinate System,’ AAAI 2025, 2024-12-12. Status: published. TCS: extracts a PCA coordinate system from a (possibly self-supervised) teacher in one forward pass and aligns student features to it; teacher-agnostic, cheap, few-shot capable.

- [zhu2021fedgen] Zhuangdi Zhu et al., ‘Data-Free Knowledge Distillation for Heterogeneous Federated Learning,’ ICML 2021 (PMLR 139), 2021-05-20. Status: published. CLASSIC: FedGen, data-free generator-based KD for heterogeneous FL.

- [zhu2021sckd] Yichen Zhu et al., ‘Student Customized Knowledge Distillation: Bridging the Gap Between Student and Teacher,’ ICCV 2021, 2021-10. Status: published. Supervised-primary gradient-similarity gating of KD terms: closest KD precedent for asymmetric KD.

- [zhu2026upmopd] Taojie Zhu et al., ‘UP-MOPD: Update Projection in Multi-Teacher On-Policy Distillation,’ , 2026-10-06. Status: preprint. Projects per-teacher updates to remove conflicting directions in multi-teacher on-policy LLM distillation; PCGrad-style gradient projection applied to KD (2026 preprint).

- [zi2021rslad] Bojia Zi et al., ‘Revisiting Adversarial Robustness Distillation: Robust Soft Labels Make Student Better,’ ICCV 2021, 2021. Status: published. CLASSIC/lineage: RSLAD, robust soft labels from a robust teacher; the standard robust-KD baseline.

## lexicographic

- [gong2021dbgd] Chengyue Gong et al., ‘Automatic and Harmless Regularization with Constrained and Lexicographic Optimization: A Dynamic Barrier Approach,’ NeurIPS 2021, 2021-12-06. Status: published. Direct ancestor: for K=2 the PCD QP coincides with the DBGD update (raw gradients); DBGD has convergence proofs for constrained/lexicographic settings that PCD lacks.

- [skalse2022lmorl] Joar Skalse et al., ‘Lexicographic Multi-Objective Reinforcement Learning,’ IJCAI 2022, 2022. Status: published. Lexicographic (strict priority) optimization in learning; contrasts with PCD's soft τ-priority.

## moo

- [chen2026gradmoo] Weiyu Chen et al., ‘Gradient-Based Multi-Objective Deep Learning: Algorithms, Theories, Applications, and Beyond,’ Transactions on Machine Learning Research (TMLR), 2026-08. Status: published. Survey of gradient-based MOO for deep learning (MGDA-style gradient balancing, Pareto sets, theory, applications); MOO-side row of Table I, showing MOO surveys do not cover KD.

- [shamsian2023auxinash] Aviv Shamsian et al., ‘Auxiliary Learning as an Asymmetric Bargaining Game,’ ICML 2023, PMLR 202, 2023. Status: published. Introduces AuxiNash for asymmetric auxiliary-task bargaining and learns task preferences from their main-task contribution. It is a preference-aware MOO comparator, not a KD-specific method.

## mtl

- [chen2018gradnorm] Zhao Chen et al., ‘GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks,’ ICML 2018, 2017-11-07. Status: published. Gradient-norm balancing; the natural 'normalization-only' control for PCD's EMA normalization.

- [kendall2018uncertainty] Alex Kendall et al., ‘Multi-Task Learning Using Uncertainty to Weigh Losses for Scene Geometry and Semantics,’ CVPR 2018, 2017-05-19. Status: published. Learned loss weighting baseline (symmetric).

- [kurin2022unitary] Vitaly Kurin et al., ‘In Defense of the Unitary Scalarization for Deep Multi-Task Learning,’ NeurIPS 2022, 2022-01-11. Status: published. CONTRADICTING EVIDENCE: argues tuned plain summation matches specialized MTL optimizers.

- [lin2022randomweighting] Baijiong Lin et al., ‘Reasonable Effectiveness of Random Weighting: A Litmus Test for Multi-Task Learning,’ , 2021-11-20. Status: unverified. CONTRADICTING EVIDENCE / litmus baseline: random loss weights as a sanity baseline for MTL optimizers.

- [liu2021imtl] Liyang Liu et al., ‘Towards Impartial Multi-task Learning,’ ICLR 2021, 2021. Status: published. IMTL; equal-projection gradient balancing (symmetric).

- [liu2023famo] Bo Liu et al., ‘FAMO: Fast Adaptive Multitask Optimization,’ NeurIPS 2023, 2023-06-06. Status: published. O(1)-cost loss-weighting MTL baseline used in PCD's experiments; relevant as a cheap alternative to K-backprop methods.

- [navon2022nashmtl] Aviv Navon et al., ‘Multi-Task Learning as a Bargaining Game,’ ICML 2022, 2022-02-02. Status: published. Nash-MTL; symmetric bargaining baseline (AuxiNash is its asymmetric auxiliary-learning descendant).

- [royer2023scalarization] Amelie Royer et al., ‘Scalarization for Multi-Task and Multi-Domain Learning at Scale,’ NeurIPS 2023, 2023-10-13. Status: published. CONTRADICTING EVIDENCE: scalarization competitive at scale.

- [sener2018mgda] Ozan Sener et al., ‘Multi-Task Learning as Multi-Objective Optimization,’ NeurIPS 2018, 2018-10-10. Status: published. MGDA(-UB) for deep MTL; min-norm convex-combination baseline. (Original MGDA: Désidéri 2012, cited by PCD, not separately verified.)

- [senushkin2023alignedmtl] Dmitry Senushkin et al., ‘Independent Component Alignment for Multi-Task Learning,’ CVPR 2023, 2023-05-30. Status: published. Aligned-MTL; condition-number-based gradient alignment (symmetric).

- [xin2022mtohelp] Derrick Xin et al., ‘Do Current Multi-Task Optimization Methods in Deep Learning Even Help?,’ NeurIPS 2022, 2022-12-06. Status: published. CONTRADICTING EVIDENCE: large-scale study finding specialized MTO methods do not beat well-tuned scalarization; sets the bar for PCD comparisons (tuned baselines, equal search effort).

## pareto

- [lin2019paretomtl] Xi Lin et al., ‘Pareto Multi-Task Learning,’ NeurIPS 2019, 2019-12-30. Status: published. Preference-vector Pareto methods: an alternative way to encode unequal importance.

- [ye2022pngd] Mao Ye et al., ‘Pareto Navigation Gradient Descent: a First-Order Algorithm for Optimization in Pareto Set,’ UAI 2022 (PMLR 180), 2022-08-17. Status: published. Anchored program with general K and a shared scheduled margin; PCD ancestry (cited by PCD and by the survey draft).

## pcd

- [irshaid2026fedpcd] Yousef Irshaid et al., ‘FedPCD: Priority-Constrained Federated Aggregation,’ arXiv, 2026-10-09. Status: preprint. Federated extension of PCD: FedAvg aggregate as primary, per-client pseudo-gradients as secondary constraints, client-history cache; O(1/T) rate under a uniform-alignment assumption.

- [varam2026pcd] Dara Varam et al., ‘Not All Objectives Are Born Equal: Priority-Constrained Descent for Hierarchical Multi-Objective Optimization,’ Transactions on Machine Learning Research (TMLR), 2026-09. Status: published. The method under study. Defines the PCD QP, EMA normalization, guarantees (per-step secondary progress, CMS fixed points) and their scope; evaluated on pruning/sparsity/low-rank only.

- [varam2026pcdcode] Dara Varam et al., ‘Priority-Constrained Descent (PCD),’ GitHub, 2026-09-21. Status: published. Author-linked PyTorch rewrite with PCD CIFAR experiment scripts; release omits baselines and physical-pruning export. Its README/scripts state PCD sweeps use a --prox group soft-threshold step (lambda=1e-3; 5e-4 for MobileNetV2), but PCD paper v2 does not disclose this step; exact original-run provenance and baseline treatment need clarification.

## quantization

- [jiang2024gaqat] Jiacheng Jiang et al., ‘GAQAT: gradient-adaptive quantization-aware training for domain generalization,’ arXiv, 2024-12-07. Status: preprint. Prior gradient-conflict work in quantization-aware training; reduces the novelty of a PCD-QAT direction (D5).

## robustness

- [sagawa2020groupdro] Shiori Sagawa et al., ‘Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Worst-Case Generalization,’ , 2019-11-20. Status: unverified. Worst-group robustness baseline for the centralized 'groups-as-clients' PCD direction.

- [xue2024caat] Zhiyu Xue et al., ‘Conflict-Aware Adversarial Training,’ , 2024-10-21. Status: unverified. Prior work for the robustness direction: projects adversarial gradient relative to clean gradient (gradient-conflict view of the accuracy-robustness trade-off).

- [zhang2019trades] Hongyang Zhang et al., ‘Theoretically Principled Trade-off between Robustness and Accuracy,’ ICML 2019, 2019-01-24. Status: published. Clean-vs-robust trade-off objective; candidate secondary for a robustness direction.
