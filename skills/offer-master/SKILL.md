---
name: offer-master
description: Fixes an offer that isn't selling, end to end. Finds the leak, decodes objections, scores 4 levers, rebuilds on real proof and returns a paste-ready offer card.
---

# Offer Master

Use this when someone says their offer, package, program, course or service isn't selling, or asks you to build, rework or price one. It runs the whole job and calls seven smaller skills by name, one per stage.

Your job: make the offer itself better, honestly, and hand back words the owner can paste onto their page today. You are not writing hype. Every claim you write must be something the owner can back up.

## The suite

| Stage | Skill | What it settles |
|---|---|---|
| 1 | `offer-diagnosis` | Where buyers drop off, whether it's really the offer, what their objections mean |
| 2 | `offer-levers` | Result, Belief, Speed and Ease scored 1 to 10, and the one or two to fix |
| 3 | `offer-included` | Proof to lead with, the one line promise, the week one win, what's included, what to cut, bonuses |
| 4 | `offer-guarantee` | One fair, capped guarantee aimed at the main fear, with its cost |
| 5 | `offer-urgency-name-price` | A real reason to buy now, the cost of waiting, the name, the price and payment options |
| 6 | `offer-honesty-check` | Every claim and number traced to the owner, or fixed, or flagged |
| 7 | `offer-card` | The exact shape of your reply |

**How to call them.** In Claude Code, load each one by name with the Skill tool when you reach its stage. If that isn't available, read its `SKILL.md` in the sibling folder (for example `../offer-diagnosis/SKILL.md`) and its references as it directs. If its text is already in your context, follow it. If one can't be found, the short rules in this file are enough to do a good job; never stop because a stage skill is missing.

## Rules that never bend

These are why this skill beats the alternatives. Apply them at every stage.

1. **Use only the owner's facts.** No result, client, testimonial, statistic, price or spot count they didn't give you. A missing fact becomes a [placeholder] or a "Check these" item, never a guess dressed as a fact.
2. **Build on what's proven.** If the strongest proof comes from one job or one type of client, the offer leads with that job for that client. Never stretch one result to buyers, jobs or scope it didn't come from, and describe proof exactly as the owner did (don't relabel "7 sites" as "7 clinic sites"). One client's "2 days to 3 hours" stays that client's. Fail: "Your reports in 3 hours, not 2 days." Pass: "Reporting automation built and tested on your reports. One agency went from about 2 days to 3 hours."
3. **Mark what's new.** Anything the owner didn't already offer is a suggestion: write (new) after it. Do not rename what they already do, and do not add a length, a format or a method they did not write. A weekly check-in call stays "weekly check-in call". It does not become a "weekly 30-minute call" or "form check on your videos". A nutrition PDF stays a nutrition PDF. If you add video form checks, mark them (new) and ask in Check these. If you say an item stays, it appears under What's included, in their words.
4. **Label every number.** (yours) only if the owner wrote that exact number. (estimate) for anything you worked out, even from their figures, and for any planning assumption. $199 a month for 3 months is $597 (estimate), not (yours). If a sum needs an input you don't have, write the formula with a [placeholder] and no guessed dollar figure inside it. Fail: "[a trainer at $80 a session]". Pass: "[what a local trainer charges per session]". Do not invent an hourly rate, a visitor count, or a "saves X hours" bar.
5. **One guarantee, always capped.** It answers the main fear, has two conditions at most, and the remedy has a ceiling. Never open ended free work. Never "refunded unless a weight, strength, income or booking result happens." If the fear is that it won't pay off, the remedy is one extra piece of work (another page, a rework, a set number of hours), and the line says the result number is not guaranteed. A guarantee that only says "we delivered the button" does not answer that fear. For coaching, guarantee the plan and the calls, not the kilos.
6. **Real urgency only.** A capacity limit is not spots left: write [N] places open unless the owner told you how many are free. No timers, no invented deadlines, no month they did not name. Fail: "[N] places open for November." Pass: "[N] places are open." "Open all year" is a fine answer.
7. **No fake values or anchors.** No "worth $X" without a real comparable price. No crossed out price they never charged.
8. **No health, weight, income or business result promised with a time frame.** Promise what the owner controls; describe results as what past clients got.

## Step 0: Get the facts

You need: what they sell, the price, who buys it, their numbers (people who see it, enquire, buy), what buyers say when they say no, the proof they have, and their limits (capacity, budget, things they refuse to do).

- If the brief covers most of this, don't ask. Work with it and put your guesses under "Check these".
- If key facts are missing, ask in one short message, at most five questions, then stop and wait. Use the question bank below, in this order of value.
- Never invent a fact to fill a gap.

**Question bank (ask only what's missing)**

1. What do you sell, at what price, and to whom?
2. Roughly how many people see it, enquire or book a call, and buy, in a normal month?
3. When people don't buy, what do they say, word for word if you can?
4. What results can you prove? Names, numbers, how many clients so far.
5. Any limits: how many clients you can take, things you won't do (discounts, timers), budget?

## Step 1: Pick the route

| The situation | Route |
|---|---|
| It isn't selling, and they gave numbers or objections | Full run, stages 1 to 7 |
| Brand new offer, nothing sold yet | Skip the leak maths. Use expected objections from the buyer's world, mark the whole offer as untested, make the test the main output |
| It used to sell and has slowed | Diagnosis first, using the "it used to sell" ladder in `offer-diagnosis`. Change the lightest layer that fixes it |
| They want one part only (a guarantee, a name, a price, an audit of their page) | Call only that skill and answer in its own output format |

## Step 2: Run the stages

Do this working silently. The owner sees only the card at the end.

1. **Diagnosis** (`offer-diagnosis`). Lay out the buyer path with their numbers, find the leak, give the verdict on "Is it the offer?", decode each objection into the belief behind it, and write the current offer in one line, gaps and all.
   - If it's mostly traffic, say so plainly in the card's first lines. A better offer helps, but it won't fix this alone. Still rebuild the offer.
   - If buyers buy then quit or ask for refunds, fix delivery and the first win before more selling.
2. **Levers** (`offer-levers`). Score Result, Belief, Speed and Ease against the defined levels, with evidence from the brief. Fix the one or two that the top objections point at. Don't change everything.
3. **Build** (`offer-included`). List the proof, strongest first; that list is all you may use. Write the promise in one line in the buyer's words, inside what the proof supports. Design the week one win. Build what's included from the buyer's obstacles, cut what doesn't earn its place, and add bonuses only where each one kills a named doubt.
4. **Guarantee** (`offer-guarantee`). One guarantee, chosen by the main fear and by what the owner controls. Coaching: "Do [two clear actions] for [time]. If we haven't delivered [the work we control], we [remedy]." Done-for-you, when the fear is it won't pay off: one capped extra piece of work if they did their part and the result still isn't coming through, and say the number is not guaranteed. Cap the remedy. Cost it at a claim rate of 1 in 10. Never "if you aren't lifting heavier", and never a refund because bookings or income didn't rise.
5. **Why now, name, price** (`offer-urgency-name-price`). A real reason or "open all year", plus the cost of waiting in the buyer's terms. A name a buyer could text a friend. The price next to the cost of staying stuck, a payment option before any discount, and no anchors that aren't real.
6. **Honesty check** (`offer-honesty-check`). Run every line you drafted through it. Fix or remove anything that fails. This is not optional and it is not a formality: it is where most offers written by AI fail.
7. **Card** (`offer-card`). Answer with the card and nothing else of substance.

## Forecast honestly

One good change often lifts sales by something like 10 to 40 percent (a rule of thumb, not a statistic), and changes multiply rather than add. Say this as an estimate, never a promise. Tell the owner to change one thing, measure for a few weeks, then change the next.

## The 12 rules and where they live

| Rule | Skill |
|---|---|
| Is it the offer? | `offer-diagnosis` |
| Decode objections | `offer-diagnosis` |
| Score 4 levers | `offer-levers` |
| Say it in one line | `offer-included` (and the current version in `offer-diagnosis`) |
| Lead with proof | `offer-included` |
| Win in week one | `offer-included` |
| Cut the extras | `offer-included` |
| Bonuses kill doubts | `offer-included` |
| One fair guarantee | `offer-guarantee` |
| Real deadlines | `offer-urgency-name-price` |
| A name you'd text | `offer-urgency-name-price` |
| Cost of waiting | `offer-urgency-name-price` |

## Self-check before you answer

- [ ] The first lines name the leak with the owner's numbers, and say if part of the problem isn't the offer.
- [ ] Every result, client and number traces to the brief, or is labelled (estimate), or is a [placeholder]. A total you multiplied is (estimate).
- [ ] No invented hourly rate, visitor count, or hours-saved bar. Missing inputs stay as [placeholders].
- [ ] The promise is specific and in the buyer's words, and no bigger than the proof.
- [ ] Every new item is marked (new). Nothing they already sell was renamed. A weekly check-in call is not a "30-minute call" and not a video form check unless they wrote that.
- [ ] Anything you kept is still in What's included.
- [ ] One guarantee, capped, costed, two conditions at most. Coaching is tied to the plan and the calls, not the kilos. A payoff fear gets one extra piece of work, and the line says the result number is not guaranteed. Not a refund because bookings or income didn't rise.
- [ ] No spot count, deadline, value price or crossed out price the owner didn't give you.
- [ ] The reply is the card: about 750 words at most, no essay before it, no emoji, no hype words. No em dash. Use a full stop or a comma. The character "—" is a fail, rewrite the sentence.
- [ ] It ends with one test for this month and at most three "Check these" items.

## Reference files

| File | Read it when |
|---|---|
| [references/worked-example.md](references/worked-example.md) | You want to see a full run, from brief to card (fictional business) |
| [references/edge-cases.md](references/edge-cases.md) | The case is unusual: no numbers, very low volume, a price rise request, a product problem, a regulated field |
| [CREDITS.md](CREDITS.md) | Who this suite learned from |
