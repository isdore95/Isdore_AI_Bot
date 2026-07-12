import pandas as pd

def calculate_signal(data):

    if data.empty:
        return "WAIT", 0

    close = data["Close"].squeeze()
    high = data["High"].squeeze()
    low = data["Low"].squeeze()

    ema20 = close.ewm(span=20).mean()
    ema50 = close.ewm(span=50).mean()

    macd = close.ewm(span=12).mean() - close.ewm(span=26).mean()
    macd_signal = macd.ewm(span=9).mean()

    delta = close.diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = (-delta.clip(upper=0)).rolling(14).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    tr = pd.concat([
        high - low,
        (high - close.shift()).abs(),
        (low - close.shift()).abs()
    ], axis=1).max(axis=1)

    atr = tr.rolling(14).mean()

    resistance = high.tail(20).max()
    support = low.tail(20).min()

    price = float(close.iloc[-1])

    score_buy = 0
    score_sell = 0

    if ema20.iloc[-1] > ema50.iloc[-1]:
        score_buy += 25
    else:
        score_sell += 25

    if macd.iloc[-1] > macd_signal.iloc[-1]:
        score_buy += 20
    else:
        score_sell += 20

    if 50 < rsi.iloc[-1] < 70:
        score_buy += 15

    if 30 < rsi.iloc[-1] < 50:
        score_sell += 15

    if price > support:
        score_buy += 15

    if price < resistance:
        score_sell += 15

    if atr.iloc[-1] > atr.tail(10).mean():
        score_buy += 10
        score_sell += 10

    confidence = max(score_buy, score_sell)

    if score_buy >= 70:
        return "BUY", confidence

    if score_sell >= 70:
        return "SELL", confidence

    return "WAIT", confidence
