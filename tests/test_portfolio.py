"""Deterministic unit tests for Modern Portfolio Theory optimization."""

import numpy as np
import pandas as pd

from portfolio.optimize_mpt import MPTOptimizer


def _mock_market_download(*args, **kwargs):
    """Return stable multi-ticker price data so CI never depends on the network."""
    dates = pd.date_range("2023-01-01", periods=80, freq="B")
    prices = pd.DataFrame(
        {
            "AAPL": np.linspace(100, 130, len(dates)) + np.sin(np.arange(len(dates))) * 2,
            "GOOGL": np.linspace(90, 112, len(dates)) + np.cos(np.arange(len(dates))) * 1.5,
            "MSFT": np.linspace(110, 145, len(dates)) + np.sin(np.arange(len(dates)) / 2) * 2.5,
        },
        index=dates,
    )
    return pd.concat({"Adj Close": prices}, axis=1)


def _optimizer(monkeypatch):
    monkeypatch.setattr("portfolio.optimize_mpt.yf.download", _mock_market_download)
    return MPTOptimizer(["AAPL", "GOOGL", "MSFT"], "2023-01-01", "2023-06-01")


def test_portfolio_weights_sum_to_one(monkeypatch):
    optimizer = _optimizer(monkeypatch)
    weights = optimizer.optimize_sharpe()

    assert np.isclose(np.sum(weights), 1.0, atol=1e-6)


def test_weights_are_non_negative(monkeypatch):
    optimizer = _optimizer(monkeypatch)
    weights = optimizer.optimize_sharpe()

    assert np.all(weights >= -1e-8)


def test_min_volatility_weights_are_valid(monkeypatch):
    optimizer = _optimizer(monkeypatch)
    weights = optimizer.optimize_min_volatility()

    assert np.isclose(np.sum(weights), 1.0, atol=1e-6)
    assert np.all(weights >= -1e-8)


def test_efficient_frontier_shape(monkeypatch):
    optimizer = _optimizer(monkeypatch)
    frontier = optimizer.efficient_frontier(num_portfolios=25)

    assert frontier.shape == (3, 25)
    assert np.isfinite(frontier).all()
