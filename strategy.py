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

    macd = close.ewm(span=12).mean() - close.ewm(span=26).mean()
    signal = macd.ewm(span=9).mean()

    current20 = float(ema20.iloc[-1])
    current50 = float(ema50.iloc[-1])
    current_rsi = float(rsi.iloc[-1])
    current_macd = float(macd.iloc[-1])
    current_signal = float(signal.iloc[-1])

    if (
        current20 > current50
        and current_rsi < 70
        and current_macd > current_signal
    ):
        return "BUY", 95

    if (
        current20 < current50
        and current_rsi > 30
        and current_macd < current_signal
    ):
        return "SELL", 95

    return "WAIT", 60
