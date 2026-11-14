# Existing-source audit and figure refresh — 2026-11-14

No new papers, bibliography records, or citation keys were added. Existing first-pass edits were preserved.

- **Equations checked:** SCKD's printed inequality conflicts with its rationale; Algorithm 1's gate is sticky as printed. DTO-KD's equality-only coefficients can violate the stated simplex; the manuscript now distinguishes the simplex solution, degenerate equal-gradient case, Algorithm 1, and amortized approximation. These printed-source facts do not establish the authors' implemented procedure. [Evidence and official PDFs](survey-source-audit-equations.md).
- **Results:** 13 supported fills in the 112-record source table; 268 of the original 281 missing cells remain NE. Populated result counts are R8x4 73, W16-2 18, R18 83, MBV1 6. Own-teacher and stacked-variant flags remain explicit. LSKD's red gains were not treated as uncertainty. [Evidence](survey-source-audit-results-code.md), [all 281 cell dispositions](survey-source-audit-ne-cells.csv).
- **Code:** Checked the main tables' 24 row labels: 17 linked/accessible, 6 without an author implementation link located, and student-alone N/A. VRM and TopoKD are now marked linked. This is availability evidence, not reproducibility or licensing verification.
- **Figures:** Reworked five existing diagrams and visually inspected rendered manuscript pages: search flow, taxonomy, KD pipeline, knowledge types, and training schemes. Corrected card alignment, text wrapping, and arrow clearance. [Details](survey-figure-refresh.md).

## What remains unverified

Many batch retrieval attempts did not yield accessible full text, including DNS failures; those papers were not fully table-audited. Some inspected tables used different teacher/student pairs or MobileNet variants. Neither case proves a result was not reported, and no such cell was relabelled NR. Batch A inspected four additional primary PDFs; batch B checked available SimKD/Bayesian-teacher PDFs but most retrievals were blocked. [Batch A](survey-ne-batch-a.md), [Batch B](survey-ne-batch-b.md).

[Existing-paper links for uploads and unresolved checks](survey-needed-sources.md). Upload the cited PDF plus its supplement where available. This is a complete inventory of unresolved cells, not a claim that every paper was re-read. The three DISK cells have no source URL in the existing record; provide that already-cited paper/source directly.

SCKD and DTO-KD PDFs were obtained. To settle their implementation questions, we still need author code, an erratum, or author clarification; another copy of the same PDF will not resolve them. No authoritative implementation direction was invented.

## Verification

Final build and preservation-check results are recorded below after integration. No training, experiments, or code execution from external repositories was performed.

Final checks: `pytest -q` — 10 passed; bibliography/citation check — passed (239 combined entries, 234 paper-registry records); `git diff --check` — passed. Both `latexmk` builds passed: manuscript 25 pages, supplement 14 pages. No overfull boxes, undefined citations/references, or LaTeX warnings were found in the final logs; underfull spacing diagnostics remain. Rendered Figures 1–6 and affected supplementary table pages were inspected.

The snapshot comparison preserved all 112 included identities, all 234 registry IDs, the cited-key set, Owner headers, and every previously populated result value. Exactly 13 former NE cells were filled. PDF delivery copies were refreshed from the final builds. No commit or push was made.

Independent read-only verifier: PASS. Re-ran preservation, tests, bibliography, whitespace checks, and acceptance assertions for counts/code statuses; found no actionable failures. Visual/source verification remained the main session's responsibility.
