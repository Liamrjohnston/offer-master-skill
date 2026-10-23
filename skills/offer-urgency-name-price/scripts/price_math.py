#!/usr/bin/env python3
"""Price sums for offer-urgency-name-price. Standard library only, no network.

Three jobs, each a subcommand. Every result is labelled (estimate) because it
rests on inputs the owner or buyer gave; the script never invents an input.

  wait   What waiting costs the buyer, and when the price is covered.
         python3 price_math.py wait --monthly-cost 400 --price 1800 --months 3
         python3 price_math.py wait --hours 10 --rate 60 --price 2400

  plan   A payment plan's total and the honest sentence to show with it.
         python3 price_math.py plan --price 1000 --payments 4 --amount 260

  value  The price as a share of what the result is worth over a period.
         python3 price_math.py value --price 2400 --monthly-value 600 --months 12
"""
import argparse
import sys


def money(x):
    return f"${x:,.0f}" if abs(x - round(x)) < 0.005 or abs(x) >= 1000 else f"${x:,.2f}"


def num(x):
    return f"{x:.1f}".rstrip("0").rstrip(".")


def wait_report(a):
    if a.monthly_cost is not None:
        monthly = a.monthly_cost
        how = f"{money(monthly)} a month"
    else:
        monthly = a.hours * a.rate
        how = f"{num(a.hours)} hours a month at {money(a.rate)}/hour = {money(monthly)} a month"
    lines = [f"The problem costs {how} (estimate)."]
    lines.append(f"Waiting {num(a.months)} month{'' if a.months == 1 else 's'} costs about {money(monthly * a.months)} (estimate).")
    if a.price is not None:
        months_to_cover = a.price / monthly
        lines.append(f"The {money(a.price)} price equals about {num(months_to_cover)} month{'' if round(months_to_cover, 1) == 1 else 's'} of the problem (estimate).")
    lines.append("Only use this if the monthly figure came from the owner or buyer. Otherwise show the sum with [placeholders].")
    return "\n".join(lines)


def plan_report(a):
    total = a.payments * a.amount
    diff = total - a.price
    p = f"{a.payments:g} payments of {money(a.amount)}"
    if abs(diff) < 0.005:
        sentence = f"{money(a.price)}, or {p} (same total)."
    elif diff > 0:
        sentence = f"{money(a.price)}, or {p} ({money(total)} in total, {money(diff)} more than paying in full)."
    else:
        sentence = (f"{money(a.price)}, or {p} ({money(total)} in total, {money(-diff)} less than paying in full). "
                    "Check this: a plan that costs less than paying in full is unusual.")
    lines = [f"Plan total: {money(total)}. Pay in full: {money(a.price)}.", f"Show it as: {sentence}"]
    if diff > 0:
        lines.append(f"Plan costs {diff / a.price * 100:.1f}% more. Don't call paying in full a 'saving' unless both totals are shown.")
    return "\n".join(lines)


def value_report(a):
    value = a.monthly_value * a.months
    share = a.price / value
    cover = a.price / a.monthly_value
    lines = [
        f"Worth about {money(value)} over {num(a.months)} months, at {money(a.monthly_value)} a month (estimate).",
        f"The {money(a.price)} price is {share * 100:.0f}% of that (estimate). Covered after about {num(cover)} months (estimate).",
    ]
    if share >= 1:
        lines.append("The price is more than the value shown over this period. Show a different comparison or raise Result first.")
    elif share > 0.5:
        lines.append("The price is over half the value shown. The comparison may not persuade; check the inputs and the period.")
    lines.append("Only use this if the monthly value came from the owner or buyer. Never present it as a guaranteed return.")
    return "\n".join(lines)


def positive(name, value):
    if value is not None and value <= 0:
        raise ValueError(f"--{name.replace('_', '-')} must be above zero")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Honest price sums: cost of waiting, payment plans, value to price.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    w = sub.add_parser("wait", help="cost of waiting")
    g = w.add_mutually_exclusive_group(required=True)
    g.add_argument("--monthly-cost", type=float, help="what the problem costs each month")
    g.add_argument("--hours", type=float, help="hours lost each month (use with --rate)")
    w.add_argument("--rate", type=float, help="value of one hour, for --hours")
    w.add_argument("--months", type=float, default=3, help="months of waiting to show, default 3")
    w.add_argument("--price", type=float, help="the offer price, to show months to cover")

    p = sub.add_parser("plan", help="payment plan total")
    p.add_argument("--price", type=float, required=True, help="pay in full price")
    p.add_argument("--payments", type=float, required=True, help="number of payments")
    p.add_argument("--amount", type=float, required=True, help="amount of each payment")

    v = sub.add_parser("value", help="price against value")
    v.add_argument("--price", type=float, required=True)
    v.add_argument("--monthly-value", type=float, required=True, help="what the result is worth each month")
    v.add_argument("--months", type=float, default=12, help="period to compare over, default 12")

    a = ap.parse_args(argv)
    try:
        for name, val in vars(a).items():
            if name != "cmd" and isinstance(val, float):
                positive(name, val)
        if a.cmd == "wait":
            if a.hours is not None and a.rate is None:
                raise ValueError("--hours needs --rate")
            out = wait_report(a)
        elif a.cmd == "plan":
            if a.payments != int(a.payments) or a.payments < 2:
                raise ValueError("--payments must be a whole number, 2 or more")
            out = plan_report(a)
        else:
            out = value_report(a)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
