# FinLearnX: AI Financial Learning + Portfolio Platform

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Status](https://img.shields.io/badge/status-active-success)

## 🎯 Purpose

Empower users to learn finance, simulate portfolios, and practice trading using AI-driven tools and comprehensive educational modules.

## ✨ Key Features

### 🤖 AI-Powered Intelligence
- **Multi-Agent AI System**: Market analyst, portfolio advisor, risk manager, trading coach, and beginner educator
- **Intelligent Tutoring**: Personalized financial education with interactive Q&A
- **Smart Recommendations**: AI-driven portfolio suggestions and content recommendations

### 📚 Learning Hub
- **Beginner to Advanced Modules**: Structured learning paths covering fundamentals to advanced strategies
- **Case Studies**: Real-world financial scenarios (2008 crash, bond yield curves, sector rotation)
- **Interactive Quizzes**: Test your knowledge with comprehensive assessments
- **Financial Modeling Walkthroughs**: Step-by-step DCF, valuation, and portfolio construction

### 💼 Portfolio Management
- **Optimization Engines**: Mean-Variance (MPT) and Black-Litterman models
- **Risk Analytics**: VaR, volatility analysis, Monte Carlo simulations
- **Regime Detection**: ML-based market regime classification (bull/bear/sideways)
- **Sector Rotation**: Intelligent sector allocation analysis

### 🎮 Simulations & Trading
- **Backtesting Engine**: Test strategies with comprehensive performance metrics
- **Paper Trading**: Practice with virtual cash and real market data
- **Market Crash Simulator**: Stress test portfolios against historical crises
- **Bond Yield Simulator**: Interactive bond pricing and yield curve analysis
- **ETF Allocation Playground**: Experiment with different allocation strategies

### 📊 Market Analysis
- **Technical Indicators**: RSI, MACD, moving averages, volume analysis
- **Macro Analysis**: Economic indicators and their market impacts
- **Real-time Data**: Integration with Alpaca, Finnhub, and yfinance

## 🏗️ Architecture Overview

```
┌─────────────────┐
│  Streamlit UI   │
└────────┬────────┘
         │
    ┌────▼────┐
    │   AI    │◄──── Multi-Agent LLM System
    │  Layer  │
    └────┬────┘
         │
    ┌────▼────────────────────────┐
    │     Core Business Logic     │
    ├─────────────────────────────┤
    │ • Market Data Ingestion     │
    │ • Technical Indicators      │
    │ • Regime Detection          │
    │ • Portfolio Optimization    │
    │ • Risk Engine               │
    │ • Backtesting               │
    │ • Simulations               │
    └────┬────────────────────────┘
         │
    ┌────▼────┐
    │  Data   │◄──── APIs: Alpaca, Finnhub, yfinance
    │ Storage │
    └─────────┘
```

## 📁 Project Structure

```
FinLearnX/
│
├── app/                    # Streamlit frontend
│   ├── main.py
│   └── pages/
│       ├── dashboard.py
│       ├── learn.py
│       ├── ai_tutor.py
│       ├── market.py
│       ├── portfolio.py
│       ├── simulations.py
│       ├── backtesting.py
│       ├── trading.py
│       └── settings.py
│
├── core/                   # Business logic
│   ├── data_ingestion.py
│   ├── indicators.py
│   ├── regime_classifier.py
│   ├── optimizer.py
│   ├── risk.py
│   ├── portfolio.py
│   └── simulation.py
│
├── ai/                     # AI/LLM layer
│   ├── tutor_prompts.yaml
│   ├── agent_templates.py
│   └── safety_rules.yaml
│
├── models/                 # ML models
│   ├── regime_model.pkl
│   ├── monte_carlo.py
│   └── risk_model.py
│
├── portfolio/              # Optimization
│   ├── optimize_mpt.py
│   ├── black_litterman.py
│   └── rebalance.py
│
├── education/              # Learning content
│   └── modules/
│       ├── beginner.yaml
│       ├── intermediate.yaml
│       └── advanced.yaml
│
├── simulations/            # Simulation engines
│   ├── trading_sim.py
│   ├── crash_sim.py
│   └── bond_sim.py
│
├── backtesting/            # Backtest engine
│   └── engine.py
│
├── tests/                  # Unit tests
│   └── ...
│
└── docs/                   # Documentation
    └── architecture.md
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Setup Instructions

```bash
# Clone the repository
git clone https://github.com/sagarmandavkar-UX/FinLearnX.git
cd FinLearnX

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 💻 How to Run

### Launch Streamlit App

```bash
streamlit run app/main.py
```

The app will open in your browser at `http://localhost:8501`

### Run Backtests

```python
from backtesting.engine import run_backtest

# Define your strategy
results = run_backtest(ticker='AAPL', start='2020-01-01', end='2023-12-31')
print(results)
```

### Use API Integrations

Set up your API keys in `.env` file:

```
ALPACA_API_KEY=your_key_here
ALPACA_SECRET_KEY=your_secret_here
FINNHUB_API_KEY=your_key_here
```

## 📊 Usage Examples

### Portfolio Optimization

```python
from portfolio.optimize_mpt import optimize_portfolio

tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
weights = optimize_portfolio(tickers, risk_tolerance=0.5)
print(f"Optimal weights: {weights}")
```

### Market Crash Simulation

```python
from simulations.crash_sim import simulate_crash

portfolio = {'AAPL': 0.3, 'BONDS': 0.3, 'GOLD': 0.4}
impact = simulate_crash(portfolio, scenario='2008_crisis')
print(f"Portfolio impact: {impact}%")
```

### AI Tutor Chat

```python
from ai.agent_templates import MarketAnalystAgent

agent = MarketAnalystAgent()
response = agent.ask("Explain the concept of beta in portfolio management")
print(response)
```

## 🎓 Educational Modules

### Beginner Track
- Introduction to Markets
- Building a Starter Portfolio
- Understanding Risk & Return
- Basics of Technical Analysis

### Intermediate Track
- Portfolio Optimization Theory
- Technical Indicators Deep Dive
- Options & Derivatives
- Sector Rotation Strategies

### Advanced Track
- Black-Litterman Optimization
- Monte Carlo Risk Analysis
- Quantitative Trading Strategies
- Market Microstructure

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **ML/AI**: scikit-learn, TensorFlow, LangChain
- **Data**: pandas, numpy, yfinance
- **Visualization**: matplotlib, plotly
- **APIs**: Alpaca, Finnhub, Yahoo Finance

## 📈 Roadmap

- [ ] Deep brokerage integration (live trading)
- [ ] News sentiment analysis
- [ ] Options data and strategies
- [ ] Multi-agent orchestration enhancements
- [ ] Mobile app (React Native)
- [ ] Community content sharing
- [ ] Real-time collaboration features
- [ ] Advanced ML models for prediction

## ⚠️ Disclaimer

**This platform is for educational purposes only and is NOT financial advice.**

- Do not make investment decisions based solely on this tool
- Past performance does not guarantee future results
- All investments carry risk; you may lose money
- Consult with a licensed financial advisor before making investment decisions
- The creators are not responsible for any financial losses incurred

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Sagar Mandavkar**
- GitHub: [@sagarmandavkar-UX](https://github.com/sagarmandavkar-UX)

## 🙏 Acknowledgments

- Financial data providers: Alpaca, Finnhub, Yahoo Finance
- Open source community
- Financial education resources

---

**Built with ❤️ for financial education and empowerment**
