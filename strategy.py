
import pandas as pd

def calculate_signal(data):
    if data.empty:
        return "WAIT", 0

    close = data["Close"].squeeze()

    ema20 = close.ewm(span=20).mean()
    ema50 = close.ewm(span=50).mean()

    delta = close.diff()

    gain = delta.clip(lower=0).rolling(14).mean()
    loss = (-delta.clip(upper=0)).rolling(14).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    current20 = float(ema20.iloc[-1])
    current50 = float(ema50.iloc[-1])
    current_rsi = float(rsi.iloc[-1])

    confidence = 60

    if current20 > current50 and current_rsi < 70:
        confidence = 90
        return "BUY", confidence

    if current20 < current50 and current_rsi > 30:
        confidence = 90
        return "SELL", confidence

    return "WAIT", confidence
