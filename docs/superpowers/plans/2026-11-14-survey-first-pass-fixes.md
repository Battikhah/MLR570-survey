# Survey first-pass fixes implementation plan

> **For agentic workers:** Use the existing review as the checklist. Execute scoped edits with cheaper build agents and one final independent verifier.

**Goal:** Apply the 98 findings in `docs/reviews/survey-first-pass.md` to the LaTeX and its owning generated sources, then deliver rebuilt PDFs.

**Architecture:** Preserve the section structure, citations, source registry and method coverage. Clarify uncertain source descriptions instead of inventing resolutions. Generated table changes flow through the Markdown source and generator.

**Tech Stack:** LaTeX/TikZ, Python, pytest, latexmk.

**Spec:** `docs/reviews/survey-first-pass.md`.

## Global constraints

- Preserve all 112 included citation records and section `% Owner:` headers.
- Do not invent source results, new citations, publication status or repository availability.
- Correct counts only using documented repository evidence; preserve all reported accuracy values.
- PCD remains a general reference rule without KD results. SCKD’s rule remains explicitly uncertain.
- No project experiments, new dependencies, commits or pushes.
- Use Luna build agents for implementation; main handles integration and a final verifier independently checks results.

## Review focus

- Every review ID needs an edit or an explicit evidence-based disposition.
- No source-sensitive caveat is silently replaced with a stronger claim.
- All cited included records remain covered in the supplement.
- Missingness and alternative pairs stay distinguishable without pretending papers were re-read.
- Built figures and tables remain legible, with no undefined references/citations or clipped content.

## Tasks

- [x] Task 1 — Main manuscript and section edits: `paper/survey/main.tex`, `paper/survey/sections/*.tex`. Apply prose, internal consistency and section-table findings. Write an ID disposition note.
- [x] Task 2 — Figures, supplement and owning generator/source edits: `paper/survey/figures/*`, `paper/survey/supplement.tex`, `scripts/build_supplement.py`, `docs/survey/included-methods.md`, relevant tests. Apply figure/table findings and regenerate S2. Write an ID disposition note.
- [x] Task 3 — Integrate: reconcile all 98 IDs, run bibliography check, supplement regeneration consistency, pytest, latexmk, whitespace and citation/header preservation checks; inspect rebuilt PDFs, apply one focused repair if needed, refresh `pdf/` artifacts. Independent verifier checks the complete result.

## Decisions

- Internal S2 evidence currently gives 112 rows, 72 R8x4 values and 80 R18 values. Preserve the PEFD extension as a separate included record and describe the denominator as result rows rather than distinct algorithms.
- Ten included DF records include nine tabulated WRN values and HiDFD’s alternative pair in Notes. Four other records report outside the tabulated pair columns.
- Missing original-paper verification is handled with an explicit limitation in the manuscript, not an invented correction.
