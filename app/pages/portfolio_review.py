"""FinLearnX contextual portfolio learning review.

Turns a simulated portfolio into educational feedback about concentration,
diversification, and decision quality. Educational use only.
"""

from pathlib import Path
import sys

import pandas as pd
import streamlit as st
import yfinance as yf

# Ensure the repository root is importable whether this page is opened through
# Streamlit multipage navigation or run directly.
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from simulations.trading_sim import TradingSimulator
from core.learning_events import record_event
from ai.portfolio_coach import explain_portfolio

st.set_page_config(page_title="Portfolio Learning Review", page_icon="🧭", layout="wide")

if "simulator" not in st.session_state:
    st.session_state.simulator = TradingSimulator(initial_capital=100000)

simulator = st.session_state.simulator
record_event(st.session_state, "portfolio_review_opened")

st.title("🧭 Portfolio Learning Review")
st.write(
    "Turn your simulated portfolio into a learning moment. This review focuses on portfolio structure and decision quality—not personalized investment advice."
)

if not simulator.portfolio:
    st.info("Your simulated portfolio is empty. Make at least one trade in the $100K Simulator, then return here for feedback.")
    st.page_link("simulations.py", label="Open $100K Simulator", icon="🎮")
    st.stop()

rows = []
for ticker, quantity in simulator.portfolio.items():
    try:
        stock = yf.Ticker(ticker)
        history = stock.history(period="5d")
        if history.empty:
            continue
        price = float(history["Close"].iloc[-1])
        value = quantity * price
        rows.append({"Ticker": ticker, "Quantity": quantity, "Price": price, "Value": value})
    except Exception:
        continue

if not rows:
    st.warning("Market data is temporarily unavailable for the current holdings.")
    st.stop()

if len(rows) != len(simulator.portfolio):
    st.warning("Some holdings have no current market price. The breakdown below excludes them, so its weights and total are incomplete.")

holdings = pd.DataFrame(rows)
invested_value = float(holdings["Value"].sum())
portfolio_value = invested_value + simulator.cash
holdings["Weight"] = holdings["Value"] / portfolio_value if portfolio_value else 0

largest_weight = float(holdings["Weight"].max()) if not holdings.empty else 0
num_positions = len(holdings)

# A simple educational heuristic, not an investment recommendation.
position_component = min(60, num_positions * 12)
concentration_component = max(0, 40 * (1 - largest_weight))
diversification_score = int(round(min(100, position_component + concentration_component)))

if largest_weight >= 0.50:
    concentration_label = "High concentration"
elif largest_weight >= 0.30:
    concentration_label = "Moderate concentration"
else:
    concentration_label = "Lower single-position concentration"

c1, c2, c3, c4 = st.columns(4)
c1.metric("Portfolio value", f"${portfolio_value:,.0f}")
c2.metric("Positions", num_positions)
c3.metric("Largest position", f"{largest_weight * 100:.1f}%")
c4.metric("Diversification score", f"{diversification_score}/100")

st.caption(
    "The diversification score is a simple educational heuristic based on position count and single-position concentration. It is not a financial recommendation."
)

st.subheader("Portfolio structure")
display = holdings.copy()
display["Price"] = display["Price"].map(lambda x: f"${x:,.2f}")
display["Value"] = display["Value"].map(lambda x: f"${x:,.2f}")
display["Weight"] = display["Weight"].map(lambda x: f"{x * 100:.1f}%")
st.dataframe(display, use_container_width=True, hide_index=True)

st.subheader("What your portfolio can teach you")

with st.container(border=True):
    st.markdown(f"### 1. Concentration — {concentration_label}")
    largest_ticker = holdings.loc[holdings["Weight"].idxmax(), "Ticker"]
    st.write(
        f"Your largest position is **{largest_ticker} at {largest_weight * 100:.1f}%** of total portfolio value. "
        "A larger single position means one company can have a greater effect on overall results."
    )
    if largest_weight >= 0.50:
        st.warning(
            "Learning prompt: What would happen to your portfolio if this single position fell 25% while everything else stayed unchanged?"
        )
    else:
        st.info("Learning prompt: Compare your largest position with the rest of the portfolio. What risk is that weight helping you take—or avoid?")

with st.container(border=True):
    st.markdown("### 2. Diversification")
    st.write(
        f"You currently hold **{num_positions} positions**. More positions can reduce company-specific concentration, but the number of holdings alone does not guarantee diversification."
    )
    st.write(
        "Learning prompt: Are these companies exposed to different industries and economic drivers, or could they all react similarly to the same event?"
    )

with st.container(border=True):
    st.markdown("### 3. Cash allocation")
    cash_weight = simulator.cash / portfolio_value if portfolio_value else 0
    st.write(f"Cash represents **{cash_weight * 100:.1f}%** of your simulated portfolio.")
    st.write(
        "Learning prompt: Why did you choose to keep this amount uninvested? Was it intentional risk management, optionality, or simply unused capital?"
    )

with st.container(border=True):
    st.markdown("### 4. Outcome vs. decision quality")
    returns = simulator.get_returns()
    st.write(f"Your simulated return is currently **{returns['percentage_return']:.2f}%**.")
    st.write(
        "A positive return does not automatically mean the original decision was strong, and a negative return does not automatically mean it was poor. "
        "Evaluate what information you used, what risk you accepted, and whether the result matched your original thesis."
    )

st.subheader("Decision reflection")
thesis = st.text_area("What was your main reason for building this portfolio?", placeholder="Example: I wanted diversified exposure to large technology and consumer companies...")
risk = st.text_area("What is the biggest risk you now see in the portfolio?", placeholder="Example: Too much of the portfolio depends on one sector...")
next_decision = st.text_area("What would you change in your next simulation?", placeholder="Example: Reduce my largest position and add exposure to a different industry...")

if st.button("Complete learning review", type="primary"):
    if thesis.strip() and risk.strip() and next_decision.strip():
        record_event(st.session_state, "learning_review_completed")
        st.success("Learning review completed. The next step is to apply one of these insights in your next simulation.")
    else:
        st.warning("Complete all three reflection prompts to finish the learning review.")

st.subheader("AI learning coach")
st.write("Get an explanation of this virtual portfolio and suggested learning exercises. The portfolio summary is sent to an AI service when you click Generate.")
if st.button("Generate educational explanation"):
    record_event(st.session_state, "ai_explanation_requested")
    snapshot = {
        "cash": round(simulator.cash, 2),
        "holdings": [{"ticker": row["Ticker"], "weight_pct": round(row["Weight"] * 100, 1)} for row in holdings.to_dict("records")],
        "missing_price_count": len(simulator.portfolio) - len(rows),
        "diversification_heuristic": diversification_score,
    }
    try:
        st.session_state.ai_explanation = explain_portfolio(snapshot, st.session_state.get("goal", "Learn investing basics"))
    except Exception as exc:
        st.session_state.ai_explanation = None
        st.warning(f"AI explanation unavailable: {exc}")
if st.session_state.get("ai_explanation"):
    st.markdown(st.session_state.ai_explanation)
st.caption("AI text may contain mistakes. Educational exercises only, not investment advice.")

st.divider()
st.caption("Educational simulation only. This review does not provide personalized financial advice.")
