<p align="center">
  <img src="assets/hero.png" alt="Offer Master. Fix the offer that isn't selling, then paste the offer card." width="880">
</p>

# Offer Master

A Claude skill that fixes an offer that isn't selling.

People see the page. Almost nobody buys. The product is usually fine. The offer is what you change.

It finds where buyers drop off, reads what their objections actually mean, and hands back the exact words for the page. Every number is labelled as yours or an estimate.

<p align="center">
  <img src="assets/demo.gif" alt="Offer Master running in Claude. The prompt, the leak, then the offer card." width="880">
</p>

The clip is an example. The offer in it is a made-up fitness coach, the same kind of test the skill was judged on. It is not a client, and it does not promise anyone those results.

## Install

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

Type `/offer-master` and describe the offer in plain words:

```
/offer-master 400 people see my sales page each month. 1 buys. Fix my offer.
```

Give it what you have: what you sell, the price, who it's for, rough numbers (visitors, calls, sales), what buyers say when they don't buy, and any real results you can prove. It asks for anything important that's missing before it rebuilds anything.

You get back a short offer card: the name, promise, first win, what's included, the guarantee, why now and the price. Every number is labelled as yours or an estimate. It also gives you one test to run this month.

## What it does

- **Finds the leak.** Where buyers drop off, from your own numbers.
- **Reads the objections.** What "I'll think about it", "too expensive" and "I can do this with a free app" actually mean.
- **Scores four levers.** Result, Belief, Speed and Ease. It starts with the weakest.
- **Rebuilds the offer.** Promise, first win, what's included, bonuses.
- **Writes one capped guarantee.** Aimed at the buyer's main fear.
- **Sets the name and the price.** Plus an honest reason to buy now, only if that reason is real.
- **Hands you the offer card.** Exact words you can paste onto the page.

## What it will not do

It will not invent client results, fake scarcity, fake deadlines, fake bonus values, or promises you can't keep. If something needs checking, it lists it under "Check these".

## Why this one

Written from scratch after reading 18 public offer skills in full. The ones it learned from are in [CREDITS](skills/offer-master/CREDITS.md).

In blind tests it beat the most installed offer skill, plain Claude, and a strong one line prompt in 9 out of 9 judgings. Those tests used made-up businesses, the same way the picture above does.

## License

MIT. See [LICENSE](LICENSE).
