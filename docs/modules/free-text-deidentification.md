# Module: Free-Text Deidentification

A module of the [Five Safes RO-Crate profile](../index.md). It is declared alongside the core profile in an RO-Crate's `conformsTo`.

Under construction.

## Overview

This module has been developed using guidance from the protocol developed during the [SafeText project](https://dareuk.org.uk/community-groups-listing/safetext-community-led-protocols-for-the-safe-and-responsible-use-of-de-identified-and-synthetic-healthcare-text-for-ai-development/), which provides guidelines for TREs on how to make (clinical) free-text data available for the development of Natural Language Processing (NLP) or other Artificial Intelligence (AI) tools, or potentially for researchers wanting to perform other forms of large scale quantitative analysis. Free-text refers to any data represented as natural language. The protocol can be found here (*link when launched - Nov.).

This use case focuses on de-identification of sensitive free-text data, whether this be real or synthetic (generated) data. De-identification processes remove explicit or implicit identifiers in free-text data that could result in the identification of individuals in a patient population.

## Scope
For this use case, it is necessary to capture the following in a meta-data schema:

### Deidentification Protocols:
Documents or other resources describing a procedure for deidentifying clinical text. Includes details on whether the approach is human or automated, which identifiers (implicit or explicit) are removed or replaced.

### Deidentification Process:
Application of a general protocol to a specific dataset, resulting in a deidentified dataset. Includes details of what the source / output datasets are, tool(s) used, evaluations of the efficacy of the process (if available), which metrics were used, sample sizes…. 

### Free-Text Datasets
Capturing the details of source and output (deidentified) datasets. Includes context (e.g. a clinical research question), corresponding query (e.g. in some formal language such as SNOMED CT’s ECL or OMOP), projects using the dataset, cohort descriptions, access restrictions, licensing…

### Risk Assessments:
(???) Potentially any risk assessments carried out on the dataset that go beyond the evaluation in the deidentification step. Could include assessments of risk when multiple datasets are used in conjunction…details?

