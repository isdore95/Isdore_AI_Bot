import pandas as pd

def trend_filter(data):
    if data.empty:
        return "SIDEWAYS"

    close = data["Close"].squeeze()

    ema50 = close.ewm(span=50).mean()
    ema200 = close.ewm(span=200).mean()

    if ema50.iloc[-1] > ema200.iloc[-1]:
        return "UP"

    elif ema50.iloc[-1] < ema200.iloc[-1]:
        return "DOWN"

    return "SIDEWAYS"
