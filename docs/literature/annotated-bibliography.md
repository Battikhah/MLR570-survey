# Annotated bibliography

## auxiliary-learning

- [du2018auxgradsim] Yunshu Du et al., ‘Adapting Auxiliary Losses Using Gradient Similarity,’ , 2018-12-05. Status: preprint. Main-task-anchored gating of auxiliary losses by gradient cosine; asymmetric precedent.

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

- [chen2026scope] Tao Chen et al., ‘Selective Confidence-Guided Projection-Based Encoding for Medical Image Classification,’ Journal of Imaging, 2026-09-11. Status: published. Classification-priority gradient-conflict removal for KD plus confidence-weighted relations: very close to the KD proposal.

- [hayder2026dtokd] Zeeshan Hayder et al., ‘DTO-KD: Dynamic Trade-off Optimization for Effective Knowledge Distillation,’ ICLR 2026, 2026. Status: published. MOO-based KD comparator (dynamic task/KD trade-off).

- [hinton2015kd] Geoffrey Hinton et al., ‘Distilling the Knowledge in a Neural Network,’ NIPS 2014 Deep Learning Workshop, 2015-03-09. Status: published. Standard KD loss used as the secondary in the current proposal.

- [kang2025dho] Seongjae Kang et al., ‘Simple yet Effective Semi-supervised Knowledge Distillation from Vision-Language Models via Dual-Head Optimization,’ NeurIPS 2026 (per arXiv comment), 2025-05-12. Status: accepted. Only source found with MEASURED CE–KD gradient cosine: single-head CE+KD baseline final-epoch cos(∇CE, ∇KD) ≈ −0.39 to −0.45 across ResNet-18 stages and −0.76 at the classifier head (8-dataset mean, 16-shot, CLIP RN50 zero-shot teacher). Prop. 1 proves head-level conflict whenever the student prediction lies in the ball with diameter [y, p].

- [sumit2026chad] Dipto Sumit et al., ‘When Does Knowledge Distillation Hurt? Reliability-Aware Distillation for Low-Resource Language Summarization,’ arXiv, 2026-07-22. Status: preprint. Reliability-aware KD reporting that teacher-confidence-only gates offered little benefit (per survey draft).

- [yuan2026tpkd] Qianfeng Yuan et al., ‘Learning Beyond Full Imitation: Task-Preserving Knowledge Distillation,’ arXiv, 2026-09-30. Status: preprint. Asymmetric KD that projects teacher directions to protect task margins: close to PCD-KD.

- [zhu2021sckd] Yichen Zhu et al., ‘Student Customized Knowledge Distillation: Bridging the Gap Between Student and Teacher,’ ICCV 2021, 2021-10. Status: published. Supervised-primary gradient-similarity gating of KD terms: closest KD precedent for asymmetric KD.

## lexicographic

- [gong2021dbgd] Chengyue Gong et al., ‘Automatic and Harmless Regularization with Constrained and Lexicographic Optimization: A Dynamic Barrier Approach,’ NeurIPS 2021, 2021-12-06. Status: published. Direct ancestor: for K=2 the PCD QP coincides with the DBGD update (raw gradients); DBGD has convergence proofs for constrained/lexicographic settings that PCD lacks.

- [skalse2022lmorl] Joar Skalse et al., ‘Lexicographic Multi-Objective Reinforcement Learning,’ IJCAI 2022, 2022. Status: published. Lexicographic (strict priority) optimization in learning; contrasts with PCD's soft τ-priority.

## mtl

- [chen2018gradnorm] Zhao Chen et al., ‘GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks,’ ICML 2018, 2017-11-07. Status: published. Gradient-norm balancing; the natural 'normalization-only' control for PCD's EMA normalization.

- [kendall2018uncertainty] Alex Kendall et al., ‘Multi-Task Learning Using Uncertainty to Weigh Losses for Scene Geometry and Semantics,’ CVPR 2018, 2017-05-19. Status: published. Learned loss weighting baseline (symmetric).

- [kurin2022unitary] Vitaly Kurin et al., ‘In Defense of the Unitary Scalarization for Deep Multi-Task Learning,’ NeurIPS 2022, 2022-01-11. Status: published. CONTRADICTING EVIDENCE: argues tuned plain summation matches specialized MTL optimizers.

- [lin2022randomweighting] Baijiong Lin et al., ‘Reasonable Effectiveness of Random Weighting: A Litmus Test for Multi-Task Learning,’ , 2021-11-20. Status: unverified. CONTRADICTING EVIDENCE / litmus baseline: random loss weights as a sanity baseline for MTL optimizers.

- [liu2021imtl] Liyang Liu et al., ‘Towards Impartial Multi-task Learning,’ ICLR 2021, 2021. Status: published. IMTL; equal-projection gradient balancing (symmetric).

- [liu2023famo] Bo Liu et al., ‘FAMO: Fast Adaptive Multitask Optimization,’ , 2023-06-06. Status: unverified. O(1)-cost loss-weighting MTL baseline used in PCD's experiments; relevant as a cheap alternative to K-backprop methods.

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
