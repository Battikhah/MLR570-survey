from scripts.build_supplement import rows, tex_row

MD = """| # | Method | Fam. | Venue | R8x4 | W16-2 | R18 | MBV1 | Src. | Notes | Reference |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | e^2KD | L | NeurIPS'24 | 76.1 | -- | 71.0 | -- | C T2; IN T3 | 3 runs & 5% | A. "T". X, 2024. (registry `p2024e`) |
"""


def test_rows_parse_and_escape():
    (r,) = rows(MD)
    assert r[:2] == ("e^2KD", "p2024e")
    line = tex_row(r)
    assert line.startswith(r"e\^{}2KD~\citep{p2024e} & L & NeurIPS'24 & 76.1 & -- & 71.0 & --")
    assert r"C~T2; IN~T3 & 3 runs \& 5\% \\" in line


def test_dagger_and_backslash():
    from scripts.build_supplement import esc
    assert esc(r"DiffKD\dagger 72.49") == r"DiffKD$^\dagger$ 72.49"
    assert esc("a\\b") == r"a\textbackslash{}b"
