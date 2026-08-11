# Five Safes RO-Crate 1.0

Authors:

1. Alexander Hambley, The University of Manchester <https://orcid.org/0000-0003-1193-6632>
2. Warren Del-Pinto, The University of Manchester <https://orcid.org/0000-0003-3307-9432>
3. Douglas Lowe, The University of Manchester <https://orcid.org/0000-0002-1248-3594>
4. Eli Chadwick, The University of Manchester <https://orcid.org/0000-0002-0035-6475>
5. Stian Soiland-Reyes, The University of Manchester <https://orcid.org/0000-0001-9842-9718>

This document specifies a profile of [RO-Crate](https://w3id.org/ro/crate) for recording and exchanging the activity of Trusted Research Environments (TREs).

* Permalink: <https://w3id.org/5s-crate/1.0>
* Version: 1.0
* Status: Working Draft
* Release notes: <https://github.com/eScienceLab/Five-Safes-RO-Crate/releases>
* Published: 2027-XX-XX
* Comments and suggestions: <https://github.com/eScienceLab/Five-Safes-RO-Crate/issues>

_The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [[RFC2119](https://doi.org/10.17487/RFC2119)] [[RFC8174](https://doi.org/10.17487/RFC8174)] when, and only when, they appear in all capitals, as shown here._

!!! note 
    All references to schema.org types/properties/instances use the prefix `http://schema.org/` (not https) to correspond with their official JSON-LD context.


## Introduction

What a Five Safes RO-Crate ("Five Safes Crate") is, who it serves (researchers, TRE operators, auditors, the public), how its content evidences the Five Safes framework, and how this specification relates to RO-Crate 1.3, SATRE, and so on.

## Concepts

This section explains the core ideas in plain English. You do not need to know about RO-Crate to understand it.

### The TRE Activity Record

A Five Safes Crate is a **TRE Activity Record**, or "record" for short. It is a versioned account of activity in a TRE. As a rough guide, each record covers one piece of work that the TRE governs as a unit. If the work involves several nodes, the record covers them all.

The [working record and each snapshot](#working-record-and-snapshots) are both Five Safes Crates. They are the same kind of document, but they capture the work at different points in its life.

A record grows as the work progresses. It brings together what the work produces and requires: queries and analyses, decisions about them, the agreements that govern them, and any outputs that are released. It describes the data involved in the work, but sensitive data stays where it is governed. In such a case, the record [refers to that data but does not contain it](#structure-of-a-five-safes-crate). One record may cover a single cohort discovery query answered within a minute; another may cover a study lasting months or years. Both are the same kind of record.

This specification does not define exactly where one record ends and another begins because TREs govern work in different ways. For example, one TRE may treat each query in a discovery portal as a separate unit of work, while another may treat an entire workspace in an interactive analysis environment as one unit. 

<!-- The agreements provide the most reliable boundary: work governed together under one set of agreements belongs in one record. -->

A record can include only activity that the TRE could observe. A portal may record every query as it happens. An interactive workspace may capture only the governance points around a session, with the analysis between them summarised when outputs leave. Both are valid records.

!!! note
    This specification deliberately has no "project" item in a record. The word can mean too many different things: a grant, a study, a workspace, or an access agreement. Instead, the specific things that "project" might refer to appear in the record in their own right.

When work spans several TREs or several nodes in a federated network, the aim is still to keep one record for the whole piece of work. That record includes activity from every node. Each node still keeps any operational logs that its regulators require. This specification asks for the work itself to be reported once, in one place. Who maintains the record - for example, the coordinating service, the lead TRE, or the portal - is a deployment decision.

### Assets, Processes, Context

Every item in a record belongs to one of three categories.

| Category | Description |
|---|---|
| Assets | Artefacts that processes consume or produce, such as protocols. |
| Processes | Things that happen, including activities that have been requested but have not yet run. |
| Context | People, organisations, agreements, and the TRE itself. |

**Assets** are durable items such as datasets and extracts, analysis outputs, trained models, software, and protocol documents. Two rules are important:

- A protocol, such as a deidentification procedure, workflow, or standard operating procedure, is an asset rather than a process. It can be versioned, approved, and reused. Following the protocol on a particular occasion is a process.

- Derived data is a separate asset. For example, a deidentified copy of a dataset is different from its source and has its own history.

**Processes** are things that happen. Examples include executing a query, running a workflow, checking an output, and applying a protocol. A completed process records what it consumed and produced, which protocol it followed, when it ran, who was responsible for it, and any software it used.

A process can appear in the record before it happens. For example, a requested analysis that is awaiting a decision is already part of the record and is marked as not yet run. It may later complete, fail, be withdrawn, or be refused without ever running. The refusal is itself a decision in the record. Some processes may not produce a new asset.

**Context** records who and what are involved, and under what authority: people, organisations, agreements, and the TRE itself, together with credentials, training, and policies. Processes do not operate on context in the same way that they operate on assets. However, context can be the subject of a process. Signing an agreement, granting a credential, and accrediting a researcher are all processes whose subject is context. Each context item is recorded once and referred to wherever it is needed.

These categories also show how a record provides evidence for the Five Safes. Safe projects are evidenced by the record as a whole, including the agreements governing the work and the decisions that allowed it to proceed; safe people and safe settings are evidenced in context; safe data is evidenced in assets; and safe outputs are evidenced by the checking processes that control what may leave.

### Working Record and Snapshots

The working record reflects the current understanding of the work. It changes as queries run, decisions are returned, and outputs appear. A snapshot is a complete copy of the record taken at a meaningful moment. It freezes the record as it stood then and is never edited afterwards. The working record and each snapshot have separate, stable identities. Each snapshot after the first links to the previous one, so the snapshots trace the record's history.

<!-- !!! note
    Where several parties contribute in parallel, such as in a federated system, that history can branch and reconverge; merging the branches is the job of whoever maintains the record. -->

The working record and its snapshots answer different questions. The working record keeps the same identity throughout its life, meaning "this piece of work". A snapshot has its own identity, meaning "this piece of work, exactly as it stood at that moment". This makes it clear exactly which version an approval applies to.

A snapshot is not the same as "one run". It may contain no runs, one run, or many runs. How the work is divided into processes and when a snapshot is taken are separate choices. Whoever maintains the record decides when to take a snapshot, with one expectation: every decision and every exchange refers to an existing snapshot. Without a snapshot, an approval has no fixed version to point to, so it preserves no evidence of what was approved. Examples of when to take a snapshot include when something is submitted, when a result leaves, and when the record closes; that is, when no further activity is expected.

<!-- TODO: Revisit above when we have example processes -->

Snapshots preserve provenance. A decision concerns the record as it stood at the time. The snapshot preserves what the record said then, so that information remains available for later inspection even if the working record has moved on or the data it refers to is no longer available under the data access agreement.

### Snapshots as Messages



## Structure of a Five Safes Crate

A Five Safes Crate is an RO-Crate: a directory, or an archive of one, containing a metadata file that describes its contents. This section states what that metadata file contains for the RO-Crate to be a Five Safes Crate.

### Metadata File

The `ro-crate-metadata.json` metadata file MUST conform to [RO-Crate 1.3](https://www.researchobject.org/ro-crate/specification/1.3/), and its descriptor MUST declare the version it conforms to. For RO-Crate 1.3:

```json
{
  "@type": "CreativeWork",
  "@id": "ro-crate-metadata.json",
  "about": {"@id": "./"},
  "conformsTo": {"@id": "https://w3id.org/ro/crate/1.3"}
}
```

This profile defines no vocabulary of its own, so an RO-Crate conforming to the core profile needs no further context. The context SHOULD be given in the array form, so that an RO-Crate can extend it:

```json
{ "@context": ["https://w3id.org/ro/crate/1.3/context"],
  "@graph": [ ]
}
```

Terms from other published vocabularies are used as **values**, for example to say what kind of check or agreement something is. These are typically used in modules. Such a term MUST be written as a full absolute IRI, and MUST be given as `{"@id": "..."}` where it is the value of a property. A bare string is read as text rather than as a reference to the term, and a shortened form such as `ex:Thing` will not expand unless its prefix is bound. An RO-Crate SHOULD also describe the term with a contextual entity carrying its name and definition.

!!! note
    The RO-Crate context binds `pav`, `prov` and `dct` among others, so `pav:previousVersion` and `dct:isVersionOf` can be written in short form. Note that it binds `dct`, not `dcterms`.

A module MAY draw on vocabularies the core profile does not, such as the [Safe Haven Provenance ontology](https://w3id.org/shp) for governance processes. Where a module uses such a vocabulary only for values, the rule above is enough. Where it needs one for property names, the module declares its own context, and an RO-Crate conforming to that module gives both contexts.

### Root Data Entity

The root data entity is this RO-Crate: one representation of the record, either the working record or one snapshot of it. The record itself is a separate identifier that the RO-Crate refers to. Alongside the properties RO-Crate requires of any root data entity, this profile requires the following.

| Property | Requirement | Description |
|---|---|---|
| `@id` | MUST | `./`, as for any attached RO-Crate. |
| `@type` | MUST | `Dataset`, or an array containing `Dataset`. |
| `conformsTo` | MUST | Contains this profile's IRI, and the IRI of each module the RO-Crate declares. The array is unordered. Each IRI MUST also have a contextual entity, as RO-Crate requires. See [Conformance and Modules](#conformance-and-modules). |
| `identifier` | MUST | The stable IRI of this RO-Crate. See [Versioning and Snapshots](#versioning-and-snapshots). |
| `dct:isVersionOf` | MUST | The stable IRI of the record this RO-Crate represents. |
| `name` | MUST | Names the record. |
| `description` | MUST | Describes the work the record covers. |
| `datePublished` | MUST | When this representation of the record was written. For a snapshot, the moment it was frozen. |
| `license` | MUST | The terms under which this description may be used. This is not the licence of the data the record describes. |
| `version` | SHOULD | Distinguishes this RO-Crate from other representations of the record. |
| `hasPart` | MUST, if the RO-Crate holds or refers to data entities | Each data entity MUST be reachable from the root through `hasPart`, directly or through nested `Dataset` entities. |
| `mentions` | SHOULD | The processes recorded in this RO-Crate. |

An example root, with the RO-Crate's other entities omitted:

```json
{
  "@id": "./",
  "@type": "Dataset",
  "conformsTo": [
    {"@id": "https://w3id.org/5s-crate/1.0"},
    {"@id": "https://w3id.org/5s-crate/1.0/modules/cohort-discovery"}
  ],
  "identifier": {"@id": "https://tre72.example.org/activities/A123/versions/2"},
  "dct:isVersionOf": {"@id": "https://tre72.example.org/activities/A123"},
  "name": "Feasibility enquiry A123 (TRE72)",
  "description": "Cohort feasibility counts across two participating sites.",
  "datePublished": "2027-03-14T09:21:00Z",
  "license": {"@id": "https://spdx.org/licenses/CC-BY-4.0"},
  "version": "2",
  "pav:previousVersion": {
    "@id": "https://tre72.example.org/activities/A123/versions/1"
  },
  "hasPart": [{"@id": "query.sql"}],
  "mentions": [{"@id": "#enquiry-3f2b"}]
}
```

### Assets, Processes, and Context

The three categories are how this profile describes a record's contents. They are not structures in the metadata file.

| Category | Description |
|---|---|
| Assets | Data entities, reachable from `hasPart`. An asset the RO-Crate holds is a file or directory within it; an asset the RO-Crate refers to is a data entity with an absolute IRI. |
| Processes | Contextual entities, referenced from the root's `mentions`. |
| Context | Contextual entities, referenced from wherever they are relevant. |

### What a Five Safes Crate Contains and References 

An RO-Crate MAY hold artefacts that carry the work's governance, such as the text of a query, a protocol document, or a report. These are files within the RO-Crate, listed under `hasPart`.

Data that is governed where it lives MUST NOT be held in the RO-Crate. It is described instead as a [Web-based Data Entity](https://www.researchobject.org/ro-crate/specification/1.3/data-entities.html): a data entity whose `@id` is an absolute IRI, so the RO-Crate describes the data and lists it under `hasPart`, whilst the data itself stays where it is. A record can then travel without the data travelling with it. Whether an artefact may travel with a record is a question of governance.

Another RO-Crate MAY be held inside a Five Safes Crate, or referred to by its IRI. In either case it appears as a `Dataset` in `hasPart` with its own `conformsTo`; a referenced RO-Crate SHOULD declare `conformsTo` of `https://w3id.org/ro/crate`. Its own metadata file is not merged into this RO-Crate's graph, and this RO-Crate MUST NOT redescribe the entities inside it.

!!! note
    An asset the RO-Crate only refers to is still a first-class asset: processes name it as an input or output in the ordinary way.

## Assets

Asset types and their expected metadata, including catalogue entries for sensitive data held within the TRE; protocols as versionable and approvable assets that processes refer to.

## Processes

The "action pattern" for recording occurrences - inputs, outputs, instruments, agents, timing, and status - and how governance checks and decisions are typed, with manual versus automated checking expressed through who or what performed the action.

## Context

Captures people, organisations, credentials, agreements, working environment, and the TRE and its nodes.

## Versioning and Snapshots

A record exists as a working RO-Crate that changes, and as snapshots that do not. This section states how the two are identified and how snapshots relate to one another.

### RO-Crate Identifiers

A record has one identifier that never changes. Each RO-Crate representing it, whether the working record or a snapshot, has an identifier of its own.

| Identifier | Written as | Meaning |
|---|---|---|
| Record identifier | `dct:isVersionOf` on the root | The record across its whole life. It is the same in every RO-Crate that represents the record. |
| RO-Crate identifier | `identifier` on the root | This one representation of the record: the working record, or one snapshot. |

Both MUST be absolute IRIs, and MUST NOT be used by their minting authority to identify anything else. Either MAY be a URI that resolves over the web. A TRE that cannot expose resolvable identifiers, such as one with no external network access, still needs stable ones; a UUID URN is sufficient.

The RO-Crate identifier MUST be present when the RO-Crate is written, since a snapshot cannot be changed afterwards to add one. An RO-Crate MAY carry further identifiers, such as a persistent identifier assigned when a snapshot is later deposited somewhere; where that identifier is minted after the snapshot was frozen, it is recorded in a later snapshot rather than in the frozen one.

The following approach is one way to satisfy these rules, and is not required:

```
https://tre72.example.org/activities/A123             the record
https://tre72.example.org/activities/A123/current     the working record
https://tre72.example.org/activities/A123/versions/1  a snapshot
https://tre72.example.org/activities/A123/versions/2  a later snapshot
```

### Snapshots

A snapshot is a complete RO-Crate. It describes everything the record described at the moment it was taken, and is not changed afterwards: a correction is made by taking a later snapshot rather than by altering an earlier one.

Each snapshot after the first MUST identify the snapshot it follows, using `pav:previousVersion` pointing at that snapshot's RO-Crate identifier:

```json
{
  "@id": "./",
  "@type": "Dataset",
  "identifier": {"@id": "https://tre72.example.org/activities/A123/versions/2"},
  "dct:isVersionOf": {"@id": "https://tre72.example.org/activities/A123"},
  "version": "2",
  "pav:previousVersion": {
    "@id": "https://tre72.example.org/activities/A123/versions/1"
  }
}
```

The first snapshot of a record has no predecessor and omits the property.

!!! note
    `pav:previousVersion` is a subproperty of `prov:wasRevisionOf`, so a consumer that loads the Provenance, Authoring and Versioning (PAV) ontology can infer the PROV revision relationship without this profile defining one.

### What Snapshots Are For

A snapshot fixes what a claim was made about. A decision recorded in a record concerns the record as it stood at the time, and without a snapshot there is no fixed version for it to point at.

When to take a snapshot is for whoever maintains the record to decide. This profile does not require snapshots at fixed intervals.

<!-- TODO: Still to be defined:

Three things in this area are not yet settled:
    - How a decision refers to the snapshot it concerns. This needs a property, which will be defined alongside decisions in [Processes](#processes).
    - What a snapshot must contain when it marks a "release". Output checking is defined in [Processes](#processes)
    - Snapshot integrity and what happens when content must be removed from a record for legal reasons. (Provenance Crate module?) (Removing BagIt removed the checksums) - These are governance questions as much as technical ones -->

### Federated TRE Records


## Conformance and Modules

## Federation

## Security and Privacy

## Media Type and Signposting

## References

Specifications and vocabularies this profile builds on.

## Appendix A. Terms and Properties

Every term and property used by this profile that is not plain schema.org, with its source vocabulary and definition.

## Appendix B. Changes From 0.4
