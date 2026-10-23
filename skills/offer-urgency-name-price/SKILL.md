---
name: offer-urgency-name-price
description: Sets the honest why now, the cost of waiting, a name a buyer would text a friend, and the price shown against real value, with payment options. Real deadlines only, no fake anchors.
---

# Urgency, name and price

Three rules live here: **Real deadlines, Cost of waiting, A name you'd text,** plus pricing from real value. These are the parts of an offer where pressure tactics creep in. Every one has an honest version that works, and that's the only version this skill writes.

## When to use it

- After the offer is built (`offer-included`) and the guarantee is set (`offer-guarantee`).
- Someone asks "how do I create urgency?", "what should I call it?", "what should I charge?", "should I offer a payment plan?" or "should I raise my price?"

## What you need

The price and how it's billed, any real limits (capacity, start dates, price changes the owner will actually make, seasons in the buyer's world), the buyer's cost of staying stuck if the owner knows it, and the current name. If missing, ask (at most three):

1. Is there anything real that changes if someone waits: a start date, a capacity limit, a price change you'll actually make, a season?
2. What does the problem cost your buyer each month they don't fix it? Money, hours or something else.
3. How do people pay now, and would you take payment in parts?

## Procedure

### 1. Rule: Real deadlines

Use a reason to act now only if it's true, the buyer could check it, and the owner will stick to it. Check each candidate:

| Question | If no |
|---|---|
| Is it true today? | Drop it |
| Will the owner enforce it, every time? | Drop it |
| Could the buyer check it? | Make it checkable or drop it |
| Will it still be honest next month (no rolling "ends tonight")? | Drop it |

Honest reasons, and how to word them:

| Reason | Wording |
|---|---|
| Capacity | "I take [max] clients at a time. [N] places are open." The max is the owner's; the open places stay [N] unless the owner said |
| A real start date | "The next group starts on [date]. Joining after that means waiting for the following one." |
| A real price change | "The price goes to [new price] on [date]." Only if it really will |
| A season in the buyer's world | "To be ready for [tax deadline / summer / the busy season], start by [date]." |
| A bonus that really ends | "[Bonus] is included for anyone who starts before [date]." Only if it really ends |

If none is true, write "Open all year." That's a fine answer; the cost of waiting does the work. Never invent spots, timers or "price goes up soon". More in [references/real-urgency.md](references/real-urgency.md).

### 2. Rule: Cost of waiting

Say what another month of the problem costs the buyer, in their terms. Always available, always honest, when built from real inputs.

- Use the buyer's numbers or the owner's numbers. If an input is missing, write the sum with a placeholder: "each month costs [hours lost] × [your hourly rate]". Don't invent the input.
- Money is best when it's real. Time, missed chances and the problem getting worse also count.
- Label any sum (estimate). Keep it to one line.

### 3. Rule: A name you'd text

The test: could the buyer text the name to a friend and the friend would know what it is? Draft five, pick one.

- Say who it's for or what it does. Plain beats clever.
- Two to five words. A container word helps: plan, program, setup, sprint, clinic, course.
- Never a money, weight or health result with a time frame ("Lose 10 kg in 12 Weeks", "$10k Month Method"). Results go in proof.
- No jargon, no acronyms the buyer doesn't use, no hype words ("ultimate", "mastery", "secret").
- Don't borrow a trademarked framework name.

Patterns and examples: [references/naming.md](references/naming.md).

### 4. The price

Price from real value, show it honestly, and make it easy to pay. Maths and rules in [references/pricing-math.md](references/pricing-math.md); `scripts/price_math.py` does the sums if you can run code.

- **Show it next to the cost of staying stuck** or the next real alternative (hiring someone, doing it badly, the owner's own other prices). Every comparison must be real and checkable.
- **Match billing to the promise.** A 12 week program reads better as one 12 week price, payable in parts, than an open monthly fee.
- **A payment option before any discount.** If the plan costs more in total, say the total plainly. Never sell a costlier plan as a saving.
- **No fake anchors.** No "worth $X" without a real comparable, no crossed out price the owner never charged, no "you save" against a made up number.
- **Never discount to win a new customer.** It cheapens the offer and draws buyers who leave first. Rewards for existing customers are fine.
- **A higher price needs Result and Belief at 7 or more** (see `offer-levers`). Otherwise raise those first.
- **The stress test:** if buyers say it feels too cheap, they don't trust it; if they say too expensive, they can't see the value. Fix the cause, not the number.

## Output (when used on its own)

```
**Why now:** [a real reason, worded honestly, or "Open all year"]
**Cost of waiting:** [one line, (estimate), placeholders where inputs are missing]
**Name:** [pick], from: [four others]. Passes the text test because [reason].
**Price:** [price, billed to match the promise], or [payment option, with total]. Shown next to [real comparison] (estimate).
**Don't:** [any tactic the owner asked for that isn't honest, and the honest version]
**Check these:** [at most three]
```

## Worked example (illustration, fictional business)

A landscaper sells a spring garden reset for $1,800. He can do 6 a month in spring. He wants "a countdown timer, like the big brands". Clients say "I'll do it in summer".

- **Why now:** "I do 6 spring resets a month. [N] places are open for April." No timer: it would be fake, and the season is the real deadline. "Planting done in April has the whole season to fill in; done in July it mostly waits for next year." (Check the landscaper agrees with that claim.)
- **Cost of waiting:** "Each month you wait is a month of the garden you're paying for and not using." No number, because the owner gave none.
- **Name:** "Spring Garden Reset" (from: Garden Fresh Start, The April Reset, Weekend Garden Fix, Spring Yard Plan). A friend would know exactly what it is.
- **Price:** $1,800, or $900 to book and $900 on completion, same total. Shown next to [what a full redesign costs, if the landscaper offers one].
- **Don't:** the countdown timer. Honest version: the real April capacity.

## Self-check

- [ ] Every reason to act now is true, checkable and enforced, or the answer is "Open all year".
- [ ] Open places are [N] unless the owner said how many are free.
- [ ] The cost of waiting uses real inputs or placeholders, labelled (estimate).
- [ ] The name passes the text test and makes no result plus time claim.
- [ ] The price comparison is real; no fake anchor, no "you save", no crossed out price.
- [ ] Any payment plan states its total; no discount to win new buyers.

## Reference files

| File | Read it when |
|---|---|
| [references/real-urgency.md](references/real-urgency.md) | Choosing and wording a reason to act now, and the tactics to refuse |
| [references/naming.md](references/naming.md) | Naming patterns, examples and the names to avoid |
| [references/pricing-math.md](references/pricing-math.md) | Cost of waiting sums, value to price, payment plans, anchors, discounts and price rises |
| [scripts/price_math.py](scripts/price_math.py) | You can run Python and want the waiting, plan or value sums done |
