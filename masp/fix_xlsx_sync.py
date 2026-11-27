#!/usr/bin/env python3
"""Undo what syncing a spreadsheet to JSON with generate-masp-docs 0.1.0 changes besides the edits.

Usage: python3 masp/fix_xlsx_sync.py <synced ro-crate-metadata.json> <Profile Crate ro-crate-metadata.json>

Merges the synced JSON into the Profile Crate's JSON (the second file, which is rewritten):
keeps its @context and the descriptor's RO-Crate version, writes sh:minCount and sh:maxCount as
integers, drops the isPartOf the tool adds as the inverse of every hasPart (such as on
every rule) and the identifier it adds to the
descriptor, and keeps the original order of entities and of unchanged lists, so that the diff
shows only what was edited in the spreadsheet. It also removes the vocabularies and the other
descriptors' artifacts (such as the conformance indicators) that the tool adds to the rules. Standard library only.
"""
import json
import sys

COUNTS = ("sh:minCount", "sh:maxCount")


def as_list(value):
    return value if isinstance(value, list) else [value]


def same_items(a, b):
    key = lambda v: json.dumps(v, sort_keys=True)
    return sorted(map(key, as_list(a))) == sorted(map(key, as_list(b)))


def main(synced_path, crate_path):
    synced = json.load(open(synced_path, encoding="utf-8"))
    crate = json.load(open(crate_path, encoding="utf-8"))
    before = {e["@id"]: e for e in crate["@graph"]}
    # the tool adds isPartOf as the inverse of every hasPart
    parents = {}
    for e in synced["@graph"]:
        for part in as_list(e.get("hasPart", [])):
            if isinstance(part, dict):
                parents.setdefault(part.get("@id"), []).append({"@id": e["@id"]})

    types = {e["@id"]: as_list(e.get("@type", [])) for e in synced["@graph"]}
    schema = next((e["@id"] for e in crate["@graph"]
                   if {"@id": "http://www.w3.org/ns/dx/prof/role/schema"} in as_list(e.get("hasRole", []))), None)

    artifacts = [a for e in crate["@graph"] for a in as_list(e.get("hasArtifact", []))]

    merged = {}
    for entity in synced["@graph"]:
        old = before.get(entity["@id"], {})
        fixed = {}
        for key, value in entity.items():
            if key in COUNTS and isinstance(value, str) and value.strip().lstrip("-").isdigit():
                value = int(value)
            if key not in old:
                if key == "isPartOf" and all(v in parents.get(entity["@id"], []) for v in as_list(value)):
                    continue
                if key == "identifier" and entity["@id"] == "ro-crate-metadata.json":
                    continue
            if key == "hasPart" and entity["@id"] == schema:
                # the tool adds the vocabularies and other descriptors' artifacts to the rules
                value = [v for v in as_list(value) if v in as_list(old.get(key, []))
                         or not ("DefinedTermSet" in types.get(v.get("@id"), []) or v in artifacts)]
            if key in old and isinstance(value, list) and same_items(value, old[key]):
                value = old[key]  # keep the original order
            fixed[key] = value
        if entity["@id"] == "ro-crate-metadata.json" and "conformsTo" in old:
            fixed["conformsTo"] = old["conformsTo"]  # the tool declares RO-Crate 1.2
        # keep the original order of properties, new ones last
        merged[entity["@id"]] = {k: fixed[k] for k in [*old, *fixed] if k in fixed}

    order = [i for i in before if i in merged] + [i for i in merged if i not in before]
    removed = [i for i in before if i not in merged]
    out = {"@context": crate["@context"], "@graph": [merged[i] for i in order]}
    with open(crate_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    added = [i for i in merged if i not in before]
    print(f"Wrote {crate_path}: {len(order)} entities, added {added or 'none'}, removed {removed or 'none'}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
