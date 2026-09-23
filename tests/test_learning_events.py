"""Session event semantics used for activation measurement."""

from core.learning_events import funnel_progress, record_event


def test_funnel_records_a_milestone_once_across_reruns():
    state = {}
    record_event(state, "onboarding_started")
    record_event(state, "onboarding_started")
    record_event(state, "first_trade_completed")
    assert len(state["learning_events"]) == 2
    assert funnel_progress(state["learning_events"])["first_trade_completed"]
    assert not funnel_progress(state["learning_events"])["learning_review_completed"]
