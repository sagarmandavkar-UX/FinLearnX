"""Backtesting Engine

Test trading strategies against historical data
"""

import pandas as pd
import numpy as np
import yfinance as yf

class BacktestEngine:
    """Simple backtesting engine for trading strategies"""
    
    def __init__(self, ticker, start_date, end_date, initial_capital=100000):
        self.ticker = ticker
        self.data = yf.download(ticker, start=start_date, end=end_date)
        self.initial_capital = initial_capital
        self.results = None
    
    def moving_average_strategy(self, short_window=20, long_window=50):
        """Simple moving average crossover strategy"""
        signals = pd.DataFrame(index=self.data.index)
        signals['price'] = self.data['Adj Close']
        signals['short_ma'] = self.data['Adj Close'].rolling(window=short_window).mean()
        signals['long_ma'] = self.data['Adj Close'].rolling(window=long_window).mean()
        signals['signal'] = 0.0
        signals['signal'][short_window:] = np.where(
            signals['short_ma'][short_window:] > signals['long_ma'][short_window:], 1.0, 0.0
        )
        signals['positions'] = signals['signal'].diff()
        
        return signals
    
    def calculate_returns(self, signals):
        """Calculate strategy returns"""
        positions = pd.DataFrame(index=signals.index).fillna(0.0)
        positions['holdings'] = signals['signal'] * signals['price']
        
        portfolio = positions.multiply(self.initial_capital / signals['price'].iloc[0], axis=0)
        pos_diff = positions.diff()
        
        portfolio['cash'] = self.initial_capital - (pos_diff.multiply(signals['price'], axis=0)).cumsum().sum(axis=1)
        portfolio['total'] = portfolio['cash'] + portfolio['holdings']
        portfolio['returns'] = portfolio['total'].pct_change()
        
        return portfolio
    
    def run_backtest(self, strategy='moving_average'):
        """Run backtest and calculate metrics"""
        if strategy == 'moving_average':
            signals = self.moving_average_strategy()
        
        portfolio = self.calculate_returns(signals)
        
        # Calculate metrics
        total_return = (portfolio['total'].iloc[-1] - self.initial_capital) / self.initial_capital
        sharpe_ratio = portfolio['returns'].mean() / portfolio['returns'].std() * np.sqrt(252)
        max_drawdown = (portfolio['total'] / portfolio['total'].cummax() - 1).min()
        
        self.results = {
            'total_return': total_return * 100,
            'sharpe_ratio': sharpe_ratio,
            'max_drawdown': max_drawdown * 100,
            'final_value': portfolio['total'].iloc[-1],
            'portfolio': portfolio
        }
        
        return self.results
