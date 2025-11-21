"""Data Ingestion Module

Handles fetching and caching market data from multiple sources
"""

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
from typing import List, Dict, Optional

class DataIngestion:
    """Main class for data ingestion from multiple APIs"""
    
    def __init__(self, cache_dir="./data/cache"):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
    
    def load_data(self, tickers: List[str], start_date: str, end_date: str,
                  interval: str = "1d") -> pd.DataFrame:
        """
        Load market data for given tickers
        
        Args:
            tickers: List of ticker symbols
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
            interval: Data interval (1d, 1h, etc.)
        
        Returns:
            DataFrame with OHLCV data
        """
        try:
            data = yf.download(tickers, start=start_date, end=end_date,
                             interval=interval, progress=False)
            return self._clean_data(data)
        except Exception as e:
            print(f"Error loading data: {e}")
            return pd.DataFrame()
    
    def _clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean and validate market data"""
        # Remove NaN values
        df = df.dropna()
        
        # Forward fill any remaining gaps
        df = df.fillna(method='ffill')
        
        return df
    
    def get_latest_price(self, ticker: str) -> float:
        """Get latest closing price for a ticker"""
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period="1d")
            return data['Close'].iloc[-1] if not data.empty else 0.0
        except:
            return 0.0
    
    def get_company_info(self, ticker: str) -> Dict:
        """Get company information"""
        try:
            stock = yf.Ticker(ticker)
            return stock.info
        except:
            return {}
    
    def cache_data(self, df: pd.DataFrame, filename: str):
        """Cache data to local storage"""
        filepath = os.path.join(self.cache_dir, filename)
        df.to_csv(filepath)
    
    def load_cached_data(self, filename: str) -> Optional[pd.DataFrame]:
        """Load data from cache"""
        filepath = os.path.join(self.cache_dir, filename)
        if os.path.exists(filepath):
            return pd.read_csv(filepath, index_col=0, parse_dates=True)
        return None
