#!/usr/bin/env python3
"""Guarantee cost calculator for offer-guarantee. Standard library only, no network.

The cost of one claim is either a money amount (--remedy) or hours of the
owner's time (--hours with --rate). Everything printed is an estimate: the
claim rate is a planning assumption, not a prediction.

Examples:
  python3 guarantee_cost.py --price 3500 --hours 6 --rate 75
  python3 guarantee_cost.py --price 597 --remedy 199 --sales-per-month 4
  python3 guarantee_cost.py --price 2000 --remedy 2000 --profit 1600 --claim-rate 0.1 --stress 0.2
"""
import argparse
import sys


def money(x):
    return f"${x:,.0f}" if abs(x - round(x)) < 0.005 or abs(x) >= 100 else f"${x:,.2f}"


def per_n(extra_per_10):
    """Turn 'extra sales per 10' into a readable phrase."""
    if extra_per_10 <= 0:
        return "no extra sales"
    if extra_per_10 >= 1:
        n = f"{extra_per_10:.1f}".rstrip("0").rstrip(".")
        return f"{n} extra sale{'' if n == '1' else 's'} per 10"
    n = round(10 / extra_per_10)
    return f"about 1 extra sale per {n}"


def calc(price, claim_cost, claim_rate, profit=None, sales_per_month=None):
    claims_per_10 = 10 * claim_rate
    cost_per_10 = claims_per_10 * claim_cost
    revenue_per_10 = 10 * price
    share = cost_per_10 / revenue_per_10 if revenue_per_10 else float("nan")
    basis = profit if profit else price
    breakeven_per_10 = cost_per_10 / basis if basis else float("inf")
    out = {
        "claims_per_10": claims_per_10,
        "cost_per_10": cost_per_10,
        "share": share,
        "breakeven_per_10": breakeven_per_10,
        "basis": "using profit per sale" if profit else "using price, not profit",
    }
    if sales_per_month:
        out["monthly_cost"] = sales_per_month * claim_rate * claim_cost
    return out


def report(args):
    if args.remedy is not None:
        claim_cost = args.remedy
        what = f"a remedy of {money(args.remedy)}"
    else:
        claim_cost = args.hours * args.rate
        what = f"up to {args.hours:g} hours at {money(args.rate)}/hour = {money(claim_cost)}"
    lines = [f"Price {money(args.price)}. One claim costs {what}."]
    if claim_cost > args.price and args.remedy is not None:
        lines.append("Warning: the remedy is bigger than the price. Check this is intended.")
    for label, rate in (("Planning rate", args.claim_rate), ("Stress test", args.stress)):
        r = calc(args.price, claim_cost, rate, args.profit, args.sales_per_month)
        c = r['claims_per_10']
        line = (f"{label}, {rate * 100:g}% claim: per 10 sales, {c:g} claim{'' if c == 1 else 's'} cost "
                f"{money(r['cost_per_10'])}, {r['share'] * 100:.1f}% of that revenue (estimate). "
                f"Pays for itself with {per_n(r['breakeven_per_10'])} (estimate, {r['basis']}).")
        if "monthly_cost" in r:
            line += f" At {args.sales_per_month:g} sales a month: about {money(r['monthly_cost'])} a month (estimate)."
        lines.append(line)
    stress = calc(args.price, claim_cost, args.stress, args.profit)
    if args.max_share is None:
        lines.append(f"At the stress rate it costs {stress['share'] * 100:.0f}% of revenue. If the owner couldn't carry that, "
                     "shrink the remedy (a partial refund, fewer hours), not the honesty. Keep the cap in the words.")
    elif stress["share"] > args.max_share:
        lines.append(f"Too costly at the stress rate ({stress['share'] * 100:.0f}% of revenue, over the {args.max_share * 100:.0f}% limit given). "
                     "Shrink the remedy (a partial refund, fewer hours), not the honesty.")
    else:
        lines.append(f"Within the {args.max_share * 100:.0f}% limit given, even at the stress rate. Keep the cap in the words.")
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description="What a guarantee costs at a planning claim rate and a stress rate.")
    ap.add_argument("--price", type=float, required=True, help="price of one sale")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--remedy", type=float, help="money cost of one claim (a refund or credit)")
    g.add_argument("--hours", type=float, help="extra hours of work per claim (use with --rate)")
    ap.add_argument("--rate", type=float, help="the owner's hourly rate or cost, for --hours")
    ap.add_argument("--claim-rate", type=float, default=0.10, help="planning claim rate, default 0.10 (1 in 10)")
    ap.add_argument("--stress", type=float, default=0.20, help="stress test claim rate, default 0.20 (1 in 5)")
    ap.add_argument("--profit", type=float, help="profit per sale, for a truer break even")
    ap.add_argument("--sales-per-month", type=float, help="sales a month, to show a monthly cost")
    ap.add_argument("--max-share", type=float, help="the owner's own limit, as a share of revenue, e.g. 0.1; gives a verdict at the stress rate")
    args = ap.parse_args(argv)
    if args.hours is not None and args.rate is None:
        print("Error: --hours needs --rate", file=sys.stderr)
        return 2
    for name in ("price", "claim_rate", "stress"):
        if getattr(args, name) <= 0:
            print(f"Error: --{name.replace('_', '-')} must be above zero", file=sys.stderr)
            return 2
    if args.claim_rate > 1 or args.stress > 1:
        print("Error: claim rates are fractions, e.g. 0.1 for 1 in 10", file=sys.stderr)
        return 2
    print(report(args))
    return 0


if __name__ == "__main__":
    sys.exit(main())
