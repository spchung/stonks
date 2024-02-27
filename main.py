import numpy as np
np.set_printoptions(threshold=np.inf)
from indicators.super_trend import visual_super_trend
from candle import get_candles_pattern, visualize_candle_patterns
from alpaca_util import get_crypto_historical_data
from alpaca.data.timeframe import TimeFrame
from datetime import datetime


def main():
    df = get_crypto_historical_data(
        ["BTC/USD"],
        timeframe=TimeFrame.Hour,
        start=datetime(2024,2,22),
        end=datetime(2024,2,27)
    )

    df.rename(columns={'index':'Date'}, inplace=True)
    df_with_candles = get_candles_pattern(df)
    visualize_candle_patterns(df_with_candles)

if __name__ == "__main__":
    main()