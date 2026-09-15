"""Unit tests for the FinLearnX paper-trading simulator."""

import pandas as pd

from simulations.trading_sim import TradingSimulator


class _FakeTicker:
    def __init__(self, ticker):
        self.ticker = ticker

    def history(self, period="1d"):
        return pd.DataFrame({"Close": [175.0]})


class TestTradingSimulator:
    def setup_method(self):
        self.sim = TradingSimulator(initial_capital=100000)

    def test_initial_state(self):
        assert self.sim.initial_capital == 100000
        assert self.sim.cash == 100000
        assert self.sim.portfolio == {}
        assert self.sim.transaction_history == []

    def test_successful_buy(self):
        result = self.sim.buy("AAPL", 10, 150.0)
        assert result["success"] is True
        assert self.sim.portfolio["AAPL"] == 10
        assert self.sim.cash == 98500
        assert len(self.sim.transaction_history) == 1

    def test_buy_insufficient_funds(self):
        result = self.sim.buy("AAPL", 1000, 150.0)
        assert result["success"] is False
        assert "Insufficient funds" in result["message"]
        assert "AAPL" not in self.sim.portfolio
        assert self.sim.cash == 100000

    def test_multiple_buys_same_stock(self):
        self.sim.buy("AAPL", 10, 150.0)
        self.sim.buy("AAPL", 5, 155.0)
        assert self.sim.portfolio["AAPL"] == 15
        assert len(self.sim.transaction_history) == 2

    def test_successful_sell(self):
        self.sim.buy("AAPL", 10, 150.0)
        initial_cash = self.sim.cash
        result = self.sim.sell("AAPL", 5, 160.0)
        assert result["success"] is True
        assert self.sim.portfolio["AAPL"] == 5
        assert self.sim.cash == initial_cash + 800

    def test_sell_all_shares_removes_position(self):
        self.sim.buy("AAPL", 10, 150.0)
        self.sim.sell("AAPL", 10, 160.0)
        assert "AAPL" not in self.sim.portfolio

    def test_sell_insufficient_shares(self):
        self.sim.buy("AAPL", 10, 150.0)
        result = self.sim.sell("AAPL", 15, 160.0)
        assert result["success"] is False
        assert "Insufficient shares" in result["message"]

    def test_sell_without_owning_position(self):
        result = self.sim.sell("AAPL", 10, 150.0)
        assert result["success"] is False

    def test_portfolio_value_uses_market_price_without_network(self, monkeypatch):
        monkeypatch.setattr("simulations.trading_sim.yf.Ticker", _FakeTicker)
        self.sim.buy("AAPL", 10, 150.0)
        # cash 98,500 + 10 shares * $175
        assert self.sim.get_portfolio_value() == 100250

    def test_returns_calculation_profit(self):
        self.sim.buy("AAPL", 100, 100.0)
        self.sim.sell("AAPL", 100, 150.0)
        returns = self.sim.get_returns()
        assert returns["absolute_return"] == 5000
        assert returns["percentage_return"] == 5
        assert returns["current_value"] == 105000

    def test_returns_calculation_loss(self):
        self.sim.buy("AAPL", 100, 150.0)
        self.sim.sell("AAPL", 100, 100.0)
        returns = self.sim.get_returns()
        assert returns["absolute_return"] == -5000
        assert returns["percentage_return"] == -5
        assert returns["current_value"] == 95000

    def test_transaction_history_records_actions(self):
        self.sim.buy("AAPL", 10, 150.0)
        self.sim.buy("GOOGL", 5, 2000.0)
        self.sim.sell("AAPL", 5, 160.0)
        assert [row["type"] for row in self.sim.transaction_history] == ["BUY", "BUY", "SELL"]

    def test_diversified_portfolio_tracks_multiple_positions(self):
        self.sim.buy("AAPL", 10, 150.0)
        self.sim.buy("GOOGL", 5, 2000.0)
        self.sim.buy("MSFT", 20, 300.0)
        assert set(self.sim.portfolio) == {"AAPL", "GOOGL", "MSFT"}

    def test_cash_management(self):
        self.sim.buy("AAPL", 10, 100.0)
        self.sim.sell("AAPL", 5, 120.0)
        assert self.sim.cash == 99600
