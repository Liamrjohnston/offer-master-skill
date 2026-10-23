#!/usr/bin/env python3
"""First pass scanner for offer-honesty-check. Standard library only, no network.

Lists every number and red flag phrase in a piece of offer copy. With --facts,
it also says which numbers appear in the owner's facts. It finds candidates;
a person (or Claude) decides keep, fix, cut or flag.

  python3 flag_claims.py copy.md
  python3 flag_claims.py copy.md --facts brief.md
  cat copy.md | python3 flag_claims.py - --facts brief.md
"""
import argparse
import re
import sys

NUMBER = re.compile(
    r"(?<![\w\[])"                                # not inside a word or right after [
    r"(?P<cur>[$£€])?\s?"
    r"(?P<num>\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)"
    r"(?P<mult>\s?[kK]\b)?"
    r"(?P<pct>\s?%|\s?percent\b)?"
    r"(?P<x>x\b)?"
)

LIST_MARKER = re.compile(r"^\s*(?:[-*]\s*)?\d+[.)]\s")
LABEL = re.compile(r"\((?:yours|estimate)[^)]*\)", re.I)
PLACEHOLDER = re.compile(r"\[[^\]]*\]")

RED_FLAGS = {
    "fake value or anchor": [
        r"\bworth \$", r"\bvalued at\b", r"\b(?:a|an) \$[\d,]+ value\b", r"\btotal (?:bonus )?value\b",
        r"\bvalue:?\s*~?\$", r"\(value[: ]", r"\bregular(?:ly)? price", r"\bnormally \$", r"\bwas \$",
        r"\byou save\b", r"\bsave \$", r"\d+% off\b", r"~~[^~]+~~",
    ],
    "fake scarcity or pressure": [
        r"\bonly \d+ (?:spots?|places?|seats?)\b", r"\bspots? left\b", r"\bplaces? left\b", r"\balmost full\b",
        r"\bends tonight\b", r"\blast chance\b", r"\btoday only\b", r"\blimited time\b",
        r"\bprice (?:is )?going up\b", r"\bcountdown\b", r"\btimer\b", r"\bhurry\b", r"\bact now\b",
        r"\bpeople are viewing\b",
    ],
    "promise nobody can keep": [
        r"\bguaranteed (?:results?|to)\b", r"\bguarantee(?:s|d)? (?:you(?:'ll| will)?)\b",
        r"\blose \d+\s?(?:kg|lbs?|pounds|kilos)\b", r"\bdrop \d+ (?:sizes?|kg|lbs?)\b",
        r"\b(?:double|triple|10x)\b", r"\b\d+x (?:more|your)\b", r"\bmake \$", r"\bearn \$",
        r"\brisk[- ]free\b", r"\bno risk\b", r"\b100%\b", r"\bevery time\b", r"\bnever fails?\b",
    ],
    "borrowed authority or vague proof": [
        r"\bstudies show\b", r"\bresearch (?:shows|proves)\b", r"\bexperts agree\b",
        r"\bindustry (?:average|benchmark|standard)\b", r"\bon average\b", r"\btypically\b",
        r"\bmost (?:clients|people|customers|businesses)\b", r"\b\d+% of (?:clients|people|customers|businesses)\b",
        r"\bproven (?:system|method|process|framework)\b", r"\bthousands of\b", r"\b\d+\+ (?:clients|customers|happy)\b",
        r"\bas seen in\b", r"\bfeatured in\b", r"\baward[- ]winning\b",
    ],
    "hype word": [
        r"\bultimate\b", r"\bsecret\b", r"\brevolutionary\b", r"\bgame[- ]chang", r"\blife[- ]chang",
        r"\bunlock\b", r"\bskyrocket", r"\bsupercharge", r"\binsane\b", r"\bno[- ]brainer\b",
    ],
}


SENTENCE_END = re.compile(r"[.!?;](?=\s)|\|")


def sentence_around(line, start, end):
    """The sentence (or table cell) of line that holds positions start..end."""
    left = 0
    for m in SENTENCE_END.finditer(line, 0, start):
        left = m.end()
    nxt = SENTENCE_END.search(line, end)
    right = nxt.end() if nxt else len(line)
    return line[left:right]


def norm(match):
    """Turn a number match into a comparable value: '$3.5k' -> 3500.0."""
    n = float(match.group("num").replace(",", ""))
    if match.group("mult"):
        n *= 1000
    return n


def numbers_in(text):
    """All (value, is_percent) pairs in text, for matching against the copy."""
    vals = set()
    for line in text.splitlines():
        for m in NUMBER.finditer(line):
            vals.add((norm(m), bool(m.group("pct"))))
    return vals


def fmt(v):
    return f"{v:,.0f}" if v == int(v) else f"{v:,.2f}".rstrip("0").rstrip(".")


def scan(copy, facts=None):
    fact_vals = numbers_in(facts) if facts is not None else None
    found = {}
    flags = []
    for i, raw in enumerate(copy.splitlines(), 1):
        line = PLACEHOLDER.sub(lambda m: " " * len(m.group(0)), raw)
        if LIST_MARKER.match(line):
            line = LIST_MARKER.sub(lambda m: " " * len(m.group(0)), line, count=1)
        for m in NUMBER.finditer(line):
            labelled = bool(LABEL.search(sentence_around(raw, m.start(), m.end())))
            text = m.group(0).strip()
            v = norm(m)
            key = (v, bool(m.group("pct")))
            item = found.setdefault(key, {"text": text, "lines": [], "labelled": [], "value": v})
            item["lines"].append(i)
            item["labelled"].append(labelled)
        low = raw.lower()
        for group, pats in RED_FLAGS.items():
            for p in pats:
                for m in re.finditer(p, low):
                    flags.append((i, group, raw[m.start():m.end()], raw.strip()))
    rows = []
    for (v, pct), it in sorted(found.items(), key=lambda kv: kv[1]["lines"][0]):
        all_labelled = all(it["labelled"])
        some_labelled = any(it["labelled"])
        if fact_vals is None:
            source = "no facts given"
        else:
            source = "in facts" if (v, pct) in fact_vals else "NOT in facts"
        if fact_vals is not None and (v, pct) not in fact_vals:
            action = "Trace it: label (estimate) with its sum, use a [placeholder], or cut" if some_labelled \
                else "Unlabelled and not in the facts: trace it, label it, or cut it"
        elif all_labelled:
            action = "Labelled. Check the label is right"
        else:
            action = "Add a label: (yours) if the owner wrote it, (estimate) if worked out"
        rows.append((it["text"], ", ".join(map(str, it["lines"][:6])) + ("..." if len(it["lines"]) > 6 else ""),
                     source, "yes" if all_labelled else ("some" if some_labelled else "no"), action))
    return rows, flags


def report(rows, flags, has_facts):
    out = ["## Numbers", "", "| Number | Lines | Source | Labelled | What to do |", "|---|---|---|---|---|"]
    for r in rows:
        out.append("| " + " | ".join(r) + " |")
    if not rows:
        out.append("| (none found) | | | | |")
    out += ["", "## Red flag phrases", "", "| Line | Type | Phrase | Context |", "|---|---|---|---|"]
    for line, group, phrase, ctx in flags:
        ctx = ctx if len(ctx) <= 90 else ctx[:87] + "..."
        out.append(f"| {line} | {group} | {phrase} | {ctx.replace('|', '/')} |")
    if not flags:
        out.append("| | (none found) | | |")
    missing = sum(1 for r in rows if r[2] == "NOT in facts")
    unlabelled = sum(1 for r in rows if r[3] != "yes")
    out += ["", "## Summary", "",
            f"{len(rows)} distinct number{'' if len(rows) == 1 else 's'}, {unlabelled} not fully labelled"
            + (f", {missing} not found in the facts" if has_facts else " (no facts given, so none can be cleared)")
            + f". {len(flags)} red flag phrase{'' if len(flags) == 1 else 's'}.",
            "This is a first pass. Numbers worked out from the facts will show as NOT in facts; that's fine if labelled (estimate) with the sum shown."]
    return "\n".join(out)


def read(path):
    if path == "-":
        return sys.stdin.read()
    with open(path, encoding="utf-8") as f:
        return f.read()


def main(argv=None):
    ap = argparse.ArgumentParser(description="List numbers and red flag phrases in offer copy.")
    ap.add_argument("copy", help="file with the copy to check, or - for stdin")
    ap.add_argument("--facts", help="file with the owner's facts (the brief)")
    a = ap.parse_args(argv)
    try:
        copy = read(a.copy)
        facts = read(a.facts) if a.facts else None
    except OSError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2
    rows, flags = scan(copy, facts)
    print(report(rows, flags, facts is not None))
    return 0


if __name__ == "__main__":
    sys.exit(main())
