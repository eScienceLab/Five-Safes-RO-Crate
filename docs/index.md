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

!!! tip
    All references to schema.org types/properties/instances use the prefix `http://schema.org/` (not https) to correspond with their official JSON-LD context.

## Introduction

The [Five Safes](https://doi.org/10.13140/RG.2.1.3661.1604) framework ([Desai, Ritchie and Welpton, 2016](#references)) is an approach to consider safe access to sensitive data across five dimensions: safe projects, safe people, safe settings, safe data, and safe outputs. In TREs, this is applied through governance: work is proposed and approved, researchers are accredited, environments are controlled, data is prepared, and outputs are checked.

A Five Safes RO-Crate records this activity so that it can be retained as provenance, exchanged between systems, and inspected later. This profile specifies how that activity is represented as an RO-Crate.

This profile succeeds [Five Safes RO-Crate 0.4](https://w3id.org/5s-crate/0.4).

## Concepts

...

### The TRE Activity Record

A **TRE Activity Record** ("activity record") is a versioned account of activity in a TRE. Each activity record covers one piece of work under the applicable TRE or federation arrangements, from a single cohort discovery query to a study lasting years. If work consists of several organisations, one activity record captures the whole piece of work.

An activity record grows as the work progresses, and may capture queries and analyses, decisions about them, the agreements which govern them, and any outputs that are released. This activity record is represented as a **Five Safes RO-Crate**.

### Observation and Scope

An activity record focuses on activity that was observed or attested: this is work in which a system captured the event as it happened, such as a portal logging each query, or work that a person or organisation stated happened, such as a manual output review. 

A portal may record every query, or an interactive workspace may capture only the governance points around a session, with the analysis between them summarised. Both are valid activity records with different scopes. 

### Assets, Processes, Context

Every entity describing the governed work has one or more of three roles.

| Role | Description |
|---|---|
| Assets | Artefacts that processes act on, consume, produce, or follow: datasets and extracts, outputs, models, software, plans, protocols, agreement texts. |
| Processes | Things that happen: submitting a request, making a decision, running a query, checking an output. |
| Context | People, organisations, agreements, and the TRE itself. |

The same entity can have more than one role. A protocol or plan is an asset, whilst following it is a process. Derived data is a separate asset with its own history, rather than a version of the original data. If planned work never begins, the request and its refusal or withdrawal still happened and remain in the activity record. 

Context can be the subject of a process. For example, signing an agreement or accrediting a researcher are processes. Each context item is recorded once and referred to wherever needed.

### Working Record and Snapshots

The **working record** reflects the current activity record, and captures the understanding of the work and changes as queries run, decisions are returned, and outputs appear. A **snapshot** is a fixed representation of the working record taken at a significant moment, and once published, it is never changed; corrections are made by taking a later Snapshot. 

The working record keeps one identity throughout its life, meaning "this piece of work"; each snapshot has its own identity, meaning "this piece of work, exactly as it stood at this point". A snapshot carries a version number and, after the first, a link to its predecessor; the working record carries neither. Together, the working record and snapshots form a record sequence. 

This profile does not prescribe when you should take a snapshot. However, submitting, exchanging, and closing an activity record are reasonable choices.

### Core and Modules

Every Five Safes RO-Crate must follow the "core" profile outlined in this document. Additional "modules" add rules for particular kinds of work, such as output checking, cohort discovery, or workflow execution. An activity record may follow the core alone or declare any combination of modules.

## Structure of a Five Safes Crate

A Five Safes RO-Crate is an RO-Crate that contains a metadata file that describes its contents. The following sections outline the metadata file and structure.

### Metadata File

The `ro-crate-metadata.json` metadata file MUST conform to [RO-Crate 1.3](https://www.researchobject.org/ro-crate/specification/1.3/), and its descriptor MUST declare the version it conforms to. 

```json
{
  "@type": "CreativeWork",
  "@id": "ro-crate-metadata.json",
  "about": {"@id": "./"},
  "conformsTo": {"@id": "https://w3id.org/ro/crate/1.3"}
}
```

### JSON-LD

The core profile defines no vocabulary of its own, so an RO-Crate conforming to this core needs no context beyond RO-Crate. The context SHOULD be given in the array form, so that a module may add to it:

```json
{ "@context": ["https://w3id.org/ro/crate/1.3/context"],
  "@graph": [ ]
}
```

A term used as a property value MUST be written as a full absolute IRI in `{"@id": "..."}` form, whilst a term used in `@type` is written as a plain string:

```json
{
  "@type": ["CreateAction", "prov:Activity"],
  "actionStatus": {"@id": "http://schema.org/CompletedActionStatus"}
}
```

Writing `"actionStatus": "CompletedActionStatus"` instead produces the text `"CompletedActionStatus"`, not a reference to the term. This is because the RO-Crate context does not coerce property values to references.

!!! warning
    The RO-Crate context binds `pav`, `prov` and `dct` among others, so `pav:previousVersion` and `dct:isVersionOf` can be written in short form. Note that it binds `dct`, not `dcterms`.

A module MAY require an additional context and further vocabularies; the rules for declaring and describing them are in [Authoring Modules](authoring-modules.md).

### Entity Identifiers

Every entity described as a separate node in `@graph` MUST have an absolute IRI as its `@id`, with three exceptions: the metadata descriptor (`ro-crate-metadata.json`); the root, and contained `File` or `Dataset` entities (their relative payload paths). A UUID URN is sufficient and need not resolve.

### Complete Example

The following is a complete, minimal conforming working record of a feasibility query executed in a TRE, with the query and its output held in the RO-Crate. It uses an absolute root `@id`, with the metadata descriptor's `about` set to the same value:

```json
{
  "@context": ["https://w3id.org/ro/crate/1.3/context"],
  "@graph": [
    {
      "@type": "CreativeWork",
      "@id": "ro-crate-metadata.json",
      "about": {"@id": "https://tre72.example.org/activities/A123/current"},
      "conformsTo": {"@id": "https://w3id.org/ro/crate/1.3"}
    },
    {
      "@id": "https://tre72.example.org/activities/A123/current",
      "@type": "Dataset",
      "conformsTo": [{"@id": "https://w3id.org/5s-crate/1.0"}],
      "identifier": {"@id": "https://tre72.example.org/activities/A123/current"},
      "dct:isVersionOf": {"@id": "https://tre72.example.org/activities/A123"},
      "name": "Feasibility enquiry A123 (TRE72)",
      "description": "Cohort feasibility counts for the A123 enquiry.",
      "dateCreated": "2027-03-13T09:00:00Z",
      "dateModified": "2027-03-14T09:20:31Z",
      "datePublished": "2027-03-13T09:01:00Z",
      "license": {"@id": "https://creativecommons.org/publicdomain/zero/1.0/"},
      "publisher": {"@id": "https://ror.org/027m9bs27"},
      "hasPart": [{"@id": "query.sql"}, {"@id": "outputs/counts.csv"}],
      "mentions": [{"@id": "urn:uuid:6b1eaa63-25b0-4dd2-9c92-a35a3f5cd58a"}]
    },
    {
      "@id": "https://w3id.org/5s-crate/1.0",
      "@type": ["CreativeWork", "Profile"],
      "name": "Five Safes RO-Crate profile",
      "version": "1.0"
    },
    {
      "@id": "urn:uuid:6b1eaa63-25b0-4dd2-9c92-a35a3f5cd58a",
      "@type": ["CreateAction", "prov:Activity"],
      "name": "Execute feasibility query",
      "agent": {"@id": "https://orcid.org/0000-0002-1825-0097"},
      "provider": {"@id": "https://ror.org/027m9bs27"},
      "object": {"@id": "query.sql"},
      "result": {"@id": "outputs/counts.csv"},
      "startTime": "2027-03-14T09:20:30Z",
      "endTime": "2027-03-14T09:20:31Z",
      "actionStatus": {"@id": "http://schema.org/CompletedActionStatus"}
    },
    {
      "@id": "query.sql",
      "@type": "File",
      "name": "Feasibility query",
      "encodingFormat": "application/sql"
    },
    {
      "@id": "outputs/counts.csv",
      "@type": "File",
      "name": "Feasibility counts",
      "encodingFormat": "text/csv"
    },
    {
      "@id": "https://orcid.org/0000-0002-1825-0097",
      "@type": "Person",
      "name": "Example analyst",
      "affiliation": {"@id": "https://ror.org/027m9bs27"}
    },
    {
      "@id": "https://ror.org/027m9bs27",
      "@type": "Organization",
      "name": "TRE72"
    }
  ]
}
```

To publish a snapshot, a producer copies the working record and changes the root: `identifier` becomes the snapshot's own IRI, such as `.../activities/A123/versions/1` for the first; `version` is added with the matching integer, and `dateCreated` is set to when the snapshot was taken. Any `dateModified` is removed; and `datePublished` is set to when the snapshot was made available. If the root has an absolute `@id`, it MUST be changed to an absolute IRI identifying the snapshot, and the metadata descriptor's `about` MUST be changed to match (see [Versioning and Snapshots](#versioning-and-snapshots)).

## Root Data Entity

The Root Data Entity describes this RO-Crate as a single representation of the activity record. This profile uses two identifiers: 

- `identifier` is the canonical RO-Crate identifier, and specifies this particular RO-Crate representation; 
- `dct:isVersionOf` identifies the activity record across all its versions.

[Versioning and Snapshots](#versioning-and-snapshots) define both fully.

Alongside the properties RO-Crate requires of any root, this profile requires the following:

| Property | Requirement | Description |
|---|---|---|
| `@id` | MUST | Identifies the Root Data Entity. The metadata descriptor's `about` MUST use exactly the same value. |
| `@type` | MUST | `Dataset`, or an array containing `Dataset`. |
| `conformsTo` | MUST | This profile's IRI and the IRI of each declared module; other application profiles MAY be present. Each profile IRI MUST also be described by a contextual entity. See [Conformance and Modules](#conformance-and-modules). |
| `identifier` | MUST, exactly one | The canonical RO-Crate identifier: an absolute IRI in `{"@id": "..."}` form not identifying a [`PropertyValue`](#record-and-ro-crate-identifiers). |
| `dct:isVersionOf` | MUST, exactly one | The activity record identifier, an absolute IRI. |
| `name` | MUST | Names the activity record. |
| `description` | MUST | Describes the work the activity record covers. |
| `dateCreated` | MUST, exactly one | When this representation was created. |
| `dateModified` | MUST, exactly one if a working record has changed since creation; <br> <br> MUST NOT on a snapshot | The most recent actual change. |
| `datePublished` | MUST, exactly one | When this representation was first published. A snapshot becomes immutable at this time. |
| `license` | SHOULD, on a published RO-Crate | Describes the licence of the output data, either an open licence or restrictive, TRE-specific conditions of access. |
| `publisher` | SHOULD | The `Organization` that published this representation. |
| `version` | MUST, exactly one on a snapshot; <br> <br> MUST NOT, on a working record | A positive JSON integer. See [Representation State](#representation-state). |
| `pav:previousVersion` | MUST, exactly one on a snapshot after the first; <br> <br> MUST NOT, otherwise | The canonical RO-Crate identifier of the direct predecessor. |
| `hasPart` | MUST, if the RO-Crate holds or refers to data entities | Each data entity MUST be reachable from the root through `hasPart`, directly or through nested `Dataset` entities. |
| `mentions` | MUST, if the RO-Crate records any processes | The processes recorded in this RO-Crate. See [Processes](#processes). |

!!! note
    The root `@id` does not by itself determine whether an RO-Crate is Attached or Detached; those forms depend on how the metadata document and any payload are packaged, [as defined in the RO-Crate 1.3 base profile](https://www.researchobject.org/ro-crate/specification/1.3/root-data-entity.html#root-data-entity-identifier).

## Assets

Assets are the durable things processes act on, consume, produce, or follow.

### Kinds of Asset

An asset representing a file or dataset MUST be a data entity that is reachable from the root through `hasPart`. An abstract asset, such as a plan, an exact protocol version, or a software application, is instead a contextual entity with an absolute IRI, referenced from the processes for which it is relevant.

| Asset | Described as |
|---|---|
| A file held in the RO-Crate | `File`, with its relative payload path as `@id` |
| A directory held in the RO-Crate | `Dataset`, with its relative payload path as `@id` |
| Data represented without its payload | `File` or `Dataset` with an absolute IRI |
| A packaged software source file | `["File", "SoftwareSourceCode"]` |
| An exact software version referred to by a process | `SoftwareApplication` or `SoftwareSourceCode`, with an absolute IRI |
| An exact procedure or protocol version | `CreativeWork`, and MAY add `HowTo`, with an absolute IRI |
| A plan for intended work | `["CreativeWork", "prov:Plan"]`, with an absolute IRI |
| An exact trained-model version | `File`, `Dataset`, or another appropriate type |

An asset SHOULD carry `name`. A versioned asset such as a protocol, software, or a released extract SHOULD carry `version`. Software a process used is a contextual entity, and SHOULD be recorded as the `instrument` of the process that used it.

A data entity represented by reference has an absolute IRI as its `@id`, is listed under `hasPart`, and MUST NOT also use a relative path as though it were a contained file. A referenced RO-Crate follows [the referenced-RO-Crate pattern](#the-referenced-ro-crate-pattern). 

Whilst governance determines whether a payload is included, an asset only referred to is still a first-class asset that processes name in the ordinary way.

### Referencing Assets from Processes

A process refers to the assets it acted on with `object`, `result`, and `instrument`, and to the artefacts it referred to as evidence with `prov:used`. A file or directory held in this RO-Crate MAY be referenced directly by its relative path. 

!!! note
    A relative path always means the copy inside the containing RO-Crate. The same path in a snapshot identifies that snapshot's own copy.

Therefore, an asset MUST be referenced through an entity with an absolute IRI where the exact asset needs an identity beyond this one RO-Crate. This may be when it is the `object` of a `SendAction` or `ReceiveAction`; it is identified by a decision, as its `object` or under `prov:used`; or when the producer asserts it is the same asset as one described in another RO-Crate, or across representations of the activity record.

Reuse of an absolute `@id` across descriptions and representations follows [Identity Across Representations](#identity-across-representations): one IRI names one exact asset and version throughout a record sequence.

### Packaged Copies of Identified Assets

An asset with an absolute IRI and a copy of that asset included in the RO-Crate MUST be described as two separate entities:

```plaintext
outputs/count-v1.csv
    └── encodesCreativeWork
          └── https://tre72.example.org/activities/A123/assets/count/v1
```

A packaged file MUST use `encodesCreativeWork` for this relationship. A packaged directory MUST instead use `exampleOfWork`. In either case, the target MUST identify the exact asset version and MUST be typed as `CreativeWork` or one of its subtypes, such as `Dataset`. The core profile does not define an equivalent relationship for an asset that is not a CreativeWork.

Moving, renaming, or encoding the same asset in another format does not by itself create a new version or asset. Therefore, multiple packaged representations can point to the same absolute IRI. `prov:wasDerivedFrom` MUST NOT be used to connect a packaged representation to the asset it encodes; it is reserved for cases in which a process produced a distinct asset from another asset.

The following fragment shows an output given an absolute identity for a release decision, and an agreement version, each with a packaged copy:

```json
[
  {
    "@id": "https://tre72.example.org/activities/A123/assets/count/v1",
    "@type": "Dataset",
    "name": "Cohort count result, version 1",
    "version": "1"
  },
  {
    "@id": "outputs/count-v1.csv",
    "@type": ["File", "DataDownload"],
    "name": "CSV encoding of cohort count result, version 1",
    "encodingFormat": "text/csv",
    "encodesCreativeWork": {
      "@id": "https://tre72.example.org/activities/A123/assets/count/v1"
    }
  },
  {
    "@id": "https://tre72.example.org/agreements/DUA-42/versions/3",
    "@type": "CreativeWork",
    "name": "Data use agreement 42, version 3",
    "version": "3"
  },
  {
    "@id": "agreements/dua-v3.pdf",
    "@type": "File",
    "name": "PDF encoding of data use agreement 42, version 3",
    "encodingFormat": "application/pdf",
    "encodesCreativeWork": {
      "@id": "https://tre72.example.org/agreements/DUA-42/versions/3"
    }
  }
]
```

### Protocols

A protocol is an asset that sets out how something is intended to be done; each occasion of following it is a separate process instance that records the exact protocol version with the `instrument`, referring to the absolute protocol entity. The same asset may be a protocol for one process and an ordinary input to another.

### Derived Data

Data produced by a process MUST be a separate asset from the data it came from, and MUST NOT be captured as a revision of its source. 

The producing process documents source and product as its `object` and `result`, and where derivation was observed or attested, the derived asset SHOULD also identify its source with `prov:wasDerivedFrom`, so the relationship survives being read without the process. An RO-Crate MUST use `prov:wasDerivedFrom` only on that basis.

### Software and Models

A held or produced software or trained-model asset SHOULD carry `name` and `version`, and `author` where known. A model produced by a recorded process is its `result`; a model assessed or decided upon is that process's `object`. This profile does not determine whether a model may be transferred or released.

## Processes

Processes are the things that happen. For example, a researcher executing an SQL query on some data; software applying a deidentification protocol on free-text data; or an output checker verifying outputs during the disclosure control process. Each MUST be a [Contextual Entity](https://www.researchobject.org/ro-crate/specification/1.3/contextual-entities.html), referenced from the root's `mentions`.

### Process Shape

Every process MUST be an [Action](http://schema.org/Action) whose `@type` includes one of the types in [Kinds of Process](#kinds-of-process) and also `prov:Activity`.

| Property | Requirement | Description |
|---|---|---|
| `@id` | MUST | An absolute IRI identifying this process occurrence. |
| `@type` | MUST | See [Kinds of Process](#kinds-of-process). |
| `agent` | MUST | The people or organisations that directly performed or operated the process, each described in the RO-Crate as a `Person` or `Organization`. |
| `actionStatus` | MUST, exactly one | See [Status](#status); written as `{"@id": ...}`. |
| `name` | SHOULD | What happened, in words. |
| `object` | SHOULD | What the process acted on. A decision MUST have at least one value identifying what was decided upon. |
| `result` | MUST; <br><br> MUST NOT | A `CreateAction` with `CompletedActionStatus` that produced an asset MUST identify it. <br><br> An anticipated, suppressed, or withheld output MUST NOT appear as `result`. |
| `instrument` | SHOULD, where Assets actually helped perform the process | The exact protocol, software, or other Asset that helped; applicability alone does not make an Asset an instrument. |
| `provider` | MUST, where the process was carried out within a TRE [or one of its nodes](#the-tre-and-its-nodes) | The `Organization` that provided or operated the environment or service. |
| `prov:atLocation` | MAY | A runtime location (workspace, virtual machine), with an absolute `@id` and `@type` including `Thing` and `prov:Location`. |
| `startTime` | SHOULD | When the process actually began; never an anticipated time. |
| `endTime` | MUST, where `actionStatus` is `CompletedActionStatus` or `FailedActionStatus`; <br><br> MUST NOT where `ActiveActionStatus` | When the process ended. |
| `description` | MAY | Further detail, such as the command run. |

Asset references from `object`, `result`, `instrument`, and `prov:used` follow [Referencing Assets from Processes](#referencing-assets-from-processes).

### Kinds of Process

| Kind | Described as |
|---|---|
| Submitting a plan for action | `AskAction` |
| Work intended to create an asset, such as a query execution or workflow run | `CreateAction` |
| Work that produces no asset and has no more specific type below | `Action` |
| A check or assessment that reaches no decision by itself | `AssessAction` |
| A decision that permits something | `AuthorizeAction` |
| A decision that refuses something | `RejectAction` |
| Withdrawing a request before the work begins | `CancelAction` |
| A change to the record or the RO-Crate as a whole | `UpdateAction` |
| Moving something between parties | `SendAction`, `ReceiveAction` |


The `@type` array MAY include further, more specific types alongside a listed type.

An `AssessAction` records a check or assessment but does not itself assert permission or refusal, and any such decision MUST be recorded as a separate `AuthorizeAction` or `RejectAction`; the outcome is distinguished by that type.

A process MAY carry `additionalType`, referring to the exact IRI of a published term for a more specific kind of process. If the term comes from another vocabulary, its exact published IRI MUST be used and its published meaning MUST NOT be changed. A module MAY define or require terms for the processes it covers.

Work that intended to create an artefact but completed without returning one MUST keep its `CreateAction` type and `CompletedActionStatus`, MUST NOT record a `result`, and SHOULD explain the outcome in `description`.

!!! tip
    `CreateAction` should be used for changes to a file within a dataset, with the original as `object` and the new version as `result`. `UpdateAction` should be used for changes affecting the activity record as a whole.

### Requests, Plans, and Execution

Intended work recorded before it begins MUST be an asset whose `@type` includes `prov:Plan` and has an absolute IRI. A plan submitted for action MUST identify the exact submitted version: a change after submission creates a new plan with a new `@id`, linked to its immediate predecessor with `pav:previousVersion`. 

Submitting a plan MUST be a separate `AskAction` with exactly one object (the plan), exactly one recipient (the person or organisation asked to act, described in the RO-Crate as a `Person` or `Organization`) and `CompletedActionStatus`. 

A decision on the request MUST be a separate `AuthorizeAction` or `RejectAction` with the same plan version as its only object, identifying the `AskAction` with `prov:wasInformedBy`. 

`CancelAction` describes future work that will no longer happen, such as withdrawing a pending request. This follows the pattern above. 

If the planned work begins, each execution attempt MUST be a separate `Action` with its own identity, status, and times; one plan may have any number of executions. A conforming RO-Crate SHOULD record every observed or attested execution attempt within its [scope](#observation-and-scope). A failed attempt MUST NOT be changed back to active; a retry MUST be a new `Action`.

When planned work is executed, the execution MUST link to the plan through at least one `prov:qualifiedAssociation`. This is a Contextual Entity typed `prov:Association` with exactly one `prov:agent`, which is also an `agent` of the execution, and exactly one `prov:hadPlan` identifying the exact plan version. There should be one association per agent-and-plan pair.

```mermaid
flowchart LR
    R["Request<br/>AskAction and prov:Activity"] -->|"object"| P["Submitted plan version<br/>prov:Plan"]
    D["Decision<br/>AuthorizeAction or RejectAction<br/>and prov:Activity"] -->|"object"| P
    C["Withdrawal<br/>CancelAction and prov:Activity"] -->|"object"| P
    D -->|"prov:wasInformedBy"| R
    C -->|"prov:wasInformedBy"| R
    D -.->|"prov:used, if consulted"| S["Pre-existing snapshot<br/>artefacts as evidence"]
    E["Execution attempt<br/>Action and prov:Activity<br/>0..* per plan"] -->|"prov:qualifiedAssociation"| A["Association<br/>prov:Association"]
    A -->|"prov:hadPlan"| P
    A -->|"prov:agent"| G["Performer<br/>Person or Organization"]
```

In the diagram above, the request, decision, withdrawal, and execution are independent claims. Note that the arrows are properties recorded in the metadata and do not imply that all the processes shown occurred.

The following fragment describes a submitted plan, its request, and one execution linked to the plan through an association. The decision answering this request is shown under [Decision Subjects and Evidence](#decision-subjects-and-evidence); the person and organisation entities are omitted:

```json
[
  {
    "@id": "https://tre72.example.org/activities/A123/plans/enquiry-3f2b",
    "@type": ["CreativeWork", "prov:Plan"],
    "name": "Analysis plan for enquiry A123"
  },
  {
    "@id": "https://tre72.example.org/activities/A123/requests/enquiry-3f2b",
    "@type": ["AskAction", "prov:Activity"],
    "name": "Submit analysis plan",
    "agent": {"@id": "https://orcid.org/0000-0002-1825-0097"},
    "provider": {"@id": "https://ror.org/027m9bs27"},
    "object": {
      "@id": "https://tre72.example.org/activities/A123/plans/enquiry-3f2b"
    },
    "recipient": {"@id": "https://ror.org/027m9bs27"},
    "endTime": "2027-03-13T15:00:00Z",
    "actionStatus": {"@id": "http://schema.org/CompletedActionStatus"}
  },
  {
    "@id": "https://tre72.example.org/activities/A123/runs/run-1",
    "@type": ["CreateAction", "prov:Activity"],
    "name": "Execute approved analysis",
    "agent": {"@id": "https://orcid.org/0000-0002-1825-0097"},
    "provider": {"@id": "https://ror.org/027m9bs27"},
    "prov:qualifiedAssociation": {
      "@id": "urn:uuid:d0f1c2b3-4a5e-4f60-9b7c-8d9e0f1a2b3c"
    },
    "result": {"@id": "outputs/analysis-report.html"},
    "startTime": "2027-03-14T10:00:00Z",
    "endTime": "2027-03-14T11:30:00Z",
    "actionStatus": {"@id": "http://schema.org/CompletedActionStatus"}
  },
  {
    "@id": "urn:uuid:d0f1c2b3-4a5e-4f60-9b7c-8d9e0f1a2b3c",
    "@type": "prov:Association",
    "prov:agent": {"@id": "https://orcid.org/0000-0002-1825-0097"},
    "prov:hadPlan": {
      "@id": "https://tre72.example.org/activities/A123/plans/enquiry-3f2b"
    }
  }
]
```

### Status

| Value | Meaning |
|---|---|
| `ActiveActionStatus` | The process has begun and is still running. |
| `CompletedActionStatus` | The process finished. |
| `FailedActionStatus` | The process began but did not finish successfully. |

Every process MUST have exactly one value from the table above. A completed or failed process MUST carry `endTime`, an active one MUST NOT, and a process keeps its `@id` as it moves from active to completed or failed. 

!!! warning
    `PotentialActionStatus` MUST NOT be used: a submitted request is a completed `AskAction`, and refusal and withdrawal are completed `RejectAction` and `CancelAction` processes. An execution Action appears only if work begins.

### Who Performed a Process

The `agent` of a process is the person or organisation that directly performed or operated it, as observed or attested in the activity record. A role, account, or pool of people MUST NOT be used as the `agent`. The organisation that provided the environment is the `provider`, whether or not it is also an `agent`. 

Where an automated step is attributed to an operating organisation, `agent` identifies the organisation and the `instrument` (the software).

### Exchange Processes

An exchange records the transfer of one or more exact assets, such as a dataset, an approved output, or a snapshot, from one `Person` or `Organisation` to another. For example, during a federated analysis, one node may send an intermediate result to another node for the next stage of processing.

An exchange process MUST be typed as a `SendAction` or `ReceiveAction`. Each observed or attested dispatch of an asset is a `SendAction`, and each observed or attested delivery is a separate `ReceiveAction`. 

!!! warning
    Recording either process does not establish that the other occurred, and either MAY therefore appear alone. For example, a sender may know that an asset was sent, without knowing whether delivery was successful.

| Process | Additional requirements |
|---|---|
| `SendAction` | <ul> <li> `object` MUST identify one or more exact assets dispatched; </li> <li> `recipient` MUST identify exactly one receiving party, described in the RO-Crate as a `Person` or `Organization`; </li> <li> Dispatches to different recipients MUST be represented with a separate `SendAction`, even when they concern the same assets. </li> </ul>|
| `ReceiveAction` | <ul> <li> `object` MUST identify one or more exact assets received; </li> <li> `sender` MUST identify exactly one sending party, described in the RO-Crate as a `Person` or `Organization`. </li> </ul> |

Each `object` MUST [identify an exact asset using an absolute IRI](#referencing-assets-from-processes), and an exchange Action MAY have several `object` values only when the assets were transferred as part of the same occurrence. 

The Action’s `actionStatus`, `startTime`, and `endTime` apply to every listed asset. Assets transferred in different occurrences, to or from different senders and recipients, with different statuses, or at different recorded times MUST be represented by separate Actions.

`SendAction` and `ReceiveAction` describe asset transfers. If preparing an export for sending or unpacking a delivery upon receipt produces a new asset, that production MUST be recorded as a separate `CreateAction`.

#### Transferred Snapshots

An exchange's `object` identifies a snapshot only where the complete snapshot RO-Crate was itself transferred. By the end of a completed exchange the transferred asset MUST satisfy the [snapshot requirements](#snapshot-requirements) and [have been published](#representation-dates) (that is, made available as an immutable RO-Crate); first publication may occur during the exchange. 

The snapshot's `datePublished` MUST NOT be later than the exchange's `endTime`, and the transferred snapshot's canonical identifier MUST NOT equal that of the RO-Crate describing the exchange. A later snapshot that records the exchange MUST NOT be identified as its `object`.

#### Correlating Dispatch and Receipt

Where the RO-Crate asserts that a receipt resulted from a particular dispatch, the `ReceiveAction` MUST identify that exact `SendAction` with `prov:wasInformedBy`, as an absolute IRI; the `SendAction` does not need to be described in the same RO-Crate. The link MUST be asserted only where the causal relationship was observed or attested, and a missing counterpart MUST NOT be inferred.

The two Actions MAY share an `object` IRI where they concern the same asset and version; where the received copy is treated as distinct and derivation was observed or attested, it SHOULD identify the sent asset with `prov:wasDerivedFrom`. The `SendAction`’s `startTime` MUST NOT be later than the `ReceiveAction`’s `endTime`.

!!! warning "Time Zones"
    Care should be taken with `startTime` and `endTime` across systems, particularly in federated environments. Services may record times in their local time, which may make `startTime` and `endTime` appear out of sequence.

```json
[
  {
    "@id": "https://tre-a.example.org/records/R/actions/send-output-17",
    "@type": ["SendAction", "prov:Activity"],
    "name": "TRE node A sent output 17 to TRE node B",
    "agent": {"@id": "https://tre-a.example.org/node"},
    "provider": {"@id": "https://tre-a.example.org/node"},
    "recipient": {"@id": "https://tre-b.example.org/node"},
    "object": {"@id": "https://tre-a.example.org/records/R/assets/output-17"},
    "startTime": "2027-04-06T14:00:00Z",
    "endTime": "2027-04-06T14:00:05Z",
    "actionStatus": {"@id": "http://schema.org/CompletedActionStatus"}
  },
  {
    "@id": "https://tre-b.example.org/records/R/actions/receive-output-17",
    "@type": ["ReceiveAction", "prov:Activity"],
    "name": "TRE node B received output 17 from TRE node A",
    "agent": {"@id": "https://tre-b.example.org/node"},
    "provider": {"@id": "https://tre-b.example.org/node"},
    "sender": {"@id": "https://tre-a.example.org/node"},
    "object": {"@id": "https://tre-a.example.org/records/R/assets/output-17"},
    "prov:wasInformedBy": {
      "@id": "https://tre-a.example.org/records/R/actions/send-output-17"
    },
    "startTime": "2027-04-06T14:00:04Z",
    "endTime": "2027-04-06T14:00:06Z",
    "actionStatus": {"@id": "http://schema.org/CompletedActionStatus"}
  },
  {
    "@id": "https://tre-a.example.org/records/R/assets/output-17",
    "@type": "Dataset",
    "name": "Checked output 17"
  },
  {
    "@id": "https://tre-a.example.org/node",
    "@type": "Organization",
    "name": "TRE node A"
  },
  {
    "@id": "https://tre-b.example.org/node",
    "@type": "Organization",
    "name": "TRE node B"
  }
]
```

### Decision Subjects and Evidence

The subject of a decision, the request it answers, and the evidence it used are different relationships.

| Property | Meaning |
|---|---|
| `object` | What was decided upon. Every decision MUST have at least one. |
| `prov:wasInformedBy` | An earlier process that informed the decision, including the request being answered. |
| `prov:used` | Evidence the decision activity actually used. |

An `AuthorizeAction` or `RejectAction` answering an `AskAction` MUST have exactly one `object` (the exact submitted plan version) and MUST identify that `AskAction` with `prov:wasInformedBy`. Any other decision identifies whatever it decided upon as its `object`.

A decision MAY identify a snapshot with `prov:used` only if the snapshot existed and was actually used in reaching it; one that merely existed, was created afterwards, or later records the decision MUST NOT be identified, and where no snapshot was used its absence does not make the decision incomplete. A snapshot under `prov:used` is referenced under [the referenced-RO-Crate pattern](#the-referenced-ro-crate-pattern) and MUST already have been published when the decision ended: where both values are timezone-qualified times from a known common or synchronised clock, the snapshot's `datePublished` MUST NOT be later than the decision's `endTime`. A module MAY require decisions of a kind it defines to identify pre-existing snapshots.

The following fragment records an approval that used snapshot version 1 as evidence; the containing root also lists the decision under `mentions` and the referenced snapshot under `hasPart`.

```json
[
  {
    "@id": "https://tre72.example.org/activities/A123/decisions/signoff-9c14",
    "@type": ["AuthorizeAction", "prov:Activity"],
    "name": "Enquiry approved for the two participating sites",
    "agent": {"@id": "https://orcid.org/0000-0002-1825-0097"},
    "provider": {"@id": "https://ror.org/027m9bs27"},
    "object": {"@id": "https://tre72.example.org/activities/A123/plans/enquiry-3f2b"},
    "prov:wasInformedBy": {
      "@id": "https://tre72.example.org/activities/A123/requests/enquiry-3f2b"
    },
    "prov:used": {
      "@id": "https://tre72.example.org/activities/A123/versions/1"
    },
    "endTime": "2027-03-13T16:40:00Z",
    "actionStatus": {"@id": "http://schema.org/CompletedActionStatus"}
  },
  {
    "@id": "https://tre72.example.org/activities/A123/versions/1",
    "@type": "Dataset",
    "name": "Submission snapshot for enquiry A123",
    "version": 1,
    "dct:isVersionOf": {"@id": "https://tre72.example.org/activities/A123"},
    "datePublished": "2027-03-13T16:00:00Z",
    "conformsTo": {"@id": "https://w3id.org/ro/crate"}
  }
]
```

## Context

Context records who was involved, where, and under what authority.

### People and Organisations

A person is a `Person`; an organisation, including a TRE or one of its nodes, is an `Organization`. Each MUST have an absolute IRI as its `@id` identifying the person or organisation described. This should be an external persistent identifier such as an ORCID iD or ROR identifier where appropriate, or a stable opaque IRI such as a UUID URN. The `@id` does not need to resolve or expose a public identifier, and an opaque `Person` identifier still denotes one specific person.

The `@id` MUST NOT denote a role, account, pool of people, or unidentified performer, and a parent organisation’s ROR MUST NOT be used for a distinct TRE, node, or department.

Identity of a person or organisation across representations follows [Identity Across Representations](#identity-across-representations). Independent producers (such as services in federated nodes) may assign different opaque IRIs to the same real-world entity; opaque entities remain separate unless their identity is attested. 

!!! warning
    Across a federation, the same person or organisation may appear under a different opaque IRI in each node's activity record. Duplicate entities in an
    aggregated view are therefore expected and should be merged only where identity is attested. Where cross-node identity matters and a public identifier is appropriate, use an external persistent identifier such as an ORCID iD or ROR identifier.

A `Person` MAY carry `affiliation`, referencing the exact `Organization` described in the RO-Crate. An external Web URL whose reference page unambiguously indicates the entity's identity MAY be recorded with `sameAs`; other external identifiers MAY be given under `identifier` as `PropertyValue` entities ([Record and RO-Crate Identifiers](#record-and-ro-crate-identifiers)).

The following fragment attributes an assessment to an anonymous output checker:

```json
[
  {
    "@id": "urn:uuid:0ab2bde1-6979-4bd0-b187-22e56c24ba6a",
    "@type": ["AssessAction", "prov:Activity"],
    "name": "Review submitted material",
    "agent": {"@id": "urn:uuid:79c330fe-2e70-4b0a-917b-c5f6b9cf6521"},
    "provider": {"@id": "https://example.org/tre/node-a"},
    "endTime": "2027-03-14T10:30:00Z",
    "actionStatus": {"@id": "http://schema.org/CompletedActionStatus"}
  },
  {
    "@id": "urn:uuid:79c330fe-2e70-4b0a-917b-c5f6b9cf6521",
    "@type": "Person",
    "name": "Checker 17"
  },
  {
    "@id": "https://example.org/tre/node-a",
    "@type": "Organization",
    "name": "TRE node A"
  }
]
```
