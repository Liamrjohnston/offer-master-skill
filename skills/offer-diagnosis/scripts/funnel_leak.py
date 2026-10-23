#!/usr/bin/env python3
"""Funnel leak calculator for offer-diagnosis. Standard library only, no network.

Give the buyer path as "Stage=count" pairs, in order. Counts are the owner's
numbers; every rate this prints is an estimate.

Examples:
  python3 funnel_leak.py "Page views=400" "Calls=2-3" "Sales=1"
  python3 funnel_leak.py "Page views=400" "Calls=2.5" "Sales=1" --goal 4
  python3 funnel_leak.py "Enquiries=6" "Replies=2" "Sales=1" --past "Enquiries=6" "Replies=4" "Sales=2"
"""
import argparse
import re
import sys


def parse_count(raw):
    """Return (value, note). Accepts 400, 2.5, '2-3' or '2 to 3' (midpoint)."""
    text = raw.strip().replace(",", "")
    m = re.fullmatch(r"(\d+(?:\.\d+)?)\s*(?:-|to)\s*(\d+(?:\.\d+)?)", text)
    if m:
        lo, hi = float(m.group(1)), float(m.group(2))
        if hi < lo:
            lo, hi = hi, lo
        return (lo + hi) / 2, f"range {raw.strip()}, midpoint used"
    try:
        value = float(text)
    except ValueError:
        raise ValueError(f"can't read a number from '{raw}'")
    if value < 0:
        raise ValueError(f"counts can't be negative: '{raw}'")
    return value, ""


def parse_stages(items):
    stages = []
    for item in items:
        if "=" not in item:
            raise ValueError(f"'{item}' should look like Stage=count")
        name, raw = item.rsplit("=", 1)
        value, note = parse_count(raw)
        stages.append((name.strip(), value, note))
    if len(stages) < 2:
        raise ValueError("give at least two stages")
    for (n1, v1, _), (n2, v2, _) in zip(stages, stages[1:]):
        if v2 > v1:
            raise ValueError(f"'{n2}' ({fmt(v2)}) is bigger than '{n1}' ({fmt(v1)}); stages must narrow")
    return stages


def fmt(x):
    return str(int(x)) if float(x).is_integer() else f"{x:.1f}"


def label(note):
    """A midpoint of the owner's range is our number, not theirs."""
    return f"(estimate) [{note}]" if note else "(yours)"


def pct(x):
    if x is None:
        return "n/a"
    p = x * 100
    if p >= 10:
        return f"{p:.0f}%"
    if p >= 1:
        return f"{p:.1f}%"
    return f"{p:.2f}%"


def rates(stages):
    out = []
    for (_, v1, _), (_, v2, _) in zip(stages, stages[1:]):
        out.append(v2 / v1 if v1 else None)
    return out


def report(stages, goal=None, past=None):
    lines = []
    r = rates(stages)
    lines.append("| Stage | Count | Step rate | Lost at this step |")
    lines.append("|---|---|---|---|")
    first = stages[0]
    lines.append(f"| {first[0]} | {fmt(first[1])} {label(first[2])} | | |")
    for i, (name, value, note) in enumerate(stages[1:]):
        lost = stages[i][1] - value
        lines.append(f"| {name} | {fmt(value)} {label(note)} | {pct(r[i])} (estimate) | {fmt(lost)} (estimate) |")
    overall = stages[-1][1] / stages[0][1] if stages[0][1] else None
    lines.append("")
    lines.append(f"End to end: {pct(overall)} of '{stages[0][0]}' reach '{stages[-1][0]}' (estimate).")
    small = [n for n, v, _ in stages[1:] if 0 < v < 20]
    if small:
        lines.append(f"Small numbers at {', '.join(small)}: one buyer either way moves these rates a lot. Treat them as rough.")
    weakest = min((x, i) for i, x in enumerate(r) if x is not None) if any(x is not None for x in r) else None
    if weakest:
        x, i = weakest
        lines.append(f"Lowest step rate: '{stages[i][0]}' to '{stages[i + 1][0]}' at {pct(x)} (estimate). "
                     "A low rate is a clue, not a verdict: check where buyers actually say no.")

    if past:
        pr = rates(past)
        if [n for n, _, _ in past] != [n for n, _, _ in stages]:
            lines.append("")
            lines.append("Past stages don't match the current stage names, so no comparison was made.")
        else:
            lines.append("")
            lines.append("| Step | Before | Now | Change |")
            lines.append("|---|---|---|---|")
            worst = None
            for i in range(len(r)):
                step = f"{stages[i][0]} to {stages[i + 1][0]}"
                if pr[i] and r[i] is not None:
                    change = (r[i] - pr[i]) / pr[i]
                    lines.append(f"| {step} | {pct(pr[i])} | {pct(r[i])} | {change * 100:+.0f}% (estimate) |")
                    if worst is None or change < worst[0]:
                        worst = (change, step)
                else:
                    lines.append(f"| {step} | {pct(pr[i])} | {pct(r[i])} | n/a |")
            top_change = (stages[0][1] - past[0][1]) / past[0][1] if past[0][1] else None
            if top_change is not None:
                lines.append(f"Top of path changed by {top_change * 100:+.0f}% (estimate).")
            if worst and worst[0] < 0:
                lines.append(f"Biggest fall: {worst[1]} ({worst[0] * 100:+.0f}%, estimate). Start the diagnosis there.")
            elif top_change is not None and top_change < 0:
                lines.append("No step got worse; fewer people at the top explains the drop. That's traffic.")

    if goal is not None:
        lines.append("")
        current = stages[-1][1]
        lines.append(f"Goal: {fmt(goal)} '{stages[-1][0]}' a month. Now: {fmt(current)} (yours).")
        if overall:
            needed_top = goal / overall
            lines.append(f"At today's rates you'd need about {needed_top:,.0f} '{stages[0][0]}' to reach the goal (estimate).")
        doubled = stages[0][1]
        for x in r:
            doubled *= min(1.0, 2 * x) if x is not None else 0
        lines.append(f"If every step after '{stages[0][0]}' doubled: about {fmt(round(doubled, 1))} '{stages[-1][0]}' (estimate).")
        if doubled < goal:
            lines.append("Verdict: even doubling every step falls short, so too few people see it. Traffic is part of the problem.")
        else:
            lines.append("Verdict: better steps alone could reach the goal. Traffic is not the main blocker.")
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Step rates, the biggest fall and the traffic test for a buyer path.")
    ap.add_argument("stages", nargs="+", help='Stage=count pairs in order, e.g. "Page views=400" "Calls=2-3" "Sales=1"')
    ap.add_argument("--goal", type=float, help="the number of final-stage buyers the owner wants a month")
    ap.add_argument("--past", nargs="+", help="the same stages from a period when it sold better")
    args = ap.parse_args(argv)
    try:
        stages = parse_stages(args.stages)
        past = parse_stages(args.past) if args.past else None
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2
    print(report(stages, goal=args.goal, past=past))
    return 0


if __name__ == "__main__":
    sys.exit(main())
