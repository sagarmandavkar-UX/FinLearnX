"""Modern Portfolio Theory (MPT) Optimization

Mean-variance optimization for portfolio construction
"""

import numpy as np
import pandas as pd
from scipy.optimize import minimize
import yfinance as yf

class MPTOptimizer:
    """Portfolio optimization using Mean-Variance theory"""
    
    def __init__(self, tickers, start_date, end_date):
        self.tickers = tickers
        self.data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
        self.returns = self.data.pct_change().dropna()
        self.mean_returns = self.returns.mean()
        self.cov_matrix = self.returns.cov()
    
    def portfolio_performance(self, weights):
        """Calculate portfolio return and volatility"""
        returns = np.sum(self.mean_returns * weights) * 252
        std = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix * 252, weights)))
        return returns, std
    
    def neg_sharpe_ratio(self, weights, risk_free_rate=0.02):
        """Negative Sharpe ratio for minimization"""
        returns, std = self.portfolio_performance(weights)
        return -(returns - risk_free_rate) / std
    
    def optimize_sharpe(self):
        """Optimize for maximum Sharpe ratio"""
        num_assets = len(self.tickers)
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for _ in range(num_assets))
        initial_guess = num_assets * [1. / num_assets]
        
        result = minimize(
            self.neg_sharpe_ratio,
            initial_guess,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )
        
        return result.x
    
    def optimize_min_volatility(self):
        """Optimize for minimum volatility"""
        num_assets = len(self.tickers)
        
        def portfolio_volatility(weights):
            return self.portfolio_performance(weights)[1]
        
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for _ in range(num_assets))
        initial_guess = num_assets * [1. / num_assets]
        
        result = minimize(
            portfolio_volatility,
            initial_guess,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )
        
        return result.x
    
    def efficient_frontier(self, num_portfolios=100):
        """Generate efficient frontier"""
        results = np.zeros((3, num_portfolios))
        
        for i in range(num_portfolios):
            weights = np.random.random(len(self.tickers))
            weights /= np.sum(weights)
            
            returns, std = self.portfolio_performance(weights)
            results[0, i] = returns
            results[1, i] = std
            results[2, i] = (returns - 0.02) / std
        
        return results
