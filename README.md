# FinLearnX — Learn Investing by Making Decisions

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Status](https://img.shields.io/badge/status-active-success)

FinLearnX is an educational investing simulator designed around one core idea:

> **People learn finance better when concepts are tied directly to decisions and outcomes.**

Instead of separating financial education from investing practice, FinLearnX connects them in one loop:

**Learn → Decide → Simulate → Analyze → Improve**

Users can practice investing with virtual money, inspect portfolio outcomes, and receive educational feedback about risk, diversification, and decision quality.

> ⚠️ FinLearnX is for educational purposes only and does not provide financial advice.

---

## Product problem

Beginner investors have access to more financial information than ever, but often struggle to translate concepts such as diversification, risk, volatility, and portfolio construction into actual decisions.

Traditional learning products explain concepts. Trading simulators let users act. FinLearnX is designed to connect both experiences.

### Target user

FinLearnX is currently designed for:

- college students and early-career professionals learning investing
- first-time investors who want to practice without risking real capital
- users who learn best through interactive decisions rather than passive content

### Core product loop

1. **Learn** a financial concept
2. **Make** an investment decision
3. **Simulate** the outcome with virtual capital
4. **Analyze** performance and portfolio structure
5. **Reflect** on why the result happened
6. **Improve** the next decision

---

## Flagship experience: $100K Portfolio Challenge

The strongest shipped FinLearnX experience is the stock simulation workflow.

Users start with **$100,000 in virtual cash** and can:

- buy and sell stocks using market data
- track cash, holdings, and portfolio value
- inspect portfolio allocation
- view interactive price and volume charts
- measure total return
- review trading history
- receive educational performance feedback

Run it with:

```bash
streamlit run app/pages/simulations.py
```

---

## ✅ Shipped today

### Trading simulation

- $100K virtual portfolio
- buy and sell simulated positions
- portfolio holdings and allocation
- trade history
- portfolio return tracking
- interactive price charts
- market-data integration with `yfinance`

### Portfolio analytics

- portfolio optimization utilities
- portfolio allocation analysis
- simulation infrastructure

### Financial-learning infrastructure

- AI tutor prompt library
- structured finance-learning concepts
- education-focused safety framing

### Product foundation

- Streamlit interface
- modular Python architecture
- tests and GitHub workflow structure
- financial-data ingestion utilities

---

## 🛠️ Next product priorities

The roadmap is intentionally prioritized around improving the core learning loop before expanding platform breadth.

### P0 — Complete the learning loop

- onboarding by investing experience, learning goal, and risk tolerance
- guided **Build Your First $100K Portfolio** challenge
- benchmark portfolio performance against the S&P 500
- diversification score
- concentration-risk warnings
- volatility and drawdown metrics
- educational feedback tied directly to portfolio decisions

### P1 — Personalized financial learning

- decision journal: *Why are you making this trade?*
- portfolio-specific AI explanations
- personalized lesson recommendations based on user behavior
- behavioral-finance insights such as overtrading, concentration, and loss aversion
- learning missions such as:
  - Build a diversified portfolio
  - Survive a market crash
  - Build a low-volatility portfolio
  - Protect against inflation

### P2 — Progression and scenarios

- learner levels and competency progression
- scenario stress testing
- historical crisis simulations
- risk-adjusted scoring
- portfolio-review challenges

### Later — only after core engagement is validated

- community challenges
- collaborative portfolios
- mobile experience
- options education
- deeper brokerage integrations
- advanced predictive ML

---

## Product metrics

### North Star Metric

**Weekly Learning Decisions Completed**

A learning decision is a meaningful portfolio construction, simulated trade, scenario, or portfolio review followed by educational feedback.

### Supporting metrics

| Funnel | Metric |
|---|---|
| Acquisition | New users |
| Activation | % completing first portfolio simulation |
| Engagement | Learning decisions per active user |
| Simulation | Trades / simulations per user |
| Learning | Lessons and missions completed |
| AI | Contextual tutor interactions per user |
| Retention | D7 / D30 returning learners |
| Quality | Mission completion and portfolio-review rate |

The product should optimize for **learning and decision quality**, not simply simulated returns.

---

## Product principles

### 1. Learning before speculation

FinLearnX should reward understanding, diversification, and decision quality rather than high-risk bets that happen to produce large returns.

### 2. Feedback should be contextual

Education becomes more useful when it explains the user's own portfolio or simulated decision.

### 3. Practice should be safe

All trading is simulated. FinLearnX does not execute real trades or provide personalized financial advice.

### 4. Ship depth before breadth

A complete portfolio-learning journey is more valuable than many disconnected unfinished tools.

---

## Architecture

```text
FinLearnX/
├── app/
│   ├── main.py                  # product home and onboarding
│   └── pages/
│       └── simulations.py       # flagship $100K trading simulator
├── core/
│   └── data_ingestion.py        # market-data utilities
├── ai/
│   └── tutor_prompts.yaml       # educational AI prompt definitions
├── portfolio/
│   └── optimize_mpt.py          # portfolio optimization
├── simulations/
│   └── trading_sim.py           # trading simulation engine
├── docs/
│   └── PRODUCT_STRATEGY.md      # PM strategy, metrics, roadmap
├── tests/
├── requirements.txt
└── README.md
```

This section reflects the current repository. Planned capabilities are listed separately in the roadmap rather than presented as already shipped.

---

## Installation

```bash
git clone https://github.com/sagarmandavkar-UX/FinLearnX.git
cd FinLearnX

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run the product home

```bash
streamlit run app/main.py
```

### Run the portfolio simulator directly

```bash
streamlit run app/pages/simulations.py
```

---

## Data and API configuration

Some modules support external market-data providers. Keep API keys in local environment configuration and never commit credentials.

Example:

```text
ALPACA_API_KEY=your_key_here
ALPACA_SECRET_KEY=your_secret_here
FINNHUB_API_KEY=your_key_here
```

---

## Product strategy

For the PM rationale, prioritization framework, north-star metric, user journey, roadmap, and experiment plan, see:

[`docs/PRODUCT_STRATEGY.md`](docs/PRODUCT_STRATEGY.md)

---

## Disclaimer

**FinLearnX is an educational simulation and is not financial advice.**

- simulated performance does not predict future results
- all investing involves risk
- users should not make investment decisions solely based on this project
- consult an appropriately qualified professional for personal financial advice

---

## Author

**Sagar Mandavkar**  
GitHub: [@sagarmandavkar-UX](https://github.com/sagarmandavkar-UX)

---

**FinLearnX: Learn → Decide → Simulate → Analyze → Improve**
