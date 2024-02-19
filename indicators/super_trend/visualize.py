import pandas as pd
import plotly.graph_objects as go
from indicators.super_trend.indicator import super_trend

def visual_super_trend(file_src:str, last_n_days:int=100):
    df = pd.read_csv(file_src)
    super_df = super_trend(df)
    res_df = df.join(super_df)
    if last_n_days < res_df.shape[0]:
        res_df = res_df.tail(last_n_days)

    fig = go.Figure(data=[go.Candlestick(
        x=res_df['Date'],
        open=res_df['Open'],
        high=res_df['High'],
        low=res_df['Low'],
        close=res_df['Close'],
    )])

    # add lines
    fig.add_trace(go.Scatter(x=res_df['Date'], y=res_df['Upper Bound'], mode='lines', name='Upper Line'))
    fig.add_trace(go.Scatter(x=res_df['Date'], y=res_df['Lower Bound'], mode='lines', name='Lower Line'))

    fig.update_layout(width=1500, height=1500)
    fig.show()