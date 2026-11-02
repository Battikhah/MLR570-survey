from scripts.build_literature_docs import records


def test_generated_docs_cover_every_source_once():
    rows = records()
    ids = [r["id"] for r in rows]
    assert len(ids) == len(set(ids))
    matrix = open("docs/literature/literature-matrix.md", encoding="utf-8").read()
    bibliography = open("docs/literature/annotated-bibliography.md", encoding="utf-8").read()
    assert all(matrix.count(f"| {i} |") == 1 and bibliography.count(f"[{i}]") == 1 for i in ids)
    assert "unverified" in matrix.lower()
