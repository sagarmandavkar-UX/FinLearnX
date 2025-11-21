# FinLearnX Architecture

## System Overview

FinLearnX is a comprehensive AI-driven financial education and portfolio management platform built with a modular architecture.

## Core Components

### 1. Frontend Layer (`app/`)
- **Technology**: Streamlit
- **Purpose**: Interactive UI for user interaction
- **Pages**: Dashboard, Learning Hub, AI Tutor, Market Analysis, Portfolio Builder, Simulations, Backtesting, Paper Trading

### 2. AI Layer (`ai/`)
- **Multi-Agent System**: 6 specialized agents
  - Market Analyst
  - Portfolio Advisor
  - Financial Modeling Tutor
  - Risk Manager
  - Trading Coach
  - Beginner Educator
- **Technology**: LangChain, OpenAI GPT

### 3. Core Business Logic (`core/`)
- Data Ingestion: yfinance, Alpaca, Finnhub
- Technical Indicators
- Regime Classification
- Portfolio Logic

### 4. Portfolio Module (`portfolio/`)
- MPT Optimization
- Black-Litterman Model
- Rebalancing Logic
- Efficient Frontier Generation

### 5. Models (`models/`)
- Monte Carlo Simulation
- Regime Detection ML Model
- Risk Models

### 6. Simulations (`simulations/`)
- Paper Trading
- Market Crash Scenarios
- Bond Pricing
- ETF Allocation

### 7. Backtesting (`backtesting/`)
- Strategy Testing Engine
- Performance Metrics (Sharpe, Max Drawdown)
- Moving Average Strategy

### 8. Education (`education/`)
- Structured Learning Modules
- Interactive Quizzes
- Case Studies
- Video Content

### 9. Testing (`tests/`)
- Unit Tests (pytest)
- Integration Tests
- Coverage Reports

## Data Flow

```
User Input → Streamlit UI → Core Logic → Data APIs
                ↓
         AI Agents (Analysis/Advice)
                ↓
         Results → Visualization → User
```

## Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.8+
- **ML/AI**: scikit-learn, TensorFlow, LangChain
- **Data**: pandas, numpy, yfinance
- **Visualization**: matplotlib, plotly
- **Testing**: pytest
- **Optimization**: scipy, cvxpy

## Deployment

- Containerized with Docker
- Deployed on cloud platforms (AWS/Azure/GCP)
- CI/CD with GitHub Actions

## Security

- API keys stored in environment variables
- No financial advice (educational only)
- Data privacy compliance

## Scalability

- Modular architecture for easy feature addition
- Caching for data optimization
- Async data fetching
- Horizontal scaling ready
