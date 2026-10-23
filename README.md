# Offer Master

A Claude skill that fixes an offer that isn't selling.

People see your offer, but almost nobody buys. You hear "I'll think about it", "too expensive" or "I can do this with a free app". Usually the product is fine. The offer is the problem.

Offer Master finds the real cause, then rebuilds the offer with you:

- **Finds the leak:** where buyers drop off, using your own numbers
- **Reads your buyers:** what their objections really mean
- **Scores 4 levers:** Result, Belief, Speed and Ease, and starts with the weakest
- **Rebuilds the offer:** promise, first win, what's included, bonuses
- **One capped guarantee:** aimed at the buyer's main fear
- **Name and price:** plus an honest reason to buy now, only if it's real
- **Honesty check:** no made up numbers, spots, deadlines or results
- **Offer card:** the finished offer in exact words you can paste onto your page

It was written from scratch after reading 18 public offer skills in full (the ones it learned from are in [CREDITS](skills/offer-master/CREDITS.md)). In blind tests it beat the most installed offer skill, plain Claude and a strong one line prompt in 9 out of 9 judgings.

## Install (Claude Code)

**The one step:** paste this into Claude Code:

```
https://github.com/Liamrjohnston/offer-master-skill.git
Clone this and add the skill.
```

Claude clones the repo and adds the skill to your skills folder.

**Or do it yourself:**

```bash
git clone https://github.com/Liamrjohnston/offer-master-skill.git
cd offer-master-skill
bash install.sh
```

That copies `skills/offer-master` into `~/.claude/skills/offer-master`. Start a new Claude Code session afterwards so it picks the skill up.

> **Note for Claude:** to install this skill, copy the folder `skills/offer-master` from this repo to `~/.claude/skills/offer-master` (create `~/.claude/skills` if needed). Don't overwrite an existing folder without asking. Then tell the user to start a new session and type `/offer-master`.

## Use it

Type `/offer-master` and tell it about your offer, in plain words:

```
/offer-master 400 people see my sales page each month. 1 buys. Fix my offer.
```

Give it what you have: what you sell, the price, who it's for, rough numbers (visitors, calls, sales), what buyers say when they don't buy, and any real results you can prove. It asks for anything important that's missing before it rebuilds anything.

You get back a short offer card: the name, promise, first win, what's included, the guarantee, why now and the price. Every number is labelled as yours or an estimate. It also gives you one test to run this month.

## What it won't do

It won't invent client results, fake scarcity, fake deadlines, fake bonus values or promises you can't keep. If something needs checking, it lists it under "Check these".

## License

MIT. See [LICENSE](LICENSE).
