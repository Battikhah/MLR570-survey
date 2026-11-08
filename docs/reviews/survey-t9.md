# T9 draft-preservation map

Source: `Project Files/Current_Survey.md`, §“Teacher Reliability and Selective Transfer,” lines 36–106. Each substantive statement is carried into §V of `paper/survey/sections/05_reliability.tex`; citations retain the draft attribution through the source identifiers listed below. The corresponding Table III rows provide the requested signal / rejected-supervision / limitation summary. No original factual statement was silently dropped.

| Draft lines | Draft claim or note | New location and attribution | Disposition |
|---|---|---|---|
| 40 | Correctness means teacher top class matches the observed label; CTSL is a precedent for conditional admission. | `paper/survey/sections/05_reliability.tex:7`; Table III CTSL row; `meng2019conditionalts` | Preserved. |
| 41 | Maximum confidence differs from probability on the known correct class; CCKD uses correct-class probability. | `paper/survey/sections/05_reliability.tex:7`; Table III CCKD row; `mishra2021cckd` | Preserved; CCKD remains explicitly identified as an arXiv preprint. |
| 42 | Calibration is empirical confidence correctness; temperature scaling calibrates and differs in purpose from KD temperature. | `paper/survey/sections/05_reliability.tex:9`; `guo2017calibration` | Preserved, with the two uses of temperature distinguished. |
| 43 | Teacher correctness/confidence do not establish student usefulness; selection and target repair address distinct aspects. | `paper/survey/sections/05_reliability.tex:13,22`; `zhu2021sckd`, `sun2025rld`, `lan2025labelrevision`, `sumit2026chad` | Preserved as a distinction among evidence types; causal usefulness is not claimed. |
| 44 | Calibration may fail under shift; label agreement inherits label errors. | `paper/survey/sections/05_reliability.tex:7,9`; `ovadia2019shiftuncertainty`, `meng2019conditionalts`; Table III CTSL row | Preserved. Removed “proposed gate” wording because it referred to the project rather than the surveyed methods. |
| 48–53 | CTSL source/authors/venue; correctness signal; use labels if teacher is wrong; switch targets; strengths and speech-adaptation limit. | `paper/survey/sections/05_reliability.tex:7`; Table III CTSL row; `meng2019conditionalts` | Claims preserved with the same source attribution; “no PCD program” is omitted as project framing. |
| 57–62 | CCKD source/status; confidence weighting; loss and target variants; optional student-easy sample skipping; strengths and distinction from Boolean correctness/max-confidence gate. | `paper/survey/sections/05_reliability.tex:7`; Table III CCKD row; `mishra2021cckd` | Preserved; variant-specific supervision behavior is explicit. The source remains labeled preprint because no later venue was verified. |
| 66–71 | Hard Gate KD source/venue; calibrated teacher/student true-token or sentence probabilities; routing between labels and teacher; strengths and NLG-specific limit. | `paper/survey/sections/05_reliability.tex:9`; Table III Hard Gate KD row; `lee2022hardgatekd` | Preserved. The table and prose state that label supervision can be off when teacher guidance is selected. “Not PCD” and proposal-comparison framing are omitted. |
| 75–80 | CA-MKD attribution; label cross-entropy controls sample-wise teacher weights; feature transfer; strengths; differs from one-teacher hard rejection. | `paper/survey/sections/05_reliability.tex:9`; Table III CA-MKD row; `zhang2022camkd` | Preserved. Unchecked separate student-CE persistence remains an explicit uncertainty, not a settled claim. |
| 84–89 | LR-DS attribution; label information and influence scores; unselected examples retain label supervision; revises/selects; strengths and distinction from a binary predicate. | `paper/survey/sections/05_reliability.tex:13`; Table III LR-DS row; `lan2025labelrevision` | Preserved. The journal/preprint loss-formulation comparison and inaccessible author-PDF note are condensed to the explicit uncertainty that final journal loss details were not checked line by line. |
| 93–98 | RLD attribution; label-conditioned refinement of confidence/class correlations; labels form targets; useful information can be retained; limitations. | `paper/survey/sections/05_reliability.tex:13`; Table III RLD row; `sun2025rld` | Preserved. Unverified fixed all-example CE is not asserted; repair is distinguished from rejecting the whole distribution. “Not PCD” is omitted as project framing. |
| 102–106 | CHAD title/source/status; validation-gradient alignment and learned weights; teacher-confidence-only gates provide little benefit; local-proxy limitation; multilingual result is EWAD+CPDP, not CHAD. | `paper/survey/sections/05_reliability.tex:13`; Table III CHAD row; `sumit2026chad` | Preserved. Explicitly labeled a 2026 preprint; BanSum comparison is attributed to the paper's reported experiment, and multilingual effectiveness is not inferred. |

## Justified exclusions and uncertainty labels

The phrases “the proposed method,” “the proposal,” and comparisons against the proposed correctness-plus-confidence rule were removed because they describe the course project, not neutral survey findings. Statements that a source does not establish a PCD program were likewise removed; the surveyed work is compared by its actual reliability signal and supervision handling. Process notes about unavailable or unchecked material were converted into bounded claims: CCKD venue unverified; CA-MKD's separate all-example student-CE persistence unresolved; LR-DS's final-journal loss not checked line by line against the preprint; and CHAD kept as an unreviewed preprint; its BanSum table result (gates within 0.0001 ROUGE-L of CE; CHAD +0.0173 over KD) is now cited from the full text. No source with unverified publication status is presented as peer-reviewed CORE evidence.

## Added inventory methods

The section also covers reliability-related inventory methods TGeo-KD (`hu2024tgeokd`), EA-KD (`su2025eakd`), LTKD (`kim2026ltkd`), AGRE-KD (`kenfack2025agrekd`), CaRE-KD (`sengupta2026casd`), and TPKD (`yuan2026tpkd`). TPKD is qualified as a preprint and its benchmark limitation is stated. These additions are separate from the 100% preservation mapping above.

**Condense pass 2 (2026-11-08):** the §V reliability table (formerly Table III) was removed to meet the
page target. Every claim the rows above attribute to "Table III" is still carried by the §V prose at the
cited `05_reliability.tex` paragraphs (CTSL, CCKD, Hard Gate KD, CA-MKD, LR-DS, RLD, CHAD), and every
method in that table remains cited in §V and in the appendix (Table `tab:app-methods`).

**Reference cut (2026-11-08):** the appendix table moved to the supplementary file
`docs/survey/included-methods.md`; Table III (`tab:reliability`) is restored in §V with only cited
methods. All mapped draft claims above keep their citations. The added inventory methods TGeo-KD,
LTKD, AGRE-KD and CaRE-KD are no longer cited in the main text (uncited summary sentences only) and
remain in the supplementary list.
