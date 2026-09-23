"""AI integration is opt-in and sends only a small simulated snapshot."""

import sys
from types import SimpleNamespace

import pytest

from ai.portfolio_coach import explain_portfolio


def test_requires_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(RuntimeError, match="OPENAI_API_KEY"):
        explain_portfolio({"cash": 100000})


def test_passes_snapshot_and_no_storage(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    calls = []
    def create(**kwargs):
        calls.append(kwargs)
        return SimpleNamespace(output_text="Try comparing position weights.")
    monkeypatch.setitem(sys.modules, "openai", SimpleNamespace(OpenAI=lambda **kwargs: SimpleNamespace(responses=SimpleNamespace(create=create))))
    result = explain_portfolio({"cash": 100000}, "Understand risk")
    assert result == "Try comparing position weights."
    assert calls[0]["store"] is False
    assert '"cash": 100000' in calls[0]["input"]
    assert '"learning_goal": "Understand risk"' in calls[0]["input"]
