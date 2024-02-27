from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime
import pandas as pd
from alpaca.data.historical import CryptoHistoricalDataClient

# No keys required for crypto data
client = CryptoHistoricalDataClient()

def get_crypto_historical_data(
  symbol_or_symbols: list[str],
  timeframe: TimeFrame,
  start: datetime,
  end: datetime
) -> pd.DataFrame:
  request = CryptoBarsRequest(
    symbol_or_symbols=symbol_or_symbols,
    timeframe=timeframe,
    start=start,
    end=end
  )

  bars = client.get_crypto_bars(request) # add 'timestamp' column
  df = bars.df
  
  df['timestamp'] = df.index.get_level_values(1)
  # df.reset_index(level=1, inplace=True)
  return df
