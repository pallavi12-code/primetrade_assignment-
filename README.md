# Market Sentiment & Trader Performance Analysis

An exploratory data-analysis project that studies how trader performance changes across Bitcoin market-sentiment regimes using historical trading data and a Fear & Greed index.

> Originally created as an assignment; the repository is documented here as a standalone analytics project.

## Questions explored

- How does average and total PnL vary by sentiment regime?
- How does win rate change between market conditions?
- Do traders change average position size as sentiment changes?
- How do trading fees vary across regimes?

## Analysis workflow

```text
Historical trades + Fear & Greed index
              ↓
Timestamp/date normalization
              ↓
Numeric cleaning
              ↓
Date-based merge
              ↓
PnL / win-rate / position-size metrics
              ↓
Sentiment-level summary
```

## Key metrics

The analysis produces, by sentiment classification:

- Total trades
- Average PnL
- Total PnL
- Average position size
- Win rate
- Average trading fee

## Project structure

```text
.
├── data/
│   ├── fear_greed_index.csv
│   └── historical_data.csv
├── outputs/
├── analysis.py
└── README.md
```

## Run locally

```bash
git clone https://github.com/pallavi12-code/primetrade_assignment-.git
cd primetrade_assignment-
pip install pandas
python analysis.py
```

The script writes `outputs/summary_metrics.csv`.

## Important interpretation note

This is observational analysis, not a trading strategy or financial advice. Differences between sentiment groups describe patterns in the supplied historical data and do not establish causation or guarantee future returns.

## Tech stack

- Python
- Pandas
- Exploratory data analysis
- CSV-based data processing

## Author

**Pallavi Reddy** — AI & Machine Learning Engineering Student, CBIT
