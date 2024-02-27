import os
import sys
from itertools import compress

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import talib
from data.get_data import get_data
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from .utils import candle_rankings

def get_candles_pattern(df:pd.DataFrame, last_n_period:int=100):
    candle_names = talib.get_function_groups()['Pattern Recognition']
    
    # date = df['timestamp']
    op = df['open']
    hi = df['high']
    lo = df['low']
    cl = df['close']
    # create columns for each pattern
    for candle in candle_names:
        # PATTERN RECOGNITION
        df[candle] = getattr(talib, candle)(op, hi, lo, cl)

    df['candlestick_pattern'] = np.nan
    df['candlestick_match_count'] = np.nan
    
    for index, row in df.iterrows():
        # no pattern found
        if len(row[candle_names]) - sum(row[candle_names] == 0) == 0:
            df.loc[index,'candlestick_pattern'] = "NO_PATTERN"
            df.loc[index, 'candlestick_match_count'] = 0
        
        # single pattern found
        elif len(row[candle_names]) - sum(row[candle_names] == 0) == 1:
            # bull pattern 100 or 200
            if any(row[candle_names].values > 0):
                pattern = list(compress(row[candle_names].keys(), row[candle_names].values != 0))[0] + '_Bull'
            # bear pattern -100 or -200
            else:
                pattern = list(compress(row[candle_names].keys(), row[candle_names].values != 0))[0] + '_Bear'
            
            if pattern in candle_rankings:
            # if pattern in all_candle_rankigs:
                df.loc[index, 'candlestick_pattern'] = pattern
                df.loc[index, 'candlestick_match_count'] = 1
            else:
                df.loc[index, 'candlestick_pattern'] = "NO_PATTERN"
                df.loc[index, 'candlestick_match_count'] = 0

        # multiple patterns matched -- select best performance
        else:
            # filter out pattern names from bool list of values
            patterns = list(compress(row[candle_names].keys(), row[candle_names].values != 0))
            container = []
            for pattern in patterns:
                if row[pattern] > 0:
                    container.append(pattern + '_Bull')
                else:
                    container.append(pattern + '_Bear')
            rank_list = [candle_rankings[p] for p in container if p in candle_rankings]
            # rank_list = [candle_rankings[p] for p in container]
            if len(rank_list) == len(container):
                rank_index_best = rank_list.index(min(rank_list))
                df.loc[index, 'candlestick_pattern'] = container[rank_index_best]
                df.loc[index, 'candlestick_match_count'] = len(container)
    # clean up candle columns
    df.drop(candle_names, axis = 1, inplace = True)
    return df