import numpy as np
np.set_printoptions(threshold=np.inf)
from indicators.super_trend import visual_super_trend
from candle import get_candles_pattern, visualize_candle_patterns
from alpaca_util import get_crypto_historical_data
from alpaca.data.timeframe import TimeFrame
from datetime import datetime
from candlestick import candlestick


def main():
    df = get_crypto_historical_data(
        ["BTC/USD"],
        timeframe=TimeFrame.Day,
        start=datetime(2024,1,1),
        end=datetime(2024,2,28)
    )

    patterns_dict = {
        "InvHammer": candlestick.inverted_hammer,
        "BullEngulf": candlestick.bullish_engulfing,
        "BearEngulf": candlestick.bearish_engulfing,
        "MorningStar": candlestick.morning_star,
        "Hammer": candlestick.hammer,
    }

    df.rename(columns={'index':'Date'}, inplace=True)

    for pattern, func in patterns_dict.items():
        df = func(df, target=pattern)
    
    

if __name__ == "__main__":
    main()