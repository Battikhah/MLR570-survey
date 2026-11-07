# literature/

| Path | Purpose | Committed? |
|---|---|---|
| `sources.yaml` | Machine-readable registry of every source (papers, repos, datasets) | yes |
| `notes/<id>.md` | Reading notes per source | yes |
| `pdfs/<id>.pdf` | Local copies of freely available PDFs | **no** (git-ignored) |

## `sources.yaml` record schema

```yaml
- id: varam2026pcd            # firstauthorYEARkeyword, lowercase, unique
  type: paper                 # paper | repository | dataset | supplementary | webpage
  title: "Exact title as published"
  authors: ["First Last", "First Last"]
  date: 2026-01-15            # publication / release date (YYYY or YYYY-MM-DD)
  year: 2026                  # optional: venue year for citations when date is an earlier arXiv date
  venue: "TMLR"               # journal/conference/arXiv/GitHub; null if unknown
  status: published           # published | accepted | preprint | under-review | unverified
  urls:
    official: https://...     # publisher / OpenReview / proceedings page
    arxiv: https://arxiv.org/abs/...
    code: https://github.com/...
  identifiers: {doi: null, arxiv: null}
  license: null               # REQUIRED for repositories/datasets (e.g. MIT, CC-BY-4.0, "none stated")
  verified_by: "how metadata was checked (e.g. 'arXiv abs page + OpenReview forum, 2026-11-02')"
  relevance: "1–2 sentences: why it matters to this project"
  topics: [pcd, gradient-conflict, federated]
  local_pdf: false            # true if saved under literature/pdfs/<id>.pdf
```

Rules: no invented fields; unknown values are `null`; anything not checked against a primary source
is `status: unverified`. Repository provenance must show the repo is owned/linked by the paper's authors.
