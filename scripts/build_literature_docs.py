#!/usr/bin/env python3
"""Build deterministic literature summaries from the source registries."""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_records(path):
    with path.open(encoding="utf-8") as f:
        records = yaml.safe_load(f) or []
    return records


def records():
    sources = load_records(ROOT / "literature/sources.yaml")
    repos_path = ROOT / "literature/repositories.yaml"
    if repos_path.exists():
        sources += load_records(repos_path)
    return sorted(sources, key=lambda r: r["id"])


def authors(record):
    names = record.get("authors") or []
    return names[0] + (" et al." if len(names) > 1 else "")


def generate():
    rows = records()
    table = ["# Literature matrix", "", "| ID | Title | Authors | Year | Venue | Status | Topics | Relevance |", "|---|---|---|---:|---|---|---|---|"]
    for r in rows:
        year = str(r.get("date") or "")[:4]
        topics = ", ".join(r.get("topics") or [])
        fields = [r["id"], r.get("title") or "", authors(r), year, r.get("venue") or "", r.get("status") or "unverified", topics, r.get("relevance") or ""]
        table.append("| " + " | ".join(str(v).replace("|", "\\|").replace("\n", " ") for v in fields) + " |")
    grouped = {}
    for r in rows:
        topic = (r.get("topics") or ["uncategorized"])[0]
        grouped.setdefault(topic, []).append(r)
    bib = ["# Annotated bibliography", ""]
    for topic, entries in sorted(grouped.items()):
        bib.extend([f"## {topic}", ""])
        for r in entries:
            date = str(r.get("date") or "n.d.")
            entry = f"[{r['id']}] {authors(r)}, ‘{r.get('title') or ''},’ {r.get('venue') or ''}, {date}. Status: {r.get('status') or 'unverified'}. {r.get('relevance') or ''}"
            bib.extend(["- " + entry, ""])
    target = ROOT / "docs/literature"
    target.mkdir(parents=True, exist_ok=True)
    (target / "literature-matrix.md").write_text("\n".join(table) + "\n", encoding="utf-8")
    (target / "annotated-bibliography.md").write_text("\n".join(bib), encoding="utf-8")


if __name__ == "__main__":
    generate()
