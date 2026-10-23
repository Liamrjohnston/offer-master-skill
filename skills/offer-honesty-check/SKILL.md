---
name: offer-honesty-check
description: Audits an offer, sales page or draft for invented numbers, fake scarcity, fake bonus values, unbacked promises and stretched results. Traces each claim to its source, then fixes or flags it.
---

# Honesty check

Most offers written with AI fail here. They invent a testimonial, put "$497 value" on a checklist, add "only 3 spots left", or promise a result in a time frame nobody can guarantee. Buyers notice, platforms notice, and in many countries it's illegal. This skill finds every claim, traces it to where it came from, and decides keep, fix, cut or flag.

## When to use it

- Always, as stage 6 of `offer-master`, on every line drafted before the card.
- On its own: "check my sales page", "is this offer honest?", "audit this copy", or any offer someone pastes in, including one written by another tool.

## What you need

The copy to check, and the owner's facts (what they sell, their numbers, their proof, their limits). Without the facts you can still flag every claim that needs a source, but you can't clear any of them. Say so at the top.

If the facts are missing, ask (at most three):

1. What results can you prove, with names and numbers?
2. Is anything here (a price, a spot count, a deadline, a bonus value) something you haven't actually done or charged?
3. Are you in a regulated field: health, money, legal, or anything aimed at children?

## Procedure

### 1. List every claim

Go line by line. A claim is anything a buyer could ask "says who?" about:

- every number (money, percentages, counts, time frames, ratings);
- every result, client name, testimonial or case study;
- every value, regular price, saving or anchor;
- every limit, deadline or "only N left";
- every promise about what the buyer will get or feel;
- every comparison ("better than", "the only", "most clients", "on average").

If you can run Python, `scripts/flag_claims.py` gives you a first pass: it lists every number and red flag phrase, and with `--facts` says which numbers appear in the owner's facts. It finds candidates; you decide.

### 2. Trace each one

| Source | Meaning |
|---|---|
| **Owner** | The owner wrote this exact fact or number |
| **Worked out** | Calculated from the owner's numbers; the sum can be shown |
| **Assumption** | A planning figure (a claim rate, an hourly value) not from the owner |
| **None** | Nobody gave it. It was written to sound good |

### 3. Apply the rules

Each rule below has a test and the fix. Full detail and examples: [references/honesty-rules.md](references/honesty-rules.md).

| # | Rule | Fails when | Fix |
|---|---|---|---|
| 1 | **No invented numbers** | A number has source None | Cut it, or turn it into a [placeholder] for the owner to fill |
| 2 | **Label every number** | A number has no label, or a calculated total is marked (yours) | (yours) only if the owner wrote that exact number. $199 times 3 months is $597 (estimate). An hourly rate, visitor count or hours-saved bar they did not write is a [placeholder], not a guess. |
| 3 | **Show the sum** | An estimate rests on an input nobody gave | Write a formula with a [placeholder]: "[hours saved] × [your rate]" |
| 4 | **No fake scarcity** | A spot count, timer or deadline the owner didn't state and won't enforce | "[N] places open", a real date, or "Open all year" |
| 5 | **No fake values** | "Worth $X", "total value", "valued at" with no real comparable | Remove the number; describe what the item does instead |
| 6 | **No fake anchors** | A crossed out, regular or "was" price never charged; "you save" against it | Remove it. Compare with a real alternative or the cost of the problem |
| 7 | **Promise only what the owner controls** | A health, weight, income or business result with a time frame; "guaranteed results" | Promise the work, the delivery or the first step; describe results as what past clients got |
| 8 | **No stretched proof** | One client's result promised to every buyer, to a different kind of buyer, or to a bigger scope; the owner's words sharpened or relabelled | Use the proof exactly as given, for the kind of client and job it came from |
| 9 | **No borrowed authority** | "Studies show", "industry average", "most businesses" without a source | Cut it, or ask the owner for the source |
| 10 | **Mark what's new** | Something the owner doesn't offer yet reads as existing | Add (new) |
| 11 | **Honest plans and terms** | A payment plan costs more without saying the total; a guarantee without conditions or a cap | State the total; add the cap and the claim steps |
| 12 | **No made up voices** | An invented testimonial, review, rating or "as seen in" | Cut it. Leave a [testimonial from a real client] slot |

### 4. Give each claim a verdict

| Verdict | When |
|---|---|
| **Keep** | Source Owner and used exactly as given, or Worked out and labelled |
| **Fix** | True underneath, but unlabelled, sharpened, stretched or worded as a promise. Write the fixed version |
| **Cut** | Source None, or a fake value, anchor or scarcity. Remove it |
| **Flag** | Might be true but you can't tell. Goes in "Check these" for the owner |

When unsure between Keep and Flag, Flag. When unsure between Fix and Cut for a number, Cut.

### 5. Rewrite clean

Rewrite the copy with every Fix applied and every Cut removed. Keep the owner's voice and structure; change only what failed. Words that might trip a regulator or a platform go in red flag phrases: [references/red-flag-phrases.md](references/red-flag-phrases.md).

If the owner is in a regulated field (health, money, legal, children), add one line telling them to check the wording with someone qualified. This skill is common sense, not legal advice.

## Output (when used on its own)

```
**Verdict:** [one line: how many claims, how many keep / fix / cut / flag, and the most serious problem]

| # | Claim (quoted) | Source | Rule | Verdict | Fixed version |
|---|---|---|---|---|---|

**Clean version:** [the rewritten copy, ready to paste]

**Check these:** [the Flag items, at most five, each a question the owner can answer]
```

Inside `offer-master`, don't print the table. Apply the fixes silently and put one line in the card: "Honesty check: [what was cut or fixed, or 'every claim traces to your facts']".

## Worked example (illustration, fictional business)

The owner runs a bookkeeping service for cafés at $400 a month. Their facts: 14 clients, one café owner said "I get my Sundays back". A draft page says:

> "Join 50+ happy cafés. Our proven system saves owners 10 hours a week, guaranteed. Includes a Cash Flow Toolkit (worth $297). Only 2 spots left this month!"

| # | Claim | Source | Rule | Verdict | Fixed version |
|---|---|---|---|---|---|
| 1 | "50+ happy cafés" | None (owner has 14) | 1, 8 | Fix | "14 cafés so far" |
| 2 | "proven system" | None | 9 | Cut | (removed) |
| 3 | "saves 10 hours a week, guaranteed" | None | 1, 7 | Fix | "One owner told us: 'I get my Sundays back.'" |
| 4 | "worth $297" | None | 5 | Cut | "A cash flow checklist (new)" |
| 5 | "Only 2 spots left" | None | 4 | Flag | "[N] places open" if there's a real limit, else remove |

**Clean version:** "Bookkeeping for cafés, $400 a month. 14 cafés so far. One owner told us: 'I get my Sundays back.' Includes a cash flow checklist (new)."

**Check these:** Do you have a real limit on new clients each month? How many hours a week did clients spend on books before? (If you know, it can go back in, labelled.)

## Self-check

- [ ] Every number, result, name, value, limit and promise was listed, not just the obvious ones.
- [ ] Each has a source; nothing with source None survives as a fact.
- [ ] Every surviving number carries (yours) or (estimate); every estimate shows its inputs or a [placeholder].
- [ ] No value price, crossed out price, spot count or deadline the owner didn't give.
- [ ] No result promised with a time frame; past results are described as what that client got.
- [ ] Proof is used exactly as given, for the buyer and scope it came from.
- [ ] The clean version changes only what failed.

## Reference files

| File | Read it when |
|---|---|
| [references/honesty-rules.md](references/honesty-rules.md) | You need the reasoning or edge cases behind a rule |
| [references/red-flag-phrases.md](references/red-flag-phrases.md) | Scanning copy for words that usually mean a problem, with honest swaps |
| [scripts/flag_claims.py](scripts/flag_claims.py) | You can run Python and want every number and red flag phrase listed |
