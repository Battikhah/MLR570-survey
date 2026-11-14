# Survey figure refresh

Updated the five existing TikZ figures using the existing packages and restrained blue/grey styling. No sources, method claims, packages, or algorithms were added.

- **Taxonomy:** Replaced the dense 17-row tree with four linked topic panels and a full-width benchmark strip. Kept all requested method examples, moved OFA-KD under feature knowledge, and retained the current four CIFAR-100 and four ImageNet-1K examples. The caption now describes the panels and overlapping dimensions.
- **KD pipeline:** Shortened the loss nodes, made both temperature-softmax and ordinary softmax explicit, and added the weighted total objective. Labels and arrows show that only the student is updated; the teacher remains frozen.
- **Knowledge targets:** Widened the three equal-height cards and separated examples from definitions.
- **Schemes:** Recast the six schemes as equal-height cards in a 3-by-2 grid with one palette; the data-free card states that original training data are unavailable.
- **Search flow:** Separated the three source groups, full-text screening, second-pass/manual additions, final 112 arithmetic, and the two unassessable papers. The arithmetic and counts are unchanged; inclusion follows screening.
- **Captions:** Updated the taxonomy, search-flow, and knowledge-target captions to match the revised figures.

## Checks and remaining risk

The main session built the manuscript with `latexmk` and inspected rendered pages containing Figures 1–5. It corrected heading alignment, definition wrapping, and a line touching the KD-loss box. The final renders show aligned cards, readable text, and unobstructed pipeline arrows. Search counts remain 2,193 identified, 310 screened, and 112 included. Figure 6 retains the earlier geometry corrections; its mathematical directions were not changed in this refresh. No new packages or citation keys were added.
