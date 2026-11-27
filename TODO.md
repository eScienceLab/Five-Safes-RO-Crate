# TODO

## Restructure the repository for versioning

The specification, modules and Profile Crates are currently built from the
repository root and published at the root of the site, which the
`https://w3id.org/5s-crate/1.0-DRAFT` permalinks redirect to. Before a second
version can be published alongside 1.0, the repository needs a layout that
serves each version (and its Profile Crates) at its own path.

Decisions needed first:

* Module versioning: module permalinks are currently nested under the core
  version (`https://w3id.org/5s-crate/1.0-DRAFT/modules/...`), so a module
  cannot be revised without a new core version, and third-party modules cannot
  follow the same pattern. Decide whether modules get their own version
  numbers and permalinks.
* Cross-version interoperability: which core versions a module version works
  with, and how a crate declaring one version is read by tools that know
  another.
* Term namespaces: terms such as `https://w3id.org/5s-crate/1.0-DRAFT#EgressSnapshot`
  and the module outcome terms carry the version, including `-DRAFT`, so
  crates written against the draft use different term IRIs from 1.0. Decide
  whether terms move to a namespace that is stable across versions.
