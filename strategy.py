import pandas as pd

def calculate_signal(data):

    if data.empty:
        return "WAIT", 0

    close = data["Close"].squeeze()
    high = data["High"].squeeze()
    low = data["Low"].squeeze()

    ema20 = close.ewm(span=20).mean()
    ema50 = close.ewm(span=50).mean()

    delta = close.diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = (-delta.clip(upper=0)).rolling(14).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    macd = close.ewm(span=12).mean() - close.ewm(span=26).mean()
    macd_signal = macd.ewm(span=9).mean()

    resistance = high.tail(20).max()
    support = low.tail(20).min()

    price = float(close.iloc[-1])

    score_buy = 0
    score_sell = 0

    if ema20.iloc[-1] > ema50.iloc[-1]:
        score_buy += 1
    else:
        score_sell += 1

    if macd.iloc[-1] > macd_signal.iloc[-1]:
        score_buy += 1
    else:
        score_sell += 1

    if 45 < rsi.iloc[-1] < 70:
        score_buy += 1

    if 30 < rsi.iloc[-1] < 55:
        score_sell += 1

    if price > support:
        score_buy += 1

    if price < resistance:
        score_sell += 1

    confidence = max(score_buy, score_sell) * 25

    if score_buy >= 3:
        return "BUY", confidence

    if score_sell >= 3:
        return "SELL", confidence

    return "WAIT", 60
