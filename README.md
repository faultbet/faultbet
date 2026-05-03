# fault.bet

> **AI-powered tennis trading signals for Betfair traders. Built on 1.6 million matches.**

[![Live Results](https://img.shields.io/badge/live%20results-publicly%20tracked-00C853)](https://fault.bet/results)
[![Free Trial](https://img.shields.io/badge/trial-7%20days%20free-3b82f6)](https://fault.bet/trial)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

[fault.bet](https://fault.bet) is a tennis-trading signal service for [Betfair](https://www.betfair.com) traders. Every signal — pre-match and inplay — is published, timestamped, and tracked publicly on our [results page](https://fault.bet/results). No cherry-picking, no hidden losses.

---

## 🔗 Links

- 🌐 **Website** → [fault.bet](https://fault.bet)
- 📊 **Live results** → [fault.bet/results](https://fault.bet/results)
- 📰 **Blog** → [fault.bet/blog](https://fault.bet/blog)
- 💰 **Pricing** → [fault.bet/pricing](https://fault.bet/pricing)
- 🔌 **API** → [fault.bet/api](https://fault.bet/api)
- 🧪 **7-day free trial** → [fault.bet/trial](https://fault.bet/trial)

---

## 🎾 What we do

Most tennis tipster services are scams. The 90% of them that aren't outright dishonest cherry-pick wins, hide losses, and sell hope. We do the opposite: every signal we send is published live, the price we saw is timestamped, and the win/loss outcome shows up next to it within 24 hours. Numbers, not narrative.

### Methodology

- **LightGBM ensemble** trained on **1.6M+ ATP and WTA matches** since 2000
- **Markov-chain pressure model** for inplay choke detection and lead-loss probability
- **Surface-adjusted Elo** (welo) with weather-adjusted variants
- **Pinnacle/Betfair price-confirmed** signals only — never theoretical
- **Proportional staking** (fractional Kelly) with confidence-weighted bet sizing

Read the methodology breakdowns on the [blog](https://fault.bet/blog):

- [How we built it](https://fault.bet/blog/how-we-built-it) — the full architecture
- [Markov tennis pressure](https://fault.bet/blog/markov-tennis-pressure) — choke modelling
- [Staking guide](https://fault.bet/blog/staking-guide) — fractional Kelly explained
- [Tennis data API guide](https://fault.bet/blog/tennis-data-api-guide) — programmatic access

---

## 📈 Live track record

Updated daily at [fault.bet/results](https://fault.bet/results):

- **162** pre-match signals tracked since 17 March 2026
- **50.6%** win rate
- **+10.7%** Kelly P&L (1/10 Kelly staking)
- **+2.78%** flat-1% P&L
- **16.8%** average detected edge
- **2.25** average odds

Every entry shows: timestamped Betfair price, model probability, edge %, confidence, suggested stake, settled outcome.

---

## 🔌 API

The fault.bet API gives developers, quants and bookmakers programmatic access to:

- Daily pre-match signals (pre-filtered to 8%+ edge)
- Player Elo / welo ratings (overall + surface-adjusted)
- Choke index, lead-lost rate, hold/break percentages
- Match probabilities and pressure profiles
- Historical features for 1.6M+ matches

See [`examples/`](examples/) for quick-starts in Python and JavaScript.

API plans, docs and pricing → [fault.bet/api](https://fault.bet/api)

---

## 📚 Recent reading

- [Polymarket tennis trading with fault.bet](https://fault.bet/blog/polymarket-tennis-trading-with-faultbet)
- [Lucky 15 value tennis](https://fault.bet/blog/lucky-15-value-tennis)
- [Polymarket tennis API](https://fault.bet/blog/polymarket-tennis-api)
- [Rome 2026 ATP preview](https://fault.bet/blog/rome-2026-atp-preview) · [WTA preview](https://fault.bet/blog/rome-2026-wta-preview)

---

## 📜 License

Code in this repository is released under the [MIT License](LICENSE).

Tennis data, model outputs and the fault.bet brand are proprietary and remain the property of fault.bet.

---

## ⚠️ Responsible gambling

18+ only. Past performance is not a guarantee of future results. Only bet what you can afford to lose. If gambling is harming you or someone you know: [BeGambleAware.org](https://www.begambleaware.org) · [GamCare 0808 8020 133](https://www.gamcare.org.uk) · [GAMSTOP](https://www.gamstop.co.uk).

---

<sub>© 2026 [fault.bet](https://fault.bet) · [Terms](https://fault.bet/terms) · [Privacy](https://fault.bet/privacy) · [Responsible gambling](https://fault.bet/responsible-gambling)</sub>
