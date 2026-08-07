# Contributing

Suggestions, questions, and corrections are welcome as [GitHub issues](https://github.com/eScienceLab/Five-Safes-RO-Crate/issues).

Pull requests against the specification and modules (under [`docs/`](docs/)) are also welcome; for more substantive changes, please open an issue first so the change can be discussed.

## Previewing the documentation

The documentation is built with [MkDocs](https://www.mkdocs.org/). To preview it locally with live reload:

```bash
uvx --with mkdocs-mermaid2-plugin mkdocs serve
```

or, without [uv](https://docs.astral.sh/uv/): `pip install mkdocs mkdocs-mermaid2-plugin`, then `mkdocs serve`.
