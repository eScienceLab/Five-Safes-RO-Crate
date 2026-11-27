# Five Safes RO-Crate Statistical Output Checking 1.0-DRAFT: machine-actionable rules

These pages are generated from the [MASP](https://github.com/Language-Research-Technology/ro-crate-masp) rules in the Statistical Output Checking module's [Profile Crate](../ro-crate-metadata.json). The [module specification](../index.html) is normative. The rules check what the module adds; an RO-Crate declaring the module is also checked against the [core rules](../../../rules/index.html).

## Reading the rules

- A statistical output check is an `AssessAction` whose `additionalType` includes the module term. MASP cannot choose a rule by the value of `additionalType`, so the rule for checks requires the term: `masp-validate` counts only the checks that carry it, and at least one is required. Validators that check every `AssessAction` against this rule also report other checks, such as checks of trained models.
- A finding's outcome is exactly one of `#Pass`, `#Fail` and `#NeedsReview`, matched as identifiers, so the terms need not be described in the RO-Crate.
- Some requirements relate entities and are stated only in the descriptions: a finding's `about` is an `object` of its check, and a finding is listed by exactly one check.
- `masp-validate` reports a failing rule only for entities it counts or reaches through a range. A decision or request carrying an outcome term is reported by validators that check every entity, such as wpsld, but not by `masp-validate`.

${rules.all}
