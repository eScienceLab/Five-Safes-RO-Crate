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

## SHACL

The same files can be checked with the SHACL shapes in
[`docs/shacl/`](../../docs/shacl/), which apply the property rules to every
entity of a class. Copy each fixture into a folder with the payload files of
the example it varies (`feasibility-working-record`) and run:

```sh
pip install roc-validator
rocrate-validator validate -l REQUIRED --extra-profiles-path docs/shacl -p five-safes-1.0 <folder>
```

Every invalid file fails.
