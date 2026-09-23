"""Anonymous, session-scoped funnel events for product evaluation."""

from datetime import datetime, timezone

EVENTS = (
    "onboarding_started",
    "onboarding_completed",
    "simulator_opened",
    "first_trade_completed",
    "portfolio_review_opened",
    "learning_review_completed",
    "ai_explanation_requested",
)


def record_event(state, name: str, **details) -> None:
    if name not in EVENTS:
        raise ValueError(f"Unknown event: {name}")
    if "learning_events" not in state:
        state["learning_events"] = []
    # Record unique funnel milestones once per session, including Streamlit reruns.
    if any(event["event"] == name for event in state["learning_events"]):
        return
    state["learning_events"].append(
        {"event": name, "timestamp_utc": datetime.now(timezone.utc).isoformat(), **details}
    )


def funnel_progress(events) -> dict:
    observed = {event["event"] for event in events}
    return {name: name in observed for name in EVENTS}
