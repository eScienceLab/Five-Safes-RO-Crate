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

A **TRE Activity Record** (“Activity Record”) is a versioned account of activity in a TRE. Each Activity Record covers one piece of work under the applicable TRE or federation arrangements, from a single cohort discovery query to a study lasting years. If work consists of several organisations, one Activity Record captures the whole piece of work.

An Activity Record grows as the work progresses, and may capture queries and analyses, decisions about them, the agreements which govern them, and any outputs that are released. This Activity Record is represented as a **Five Safes RO-Crate**.

### Observation and Scope

An Activity Record focuses on activity that was observed or attested: this is work in which a system captured the event as it happened, such as a portal logging each query, or work that a person or organisation stated happened, such as a manual output review. 

A portal may record every query, or an interactive workspace may record only the governance points around a session, with the analysis between them summarised. Both are a valid Activity Record with different scopes. 

### Assets, Processes, Context

Every entity describing the governed work has one or more of three roles.

| Role | Description |
|---|---|
| Assets | Artefacts that processes act on, consume, produce, or follow: datasets and extracts, outputs, models, software, plans, protocols, agreement texts. |
| Processes | Things that happen: submitting a request, making a decision, running a query, checking an output. |
| Context | People, organisations, agreements, and the TRE itself. |

The same entity can have more than one role. A protocol or plan is an asset, whilst following it is a process. Derived data is a separate asset with its own history, rather than a version of the original data. If planned work never begins, the request and its refusal or withdrawal still happened and remain in the Activity Record. 

Context can be the subject of a process. For example, signing an agreement or accrediting a researcher are processes. Each context item is recorded once and referred to wherever needed.

### Working Record and Snapshots

The **Working Record** reflects the current Activity Record, and captures the understanding of the work and changes as queries run, decisions are returned, and outputs appear. A **Snapshot** is a fixed representation of the Working Record taken at a significant moment, and once published, it is never changed; corrections are made by taking a later Snapshot. 

The Working Record keeps one identity throughout its life, meaning "this piece of work"; each Snapshot has its own identity, meaning "this piece of work, exactly as it stood at this point". A Snapshot carries a version number and, after the first, a link to its predecessor; the Working Record carries neither. Together, the Working Record and snapshots form a sequence of activity records. 

This profile does not prescribe when you should take a Snapshot. However, submitting, exchanging, and closing an Activity Record are reasonable choices.

### Core and Modules

Every Five Safes RO-Crate must follow the "core" profile outlined in this document. Additional "modules" add rules for particular kinds of work, such as output checking, cohort discovery, or workflow execution. An Activity Record may follow the core alone or declare any combination of modules.

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

To publish a Snapshot, a producer copies the Working Record and changes the root: `identifier` becomes the snapshot's own IRI, such as `.../activities/A123/versions/1` for the first; `version` is added with the matching integer, and `dateCreated` is set to when the Snapshot was taken. Any `dateModified` is removed; and `datePublished` is set to when the Snapshot was made available. If the root has an absolute `@id`, it MUST be changed to an absolute IRI identifying the Snapshot, and the metadata descriptor's `about` MUST be changed to match (see [Versioning and Snapshots](#versioning-and-snapshots)).

## Root Data Entity

The root data entity describes this RO-Crate as a single representation of the Activity Record. This profile uses two identifiers: 

- `identifier` is the canonical RO-Crate identifier, and specifies this particular RO-Crate representation; 
- `dct:isVersionOf` identifies the Activity Record across all its versions.

[Versioning and Snapshots](#versioning-and-snapshots) define both fully.

Alongside the properties RO-Crate requires of any root, this profile requires the following:

| Property | Requirement | Description |
|---|---|---|
| `@id` | MUST | Identifies the root data entity. The metadata descriptor's `about` MUST use exactly the same value. |
| `@type` | MUST | `Dataset`, or an array containing `Dataset`. |
| `conformsTo` | MUST | This profile's IRI and the IRI of each declared module; other application profiles MAY be present. Each profile IRI MUST also be described by a contextual entity. See [Conformance and Modules](#conformance-and-modules). |
| `identifier` | MUST, exactly one | The canonical RO-Crate identifier: an absolute IRI in `{"@id": "..."}` form not identifying a [`PropertyValue`](#record-and-ro-crate-identifiers). |
| `dct:isVersionOf` | MUST, exactly one | The record identifier, an absolute IRI. |
| `name` | MUST | Names the record. |
| `description` | MUST | Describes the work the record covers. |
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

Therefore, an asset MUST be referenced through an entity with an absolute IRI where the exact asset needs an identity beyond this one RO-Crate. Cases include when:

- it is the `object` of a `SendAction` or `ReceiveAction`;
- it is identified by a decision, as its `object` or under `prov:used`;
- or the producer asserts it is the same asset as one described in another RO-Crate, or across representations of the record.

Within one record sequence, a producer asserting that two descriptions concern the same exact asset and version MUST reuse the same absolute `@id`, and MUST NOT reuse that `@id` for different content or meaning.

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

Data produced by a process MUST be a separate asset from the data it came from, and MUST NOT be recorded as a revision of its source. 

The producing process records source and product as its `object` and `result`, and where derivation was observed or attested, the derived asset SHOULD also identify its source with `prov:wasDerivedFrom`, so the relationship survives being read without the process. An RO-Crate MUST use `prov:wasDerivedFrom` only on that basis.

### Software and Models

A held or produced software or trained-model asset SHOULD carry `name` and `version`, and `author` where known. A model produced by a recorded process is its `result`; a model assessed or decided upon is that process's `object`. This profile does not determine whether a model may be transferred or released.
