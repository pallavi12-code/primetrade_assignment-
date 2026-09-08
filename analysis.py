"""Analyze trader performance across market-sentiment regimes.

Expected inputs:
  data/fear_greed_index.csv
  data/historical_data.csv

The original assignment analysis is preserved in Git history; this entrypoint
makes the intended workflow explicit and keeps generated outputs out of source.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent


def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    fear = pd.read_csv(ROOT / "data" / "fear_greed_index.csv")
    trades = pd.read_csv(ROOT / "data" / "historical_data.csv")
    return fear, trades


def build_summary(fear: pd.DataFrame, trades: pd.DataFrame) -> pd.DataFrame:
    fear = fear.copy()
    trades = trades.copy()
    fear["date"] = pd.to_datetime(fear["date"])
    trades["Timestamp"] = pd.to_datetime(trades["Timestamp"], unit="ms")
    trades["date"] = trades["Timestamp"].dt.normalize()
    for column in ["Closed PnL", "Size USD", "Fee"]:
        trades[column] = pd.to_numeric(trades[column], errors="coerce")

    merged = trades.merge(fear[["date", "classification"]], on="date", how="left")
    merged["win_trade"] = (merged["Closed PnL"] > 0).astype(int)

    return merged.groupby("classification", dropna=False).agg(
        total_trades=("Closed PnL", "count"),
        avg_pnl=("Closed PnL", "mean"),
        total_pnl=("Closed PnL", "sum"),
        avg_position_size=("Size USD", "mean"),
        win_rate=("win_trade", "mean"),
        avg_fee=("Fee", "mean"),
    ).reset_index().assign(win_rate=lambda df: df["win_rate"] * 100)


def main() -> None:
    fear, trades = load_data()
    summary = build_summary(fear, trades)
    output_dir = ROOT / "outputs"
    output_dir.mkdir(exist_ok=True)
    summary.to_csv(output_dir / "summary_metrics.csv", index=False)
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
