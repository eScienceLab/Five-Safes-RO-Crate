## What are Modules?

Every Five Safes RO-Crate must follow the base profile specification. The base profile is intended to be high-level and broad enough to avoid being too prescriptive regarding how a TRE functions or which capabilities it supports. In addition to this, it is possible to extend the base profile with modules. 

Modules can be viewed as "sub-profiles", created to address specific capabilities or requirements not covered in the base profile. These may include metadata for:

- Different data modalities (e.g., text, imaging)
- Phases in the TRE data lifecycle (e.g., cohort selection, data deidentification / anonymisation, output checking)
- Task handling, such as workflow execution or notebooks

A Five Safes RO-Crate must declare the base profile as well as any modules it uses. However, there is no expectation that all snapshots of a given activity record include the exact same modules. It is expected that these may change over the course of a project.

## Guidance on Module Creation

Modules should be created to address capabilities and requirements expected during the operation of a TRE, for which some metadata capture is required. However, care should be taken to avoid duplicating existing modules, for example modules should not be created to: 

- Fit solely to specific software, for example a single output checking tool rather than a general kind of output checking (e.g., semi-automated checking of machine learning models)
- Fit to a specific project or grant
- ...

While modules are intended to extend the base profile, and can be used in conjunction with other modules, they are not intended to extend one another. I.e., there is no notion of a "sub-module" or a "sub-sub-module".

Generally, a good sign that a module should be created is:

- There is a process that requires additional properties not covered by the process types in the [Five Safes RO-Crate profile](index.md#kinds-of-process).
- There are no existing modules addressing this need

