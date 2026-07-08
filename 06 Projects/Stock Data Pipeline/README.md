# Stock Data Pipeline

> Investor OS is not being built to predict the market.
>
> It is being built to improve the quality of investment decisions through data, finance, software engineering, AI, and disciplined reasoning.

---
# Overview

The Stock Data Pipeline is the first software component of Investor OS.

Its purpose is to collect, organize, analyze, and visualize stock market data. This project will gradually evolve into a complete market analysis engine capable of supporting investment research, valuation, risk analysis, portfolio management, and AI-assisted decision making.

Every feature added should contribute to making better long-term capital allocation decisions.

---
# Current Features

## Data Collection

- Download historical stock data using Yahoo Finance
- User-selected stock ticker
- Retrieve one month of historical price history

## Basic Analysis

- Last closing price
- Highest price
- Lowest price
- Average trading volume

## Feature Engineering

- Daily Return calculation
- 5-Day Simple Moving Average (SMA)
- 5-Day Exponential Moving Average (EMA)  
- Volatility (Standard Deviation of Daily Returns)

## Visualization

- Closing price chart
- Trading volume chart
- Price + Moving Average chart
- Combined Price + Volume visualization

## Software Design

- Modular architecture
- Reusable functions
- Separate data retrieval from analysis logic
- Virtual environment configured
- Dependency management using `requirements.txt`

---

# Project Structure

```text
Stock Data Pipeline/
│
├── main.py              # User interface
├── stock.py             # Data collection, analysis, and visualization
├── requirements.txt
├── README.md
├── data/
└── .venv/
```

---

# Technologies Used

- Python
- yfinance
- pandas
- matplotlib
- Git
- GitHub

---

# Skills Learned

## Python

- Functions
- Parameters
- Return values
- Modules
- Imports

## Data Analysis

- pandas DataFrames
- Percentage change (`pct_change`)
- Rolling window calculations

## Finance

- Historical market data
- Price statistics
- Volume analysis
- Daily returns
- Moving averages

## Visualization

- Line charts
- Bar charts
- Dual-axis charts

## Software Engineering

- Modular programming
- Git
- GitHub
- Project organization

---

# Development Roadmap

## Phase 1 — Data Pipeline

- ✅ Download stock data
- ✅ Price statistics
- ✅ Volume statistics
- ✅ Price chart
- ✅ Volume chart
- ✅Custom date ranges
- ✅Multiple time periods

---

## Phase 2 — Feature Engineering & Technical Analysis

- ✅ Daily Returns
- ✅ Simple Moving Average (SMA)
- ✅ Exponential Moving Average (EMA)
- ✅RSI
- ✅ MACD
- ✅Bollinger Bands
- ⏳ Support & Resistance
- ⏳ Candlestick Charts

---

## Phase 3 — Financial Analysis

- Income Statement
- Balance Sheet
- Cash Flow Statement
- Financial Ratios
- Company Fundamentals

---

## Phase 4 — Valuation

- Discounted Cash Flow (DCF)
- Intrinsic Value
- Margin of Safety
- Comparable Company Analysis

---

## Phase 5 — Macro & Risk Analysis

- Economic Indicators
- Interest Rates
- Inflation
- Beta
- Volatility
- Drawdown
- Correlation

---

## Phase 6 — AI Analysis

- AI Company Reports
- Earnings Call Summaries
- News Sentiment Analysis
- Risk Summaries
- Investment Thesis Generator

---

## Phase 7 — Portfolio Management

- Portfolio Tracking
- Diversification Analysis
- Portfolio Optimization
- Performance Attribution
- Portfolio Rebalancing

---

## Phase 8 — Investor OS Integration

- Automated Research Pipeline
- Interactive Dashboard
- Watchlists
- Report Generation
- AI Investment Assistant

---

# Mission

This project is **not** intended to become a trading bot.

Its purpose is to build a professional-grade investment research engine that improves investment judgment through:

- Finance
- Software Engineering
- Artificial Intelligence
- Systems Thinking
- Data-Driven Decision Making

The objective is not simply to generate charts.

The objective is to transform raw market data into actionable investment insight and continuously improve long-term capital allocation decisions.

---

**Status:** 
- ✅ **Day 1:** Stock data pipeline
- ✅ **Day 2:** Functions and code organization
- ✅ **Day 3:** Returns, moving averages, visualization
- ✅ **Day 4:** EMA and technical analysis improvements
- ✅ **Day 5:** RSI implementation
- ✅ **Day 6:** MACD, Signal Line, Histogram, dashboard
- ✅ **Day 7:** Bollinger Bands and comprehensive technical analysis dashboard