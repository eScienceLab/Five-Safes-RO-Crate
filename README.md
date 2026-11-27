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

## Feedback

Comments and suggestions are welcome as [GitHub issues](https://github.com/eScienceLab/Five-Safes-RO-Crate/issues). See [CONTRIBUTING](CONTRIBUTING.md).

## License

The Profile Specification is licensed under the [MIT License](LICENSE.md). Example RO-Crates and Profile Crates are in the public domain under [CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/).
