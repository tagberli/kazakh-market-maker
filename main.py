# Kazakh Market Maker Prototype — Dec 2025
# Kraken version (works in the US)

import ccxt
import pandas as pd
import numpy as np
from datetime import datetime

exchange = ccxt.kraken({
    'enableRateLimit': True
})

symbol = 'BTC/USD'
timeframe = '1m'
limit = 300

def fetch_ohlcv():
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def compute_spread(df):
    mid = (df['high'] + df['low']) / 2
    spread_bps = (df['high'] - df['low']) / mid * 10000
    return float(spread_bps.mean())

if __name__ == "__main__":
    print("Kazakh Market Maker — Prototype (Kraken)")
    df = fetch_ohlcv()
    avg_spread = compute_spread(df)
    print(f"Avg 1m spread (last {limit} candles): {avg_spread:.2f} bps")
