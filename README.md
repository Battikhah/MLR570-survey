# MLR570 survey: state-of-the-art knowledge distillation for image classification, 2022–2026

A systematic survey of knowledge distillation (KD) methods for image classification, with a primer
on multi-objective optimisation and a compilation of reported CIFAR-100 and ImageNet-1K results.
It also selects the comparison set for the team's PCD project (separate repository).

## Layout

| Path | Contents |
|---|---|
| `paper/survey/` | LaTeX source (TMLR template): `main.tex` (paper), `supplement.tex` (Tables S1–S2) |
| `docs/survey/search/` | Search logs: dated queries, every screened record with its decision |
| `docs/survey/included-methods.md` | All 112 included methods with reported results (source of Table S2) |
| `literature/sources.yaml` | Source registry; every citation key is a record here |
| `docs/reviews/survey-*` | Review rounds and audits |
| `scripts/` | `build_bib.py` (registry → `refs.bib`), `build_supplement.py` (→ Table S2) |

## Build

```bash
uv run python scripts/build_bib.py --check      # refs.bib from the registry; fails on unknown keys
uv run python scripts/build_supplement.py       # Table S2 from included-methods.md
cd paper/survey && latexmk                      # build/main.pdf and build/supplement.pdf
uv run pytest
```

Authors: Khalid Hamdan, Aly Khaled Ismail Mahmoud, Hasan Akel, Salim Akel (American University of Sharjah).
