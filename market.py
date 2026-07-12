import yfinance as yf
import pandas as pd

def get_market_data(symbol="EURUSD=X", interval="1m", period="5d"):
    try:
        data = yf.download(
            symbol,
            interval=interval,
            period=period,
            progress=False,
            auto_adjust=True,
            threads=False
        )

        if data.empty:
            return pd.DataFrame()

        return data.dropna()

    except Exception as e:
        print(e)
        return pd.DataFrame()
