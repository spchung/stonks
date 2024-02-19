import numpy as np
import talib
from pprint import pprint
import plotly.graph_objects as go
import pandas as pd

from indicators.super_trend import super_trend, visual_super_trend
np.set_printoptions(threshold=np.inf)

def main():
    visual_super_trend('data/bitcoin.csv', last_n_days=300)

if __name__ == "__main__":
    main()