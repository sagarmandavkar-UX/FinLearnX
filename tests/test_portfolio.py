"""Unit Tests for Portfolio Module

Test portfolio optimization and risk calculations
"""

import pytest
import numpy as np
import pandas as pd
from portfolio.optimize_mpt import MPTOptimizer

def test_portfolio_weights_sum_to_one():
    """Test that portfolio weights sum to 1"""
    tickers = ['AAPL', 'GOOGL', 'MSFT']
    optimizer = MPTOptimizer(tickers, '2020-01-01', '2023-01-01')
    weights = optimizer.optimize_sharpe()
    
    assert np.isclose(np.sum(weights), 1.0), "Weights should sum to 1"

def test_weights_are_positive():
    """Test that weights are non-negative"""
    tickers = ['AAPL', 'GOOGL', 'MSFT']
    optimizer = MPTOptimizer(tickers, '2020-01-01', '2023-01-01')
    weights = optimizer.optimize_sharpe()
    
    assert all(w >= 0 for w in weights), "All weights should be non-negative"

# Placeholder for more tests
# TODO: Add tests for backtesting
# TODO: Add tests for simulations
# TODO: Add tests for data ingestion
