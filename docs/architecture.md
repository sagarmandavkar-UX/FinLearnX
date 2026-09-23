# FinLearnX architecture

FinLearnX is a Streamlit educational trading simulator. It uses virtual cash and Yahoo Finance market prices; it does not place brokerage orders.

## Shipped components

| Path | Purpose |
| --- | --- |
| `app/main.py` | Learning profile, challenge entry, and session progress |
| `app/pages/simulations.py` | Virtual orders, holdings, charts, return display, and trade history |
| `app/pages/portfolio_review.py` | Portfolio structure, reflection prompts, and optional AI explanation |
| `simulations/trading_sim.py` | Cash, positions, and transaction history for the current session |
| `core/learning_events.py` | Session-only learning milestones; individual CSV export |
| `core/data_ingestion.py` | Market-data utilities |
| `ai/portfolio_coach.py` | Opt-in OpenAI Responses API call for educational exercises |
| `ai/tutor_prompts.yaml` | Prompt library, not an interactive multi-agent runtime |
| `portfolio/optimize_mpt.py` | Portfolio optimization utility |
| `backtesting/engine.py`, `models/monte_carlo.py` | Standalone analysis utilities |
| `education/modules/beginner.yaml` | Structured learning content |

## Session flow

1. The Home page records a learning profile in Streamlit session state.
2. The simulator reads market prices through `yfinance` and uses `TradingSimulator` to change virtual cash and holdings.
3. The review page fetches prices for held tickers, calculates allocation and a simple educational heuristic, and invites written reflection.
4. If the user clicks **Generate educational explanation** and the server has `OPENAI_API_KEY`, the AI module sends a small simulated portfolio snapshot and learning goal to the OpenAI API. The response contains learning exercises, not trading instructions.
5. Milestone events live in session state and may be downloaded as a CSV. Closing or resetting the session can remove them; there is no shared analytics database.

The app has no sign-in, durable user profiles, brokerage integration, deployed cloud infrastructure, or six-agent orchestration. Historical user counts and trade volume are creator-reported and have no raw participant data in this public repo. See [research and metrics](RESEARCH_AND_METRICS.md).

## Limits

- Market-data availability depends on the external provider. An unavailable price blocks a new UI trade; missing holdings prices can make review totals incomplete.
- Portfolio value and trade history are session-scoped. They are not saved across sessions.
- The AI integration needs a server-side API key and has not been exercised with a live key in automated tests.
- The diversification score is a learning heuristic, not a validated risk model or financial advice.
