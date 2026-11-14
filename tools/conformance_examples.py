#!/usr/bin/env python3
"""Validate the ECRR examples by the CDIF conformance they actually have.

For each example (paired with its building block as tools/validate_examples.py
pairs them):

1. detect_conformance.py (CDIF validation repo) decides which CDIF conformance
   classes the record's content supports -- core, discovery, data_description, ...
   An ECRR profile composes CDIF CoreDiscovery as a first guess; detection, not that
   composition, decides what a record declares.
2. The record's schema:subjectOf dcterms:conformsTo is set to those classes, keeping
   the ECRR profile URIs it declares
   (https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/<Profile>) and any
   non-CDIF claims. --write saves the result to the example file.
3. ConformanceValidate.py validates the record against every URI it now declares: a
   CDIF class against its JSON Schema and SHACL from w3id (or the validation repo's
   local map with --cdif-source local), an ECRR profile against this repo's
   resolvedSchema.json and rules.shacl.

The validation repo is the `validation/` submodule (git submodule update --init),
or --validation-dir.

    python tools/conformance_examples.py                 # check
    python tools/conformance_examples.py --write         # also update conformsTo
    python tools/conformance_examples.py --cdif-source local --verbose
"""
import argparse
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import validate_examples as ve  # noqa: E402

ECRR_PROFILES = ROOT / "_sources" / "profiles" / "ecrrProfiles"
ECRR_PREFIX = "https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/"
CDIF_PREFIX = "https://w3id.org/cdif/"


def load_validation(validation_dir):
    """Import the validation repo's engines, or exit with how to get them."""
    vdir = Path(validation_dir).resolve()
    sys.path.insert(0, str(vdir))
    try:
        import ConformanceValidate as cv
        import detect_conformance as dc
    except ImportError as e:
        sys.exit(f"CDIF validation tools not found in {vdir} ({e}).\n"
                 "Run `git submodule update --init` or pass --validation-dir.")
    return cv, dc


class EcrrResolver:
    """ECRR profile URIs -> this repo's resolvedSchema.json and rules.shacl."""

    def __init__(self):
        self.dirs = {ECRR_PREFIX + d.name: d for d in ECRR_PROFILES.iterdir()
                     if (d / "resolvedSchema.json").exists()}

    def _dir(self, uri):
        return self.dirs.get(uri.rstrip("/"))

    def schema(self, uri):
        d = self._dir(uri)
        return json.loads((d / "resolvedSchema.json").read_text(encoding="utf-8")) if d else None

    def shacl(self, uri):
        d = self._dir(uri)
        return (d / "rules.shacl").read_text(encoding="utf-8") if d and (d / "rules.shacl").exists() else None


class ChainResolver:
    """The first resolver that knows a URI answers for it."""

    def __init__(self, *resolvers):
        self.resolvers = resolvers

    def schema(self, uri):
        return next((r for r in (x.schema(uri) for x in self.resolvers) if r is not None), None)

    def shacl(self, uri):
        return next((r for r in (x.shacl(uri) for x in self.resolvers) if r is not None), None)


def conforms_to(doc):
    subj = doc.get("schema:subjectOf")
    subj = subj if isinstance(subj, dict) else {}
    return [e.get("@id") if isinstance(e, dict) else e for e in subj.get("dcterms:conformsTo") or []]


def declare(doc, detected):
    """conformsTo = the detected CDIF classes, then the record's ECRR profile URIs and
    other non-CDIF claims, in their original order. A CDIF URI the record declared
    but detection did not support is dropped."""
    subj = doc.get("schema:subjectOf")
    if not isinstance(subj, dict):
        return doc
    kept = [{"@id": u} for u in conforms_to(doc)
            if isinstance(u, str) and (u.startswith(ECRR_PREFIX) or not u.startswith(CDIF_PREFIX))]
    subj["dcterms:conformsTo"] = [{"@id": u} for u in detected] + kept
    return doc


def write_json(path, data):
    raw = path.read_bytes().decode("utf-8")
    nl = "\r\n" if "\r\n" in raw else "\n"
    indent = 2 if '\n  "' in raw.replace("\r\n", "\n") else 4
    path.write_bytes((json.dumps(data, indent=indent, ensure_ascii=False) + "\n").replace("\n", nl).encode("utf-8"))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--write", action="store_true", help="Save the detected conformsTo to each example")
    ap.add_argument("--cdif-source", choices=("w3id", "local"), default="w3id",
                    help="Where CDIF class schemas come from (default w3id, the published profiles)")
    ap.add_argument("--validation-dir", default=str(ROOT / "validation"))
    ap.add_argument("--filter", help="Only examples whose path contains this")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    cv, dc = load_validation(args.validation_dir)
    resolver = ChainResolver(EcrrResolver(), cv.build_resolver(args.cdif_source, verbose=args.verbose))

    failed = changed = skipped = 0
    pairs = [(Path(e), s) for e, s in ve.find_example_schema_pairs()
             if not args.filter or args.filter in str(e)]
    for example, _schema in pairs:
        doc = json.loads(example.read_text(encoding="utf-8"))
        if not isinstance(doc.get("schema:subjectOf"), dict):
            # A building block's fragment example, not a record: no catalog record to
            # declare conformance in. tools/validate_examples.py checks it.
            skipped += 1
            print(f"SKIP {example.relative_to(ROOT)} (no catalog record)")
            continue
        detected = dc.detect_cdif_conformance(doc, verbose=False)
        new = declare(copy.deepcopy(doc), detected)
        if conforms_to(new) != conforms_to(doc):
            changed += 1
            if args.write:
                write_json(example, new)
        result = cv.run_conformance(new, resolver, verbose=args.verbose)
        bad = [p for p in result["profiles"]
               if p["schema"]["status"] in ("failed", "error") or p["shacl"]["status"] in ("failed", "error")]
        status = "FAIL" if bad else "PASS"
        failed += bool(bad)
        rel = example.relative_to(ROOT)
        print(f"{status} {rel}")
        print(f"     declares: {', '.join(u.replace(CDIF_PREFIX, '') for u in conforms_to(new))}")
        if conforms_to(new) != conforms_to(doc):
            print(f"     was:      {', '.join(str(u).replace(CDIF_PREFIX, '') for u in conforms_to(doc))}")
        for p in result["profiles"]:
            for kind in ("schema", "shacl"):
                r = p[kind]
                if r["status"] not in ("passed",):
                    errs = r.get("errors") or []
                    print(f"     {kind:6s} {r['status']:10s} {p['uri'].replace(CDIF_PREFIX, '')}"
                          + (f"  ({len(errs)} errors)" if errs else ""))
                    for e in errs[: 3 if args.verbose else 1]:
                        msg = e.get("message") or e.get("Message") or str(e)
                        where = e.get("path") or e.get("Result Path") or ""
                        print(f"            {where} {msg[:160]}")
    checked = len(pairs) - skipped
    verb = "updated" if args.write else "would change"
    print(f"\nResults: {checked - failed} passed, {failed} failed, {skipped} skipped "
          f"(no catalog record) of {len(pairs)}; conformsTo {verb} in {changed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
