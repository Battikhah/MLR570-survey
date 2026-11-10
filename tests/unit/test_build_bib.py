from scripts.build_bib import check, entry

BASE = {"type": "paper", "title": "A & B", "authors": ["Ann One", "Bob Two"], "date": 2024,
        "urls": {"official": "https://x.org/p"}, "identifiers": {"doi": None, "arxiv": None}}


def test_entry_kinds_and_fields():
    conf = entry({**BASE, "id": "c", "venue": "CVPR 2024", "status": "published"})
    assert conf.startswith("@inproceedings{c,")
    assert "booktitle = {CVPR}" in conf and "author = {Ann One and Bob Two}" in conf
    assert "title = {{A \\& B}}" in conf and "note" not in conf
    jour = entry({**BASE, "id": "j", "venue": "Transactions on Machine Learning Research (TMLR)",
                  "status": "published"})
    assert jour.startswith("@article{j,") and "journal = " in jour
    pre = entry({**BASE, "id": "p", "venue": None, "status": "preprint",
                 "identifiers": {"doi": None, "arxiv": "2501.00001"}})
    assert pre.startswith("@misc{p,") and "eprint = {2501.00001}" in pre
    assert "note = {Preprint}" in pre


def test_check_missing_and_unverified(tmp_path):
    (tmp_path / "s.tex").write_text(r"see \citet{a} and \citep[p.~2]{b, c} \cite{zz}")
    recs = [{"id": "a", "status": "published"}, {"id": "b", "status": "unverified"},
            {"id": "c", "status": "preprint"}]
    missing, unverified = check(recs, tmp_path)
    assert missing == ["zz"]
    assert unverified == ["b"]


def test_escaping_of_bibtex_specials_in_title_author_venue():
    r = {**BASE, "id": "e", "title": "50% of $x_1$ ^ ~ #1", "authors": ["A_B"],
         "venue": "Journal of Imaging", "status": "published"}
    out = entry(r)
    assert out.startswith("@article{e,") and "journal = {Journal of Imaging}" in out
    assert r"50\% of \$x\_1\$ \^{} \~{} \#1" in out
    assert r"author = {A\_B}" in out


def test_cite_variants_and_comments(tmp_path):
    (tmp_path / "s.tex").write_text(
        "\\citealp{x} \\citeauthor{y} \\citep*{z} \\citet[see][p. 3]{a,b}\n"
        "% \\cite{commented} is ignored\n"
        "50\\% \\cite{kept} % trailing \\cite{dropped}\n"
    )
    recs = [{"id": k, "status": "published"} for k in "x y z a b kept".split()]
    missing, unverified = check(recs, tmp_path)
    assert missing == [] and unverified == []


def test_year_field_overrides_date_for_citation_year():
    r = {**BASE, "id": "y", "date": "2023-10-05", "year": 2025, "venue": "TMLR",
         "status": "published"}
    assert "year = {2025}" in entry(r)
    assert "year = {2024}" in entry({**BASE, "id": "n", "venue": "X", "status": "published"})


def test_venue_cleaned_and_venue_year_beats_posting_date():
    r = {**BASE, "id": "v", "date": "2023-11-22", "venue": "ICCV 2025 (Highlight)",
         "status": "published"}
    assert "booktitle = {ICCV}" in entry(r) and "year = {2025}" in entry(r)
    j = entry({**BASE, "id": "t", "venue": "IEEE TPAMI 47(7), 2025", "status": "published"})
    assert "journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence}" in j
    m = entry({**BASE, "id": "m", "venue": "TMLR (02/2026)", "status": "published"})
    assert "journal = {Transactions on Machine Learning Research}" in m and "year = {2026}" in m
    a = entry({**BASE, "id": "a", "venue": "arXiv preprint (author-stated: IEEE TNNLS)",
               "status": "preprint"})
    assert a.startswith("@misc{a,")
