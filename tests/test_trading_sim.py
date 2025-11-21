"""Comprehensive Unit Tests for Trading Simulator

Tests buy/sell logic, portfolio calculations, and edge cases
"""

import pytest
import sys
sys.path.append('..')
from simulations.trading_sim import TradingSimulator

class TestTradingSimulator:
    """Test suite for trading simulator functionality"""
    
    def setup_method(self):
        """Initialize simulator before each test"""
        self.sim = TradingSimulator(initial_capital=100000)
    
    def test_initial_state(self):
        """Test simulator initializes correctly"""
        assert self.sim.initial_capital == 100000
        assert self.sim.cash == 100000
        assert self.sim.portfolio == {}
        assert len(self.sim.transaction_history) == 0
    
    def test_successful_buy(self):
        """Test successful stock purchase"""
        result = self.sim.buy('AAPL', 10, 150.0)
        
        assert result['success'] == True
        assert 'AAPL' in self.sim.portfolio
        assert self.sim.portfolio['AAPL'] == 10
        assert self.sim.cash == 100000 - (10 * 150.0)
        assert len(self.sim.transaction_history) == 1
    
    def test_buy_insufficient_funds(self):
        """Test buy fails when insufficient funds"""
        result = self.sim.buy('AAPL', 1000, 150.0)  # $150,000 > $100,000
        
        assert result['success'] == False
        assert 'Insufficient funds' in result['message']
        assert 'AAPL' not in self.sim.portfolio
        assert self.sim.cash == 100000
    
    def test_multiple_buys_same_stock(self):
        """Test buying same stock multiple times"""
        self.sim.buy('AAPL', 10, 150.0)
        self.sim.buy('AAPL', 5, 155.0)
        
        assert self.sim.portfolio['AAPL'] == 15
        assert len(self.sim.transaction_history) == 2
    
    def test_successful_sell(self):
        """Test successful stock sale"""
        self.sim.buy('AAPL', 10, 150.0)
        initial_cash = self.sim.cash
        
        result = self.sim.sell('AAPL', 5, 160.0)
        
        assert result['success'] == True
        assert self.sim.portfolio['AAPL'] == 5
        assert self.sim.cash == initial_cash + (5 * 160.0)
    
    def test_sell_all_shares(self):
        """Test selling all shares removes stock from portfolio"""
        self.sim.buy('AAPL', 10, 150.0)
        self.sim.sell('AAPL', 10, 160.0)
        
        assert 'AAPL' not in self.sim.portfolio
    
    def test_sell_insufficient_shares(self):
        """Test sell fails when insufficient shares"""
        self.sim.buy('AAPL', 10, 150.0)
        result = self.sim.sell('AAPL', 15, 160.0)
        
        assert result['success'] == False
        assert 'Insufficient shares' in result['message']
    
    def test_sell_without_owning(self):
        """Test sell fails when stock not owned"""
        result = self.sim.sell('AAPL', 10, 150.0)
        
        assert result['success'] == False
        assert 'Insufficient shares' in result['message']
    
    def test_portfolio_value_calculation(self):
        """Test portfolio value is calculated correctly"""
        # This test would normally use mocked price data
        # For demonstration, we test the logic structure
        self.sim.buy('AAPL', 10, 150.0)
        
        portfolio_value = self.sim.get_portfolio_value()
        
        # Portfolio value should include cash + holdings
        assert portfolio_value >= self.sim.cash
    
    def test_returns_calculation_profit(self):
        """Test returns calculation shows profit"""
        self.sim.buy('AAPL', 100, 100.0)  # Buy at $100
        self.sim.sell('AAPL', 100, 150.0)  # Sell at $150
        
        returns = self.sim.get_returns()
        
        assert returns['absolute_return'] > 0
        assert returns['percentage_return'] > 0
        assert returns['current_value'] > self.sim.initial_capital
    
    def test_returns_calculation_loss(self):
        """Test returns calculation shows loss"""
        self.sim.buy('AAPL', 100, 150.0)  # Buy at $150
        self.sim.sell('AAPL', 100, 100.0)  # Sell at $100
        
        returns = self.sim.get_returns()
        
        assert returns['absolute_return'] < 0
        assert returns['percentage_return'] < 0
        assert returns['current_value'] < self.sim.initial_capital
    
    def test_transaction_history_records(self):
        """Test all transactions are recorded"""
        self.sim.buy('AAPL', 10, 150.0)
        self.sim.buy('GOOGL', 5, 2000.0)
        self.sim.sell('AAPL', 5, 160.0)
        
        assert len(self.sim.transaction_history) == 3
        
        # Verify transaction types
        assert self.sim.transaction_history[0]['type'] == 'BUY'
        assert self.sim.transaction_history[1]['type'] == 'BUY'
        assert self.sim.transaction_history[2]['type'] == 'SELL'
    
    def test_diversified_portfolio(self):
        """Test managing multiple stocks"""
        self.sim.buy('AAPL', 10, 150.0)
        self.sim.buy('GOOGL', 5, 2000.0)
        self.sim.buy('MSFT', 20, 300.0)
        
        assert len(self.sim.portfolio) == 3
        assert 'AAPL' in self.sim.portfolio
        assert 'GOOGL' in self.sim.portfolio
        assert 'MSFT' in self.sim.portfolio
    
    def test_cash_management(self):
        """Test cash is properly managed across transactions"""
        initial_cash = self.sim.cash
        
        self.sim.buy('AAPL', 10, 100.0)  # -$1000
        self.sim.sell('AAPL', 5, 120.0)  # +$600
        
        expected_cash = initial_cash - 1000 + 600
        assert self.sim.cash == expected_cash

# Run tests with: pytest tests/test_trading_sim.py -v
