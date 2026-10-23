---
name: offer-diagnosis
description: Finds where buyers drop off and whether it's really the offer (or traffic, product, sales process) from the owner's numbers, and decodes what objections mean.
---

# Offer diagnosis

Two rules live here: **Is it the offer?** and **Decode objections.** Get these right and the rest of the rebuild aims at the real problem. Get them wrong and you polish an offer nobody sees.

## When to use it

- Someone says it isn't selling and gives numbers, objections or both.
- They ask why people say "I'll think about it", "too expensive" or "I can do it myself".
- `offer-master` calls it as stage one.

Not for: writing the new offer (that's `offer-included` and the others), or judging a market nobody has tried to sell to yet. For a brand new offer, skip the path maths and go straight to the objection map, using objections from the buyer's world, and say the diagnosis is untested.

## What you need

The stages a buyer passes through and a rough count at each, what buyers say when they don't buy, and where in the path they say it. If you're missing these, ask (at most three questions, then stop and wait):

1. In a normal month, roughly how many people see the offer, how many enquire or book a call, and how many buy?
2. When people don't buy, what do they say, and at what point (on the page, on a call, after the quote)?
3. Has it ever sold better? If so, what were the numbers then, and what changed?

If the owner has no numbers at all, say so, work from their objections alone, and make "count these for two weeks" the first action.

## Procedure

### 1. Lay out the path

Write the stages in order with the owner's own counts. Typical shapes:

- Content or ads, then sales page, then call booked, then sale.
- Enquiry, then quote, then reply, then sale.
- Shop page, then cart, then checkout, then repeat order.

Work out each step's rate yourself and label it (estimate). If you can run code, `scripts/funnel_leak.py` does the arithmetic and the "is it traffic?" check; otherwise do it by hand. Ranges the owner gives ("2 or 3") use the midpoint and say so.

| Stage | Count | Step rate |
|---|---|---|
| Saw the page | 600 (yours) | |
| Booked a call | 6 (yours) | 1% (estimate) |
| Bought | 3 (yours) | 50% (estimate) |

### 2. Find the leak

This skill uses no industry benchmark numbers on purpose; they vary too much to be honest. Locate the leak with these, in order:

1. **Where the evidence clusters.** Silence after a quote points at the quote. "I'll think about it" on calls points at belief or risk on the call. Nobody booking points at the page.
2. **Which step is weak next to the others.** A step that turns 1 in 100 into the next stage, followed by one that turns 1 in 2, puts the leak at the first.
3. **What changed.** If it used to sell, the step whose rate fell is the leak. Compare like with like, month to month.
4. **The traffic test.** Ask: if every step after the first doubled, would they reach the sales they need? If not, too few people see it, and traffic is part of the problem no matter how good the offer is.

### 3. Rule: Is it the offer?

Give one verdict, with the evidence for it, from this table. Most cases are one main cause plus one smaller one.

| Verdict | Signs | What to say and fix |
|---|---|---|
| **Traffic** | Very few people see it; the later steps convert fine; the traffic test fails | "Too few people see this. A better offer helps, but more reach is the main fix." Still rebuild the offer, but don't pretend it fixes reach |
| **The offer** | Plenty see it, few act; objections are about belief, value, risk or "what do I get" | Rebuild the offer. This is what the rest of the suite does |
| **The sales process** | People want it on the call, then go quiet; slow or no follow up; the quote is a bare price | Fix how the price is shown and followed up, alongside the offer. Name the one change |
| **The product** | People buy, then quit, ask for refunds or get poor results | Fix delivery and the first win before more selling. More buyers will make it worse |
| **Price presentation** | "Too expensive" with no sign they doubt the result; the price lands with no context | Show the price next to the cost of staying stuck and offer a payment option. Don't discount |
| **Wrong buyer** | Interest comes from people who can't afford it or don't have the problem badly | Narrow who it's for. Say who it's not for |

Write the verdict in two sentences: "This is mostly [verdict], because [owner's evidence]. Also fix [the smaller cause] by [one line]."

### 4. Rule: Decode objections

For every objection the owner reports, fill one row. The full map with over thirty objections is in [references/objection-map.md](references/objection-map.md).

| They say | The belief behind it | Type | Lever it hits | Fair? | What to change in the offer |
|---|---|---|---|---|---|
| "I'll think about it" | "I'm not sure it works for someone like me, and if it doesn't, I lose" | Trust, risk | Belief | Usually | Proof from people like them, shown early; a guarantee on the main fear |

Rules for decoding:

- Name the belief in the buyer's own voice, first person. That's what the offer has to change.
- Six types cover nearly everything: **value** (not worth it), **trust** (won't work for me), **effort** (too much work), **time** (too slow, or not now), **identity** (not for someone like me), **risk** (what if it fails).
- **If an objection is fair, change the offer.** If ten people say it's unclear what they get, it's unclear. Don't write a rebuttal for a true statement.
- The objection heard most, at the leaking stage, is the one the rebuild must answer first.
- Objections the owner reports are evidence. Ones you imagine are not: if you add a likely objection, say it's a guess.

### 5. Rule: Say it in one line (the current version)

Write the offer as it stands today in one sentence: "I help [who] get [result] in [time] through [what I do], for [price]." Leave a gap visibly empty when the owner's offer doesn't say it, for example "get [no result stated]". The gaps are part of the finding. `offer-included` writes the new version.

## Output (when used on its own)

```
**Where it leaks:** [path with counts, step rates labelled (estimate)]. The leak is [step], because [evidence].
**Is it the offer?** [verdict in two sentences, including any non-offer fix]
**What buyers mean:**
| They say | They mean | Fix in the offer |
**The offer today, in one line:** [sentence with visible gaps]
**Fix first:** [one or two things, in order]
**Check these:** [at most three]
```

## Worked example (illustration, fictional business)

A dog trainer sells a 6-week puppy course for $480. 900 people a month see the page from local Facebook groups, 9 book a free call, 2 buy. On calls people say "can't I just watch YouTube?" and "what if my puppy doesn't get it?"

- Path: 900 page views (yours), 9 calls (yours), 2 sales (yours). Page to call 1% (estimate). Call to sale about 22% (estimate).
- Leak: before the call, and a second, smaller one on it. The page converts 1 in 100; both objections come up on calls, so the call is losing people to doubt as well.
- Verdict: "This is mostly the offer, because people see it and don't book, and the ones who book doubt it'll work for their puppy. Also send a short written recap after each call, since there's no follow up now."
- Decoded: "YouTube" means "I'm buying information, and information is free"; fix by selling what video can't do (someone watching your dog and correcting you). "What if my puppy doesn't get it" means "the risk is mine"; fix with a guarantee on what the trainer controls.
- Today in one line: "I help [no buyer named] get [no result stated] in 6 weeks through a puppy course, for $480."

## Self-check

- [ ] Every count is the owner's, every rate is labelled (estimate), and no industry benchmark is quoted as fact.
- [ ] The verdict names one main cause and says plainly if part of it isn't the offer.
- [ ] Each objection has a belief in the buyer's voice and a change to the offer, not a rebuttal.
- [ ] Invented objections are marked as guesses.
- [ ] The current one line keeps its gaps visible.

## Reference files

| File | Read it when |
|---|---|
| [references/objection-map.md](references/objection-map.md) | Decoding any objection, collecting better ones, or building the objection list for a new offer |
| [references/leaks-and-causes.md](references/leaks-and-causes.md) | Working out the leak for a specific path shape, the "it used to sell" ladder, or fixes for non-offer problems |
| [scripts/funnel_leak.py](scripts/funnel_leak.py) | You can run Python and want the step rates and the traffic test done for you |
