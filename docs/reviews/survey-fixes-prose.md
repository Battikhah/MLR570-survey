# First-pass survey findings: prose and table dispositions

Scope: `paper/survey/main.tex` and `paper/survey/sections/*.tex`. The figure sources and supplement findings assigned to the other workstream are recorded as out of scope here. Edits preserve manuscript citation keys, Owner headers and reported accuracy values; the denominator corrections follow the documented 112-record inventory and 80 populated ImageNet result rows.

## AI-lingo findings

- A01: Replaced the “lens” metaphor with classification by gradient-combination rule and kept the explanation caveat.
- A02: Replaced “We close with” and the long question with a concise list of remaining questions.
- A03: Named the batch relations and sample weighting changes.
- A04: Said logit standardisation can combine with several distillation losses.
- A05: Removed the generic “no scheme dominates” maxim; stated the scheme-specific constraints.
- A06: Replaced “lineage” with “background precedent” for SCKD; AE-KD heading names teacher balancing.
- A07: Used label-priority, distillation-priority and symmetric-rule descriptions.
- A08: Replaced “safe start” with a practical starting point and the conditions for using it.
- A09: Replaced the unspecified cost fraction with lower inference cost.
- A10: Specified that the cited survey reviews gradient-based MOO but not distillation.
- A11: Replaced the progress-story transition with the concrete change and reported accuracy direction.
- A12: Introduced CTKD’s values directly and retained their baselines and citation.
- A13: Named RLD’s reliability topic and the next sections’ subjects.
- A14: Named teacher availability, supervision sources and data access as compute/error factors.
- A15: Explained that searched accuracy does not isolate one loss’s contribution.
- A16: Opened with the reliability signals and retained the table reference.
- A17: Described whether methods weight samples, switch sources, revise targets or select subsets.
- A18: Stated the primary-label and auxiliary-teacher convention directly.
- A19: Replaced “give back” with “reduce an existing correct-class margin.”
- A20: Described MEMA as a continuous per-sample gradient-similarity weight.
- A21: Distinguished per-pair search from per-step gradient changes.
- A22: Renamed “scalarisation debate” to evidence from multi-task learning.
- A23: Introduced TPKD’s projection ablation with its values, separately from interpretation.
- A24: Stated that PCD’s distillation benefit remains untested.
- A25: Opened with the reported CIFAR comparison and said differing protocols do not establish a reliable ranking.
- A26: Replaced the conversion metaphor with the remaining questions.

## Complicated sentences

- S01: Removed venue inventory from the abstract; venues remain in the inclusion criterion and search protocol.
- S02: Shortened the abstract’s open-question list and made its topics parallel.
- S03: Broke I1–I3 into separate description entries, clarified internal targets and MobileNetV1, and stated that families overlap.
- S04: Separated the accessible inclusion/exclusion sample counts from the two and ten unread samples.
- S05: Split DKD mechanism, ablation interpretation and reported comparison.
- S06: Split CTKD’s comparisons from LSKD’s mechanism and reported results.
- S07: Explained feature values and pairwise-distance invariants before comparing them.
- S08: Replaced the nested comparison sentence with attachment point, preserved relation and added work.
- S09: Shortened the opening and separated scope from the detailed methods.
- S10: Split the LR-DS/RLD and MCD/CHAD mechanism descriptions into paragraphs.
- S11: Explained Frank–Wolfe’s weight-search role and MGDA-UB’s shared-representation approximation.
- S12: Gave one rule per sentence; defined primary $f$, constrained $g$ and external criterion $F$.
- S13: Defined DTO-KD’s $g_{11}$, $g_{12}$ and $g_{22}$ as gradient inner products/norms; retained the derivation and deployment caveat.
- S14: Put MEMA’s damping formula on a display line and defined its constants.
- S15: Listed the three proposed baseline groups.
- S16: Separated KD comparisons, multi-task evidence and the proposed experiment.
- S17: Replaced the compressed family catalogue with practical trade-offs.

## Figure/table findings within scope

- F01–F05: Not applicable to owned files; assigned figure source work covers these diagram edits. F03–F04 likewise belong to the search-flow figure.
- F06: Caption now distinguishes historical background from included 2022–2026 methods.
- F07: Removed the caption’s preprint-star convention; publication status remains in text/registry.
- F08: Added a separate General MOO column; Chen et al. is marked there and remains uncovered for MOO in KD.
- F09: Recast the reliability table as Signal/Action/Caveat and split LR-DS from RLD. SCKD’s row states that its published threshold and rationale disagree, with direction unresolved.
- F10: Figure geometry belongs to the figure owner; no geometry edits here.
- F11: Caption states the gradient-arrow convention and $\\theta_{\\rm new}=\\theta-\\eta d$; removed unsupported generator/test narration.
- F12: Benchmark tables distinguish linked, linked-but-unreachable (as observed 2026-11-08), and not linked.
- F13: Added supported CIFAR KD and plain-student rows and the supported ImageNet KD row; labels code status and variant/configuration separately. No ImageNet plain-student result was added.
- F14–F15: Supplement table and missingness codes belong to the supplement owner.
- F16: Hyperref styling is a main-file change that may be visually evaluated during integration; no style change made in this pass.

## Conflicted findings

- C01: Reliability table now carries the SCKD threshold/rationale disagreement; it does not choose an unsupported direction.
- C02: PCD is described as a candidate general rule with no distillation evaluation.
- C03: Changed the ImageNet denominator from 79 to 80 result rows in abstract and benchmark text/captions; retained 112 records.
- C04: Distinguished ten data-free records from nine WRN result rows and noted HiDFD’s alternative pair.
- C05: Used the additive $L_{CE}+\\lambda L_{KD}$ form consistently and gave $\\lambda=\\alpha/(1-\\alpha)$ for $0\\leq\\alpha<1$, with the pure-KD endpoint.
- C06: Qualified DPK’s teacher-size result to its reported setting.
- C07: Removed the unsupported 76.0–77.5 summary range; cited GDKD and LDRLD examples instead.
- C08: Reported MEMA and TPKD ablation values while leaving conflict-vs-rescaling explanations unresolved.
- C09: Replaced the narrow reliability range with RLD, MCD and updated-teacher KD-AIF examples and their protocol distinction.
- C10: Distinguished AE-KD’s teacher-to-teacher balancing from DTO-KD’s task/distillation combination.
- C11: Separated symmetry from guarantees; PCD’s local directional condition is qualified and explicitly not a finite-step guarantee.

## Unclear-thought findings

- T01: I1 explicitly includes internally generated targets.
- T02: Taxonomy and inclusion text state that families/dimensions overlap.
- T03: Named MobileNetV1 in I3; the standard CIFAR pair is tied to CRD. Full pair inventory remains in the supplement.
- T04: Not applicable to owned files; search-source/cutoff wording is in the supplement owner’s scope.
- T05: Explained the additive-to-convex weight mapping and what changes at fixed learning rate; removed the broad optimizer equivalence claim.
- T06: Qualified the temperature-one target statement by teacher/label agreement and described the wrong-prediction case.
- T07: Said SimKD reuses the teacher classifier on learned student features without claiming identical input-space decisions.
- T08: Replaced the abstract three-question synthesis with examples tied to named methods.
- T09: Narrowed transfer-data claims to state that data-selection mechanisms are not compared here.
- T10: Removed orphaned group-metric advice rather than imply an unestablished group method.
- T11: Removed the uncited mechanism list; retained rule-specific explanations and a general caution about symmetry.
- T12: Stated feasibility, nonzero-gradient and positive-margin conditions for local directional progress; distinguished this from finite-step training.
- T13: Limited conflict-removal framing and distinguished teacher weighting, scale and schedules.
- T14: Separated seed variation from cross-paper protocol/reproduction differences; labels 0.3 points as an illustrative caution, not a threshold.
- T15: Teacher accuracy is context for TopoKD’s protocol, not grounds to invalidate the student result.
- T16: Proposed a common top-$k$/threshold policy and an accuracy change after removing selected samples.
- T17: Replaced gain ratio with absolute gains over matched KD baselines; described requirements for any ratio.
- T18: Online KD and data-free KD now have separate constraints; data-free still uses a teacher.

## Unnecessary-information findings

- U01: Removed draft-history narration from the preliminaries.
- U02: Removed COCO split counts and detection dataset detail from the classification primer.
- U03: Removed the CHAD attribution-audit aside; retained its BanSum evidence and scope limitation.
- U04: Replaced the TPKD abstract omission caveat with its pretrained-student evaluation context.
- U05: Removed the isolated DTO-KD COCO result from the MOO analysis.
- U06: Replaced repeated CHAD task-specific values with a cross-reference to reliability.
- U07: Removed generator/unit-test narration from the MOO figure caption.
- U08: Removed repeated combination-rule recommendation from the optimizer paragraph; retained the baseline comparison in one dedicated paragraph and the future-work experiment.
- U09: Removed the paragraph-template announcement.
- U10: Removed the broad uncited neighboring-settings list; retained the scoped DHO example.

## Checks and limits

No build, bibliography check, full test suite or PDF inspection was run, as requested for this workstream. The parent’s independent citation/header/count preservation check passed while these edits were in progress; it should be repeated after integration. Figure, supplement and generated-source changes remain outside this report’s ownership.
