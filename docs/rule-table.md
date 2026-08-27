
### RootDataEntity
| Property | Requirement | Description | Preconditions | Comments |
|---|---|---|---|---|
| `@id` | MUST | Identifies the Root Data Entity. The metadata descriptor's `about` MUST use exactly the same value. | | |
| `@type` | MUST | `Dataset`, or an array containing `Dataset`. | | |
| `conformsTo` | MUST | This profile's IRI and the IRI of each declared module; other application profiles MAY be present. Each profile IRI MUST also be described by a contextual entity. See [Conformance and Modules](https://github.com/eScienceLab/Five-Safes-RO-Crate/blob/1.0/docs/index.md#conformance-and-modules). | | |
| `identifier` | MUST, exactly one | The canonical RO-Crate identifier: an absolute IRI in `{"@id": "..."}` form not identifying a [`PropertyValue`](https://github.com/eScienceLab/Five-Safes-RO-Crate/blob/1.0/docs/index.md#record-and-ro-crate-identifiers). | | |
| `dct:isVersionOf` | MUST, exactly one | The activity record identifier, an absolute IRI. | | |
| `name` | MUST | Names the activity record. | | |
| `description` | MUST | Describes the work the activity record covers. | | |
| `dateCreated` | MUST, exactly one | When this representation was created. | | |
| `dateModified` | MUST, exactly one if a working record has changed since creation; <br> <br> MUST NOT on a snapshot | The most recent actual change. | | |
| `datePublished` | MUST, exactly one | When this representation was first published. A snapshot becomes immutable at this time. | | |
| `license` | SHOULD, on a published RO-Crate | Describes the licence of the output data, either an open licence or restrictive, TRE-specific conditions of access. | | |
| `publisher` | SHOULD | The `Organization` that published this representation. | | |
| `version` | MUST, exactly one on a snapshot; <br> <br> MUST NOT, on a working record | A positive JSON integer. See [Representation State](https://github.com/eScienceLab/Five-Safes-RO-Crate/blob/1.0/docs/index.md#representation-state). | | |
| `pav:previousVersion` | MUST, exactly one on a snapshot after the first; <br> <br> MUST NOT, otherwise | The canonical RO-Crate identifier of the direct predecessor. | | |
| `hasPart` | MUST | Each data entity MUST be reachable from the root through `hasPart`, directly or through nested `Dataset` entities. | The RO-Crate holds or refers to [data entities](https://www.researchobject.org/ro-crate/specification/1.2/data-entities) | |
| `mentions` | MUST | References the processes recorded in this RO-Crate. | The `@graph` contains entities representing [processes](https://github.com/eScienceLab/Five-Safes-RO-Crate/blob/1.0/docs/index.md#processes) | |
