---
name: offer-guarantee
description: Designs one fair, capped guarantee aimed at the buyer's main fear. Picks the type, sets the measure, conditions and cap, writes the exact words and claim steps, and costs it if 1 in 10 claim.
---

# The guarantee

One rule lives here: **One fair guarantee.** A good guarantee moves the risk from the buyer to the seller, on the exact thing the buyer is scared of, at a cost the owner can carry. A bad one is either toothless ("satisfaction guaranteed") or a trap for the owner (unlimited free work).

## When to use it

- After `offer-levers`, especially when Belief or the risk objection is the problem.
- Someone asks "should I offer a guarantee?", "what guarantee should I use?" or "is my guarantee any good?"
- Someone's guarantee is costing them too much, or nobody notices it.

## What you need

The price, the main objection or fear, what the owner controls versus what depends on the buyer, the owner's delivery cost or hourly rate if a remedy uses their time, and roughly how many sales they make. If missing, ask (at most three):

1. What's the buyer most scared of: that it won't work, that it won't suit them, or that you won't deliver?
2. What part of the result is fully in your hands, and what depends on the buyer doing the work?
3. If one in ten buyers claimed it, what could you afford to give back: money, extra hours, or extra weeks?

## Procedure

### 1. Name the main fear

Write it in the buyer's voice, from the top objection: "What if I do everything and nothing changes?" The guarantee must answer this sentence. A guarantee on anything else is decoration.

### 2. Pick the type

Ask these in order and stop at the first yes. The full library, with when not to use each type, is in [references/guarantee-library.md](references/guarantee-library.md).

| Question | Type | Pattern |
|---|---|---|
| Is the fear "you won't deliver what you said, when you said"? | **Delivery date** | "If it isn't [delivered] by [date], you get [credit or refund per week late], up to [cap]." |
| Is the fear "it won't pay off" or "someone cheaper could do this", on done-for-you work? | **Capped keep going** | "Do [two actions]. Use it for [the same window as the proof]. If [the feared result] still isn't coming through the work, we [one extra piece of work], up to [cap]. This does not promise [the number], and it is not a refund." |
| Is the result mostly in the owner's control? | **Outcome** | "If [measurable result] isn't [true] by [time], we [remedy, capped]." |
| Does the result depend on the buyer doing the work (training, coaching, a habit)? | **Do the work** | "Do [two clear actions] for [time]. If we haven't delivered [the work we control], we [remedy]." |
| Is the fear just "what if it's not for me"? | **No questions refund window** | "Not for you in the first [14 or 30] days? Ask and get a full refund." |
| Is the work used up straight away (custom, done for you)? | **Capped keep going** or **partial refund** | "If [result] isn't met, we keep working at no cost for up to [N hours / weeks]." or "a refund for any part not yet delivered" |
| Is the price high and the buyer needs to see it work first? | **First phase** | "Start with [phase one] for [smaller price]. If it doesn't [result], stop there and owe nothing more." |

### 3. Aim it at the nearest thing the owner controls

If the feared result isn't fully in the owner's control (weight, sales, bookings, income), guarantee the nearest measurable thing that is, and say plainly what isn't guaranteed.

| Feared result (not controllable) | Nearest controllable thing to guarantee |
|---|---|
| "I'll lose weight" or "I'll get stronger" | The plan delivered and the agreed sessions held. Not a weight, and not a heavier lift. |
| "It won't pay off" or "someone cheaper could do this" | The work live and tested, plus one capped extra pass if they did their part and the result still isn't coming through it (one more page, a listing rework, up to a set number of hours). Not a booking count. Not a refund of the fee. Say the number is not guaranteed. |
| "It'll save us time" | The automation built and running on their real work. The hours saved are theirs to measure. Do not write a number they didn't give you. |
| "I'll be able to speak the language" | The lessons held. Not a fluency promise. |

### 4. Set conditions, cap and claim steps

- **Two conditions at most**, both easy for the buyer to show (sessions attended, steps completed). Long fine print reads like a trap.
- **The measure is fair and checkable.** Agree it before the start (a before measurement, a log).
- **The remedy always has a ceiling.** A refund amount, a set number of extra hours, or a set extra period. Never "until it's fixed" with no limit; write the cap into the words.
- **Say how to claim.** Who to message, by when, what to show.
- **Any threshold you chose** (hours, kilos, bookings, days) is your suggestion. List it under "Check these" so the owner sets it.
- A guarantee adds to the buyer's legal rights; it never replaces them. Never write "all sales final".

### 5. Cost it

Assume one buyer in ten claims (a planning assumption, labelled (estimate)). Show the sum in one line, then how many extra sales would pay for it. If the remedy is your time and they never gave a rate, write [your day rate] × [days]. Do not invent $200 a day or $600. If you can run code, `scripts/guarantee_cost.py` does this, including a one in five stress test.

> Per 10 sales, 1 claim costs [remedy] = [amount] (estimate), [x]% of that revenue (estimate). It pays for itself if it brings [n] extra sale(s) per 10 (estimate).

If the owner can't afford it, shrink the remedy (a partial refund, fewer extra hours), not the honesty.

### 6. Write it

Pattern: **"If [X] doesn't happen by [Y], we [Z, capped]."** Then one line on how to claim. Plain words, no "ironclad", "risk free" or "100% guaranteed results".

## Output (when used on its own)

```
**Main fear:** "[buyer's voice]"
**Type:** [type], because [one line]
**Guarantee, exact words:** "[If..., we...]" To claim: [how].
**Conditions:** [at most two]
**Cap:** [the ceiling]
**What it doesn't cover:** [the result the owner can't control, said plainly]
**Cost if 1 in 10 claim:** [sum] (estimate). At 1 in 5: [sum] (estimate).
**Check these:** [thresholds and amounts the owner must confirm]
```

## Worked example (illustration, fictional business)

A bookkeeper charges $1,200 to clean up a year of messy books for a small shop. The fear: "What if I pay and my accountant still finds a mess?" The work is done for the buyer and used up once delivered, so a full refund after delivery would be unfair to the owner.

- Type: capped keep going, because the work is custom and the result (books the accountant accepts) is mostly in the bookkeeper's control.
- Words: "If your accountant finds an error in the books we cleaned up, we fix it at no cost, up to 6 extra hours, within 60 days of handover. To claim, forward us the accountant's note."
- Conditions: the shop sends all statements by the start date; claims within 60 days.
- Cap: 6 hours.
- Doesn't cover: tax advice or errors in records the shop didn't send.
- Cost if 1 in 10 claim, using the bookkeeper's $60 an hour: per 10 jobs, 1 claim of up to 6 hours = up to $360 (estimate), 3% of $12,000 revenue (estimate). Pays for itself with 1 extra job per 33 (estimate).

## Self-check

- [ ] It answers the main fear in the buyer's voice. If the fear is that it won't pay off, a "we delivered the button" guarantee is a fail. The remedy is one capped extra piece of work, and the line says the result number is not guaranteed.
- [ ] One guarantee, not several.
- [ ] Two conditions at most, a fair measure, a written cap and a claim step.
- [ ] It guarantees only what the owner controls, and says what isn't covered.
- [ ] No guarantee of weight, income or business results.
- [ ] Costed at 1 in 10, labelled (estimate); thresholds listed under "Check these".

## Reference files

| File | Read it when |
|---|---|
| [references/guarantee-library.md](references/guarantee-library.md) | Choosing a type, and checking when each one is the wrong choice |
| [references/terms-and-costs.md](references/terms-and-costs.md) | Writing the full terms, handling claims, the cost maths and the legal common sense |
| [scripts/guarantee_cost.py](scripts/guarantee_cost.py) | You can run Python and want the cost, the stress test and the break-even worked out |
