# Review brief: SOTA KD survey (HEAD 22fd8c5)

You are a senior ML reviewer (TMLR / NeurIPS level). Start from the assumption that the work is broken
somewhere and find where. Be adversarial and verify against the files yourself; this brief is not evidence.
Say plainly when something holds up. Do not manufacture findings. **Read-only: do not edit any file except
the report below.**

## The artifact

- Source: `paper/survey/main.tex`, `paper/survey/sections/*.tex`, `paper/survey/figures/*.tex`
- Built PDF: `paper/survey/build/main.pdf` (23 pp; main text ends p. 18; 66 references). `pdftotext` it.
- Bibliography is generated from `literature/sources.yaml` by `scripts/build_bib.py` (`refs.bib`).
- Supplementary list of all 112 included methods with numbers: `docs/survey/included-methods.md`
- Search records: `docs/survey/search/*.md`; inclusion criteria I1–I3, exclusion E1–E7 are in §I.
- Primary-source PDFs (local, git-ignored): `literature/pdfs/access/` and
  `~/orca/projects/AML-Code-and-Paper/literature/PDFs/`. No network in your sandbox; use these.
- `% src:` comments in the .tex name the table each number comes from.

## What the paper claims to be

A systematic survey of knowledge distillation for image classification, 2022–2026: documented search
(2,193 + 445 records → 310 read → 112 methods), taxonomy (logit, feature/relation, schemes, teacher
reliability, KD as multi-objective optimisation), a MOO primer, compiled reported results on CIFAR-100
ResNet32x4→ResNet8x4 and ImageNet ResNet34→ResNet18 (each paper's own claim, flagged when stacked or
setting-changed), and five open problems. It also serves to pick baselines for the authors' PCD
(priority conflict descent) project.

Known constraints the authors chose: references were deliberately cut to ~66 (the full method list is
supplementary); numbers are never re-run, only transcribed; preprints are marked.

## Do three passes

1. **Research review.** Logical gaps, unjustified claims, narrative weaknesses, whether the contribution
   suffices for TMLR. Is the "systematic" claim backed? Is the MOO angle substantive or bolted on? Is the
   reported-results section honest about comparability?
2. **Claim audit.** Pick at least 15 numeric or factual claims across sections (favour the abstract,
   §IX tables, §VI-B equations/closed forms). Check each against the local primary PDF (or the search
   record if the PDF is absent; say which). Report match / mismatch / unverifiable with the page/table.
3. **Citation audit.** (a) Any method or result named in the text, tables or figures with no citation
   in that sentence/row or an obviously adjacent one. (b) Any citation used for a claim the cited paper
   does not support. (c) Bibliography entries with wrong year, venue or authors (spot-check ≥10 against
   `sources.yaml` and the PDFs). (d) Leftover internal notes, TBDs, placeholders in the PDF text.

## Output

Write `docs/reviews/survey-final-codex.md` with exactly these sections:

1. **Verdict** (one paragraph; would you accept at TMLR as is / minor / major / reject, and why)
2. **The good** — real strengths, each with evidence (file:line or page)
3. **The bad** — weaknesses ranked by severity (critical / major / minor), each with file:line or page,
   the concrete failure, and the smallest fix
4. **Claim audit table** — claim | location | source checked | result
5. **Citation audit** — findings for (a)–(d), or "none found" with what you checked
6. **Mock TMLR review** — summary, strengths, weaknesses, questions, recommendation, confidence

Then report done.
