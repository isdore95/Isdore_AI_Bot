import pandas as pd
from patterns import bullish_engulfing, bearish_engulfing, pin_bar

def calculate_signal(data):

    if data.empty:
        return "WAIT", 0

    close = data["Close"].squeeze()
    high = data["High"].squeeze()
    low = data["Low"].squeeze()
    open_price = data["Open"].squeeze()

    ema20 = close.ewm(span=20).mean()
    ema50 = close.ewm(span=50).mean()

    macd = close.ewm(span=12).mean() - close.ewm(span=26).mean()
    macd_signal = macd.ewm(span=9).mean()

    delta = close.diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = (-delta.clip(upper=0)).rolling(14).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    tr1 = high - low
    tr2 = (high - close.shift()).abs()
    tr3 = (low - close.shift()).abs()

    atr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1).rolling(14).mean()

    support = low.tail(20).min()
    resistance = high.tail(20).max()

    price = float(close.iloc[-1])

    score_buy = 0
    score_sell = 0

    reason = []

    # EMA Trend
    if ema20.iloc[-1] > ema50.iloc[-1]:
        score_buy += 20
        reason.append("EMA Bullish")
    else:
        score_sell += 20
        reason.append("EMA Bearish")

    # MACD
    if macd.iloc[-1] > macd_signal.iloc[-1]:
        score_buy += 20
        reason.append("MACD Bullish")
    else:
        score_sell += 20
        reason.append("MACD Bearish")

    # RSI
    if 50 <= rsi.iloc[-1] <= 70:
        score_buy += 15

    if 30 <= rsi.iloc[-1] <= 50:
        score_sell += 15

    # Support / Resistance
    if price > support:
        score_buy += 15

    if price < resistance:
        score_sell += 15

    # ATR
    if atr.iloc[-1] > atr.tail(10).mean():
        score_buy += 10
        score_sell += 10

    # Candlestick Patterns
    if bullish_engulfing(data):
        score_buy += 20
        reason.append("Bullish Engulfing")

    if bearish_engulfing(data):
        score_sell += 20
        reason.append("Bearish Engulfing")

    candle = pin_bar(data)

    if candle == "BULLISH":
        score_buy += 10
        reason.append("Bullish Pin Bar")

    if candle == "BEARISH":
        score_sell += 10
        reason.append("Bearish Pin Bar")

    confidence = max(score_buy, score_sell)

    if score_buy >= 70:
        return "BUY", confidence

    if score_sell >= 70:
        return "SELL", confidence

    return "WAIT", confidence
