# Five Safes RO-Crate 1.0-DRAFT: machine-actionable rules

These pages are generated from the [MASP](https://github.com/Language-Research-Technology/ro-crate-masp) rules in the Five Safes RO-Crate [Profile Crate](../ro-crate-metadata.json). The [profile specification](../index.html) is normative; the rules restate its requirements for validators, editors and this documentation.

## Reading the rules

- Each class rule describes one kind of entity, such as a Root Data Entity, a process or a person, and names the schema.org or PROV type it specialises. A process matches the rule for its kind only when its `@type` includes both that kind, such as `CreateAction`, and `prov:Activity`; every kind inherits the rules for processes.
- The same property can have different rules on different classes. For example, `object` is suggested on any process but required on decisions, exchanges and requests, and `version` is an integer on a Root Data Entity but text on an asset.
- A property with a minimum count of 1 is required. A property with no minimum is suggested: the specification's SHOULD and MAY requirements, and requirements that only apply in some cases, such as on a snapshot but not a working record. Each rule's description states the full requirement.
- A property with no range accepts any value, typically an IRI that need not be described in the RO-Crate, such as the activity record identifier. Where the specification fixes the value, as for `actionStatus` or the core profile in the Root Data Entity's `conformsTo`, the range is a value constraint that matches the IRI without it being described.

## Checking an RO-Crate

```sh
npm install @crate-works/ro-crate-masp-validator
npx masp-validate crate/ro-crate-metadata.json profile/ro-crate-metadata.json
```

The validator reports class counts only: an entity that fails its property rules is not counted, so a problem with a process usually appears as an error about the metadata descriptor, whose Root Data Entity no longer matches. Use `--json` to see the property errors. Requirements that need comparisons or conditions, such as version ordering between snapshots or `endTime` only on completed or failed processes, are not checked by these rules.

${rules.all}

## Value lists

${rules.allItemLists}
