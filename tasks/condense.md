# Condense the survey: main text 34 -> 18 +- 2 pages (user decision 2026-11-08)

Full version preserved at git tag `survey-full-v1` (54 pp). Main text = §I-§X before References; appendix and references do not count.

## Protected (must survive; trim wording only)
- §I: scope, I1-I3/E1-E7, search counts (2,193 / 445 / 310 / 112), Table I, taxonomy figure, contributions.
- Seminal + top methods per family (keep a sentence of mechanism each): KD, DKD, MLKD, LSKD, CTKD, VRM, SKD, GDKD, EA-KD, RLD, MCD, LumiNet (only ECE source); SimKD, ReviewKD, CRD, TopoKD, projector study (miles2024projector), SRD, DIST/DIST+; DOT, DTO-KD, DeepKD, DistPro; KD-AIF (as the non-ranked case).
- §V teacher-reliability content that motivates gating (keep main argument and the gated methods).
- §VI-B KD x MOO (light trim only): DTO-KD, DOT, DeepKD, SCKD, SCOPE, TPKD, PCD (neutral, no more space than peers).
- §VI-A: scalarisation, MGDA, PCGrad, CAGrad, and the "tuned scalarisation is hard to beat" studies (xin2022mtohelp, kurin2022unitary, royer2023scalarization); other MOO methods -> one sentence.
- §VIII: protocol caveats, comparability argument, top results and the comparison logic; DeepKD camera-ready numbers (79.25 / 78.42 / ImageNet 73.34 / 74.85).
- §IX: challenges may merge to 4-5 but keep each evidence link; keep the restored Yuan 2020, Stanton 2021, Beyer 2022 claims.
- Every original-draft claim mapped in docs/reviews/survey-t8-preservation.md, survey-t9.md, survey-t11.md, survey-t16-audit.md §4 stays (it may be shortened, merged, or moved; update its location in the map if moved).

## Completeness
All 112 included methods stay cited, in a new appendix `paper/survey/sections/11_appendix_methods.tex` (after References or as \appendix): one row per method: method \citep{id}, family, venue/year, best reported R32x4->R8x4 and/or IN R34->R18, source table. Full leaderboard rows move there; main §VIII tables keep the top ~12 per dataset plus the comparison-set baselines.

## Rules
- Never change a number; never add a source. Humanizer style. Keep `% Owner:` headers.
- Removed method paragraphs: the method must still appear in the appendix (and optionally in one grouped sentence).
