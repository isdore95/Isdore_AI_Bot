
import pandas as pd

def calculate_signal(data):

    if data.empty:
        return "WAIT", 0

    close = data["Close"].squeeze()

    ema20 = close.ewm(span=20).mean()
    ema50 = close.ewm(span=50).mean()

    current20 = float(ema20.iloc[-1])
    current50 = float(ema50.iloc[-1])

    if current20 > current50:
        return "BUY", 85

    elif current20 < current50:
        return "SELL", 85

    else:
        return "WAIT", 50
