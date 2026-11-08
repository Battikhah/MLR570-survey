# Codex review: survey T14 + T15

Reviewed commits `5fc8ccd`, `e4f4834`, and `18ae3b4` in the assigned scope. Findings below are limited to claims verified against the local survey text and search/evidence records.

## Findings

### M — Table I, `paper/survey/sections/01_intro.tex:106`

**Evidence:** The “This survey” row marks LLM/VLM coverage as partial (`\tP`). The authoritative cell ledger, `docs/survey/table1-evidence.md:49`, marks this cell `✓`. The table caption defines `✓` as dedicated coverage and partial as coverage only in passing, a narrower setting, or inside another topic (`paper/survey/sections/01_intro.tex:83-87`). The source ledger therefore disagrees with the rendered cell.

**Fix:** Align the cell with the evidence ledger, or update that ledger if the survey's LLM/VLM coverage was intentionally narrowed. Do not leave the table and its documented evidence in conflict.

## Checks with no finding

- **Search counts:** `docs/survey/search/README.md:6-10` gives 656 + 985 + 552 = 2,193 identified records and 96 + 130 + 84 = 310 full-text assessments. Thus “310” in §I is scoped to the three original searches. The separately reported gap-pass batch is 445 new title hits (`README.md`, “Gap pass outcome”; `g-gap.md`, §2), with two additions after adjudicating the remaining gap items; the manual-PDF pass adds six, yielding 112 (`README.md`, “Final included set”; `manual-pdfs.md`, “Included”). The abstract's 445 and 112, and §I's 112, match those records. The abstract does not call 310 the total across later passes.
- **§IX inherited claims:** LumiNet's 0.06 versus KD's 0.11 ECE is stated in §III (`paper/survey/sections/03a_logit.tex:164-167`); the “only ... quoted” wording in §IX is consistent with the inspected body. The plug-in/base-grid claim is explicitly bounded to included papers and agrees with §VI's account of the comparisons checked (`paper/survey/sections/06b_kd_moo.tex:268`). The other enumerated inherited quantitative claims checked in §IX agree with the cited benchmark passages.
- **Table I:** Apart from the LLM/VLM cell above, the displayed survey rows and cells match `docs/survey/table1-evidence.md:39-49`.
- **Consistency:** The abstract, §I contributions, §IX and §X describe the same method scope and seven open-problem themes; the conclusion accurately frames PCD as an option without standard-pair results. The accuracy values and ImageNet row-range statements inspected agree with §VIII.
- **Style and coverage:** No instances of “delve,” “crucial,” “landscape,” “notably” or “pivotal” were found in the reviewed prose. PCD is mentioned as one optimizer-side example and is not given disproportionate space. The assigned text does not assert that all G1–G11 checklist items are complete; that checklist remains for T16.

## Severity count

- Critical: 0
- Major: 1
- Minor: 0
