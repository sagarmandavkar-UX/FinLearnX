"""FinLearnX — Learn investing by making decisions.

Product home and onboarding experience.
"""

import streamlit as st

st.set_page_config(
    page_title="FinLearnX",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Session defaults
st.session_state.setdefault("experience", "Beginner")
st.session_state.setdefault("goal", "Learn investing basics")
st.session_state.setdefault("risk_tolerance", "Moderate")
st.session_state.setdefault("onboarding_complete", False)

st.sidebar.title("💰 FinLearnX")
st.sidebar.caption("Learn → Decide → Simulate → Analyze → Improve")

selection = st.sidebar.radio(
    "Navigation",
    ["Home", "Start Challenge", "Product Roadmap", "About"],
    label_visibility="collapsed",
)

st.sidebar.divider()
st.sidebar.page_link(
    "pages/simulations.py",
    label="Open $100K Simulator",
    icon="🎮",
)
st.sidebar.page_link(
    "pages/portfolio_review.py",
    label="Review My Portfolio",
    icon="🧭",
)
st.sidebar.caption("Educational simulation only · Not financial advice")


def onboarding_card() -> None:
    with st.container(border=True):
        st.subheader("Personalize your learning path")
        st.write(
            "FinLearnX uses your experience, learning goal, and risk preference to frame the simulation and educational feedback."
        )

        c1, c2, c3 = st.columns(3)
        with c1:
            experience = st.selectbox(
                "Investing experience",
                ["Beginner", "Some experience", "Experienced"],
                index=["Beginner", "Some experience", "Experienced"].index(st.session_state.experience),
            )
        with c2:
            goal = st.selectbox(
                "Primary learning goal",
                [
                    "Learn investing basics",
                    "Build better portfolios",
                    "Understand risk",
                    "Practice trading decisions",
                ],
                index=[
                    "Learn investing basics",
                    "Build better portfolios",
                    "Understand risk",
                    "Practice trading decisions",
                ].index(st.session_state.goal),
            )
        with c3:
            risk = st.selectbox(
                "Risk tolerance",
                ["Conservative", "Moderate", "Aggressive"],
                index=["Conservative", "Moderate", "Aggressive"].index(st.session_state.risk_tolerance),
            )

        if st.button("Save learning profile", type="primary"):
            st.session_state.experience = experience
            st.session_state.goal = goal
            st.session_state.risk_tolerance = risk
            st.session_state.onboarding_complete = True
            st.success("Learning profile saved. Your next step is the $100K Portfolio Challenge.")


def challenge_preview() -> None:
    with st.container(border=True):
        st.subheader("🎯 $100K Portfolio Challenge")
        st.write(
            "Build a simulated portfolio using $100,000 in virtual cash, then evaluate what your decisions reveal about diversification, concentration, and risk."
        )

        c1, c2, c3 = st.columns(3)
        c1.metric("Starting capital", "$100,000")
        c2.metric("Objective", "Learn by doing")
        c3.metric("Real money at risk", "$0")

        st.markdown(
            """
            **Complete the challenge by:**
            1. selecting investments,
            2. making at least one simulated trade,
            3. reviewing portfolio allocation and performance,
            4. opening the Portfolio Learning Review,
            5. identifying one risk or diversification lesson from the result.
            """
        )
        a, b = st.columns(2)
        with a:
            st.page_link(
                "pages/simulations.py",
                label="Start the $100K Challenge",
                icon="🚀",
            )
        with b:
            st.page_link(
                "pages/portfolio_review.py",
                label="Review My Portfolio",
                icon="🧭",
            )


if selection == "Home":
    st.title("FinLearnX")
    st.subheader("Learn investing by making decisions")
    st.write(
        "FinLearnX connects financial concepts to simulated investment decisions so users can practice safely, see outcomes, and improve their next decision."
    )

    st.info("Core loop: **Learn → Decide → Simulate → Analyze → Improve**")

    if not st.session_state.onboarding_complete:
        onboarding_card()
    else:
        with st.container(border=True):
            st.markdown("**Your learning profile**")
            a, b, c = st.columns(3)
            a.write(f"Experience: **{st.session_state.experience}**")
            b.write(f"Goal: **{st.session_state.goal}**")
            c.write(f"Risk: **{st.session_state.risk_tolerance}**")
            if st.button("Edit profile"):
                st.session_state.onboarding_complete = False
                st.rerun()

    challenge_preview()

    st.subheader("Why FinLearnX")
    p1, p2, p3 = st.columns(3)
    with p1:
        with st.container(border=True):
            st.markdown("### Learn in context")
            st.write("Connect finance concepts to decisions instead of reading them in isolation.")
    with p2:
        with st.container(border=True):
            st.markdown("### Practice safely")
            st.write("Use virtual capital and market data without putting real money at risk.")
    with p3:
        with st.container(border=True):
            st.markdown("### Reflect and improve")
            st.write("Review performance, allocation, concentration, and decision quality after each simulation.")

elif selection == "Start Challenge":
    st.title("$100K Portfolio Challenge")
    st.write(
        "The flagship FinLearnX experience turns portfolio construction into an interactive learning exercise."
    )

    if not st.session_state.onboarding_complete:
        st.warning("Complete your learning profile first so the experience has context.")
        onboarding_card()

    challenge_preview()

    st.subheader("What to pay attention to")
    st.markdown(
        """
        - **Concentration:** Is too much of your portfolio tied to one company or sector?
        - **Diversification:** Are your positions exposed to different sources of risk?
        - **Volatility:** How much does the portfolio move over time?
        - **Decision rationale:** Why did you make each trade?
        - **Outcome vs process:** A profitable trade is not automatically a good decision.
        """
    )

elif selection == "Product Roadmap":
    st.title("Product Roadmap")
    st.caption("Depth before breadth: strengthen the learning loop before expanding the platform.")

    st.markdown("### P0 — Complete the core loop")
    st.markdown(
        """
        - guided first-portfolio challenge ✅
        - contextual portfolio learning review ✅
        - diversification and concentration feedback ✅
        - S&P 500 benchmark comparison
        - volatility and drawdown metrics
        - richer educational feedback tied to portfolio decisions
        """
    )

    st.markdown("### P1 — Personalize learning")
    st.markdown(
        """
        - decision journal: *Why are you making this trade?*
        - portfolio-specific AI explanations
        - behavioral-finance insights
        - personalized learning recommendations
        - goal-based learning missions
        """
    )

    st.markdown("### P2 — Progression and scenarios")
    st.markdown(
        """
        - learner progression and competency levels
        - historical market-crisis scenarios
        - portfolio stress testing
        - risk-adjusted challenge scoring
        """
    )

    st.info(
        "North Star Metric: **Weekly Learning Decisions Completed** — meaningful portfolio decisions or reviews followed by educational feedback."
    )

elif selection == "About":
    st.title("About FinLearnX")
    st.write(
        "FinLearnX is an educational financial-learning product that combines simulated investing with contextual feedback."
    )

    st.markdown(
        """
        **Product principles**

        1. Learning before speculation
        2. Contextual feedback over generic content
        3. Safe practice with virtual capital
        4. Depth before breadth
        5. Measure learning behavior, not just returns
        """
    )

    st.warning(
        "FinLearnX is for educational purposes only. It does not provide financial advice or execute real trades."
    )
    st.caption("Created by Sagar Mandavkar")
