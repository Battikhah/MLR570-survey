# T8 draft preservation map

Claim-level map for the Introduction and Foundations and Knowledge Types text at `Project Files/Current_Survey.md` lines 12–34. Draft wording is not edited; claims are mapped to the revised survey location or a justified exclusion.

| Draft claim | New location | Treatment |
|---|---|---|
| KD enables compact students for constrained deployment (Intro L12) | §I (intro owner) | Retain as motivation; supporting Hinton citation stays with the intro owner. |
| Larger/more accurate teacher need not yield better student because of capacity differences (Intro L13; Foundations L26) | §IV, Teacher assistants and capacity gap | Retained with Cho et al. attribution; framed as a limitation on assuming superiority. |
| Ground-truth and teacher losses can conflict, and magnitude imbalance can cause domination (Intro L14) | §VI-A (MOO owner) | Assign to gradient-conflict / objective-scaling discussion; neither feature nor scheme evidence establishes the claim. |
| Reliability and gradient compatibility are distinct (Intro L15) | §V and §VI-A (owners) | Retain as a distinction: teacher selection addresses supervision quality; gradient compatibility addresses optimization. |
| A pretrained, typically fixed teacher supervises student (Foundations L21) | §IV, Offline distillation | Retained with Hinton citation. |
| Student uses labels and softened teacher outputs (Foundations L22) | §II (preliminaries owner) | Retain in conventional objective exposition. |
| Temperature softens outputs and exposes inter-class probabilities (Foundations L23) | §II | Retain with Hinton citation. |
| CE plus temperature-scaled KL objective and coefficient (Foundations L24–25) | §II | Retain with equation and original Hinton attribution. |
| Transfer depends on compatibility and procedure, not teacher accuracy alone (Foundations L26) | §IV, Teacher assistants and capacity gap | Retained with Cho et al. attribution. |
| Logit transfer matches output distributions / relative class probabilities (Foundations L30) | §III-A and Fig. 3 | Retained as response knowledge; detailed logit section owner supplies Hinton citation. |
| Feature transfer uses intermediate representations; adapters may reconcile dimensions (Foundations L31) | §III-B, first paragraph | Retained through FitNets and projector discussion. |
| Relational transfer matches example distances and angles rather than coordinates (Foundations L32) | §III-B, first paragraph and Fig. 3 | Retained through RKD. |
| Three types differ in signal, architecture demands, and overhead (Foundations L33) | §III-B and Fig. 3 | Retained as synthesis across cited methods. |
| Combining output, feature, and relational losses introduces objectives whose reliability and interaction matter (Foundations L34) | §VI-A and §VI-B (owners) | Retain in the MOO discussion; §III-B identifies the additional objectives but does not assert their empirical conflict. |
