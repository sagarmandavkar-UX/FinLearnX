"""Trading Simulation Module

Paper trading and stock picking simulator
"""

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class TradingSimulator:
    """Paper trading simulator with virtual cash"""
    
    def __init__(self, initial_capital=100000):
        self.initial_capital = initial_capital
        self.cash = initial_capital
        self.portfolio = {}
        self.transaction_history = []
        self.portfolio_value_history = []
    
    def buy(self, ticker: str, quantity: int, price: float):
        """
        Execute a buy order
        
        Args:
            ticker: Stock ticker
            quantity: Number of shares
            price: Price per share
        """
        cost = quantity * price
        
        if cost > self.cash:
            return {"success": False, "message": "Insufficient funds"}
        
        self.cash -= cost
        
        if ticker in self.portfolio:
            self.portfolio[ticker] += quantity
        else:
            self.portfolio[ticker] = quantity
        
        self.transaction_history.append({
            "type": "BUY",
            "ticker": ticker,
            "quantity": quantity,
            "price": price,
            "date": datetime.now()
        })
        
        return {"success": True, "message": f"Bought {quantity} shares of {ticker}"}
    
    def sell(self, ticker: str, quantity: int, price: float):
        """
        Execute a sell order
        
        Args:
            ticker: Stock ticker
            quantity: Number of shares
            price: Price per share
        """
        if ticker not in self.portfolio or self.portfolio[ticker] < quantity:
            return {"success": False, "message": "Insufficient shares"}
        
        revenue = quantity * price
        self.cash += revenue
        self.portfolio[ticker] -= quantity
        
        if self.portfolio[ticker] == 0:
            del self.portfolio[ticker]
        
        self.transaction_history.append({
            "type": "SELL",
            "ticker": ticker,
            "quantity": quantity,
            "price": price,
            "date": datetime.now()
        })
        
        return {"success": True, "message": f"Sold {quantity} shares of {ticker}"}
    
    def get_portfolio_value(self) -> float:
        """Calculate current portfolio value"""
        total = self.cash
        
        for ticker, quantity in self.portfolio.items():
            try:
                stock = yf.Ticker(ticker)
                current_price = stock.history(period="1d")['Close'].iloc[-1]
                total += quantity * current_price
            except:
                pass
        
        return total
    
    def get_returns(self) -> dict:
        """Calculate portfolio returns"""
        current_value = self.get_portfolio_value()
        absolute_return = current_value - self.initial_capital
        percentage_return = (absolute_return / self.initial_capital) * 100
        
        return {
            "current_value": current_value,
            "absolute_return": absolute_return,
            "percentage_return": percentage_return
        }
    
    def simulate_stock_pick(tickers, start_date, end_date):
        """Simulate stock picking strategy"""
        data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
        returns = data.pct_change().mean(axis=1)
        cumulative_returns = (1 + returns).cumprod()
        
        return {
            "data": data,
            "returns": returns,
            "cumulative_returns": cumulative_returns,
            "final_return": (cumulative_returns.iloc[-1] - 1) * 100
        }
