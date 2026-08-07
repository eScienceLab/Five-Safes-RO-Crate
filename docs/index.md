# Five Safes RO-Crate 1.0

Authors:

1. Alexander Hambley, The University of Manchester <https://orcid.org/0000-0003-1193-6632>
2. Warren Del-Pinto, The University of Manchester <https://orcid.org/0000-0003-3307-9432>
3. Douglas Lowe, The University of Manchester <https://orcid.org/0000-0002-1248-3594>
4. Eli Chadwick, The University of Manchester <https://orcid.org/0000-0002-0035-6475>
5. Stian Soiland-Reyes, The University of Manchester <https://orcid.org/0000-0001-9842-9718>

* Permalink: <https://w3id.org/5s-crate/1.0>
* Version: 1.0
* Status: Working Draft
* Release notes: <https://github.com/eScienceLab/Five-Safes-RO-Crate/releases>
* Published: 2027-XX-XX
* Comments and suggestions: <https://github.com/eScienceLab/Five-Safes-RO-Crate/issues>

This document specifies a profile of [RO-Crate](https://w3id.org/ro/crate) for recording and exchanging the activity of Trusted Research Environments (TREs).

_The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [[RFC2119](https://doi.org/10.17487/RFC2119)] [[RFC8174](https://doi.org/10.17487/RFC8174)] when, and only when, they appear in all capitals, as shown here._

**Note**: All references to schema.org types/properties/instances use the prefix `http://schema.org/` (not https) to correspond with their official JSON-LD context.

Table of content:

1. TOC
{:toc}

## Introduction

What a Five Safes RO-Crate ("Five Safes Crate") is, who it serves (researchers, TRE operators, auditors, the public), how its content evidences the Five Safes framework, and how this specification relates to RO-Crate 1.3, SATRE, and its 0.4 predecessor.

## Concepts

Plain-language definitions of the core ideas; nothing in this section should require familiarity with RO-Crate or JSON-LD.

### The TRE Activity Record

A Five Safes Crate is a versioned record of activity in a TRE, roughly one record per conceptual project, wrapping all federated nodes.

### Assets, Processes, Context

Everything in a record is one of three kinds: 
- Assets: things processes take in or produce, including protocols;
- Processes: things that happen, including those requested but not yet run;
- Context: people, organisations, agreements, and the TRE itself.

### Working Record and Snapshots

The working record changes as activity happens; a snapshot 'freezes' the complete record at a meaningful moment, and the record and each snapshot carry separate and stable identities.

### Snapshots as Messages

When systems exchange (a submission, a response, a release), the thing that travels is a snapshot, validated against the requirements of that boundary, defined as a Process.

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
