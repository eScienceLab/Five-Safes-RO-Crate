# Five Safes RO-Crate

An [RO-Crate](https://www.researchobject.org/ro-crate/) profile for recording and exchanging the activity and provenance of work in Trusted Research Environments (TREs), such as the assets (e.g. datasets, outputs) they hold, the processes applied to them, and the contexts (e.g. people, organisations, agreements) involved.

This is the 1.0 Working Draft. [Five Safes RO-Crate 0.4](https://w3id.org/5s-crate/0.4) is maintained at [trefx/5s-crate](https://github.com/trefx/5s-crate).

## Contents

* [Profile Specification](docs/index.md)
* [Quick Reference](docs/quick-reference.md)
* Modules
    * Data Preparation: [Free-Text Deidentification](docs/modules/free-text-deidentification.md)
    * Execution: [Cohort Discovery](docs/modules/cohort-discovery.md), [Workflow Execution](docs/modules/workflow-execution.md)
    * Output Checking: [Statistical Outputs](docs/modules/statistical-output-checking.md), [Trained Models](docs/modules/trained-model-output-checking.md)

## Building the documentation

With Python 3 and pip, create a virtual environment and install the dependencies:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python -m mkdocs build
```

The generated site is in `site/`. It includes the Profile Crates
(`ro-crate-metadata.json` at the site root and in each module folder). The
GitHub Actions build also adds their `ro-crate-preview.html`; to generate them
locally, run with Node.js:

```sh
for crate in site/ro-crate-metadata.json site/modules/*/ro-crate-metadata.json site/examples/*/ro-crate-metadata.json; do
  npx --yes --package ro-crate-html@0.1.6 rochtml "$crate"
  sed -i '1s/^/<!DOCTYPE html>\n/' "$(dirname "$crate")/ro-crate-preview.html"
done
```

The core Profile Crate also holds [MASP](https://github.com/Language-Research-Technology/ro-crate-masp)
rules, from which the build generates `rules/index.html` using the template
[`masp/profile-text.md`](masp/profile-text.md); the Statistical Output Checking
module's rules likewise become `modules/statistical-output-checking/rules/index.html`
from [`masp/statistical-output-checking-text.md`](masp/statistical-output-checking-text.md).
To generate the core page locally:

```sh
mkdir -p /tmp/masp site/rules && cp site/ro-crate-metadata.json /tmp/masp/
npx --yes --package @crate-works/ro-crate-masp-tools@0.1.0 generate-masp-docs \
  /tmp/masp/ro-crate-metadata.json masp/profile-text.md /tmp/masp/profile-documentation.md
sed 's|rel="describedby" href="ro-crate-metadata.json"|rel="describedby" href="../ro-crate-metadata.json"|' \
  /tmp/masp/index.html > site/rules/index.html
```

For a live local preview, run
`python -m mkdocs serve` and open <http://127.0.0.1:8000/>.

Alternatively, build with Docker from the repository root:

```sh
docker run --rm --user "$(id -u):$(id -g)" -e HOME=/tmp \
  -v "$PWD:/docs" -w /docs python:3.12-slim \
  sh -c 'python -m pip install --user -r requirements.txt && python -m mkdocs build'
```

For a live preview with Docker, run:

```sh
docker run --rm --user "$(id -u):$(id -g)" -e HOME=/tmp \
  -v "$PWD:/docs" -w /docs -p 8000:8000 python:3.12-slim \
  sh -c 'python -m pip install --user -r requirements.txt && python -m mkdocs serve --dev-addr 0.0.0.0:8000'
```

Pushes to the `1.0` branch build and deploy the site using GitHub Actions.
In the repository's **Settings > Pages**, set the source to **GitHub Actions**
to enable deployment. Pull requests build the site without deploying it.
The workflow also checks Markdown for common mistakes and retains the generated
site as a `documentation-preview` artifact for three days. Download and extract
the artifact from the workflow run, then serve it locally, for example with
`python3 -m http.server 8000 --directory documentation-preview`.

## Validating RO-Crates

An RO-Crate can be checked against the profile with the SHACL shapes in
[`docs/shacl/`](docs/shacl/), generated from the Profile Crates' MASP rules, and
[rocrate-validator](https://github.com/crs4/rocrate-validator) (tested with
0.14.0). rocrate-validator does not yet find these shapes from the Profile
Crate (its `validation` resource) or from the profile identifier, so give a
local copy of the folder with `--extra-profiles-path`:

```sh
git clone https://github.com/eScienceLab/Five-Safes-RO-Crate.git
python3 -m pip install roc-validator
rocrate-validator validate --extra-profiles-path Five-Safes-RO-Crate/docs/shacl path/to/crate/
```

The validator chooses the profile from the crate's root `conformsTo`: a crate
that declares the Statistical Output Checking module is checked against the
module's rules and the core rules, and one that declares only the core profile
against the core rules. To choose the profile yourself, add
`-p five-safes-1.0` or `-p five-safes-statistical-output-checking-1.0` (the
identifiers have no `-DRAFT`, as the validator takes the version number from the
profile identifier). Other useful options are `-l REQUIRED` to report only
failed requirements, `--no-paging` to print the report without a pager and
`-f json` for a machine-readable report. The crate folder must include its
data files, as the validator checks that every file described is present.

Every rule becomes a REQUIRED check. The shapes check every entity of a class,
so they are stricter than `masp-validate`, which checks entities only as far as
it counts them (see [`tests/masp/`](tests/masp/)). A rule that an `@id` must be
an absolute IRI cannot be checked, as a local `#identifier` is absolute once
parsed as RDF.

The shapes are generated with `masp_to_shacl.py` from the `ro-crate-masp` skill
of [ro-crate-skills](https://github.com/stain/ro-crate-skills). Regenerate them
whenever the MASP rules change, using the
[RO-Crate 1.3 context](https://w3id.org/ro/crate/1.3/context) to map terms:

```sh
curl -sL -o ro-crate-1.3-context.jsonld https://w3id.org/ro/crate/1.3/context
python3 masp_to_shacl.py docs/ro-crate-metadata.json docs/shacl \
  --token five-safes --version 1.0-DRAFT --context ro-crate-1.3-context.jsonld
python3 masp_to_shacl.py docs/modules/statistical-output-checking/ro-crate-metadata.json docs/shacl \
  --token five-safes-statistical-output-checking --version 1.0-DRAFT --context ro-crate-1.3-context.jsonld
```

## Feedback

Comments and suggestions are welcome as [GitHub issues](https://github.com/eScienceLab/Five-Safes-RO-Crate/issues). See [CONTRIBUTING](CONTRIBUTING.md).

## License

The Profile Specification is licensed under the [MIT License](LICENSE.md). Example RO-Crates and Profile Crates are in the public domain under [CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/).
