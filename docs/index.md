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

What a Five Safes RO-Crate ("Five Safes Crate") is, who it serves (researchers, TRE operators, auditors, the public), how its content evidences the Five Safes framework, and how this specification relates to RO-Crate 1.3, SATRE, and its 0.4 predecessor.

## Concepts

Plain-language definitions of the core ideas; nothing in this section should require familiarity with RO-Crate or JSON-LD.

### The TRE Activity Record

A Five Safes Crate is a **TRE Activity Record** (from here on, "record"): a versioned account of activity in a TRE, roughly one record per piece of work the TRE governs as a unit, spanning every node that takes part.

Both the [working record and each snapshot](#working-record-and-snapshots) are Five Safes Crates. These remain the same kind of document at different moments in the work's life.

A record accumulates whatever the work produces and requires: queries and analyses, the decisions made about them, the agreements they run under, and the outputs they release. It describes the data the work touches; sensitive data itself stays where it is governed, [referred to but not contained](#structure-of-a-five-safes-crate). One record might hold a single cohort discovery query answered within a minute; another might hold a study spanning months or years. Both are the same kind of thing.

This specification does not prescribe where one record ends and the next begins as TREs are disparate and govern work differently. For example, one TRE may govern work per query in a discovery portal, whereas another per workspace in an analysis environment. The reliable anchor is the agreements: the work that one set of agreements governs together belongs in one record. A record also only holds what its TRE could observe. A portal can record every query as it happens; an interactive workspace may capture only the governance touchpoints around a session, with the analysis between them summarised when outputs leave. Both are valid records.

!!! note 
    There is deliberately no "project" item in a record. The word means too many things: a grant, a study, a workspace, an access agreement. The specific things "project" can mean appear inside the record as themselves.

When work spans several TREs, or several nodes of a federation (the sites and services taking part), the aim is one record of the whole piece of work, with each node's activity appearing in it. Nodes will keep operational logs of their own, as their own regulators require; what this specification asks is that the work itself is reported once, in one place. Who maintains that record - the coordinating service, the lead TRE, the portal - is an open deployment decision.

### Assets, Processes, Context

Everything in a record belongs to one of three categories: 

- **Assets**. Artefacts that processes consume or produce, such as protocols;

- **Processes**. Things that happen, including those requested but not yet run;

- **Context**. People, organisations, agreements, and the TRE itself.

**Assets** are the durable things: datasets and extracts, analysis outputs, trained models, software, and protocol documents. Two rules matter: 

- A protocol (such as a deidentification procedure, a workflow, a standard operating procedure) is an asset rather than a process: it is versioned, approved, and reused. Any occasion of following it is a process. 

- Derived data is its own asset: a deidentified copy of a dataset is a different thing from its source, with its own history.

**Processes** are the things that happen, such as an executed query, a workflow run, an output checked, or an applied protocol applied. A completed process records what it consumed and produced, the protocol it followed, when it ran, who was responsible for it, and what software was used, if any. 

A process can also exist before it happens. For example, a requested analysis awaiting a decision is already in the record, marked as not yet run. It later runs to completion, fails, is withdrawn, or is refused and never runs, the refusal itself being a decision in the record. Some processes may not produce a new asset.

**Context** captures who, what, and under what authority: people, organisations, agreements, and the TRE itself, along with credentials, training, and policies. Whilst processeses do not work on context, signing an agreement, granting a credential, and accrediting a researcher are things that happen, and they appear as processes whose subject is context. Each piece of context is recorded once and referred to wherever needed.

The three categories are also how a record evidences the Five Safes: safe projects in the record itself, through the agreements it runs under and the decisions that admitted the work; safe people and safe settings in context; safe data in assets; and safe outputs in the checking processes that gate what leaves.

### Working Record and Snapshots

The working record changes as activity happens; a snapshot 'freezes' the complete record at a meaningful moment, and the record and each snapshot carry separate and stable identities.

The working record is the current understanding of the work: it changes as queries run, decisions are returned, and outputs appear. A snapshot is a complete copy of the record taken at one moment and never edited afterwards. Each snapshot after the first links to the one before it, so a record's snapshots trace its history. 

<!-- !!! note
    Where several parties contribute in parallel, such as in a federated system, that history can branch and reconverge; merging the branches is the job of whoever maintains the record. -->

Working records and snapshots answer different questions. The record's identity is constant for its whole life and means "this piece of work". A snapshot's identity means "this piece of work, exactly as it stood at that moment". For example, to say what an approval was an approval *of*.

A snapshot is not "one run". A single snapshot may contain no runs, one, or many; how finely the work is divided into processes and when the record is frozen are separate choices. When to freeze is the choice of whoever maintains the record, with one expectation: every decision and every exchange refers to a snapshot that exists. This is because an approval that points at nothing preserves nothing. Example moments are when something is submitted, when a result leaves, and when the record closes, meaning no further activity is expected.
<!-- TODO: Revisit above when we have example processes -->

Snapshots exist to capture provenance. A decision is made about the record as it stood at the time, and the snapshot keeps what was asserted then inspectable later, even though the working record may have moved on and the data it refers to may since have been retired under its own retention rules.

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
