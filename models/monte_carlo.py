"""Monte Carlo Simulation for Risk Analysis

Simulate portfolio outcomes and price projections
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def monte_carlo_simulation(price_series, days=252, simulations=1000):
    """
    Run Monte Carlo simulation for price projections
    
    Args:
        price_series: Historical price data
        days: Number of days to simulate
        simulations: Number of simulation runs
    
    Returns:
        Array of simulated price paths
    """
    # Calculate returns statistics
    returns = price_series.pct_change().dropna()
    mu = returns.mean()
    sigma = returns.std()
    
    last_price = price_series.iloc[-1]
    
    # Run simulations
    simulation_results = []
    
    for _ in range(simulations):
        prices = [last_price]
        for _ in range(days):
            shock = np.random.normal(mu, sigma)
            prices.append(prices[-1] * (1 + shock))
        simulation_results.append(prices)
    
    return np.array(simulation_results)

def portfolio_monte_carlo(returns, weights, initial_value=100000, days=252, simulations=1000):
    """
    Monte Carlo simulation for portfolio
    
    Args:
        returns: Historical returns DataFrame
        weights: Portfolio weights
        initial_value: Starting portfolio value
        days: Simulation horizon
        simulations: Number of runs
    
    Returns:
        Simulated portfolio values
    """
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    
    portfolio_simulations = []
    
    for _ in range(simulations):
        portfolio_values = [initial_value]
        for _ in range(days):
            # Generate correlated random returns
            Z = np.random.multivariate_normal(mean_returns, cov_matrix)
            portfolio_return = np.dot(weights, Z)
            new_value = portfolio_values[-1] * (1 + portfolio_return)
            portfolio_values.append(new_value)
        portfolio_simulations.append(portfolio_values)
    
    return np.array(portfolio_simulations)
