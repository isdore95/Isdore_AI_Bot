import yfinance as yf
import pandas as pd

def get_market_data(symbol="EURUSD=X", interval="1m", period="1d"):
    try:
        data = yf.download(
            symbol,
            interval=interval,
            period=period,
            progress=False,
            auto_adjust=True
        )

        if data.empty:
            raise Exception("No market data received.")

        return data

    except Exception as e:
        print("Market Error:", e)
        return pd.DataFrame()
