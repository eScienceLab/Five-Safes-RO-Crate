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

Every item in a record belongs to one of three categories:

- **Assets**: artefacts that processes consume or produce, such as protocols.

- **Processes**: things that happen, including activities that have been requested but have not yet run.

- **Context**: people, organisations, agreements, and the TRE itself.

**Assets** are durable items such as datasets and extracts, analysis outputs, trained models, software, and protocol documents. Two rules are important:

- A protocol, such as a deidentification procedure, workflow, or standard operating procedure, is an asset rather than a process. It can be versioned, approved, and reused. Following the protocol on a particular occasion is a process.

- Derived data is a separate asset. For example, a deidentified copy of a dataset is different from its source and has its own history.

**Processes** are things that happen. Examples include executing a query, running a workflow, checking an output, and applying a protocol. A completed process records what it consumed and produced, which protocol it followed, when it ran, who was responsible for it, and any software it used.

A process can appear in the record before it happens. For example, a requested analysis that is awaiting a decision is already part of the record and is marked as not yet run. It may later complete, fail, be withdrawn, or be refused without ever running. The refusal is itself a decision in the record. Some processes may not produce a new asset.

**Context** records who and what are involved, and under what authority: people, organisations, agreements, and the TRE itself, together with credentials, training, and policies. Processes do not operate on context in the same way that they operate on assets. However, context can be the subject of a process. Signing an agreement, granting a credential, and accrediting a researcher are all processes whose subject is context. Each context item is recorded once and referred to wherever it is needed.

These categories also show how a record provides evidence for the Five Safes:

- safe projects are evidenced by the record as a whole, including the agreements governing the work and the decisions that allowed it to proceed;

- safe people and safe settings are evidenced in context;

- safe data is evidenced in assets;

- safe outputs are evidenced by the checking processes that control what may leave.

### Working Record and Snapshots

The working record reflects the current understanding of the work. It changes as queries run, decisions are returned, and outputs appear. A snapshot is a complete copy of the record taken at a meaningful moment. It freezes the record as it stood then and is never edited afterwards. The working record and each snapshot have separate, stable identities. Each snapshot after the first links to the previous one, so the snapshots trace the record's history.

<!-- !!! note
    Where several parties contribute in parallel, such as in a federated system, that history can branch and reconverge; merging the branches is the job of whoever maintains the record. -->

The working record and its snapshots answer different questions. The working record keeps the same identity throughout its life, meaning "this piece of work". A snapshot has its own identity, meaning "this piece of work, exactly as it stood at that moment". This makes it clear exactly which version an approval applies to.

A snapshot is not the same as "one run". It may contain no runs, one run, or many runs. How the work is divided into processes and when a snapshot is taken are separate choices. Whoever maintains the record decides when to take a snapshot, with one expectation: every decision and every exchange refers to an existing snapshot. Without a snapshot, an approval has no fixed version to point to, so it preserves no evidence of what was approved. Examples of when to take a snapshot include when something is submitted, when a result leaves, and when the record closes—that is, when no further activity is expected.
<!-- TODO: Revisit above when we have example processes -->

Snapshots preserve provenance. A decision concerns the record as it stood at the time. The snapshot preserves what the record said then, so that information remains available for later inspection even if the working record has moved on or the data it refers to is no longer available under the data access agreement.

### Snapshots as Messages



## Structure of a Five Safes Crate

Captures the metadata file more specifically: the root data entity, payload rules (what should be embedded vs referenced - e.g., bulk or sensitive data is always referenced).

## Assets

Asset types and their expected metadata, including catalogue entries for sensitive data held within the TRE; protocols as versionable, approvable assets that processes refer to.

## Processes

The action pattern for recording occurrences - inputs, outputs, instruments, agents, timing, and status - and how governance checks and decisions are typed, with manual versus automated checking expressed through who or what performed the action.

## Context

Captures people, organisations, credentials, agreements, working environment, and the TRE and its nodes.

## Versioning and Snapshots

Each snapshot is a complete immutable crate; identity and predecessor links; and the evidence expected when a snapshot marks a submission, a release, or the closure of a record.

## Conformance and Modules

## Federation

## Security and Privacy

## Media Type and Signposting

## References

Specifications and vocabularies this profile builds on.

## Appendix A. Terms and Properties

Every term and property used by this profile that is not plain schema.org, with its source vocabulary and definition.

## Appendix B. Changes From 0.4
