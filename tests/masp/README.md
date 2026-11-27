# MASP rule fixtures

RO-Crate metadata files for checking the MASP rules in the core
[Profile Crate](../../docs/ro-crate-metadata.json). The crates in
[`docs/examples/`](../../docs/examples/) are the main valid cases; `valid/` adds
variants of them, and each file in `invalid/` breaks one requirement of the
specification.

```sh
npm install @crate-works/ro-crate-masp-validator
for f in docs/examples/*/ro-crate-metadata.json tests/masp/valid/*.json tests/masp/invalid/*.json; do
  npx masp-validate "$f" docs/ro-crate-metadata.json > /dev/null 2>&1
  echo "$? $f"
done
```

Valid files exit 0 and invalid files exit 2.

## Statistical Output Checking module

[`docs/examples/statistical-review-42/`](../../docs/examples/statistical-review-42/)
is the valid case, and each file in `statistical-output-checking/invalid/`
breaks one requirement of the module. Check them against the module's Profile
Crate, and the valid one against the core Profile Crate as well:

```sh
for f in docs/examples/statistical-review-42/ro-crate-metadata.json tests/masp/statistical-output-checking/invalid/*.json; do
  npx masp-validate "$f" docs/modules/statistical-output-checking/ro-crate-metadata.json > /dev/null 2>&1
  echo "$? $f"
done
```

`53-bad-refusal-with-outcome-term.json` exits 0 with `masp-validate` 0.1.0,
which reports a failing rule only for entities it counts or reaches through a
range; validators that check every entity, such as wpsld, report it.

## SHACL

The same files can be checked with the SHACL shapes in
[`docs/shacl/`](../../docs/shacl/), which apply the property rules to every
entity of a class. Copy each fixture into a folder with the payload files of
the example it varies (`feasibility-working-record` for the core fixtures,
`statistical-review-42` for the module's) and run:

```sh
pip install roc-validator
rocrate-validator validate -l REQUIRED --extra-profiles-path docs/shacl -p five-safes-1.0 <folder>
rocrate-validator validate -l REQUIRED --extra-profiles-path docs/shacl -p five-safes-statistical-output-checking-1.0 <folder>
```

Every invalid file fails except `95-bad-local-person-id.json`: once parsed as
RDF, a local `#analyst` identifier is an absolute IRI, so the shapes cannot
tell it from an ORCID. `53-bad-refusal-with-outcome-term.json` fails here.
