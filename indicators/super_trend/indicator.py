import talib
import numpy as np
import pandas as pd
import numpy as np

def super_trend(df, period=10, multiplier=3):
    '''
        Upper line = (high + low) / 2 + multiplier x ATR
        Lower Line = (high + low) / 2 – multiplier x ATR
    '''
    mul = multiplier
    ATR = talib.ATR(
        df['High'].to_numpy(), 
        df['Low'].to_numpy(), 
        df['Close'].to_numpy(), 
    timeperiod=period)

    final_upperband = upperband = (df['High'] + df['Low']) / 2 + mul * ATR
    final_lowerband = lowerband = (df['High'] + df['Low']) / 2 - mul * ATR

    supertrend = [True] * len(df)
    for i in range(1, len(df.index)):
        curr, prev = i, i-1
        # if current close price crosses above upperband
        if df['Close'][curr] > final_upperband[prev]:
            supertrend[curr] = True
        # if current close price crosses below lowerband
        elif df['Close'][curr] < final_lowerband[prev]:
            supertrend[curr] = False
        # else, the trend continues
        else:
            supertrend[curr] = supertrend[prev]
            # adjustment to the final bands
            if supertrend[curr] == True and final_lowerband[curr] < final_lowerband[prev]:
                final_lowerband[curr] = final_lowerband[prev]
            if supertrend[curr] == False and final_upperband[curr] > final_upperband[prev]:
                final_upperband[curr] = final_upperband[prev]
        # remove bands depending on the trend direction for visualization
        if supertrend[curr] == True:
            final_upperband[curr] = np.nan
        else:
            final_lowerband[curr] = np.nan

    return pd.DataFrame({
        'Super Trend': supertrend,
        'Upper Bound': final_upperband,
        'Lower Bound': final_lowerband,
    }, index = df.index)