import numpy as np
import talib
from pprint import pprint
import plotly.graph_objects as go
import pandas as pd
from indicators.super_trend.super_trend import super_trend

def visual_super_trend(file_src:str):
    df = pd.read_csv(file_src)
    super_df = super_trend(df)
    res_df = df.join(super_df).tail(100)

    fig = go.Figure(data=[go.Candlestick(
        x=res_df['Date'],
        open=res_df['Open'],
        high=res_df['High'],
        low=res_df['Low'],
        close=res_df['Close'],
    )])

    # add lines
    fig.add_trace(go.Scatter(x=res_df['Date'], y=res_df['upper'], mode='lines', name='Upper Line'))
    fig.add_trace(go.Scatter(x=res_df['Date'], y=res_df['lower'], mode='lines', name='Lower Line'))

    fig.update_layout(width=1800, height=1800)
    fig.show()