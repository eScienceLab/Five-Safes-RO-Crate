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

The generated site is in `site/`. It includes the Profile Crate
(`ro-crate-metadata.json` at the site root). The
GitHub Actions build also adds its `ro-crate-preview.html`; to generate it
locally, run with Node.js:

```sh
for crate in site/ro-crate-metadata.json site/examples/*/ro-crate-metadata.json; do
  npx --yes --package ro-crate-html@0.1.6 rochtml "$crate"
  sed -i '1s/^/<!DOCTYPE html>\n/' "$(dirname "$crate")/ro-crate-preview.html"
done
```

The core Profile Crate also holds [MASP](https://github.com/Language-Research-Technology/ro-crate-masp)
rules, from which the build generates `rules/index.html` using the template
[`masp/profile-text.md`](masp/profile-text.md). To generate it locally:

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
[`docs/shacl/`](docs/shacl/), generated from the Profile Crate's MASP rules, and
[rocrate-validator](https://github.com/crs4/rocrate-validator) (tested with
0.14.0). rocrate-validator does not yet find these shapes from the Profile
Crate (its `validation` resource) or from the profile identifier, so give a
local copy of the folder with `--extra-profiles-path`:

```sh
git clone https://github.com/eScienceLab/Five-Safes-RO-Crate.git
python3 -m pip install roc-validator
rocrate-validator validate --extra-profiles-path Five-Safes-RO-Crate/docs/shacl path/to/crate/
```

The validator chooses the profile from the crate's root `conformsTo`. To choose
it yourself, add `-p five-safes-1.0` (the identifier has no `-DRAFT`, as the
validator takes the version number from the profile identifier). Other
useful options are `-l REQUIRED` to report only failed requirements,
`--no-paging` to print the report without a pager and `-f json` for a
machine-readable report. The crate folder must include its
data files, as the validator checks that every file described is present.

Every rule becomes a REQUIRED check. The shapes check every entity of a class,
so they are stricter than `masp-validate`, which checks entities only as far as
it counts them (see [`tests/masp/`](tests/masp/)). A rule that an `@id` must be
an absolute IRI cannot be checked, as a local `#identifier` is absolute once
parsed as RDF.

The shapes are generated files: to change what they check, change the MASP
rules in the Profile Crate and regenerate them (see below).

## Updating the Profile Crate

The Profile Crate, [`docs/ro-crate-metadata.json`](docs/ro-crate-metadata.json),
is edited directly, and its MASP rules are the source for the rules pages
and the SHACL shapes. When the specification changes, update the rules'
counts, ranges and descriptions to match, then:

1. Regenerate the SHACL shapes in [`docs/shacl/`](docs/shacl/) with
   `masp_to_shacl.py`, found in `skills/ro-crate-masp/scripts/` of
   [ro-crate-skills](https://github.com/stain/ro-crate-skills) (Python 3,
   standard library only). It maps terms with the RO-Crate 1.3 context, and
   rewrites the profile's `profile.ttl` and `must/0_masp_rules.ttl`:

   ```sh
   curl -sL -o ro-crate-1.3-context.jsonld https://w3id.org/ro/crate/1.3/context
   python3 masp_to_shacl.py docs/ro-crate-metadata.json docs/shacl \
     --token five-safes --version 1.0-DRAFT --context ro-crate-1.3-context.jsonld
   ```

   Run the commands from the repository root, so the generated files name the
   Profile Crates by relative paths. Check what the script prints as not
   converted.
2. Check the examples and the fixtures in [`tests/masp/`](tests/masp/) with
   `masp-validate` and with rocrate-validator, as described there: valid crates
   must pass and each invalid fixture must fail. Add a fixture for each new
   requirement.
3. Regenerate the spreadsheet next to the Profile Crate (see below).
4. Build the site and look at the generated rules pages (see
   [Building the documentation](#building-the-documentation)).

The Profile Crate has a spreadsheet copy, `ro-crate-metadata.xlsx`, with a
sheet per type: the class rules are on `@type=rdfs_Class` and the property
rules on `@type=rdf_Property`, which can be easier to review than the JSON.
The JSON stays the source. Regenerate a spreadsheet from it in a scratch
folder, where the newer of the two files wins, and copy only the spreadsheet
back:

```sh
mkdir -p /tmp/xlsx && cp docs/ro-crate-metadata.json /tmp/xlsx/
npx --yes --package @crate-works/ro-crate-masp-tools@0.1.0 generate-masp-docs -x \
  /tmp/xlsx/ro-crate-metadata.json masp/profile-text.md /tmp/xlsx/profile-documentation.md
cp /tmp/xlsx/ro-crate-metadata.xlsx docs/
```

The rules can also be edited in the spreadsheet. `generate-masp-docs` 0.1.0
then rewrites the whole JSON when it syncs the edits back: it declares
RO-Crate 1.2 and adds `@vocab` to the context, writes counts as strings,
adds `isPartOf` and an `identifier` that the Profile Crate does not have, adds
the vocabularies to the rules, reorders lists, and replaces prefixes in the
context with their names. So sync in
the scratch folder and merge the result with
[`masp/fix_xlsx_sync.py`](masp/fix_xlsx_sync.py), which keeps only the edits:

```sh
mkdir -p /tmp/xlsx && cp docs/ro-crate-metadata.json docs/ro-crate-metadata.xlsx /tmp/xlsx/
touch /tmp/xlsx/ro-crate-metadata.xlsx  # the newer file wins
npx --yes --package @crate-works/ro-crate-masp-tools@0.1.0 generate-masp-docs -x \
  /tmp/xlsx/ro-crate-metadata.json masp/profile-text.md /tmp/xlsx/profile-documentation.md
python3 masp/fix_xlsx_sync.py /tmp/xlsx/ro-crate-metadata.json docs/ro-crate-metadata.json
git diff docs/ro-crate-metadata.json
```

Then check the result and regenerate the SHACL shapes as above.

## Feedback

Comments and suggestions are welcome as [GitHub issues](https://github.com/eScienceLab/Five-Safes-RO-Crate/issues). See [CONTRIBUTING](CONTRIBUTING.md).

## License

The Profile Specification and its Profile Crates are licensed under the [MIT License](LICENSE.md). Example RO-Crates are in the public domain under [CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/).
