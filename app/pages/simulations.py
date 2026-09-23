"""Stock Picking Simulator - Interactive Trading Practice

Complete end-to-end simulation with real market data and charts
"""

import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from simulations.trading_sim import TradingSimulator
from core.learning_events import record_event

# Page configuration
st.set_page_config(page_title="Stock Simulator", page_icon="💵", layout="wide")

# Initialize session state
if 'simulator' not in st.session_state:
    st.session_state.simulator = TradingSimulator(initial_capital=100000)
if 'trade_history' not in st.session_state:
    st.session_state.trade_history = []
record_event(st.session_state, "simulator_opened")

# Title and description
st.title("💵 Stock Picking Simulator")
st.markdown("""
Practice trading with **$100,000 virtual cash**. Learn by doing - execute trades,
track your portfolio, and see real-time performance metrics.
""")
if not st.session_state.simulator.transaction_history:
    st.info("First step: choose a stock in the sidebar, review its price, then make one virtual trade. Open Review My Portfolio afterward to see what you learned.")
elif st.session_state.simulator.portfolio:
    st.page_link("portfolio_review.py", label="Review My Portfolio", icon="🧭")

# Sidebar - Trading Controls
with st.sidebar:
    st.header("🎯 Trading Dashboard")
    
    # Portfolio summary
    st.metric("Portfolio Value", 
              f"${st.session_state.simulator.get_portfolio_value():,.2f}",
              delta=f"${st.session_state.simulator.get_portfolio_value() - st.session_state.simulator.initial_capital:,.2f}")
    
    st.metric("Available Cash", 
              f"${st.session_state.simulator.cash:,.2f}")
    
    returns = st.session_state.simulator.get_returns()
    st.metric("Total Return", 
              f"{returns['percentage_return']:.2f}%",
              delta=f"${returns['absolute_return']:,.2f}")
    
    st.divider()
    
    # Trade execution
    st.subheader("📊 Execute Trade")
    
    action = st.radio("Action", ["Buy", "Sell"])
    
    # Stock selector with popular tickers
    popular_tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'NVDA', 'META', 'JPM', 'V', 'WMT']
    ticker = st.selectbox("Ticker Symbol", popular_tickers)
    
    # Get current price
    try:
        stock = yf.Ticker(ticker)
        current_price = stock.history(period='1d')['Close'].iloc[-1]
        st.info(f"Current Price: ${current_price:.2f}")
    except:
        current_price = 0
        st.warning("Unable to fetch price")
    
    quantity = st.number_input("Quantity", min_value=1, value=10, step=1)
    
    total_cost = current_price * quantity
    st.write(f"**Total: ${total_cost:,.2f}**")
    
    if st.button(f"▶️ {action} {quantity} shares", type="primary", use_container_width=True, disabled=current_price <= 0):
        if action == "Buy":
            result = st.session_state.simulator.buy(ticker, quantity, current_price)
        else:
            result = st.session_state.simulator.sell(ticker, quantity, current_price)
        
        if result['success']:
            record_event(st.session_state, "first_trade_completed")
            st.session_state.pop("ai_explanation", None)
            st.success(result['message'])
            st.session_state.trade_history.append({
                'time': datetime.now().strftime('%H:%M:%S'),
                'action': action,
                'ticker': ticker,
                'quantity': quantity,
                'price': current_price,
                'total': total_cost
            })
            st.rerun()
        else:
            st.error(result['message'])
    
    # Reset button
    if st.button("🔄 Reset Portfolio", use_container_width=True):
        st.session_state.simulator = TradingSimulator(initial_capital=100000)
        st.session_state.trade_history = []
        st.session_state.pop("ai_explanation", None)
        st.rerun()

# Main content area
tab1, tab2, tab3, tab4 = st.tabs(["💼 Portfolio", "📈 Charts", "📊 Performance", "📑 History"])

# Tab 1: Current Portfolio
with tab1:
    st.header("Current Holdings")
    
    if st.session_state.simulator.portfolio:
        holdings_data = []
        total_value = 0
        
        for ticker, quantity in st.session_state.simulator.portfolio.items():
            try:
                stock = yf.Ticker(ticker)
                current_price = stock.history(period='1d')['Close'].iloc[-1]
                value = quantity * current_price
                total_value += value
                
                holdings_data.append({
                    'Ticker': ticker,
                    'Quantity': quantity,
                    'Current Price': f"${current_price:.2f}",
                    'Total Value': f"${value:,.2f}",
                    'Weight': f"{(value / st.session_state.simulator.get_portfolio_value()) * 100:.1f}%"
                })
            except:
                pass
        
        if holdings_data:
            df = pd.DataFrame(holdings_data)
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            # Portfolio allocation pie chart
            st.subheader("🥧 Portfolio Allocation")
            fig = go.Figure(data=[go.Pie(
                labels=[h['Ticker'] for h in holdings_data],
                values=[float(h['Total Value'].replace('$','').replace(',','')) for h in holdings_data],
                hole=0.4
            )])
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("📊 No holdings yet. Start trading to build your portfolio!")
    else:
        st.info("👁️ Your portfolio is empty. Make your first trade using the sidebar!")

# Tab 2: Interactive Charts
with tab2:
    st.header("Stock Price Charts")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        chart_ticker = st.selectbox("Select Stock to Analyze", popular_tickers, key='chart_ticker')
    
    with col2:
        period = st.selectbox("Time Period", ['1d', '5d', '1mo', '3mo', '6mo', '1y'], index=4)
    
    try:
        # Fetch data
        stock = yf.Ticker(chart_ticker)
        hist = stock.history(period=period)
        
        if not hist.empty:
            # Candlestick chart
            fig = go.Figure(data=[go.Candlestick(
                x=hist.index,
                open=hist['Open'],
                high=hist['High'],
                low=hist['Low'],
                close=hist['Close'],
                name=chart_ticker
            )])
            
            fig.update_layout(
                title=f"{chart_ticker} Price Chart",
                yaxis_title='Price ($)',
                xaxis_title='Date',
                height=500,
                template='plotly_white'
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Volume chart
            fig_vol = go.Figure(data=[go.Bar(
                x=hist.index,
                y=hist['Volume'],
                name='Volume'
            )])
            
            fig_vol.update_layout(
                title='Trading Volume',
                yaxis_title='Volume',
                height=250,
                template='plotly_white'
            )
            
            st.plotly_chart(fig_vol, use_container_width=True)
            
            # Key metrics
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Current Price", f"${hist['Close'].iloc[-1]:.2f}")
            with col2:
                daily_change = ((hist['Close'].iloc[-1] - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2] * 100)
                st.metric("Daily Change", f"{daily_change:.2f}%")
            with col3:
                st.metric("52W High", f"${hist['High'].max():.2f}")
            with col4:
                st.metric("52W Low", f"${hist['Low'].min():.2f}")
        else:
            st.warning("No data available for this period")
    except Exception as e:
        st.error(f"Error loading chart: {str(e)}")

# Tab 3: Performance Analytics
with tab3:
    st.header("📊 Performance Metrics")
    
    returns = st.session_state.simulator.get_returns()
    
    # Key metrics in columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Portfolio Value",
            f"${returns['current_value']:,.2f}",
            delta=f"${returns['absolute_return']:,.2f}"
        )
    
    with col2:
        st.metric(
            "Total Return",
            f"{returns['percentage_return']:.2f}%",
            delta=f"{returns['percentage_return']:.2f}%"
        )
    
    with col3:
        num_trades = len(st.session_state.trade_history)
        st.metric("Total Trades", num_trades)
    
    st.divider()
    
    # Performance insights
    st.subheader("💡 Performance Insights")
    
    if returns['percentage_return'] > 10:
        st.info("Your simulated return is positive. Compare it with a benchmark over the same period before drawing conclusions about relative performance.")
    elif returns['percentage_return'] > 0:
        st.info("📈 Good job! You're generating positive returns.")
    elif returns['percentage_return'] > -5:
        st.warning("⚠️ Your portfolio is slightly negative. Consider diversification.")
    else:
        st.error("📉 Portfolio is down significantly. Review your strategy.")
    
    # Tips
    with st.expander("🎯 Trading Tips"):
        st.markdown("""
        **Key Strategies:**
        - **Diversify**: Don't put all eggs in one basket
        - **Research**: Understand companies before investing
        - **Long-term**: Focus on fundamentals, not daily fluctuations
        - **Risk Management**: Never invest more than you can afford to lose
        - **Stay Informed**: Follow market news and trends
        """)

# Tab 4: Trade History
with tab4:
    st.header("📑 Trade History")
    
    if st.session_state.trade_history:
        df_history = pd.DataFrame(st.session_state.trade_history)
        st.dataframe(df_history, use_container_width=True, hide_index=True)
        
        # Summary stats
        st.subheader("📊 Trade Statistics")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            buy_trades = len([t for t in st.session_state.trade_history if t['action'] == 'Buy'])
            st.metric("Buy Orders", buy_trades)
        
        with col2:
            sell_trades = len([t for t in st.session_state.trade_history if t['action'] == 'Sell'])
            st.metric("Sell Orders", sell_trades)
        
        with col3:
            total_volume = sum([t['total'] for t in st.session_state.trade_history])
            st.metric("Total Volume", f"${total_volume:,.2f}")
    else:
        st.info("💭 No trades executed yet. Start trading to see your history!")

# Footer
st.divider()
st.caption("⚠️ **Educational purposes only.** This is a simulation with virtual money. Not financial advice.")
