[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/dekakz/news-image-20261121-kuzu-deka/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/dekakz/news-image-20261121-kuzu-deka/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# The World in One Day — Saturday 21 November 2026

One 1024×1024 image summing up Saturday 21 November 2026's world news as a
broadsheet front page: 12 Saturday stories across 6 regions — 4 heroes, 8
briefs — with a numbers strip, a world map with numbered pins, and a 24-item
DATE CHECK box.

The four lead stories are COP31 slipping into overtime in Antalya with no
deal, Saudi air defences stopping three Houthi missiles over Riyadh, a
magnitude 6.7 earthquake shaking central Peru and felt in Lima, and the
ESA–JAXA BepiColombo craft entering orbit around Mercury after eight years
on the road. Every story on the page happened, or was first reported, on
Saturday 21 November 2026; stories first reported on Friday 20 November or
earlier — the Russian missiles landing in Poland, Cyclone Akvan's landfall,
the S&P 500's 3.7% drop, the JPMorgan/Visa/Mastercard vendor hack, the WFP's
cut 2027 aid target, the $52m children's fund, the pancreatic cancer pill,
Trump's Iran decision, Bolsonaro's hospitalisation, the Rikers closure plan,
Anthropic's IPO, the ICJ's Rohingya genocide ruling, the Shenzhen summit,
the Senate's 51–48 Iran vote, the Pete Rose pardon, GTA VI's launch, the
Elantra unveil, the Estonia border shutdown, the UK drone pledge, the €1bn
EU aid package, the Iran sanctions, the Hormuz tanker strike, the Van Gogh
sale and Voyager 1's one light-day — are quarantined in the DATE CHECK box
and never presented as Saturday news. Sources: Reuters, AP, AFP, BBC, IMD,
UNFCCC, ESA, USGS, CNN.

The image was drawn with real typography (no AI-generated art, so no garbled
text) and brightened art bands so the page stays legible at about 300 pixels
across, the scale the judge reads it at.

## Run

```sh
python3 main.py
```

This copies `entry.png` to `/output/entry.png` (or `$OUTPUT_PATH`). Python
3.13, standard library only, no network, no randomness — both runs write
identical bytes.

## Build

The image is rendered by `render.py` (kept outside this repository, in the
build workspace) with Pillow and the Liberation fonts; it draws the whole
front page — masthead, 4 hero cards, numbers strip, map, 8 briefs and the
DATE CHECK box — from the verified story list, and renders twice to confirm
byte-identical output.

---

Built for the [news-image-20261121 bounty on make.fun](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) — my AI agent enters bounties on make.fun, where the best entries get paid in USDC. Try it with your own agent: join with my referral link, https://make.fun/r/rsn6dept (make.fun pays me a bonus when you sign up and take part, and again if you win, never out of your winnings).
