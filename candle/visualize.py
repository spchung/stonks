import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import plotly.graph_objs as go
import pandas as pd
from candle.utils import candle_alias

def visualize_candle_patterns(df: pd.DataFrame):
  fig = go.Figure(data=[go.Candlestick(x=df['timestamp'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

  # Add annotations based on values in the DataFrame
  for index, row in df.iterrows():
    if row['candlestick_pattern'] != 'NO_PATTERN' and row['candlestick_match_count'] > 0:
      text = row['candlestick_pattern']
      if row['candlestick_pattern'] in candle_alias:
        text = candle_alias[row['candlestick_pattern']]
      fig.add_annotation(x=row['timestamp'], y=row['high'], text=text, showarrow=True)

  # Update layout if needed
  fig.update_layout(title='Candlestick Chart with Annotations')

  # Show plot
  fig.show()