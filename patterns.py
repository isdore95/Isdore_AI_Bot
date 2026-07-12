def bullish_engulfing(data):

    if len(data) < 2:
        return False

    prev = data.iloc[-2]
    curr = data.iloc[-1]

    return (
        prev["Close"] < prev["Open"]
        and curr["Close"] > curr["Open"]
        and curr["Open"] < prev["Close"]
        and curr["Close"] > prev["Open"]
    )


def bearish_engulfing(data):

    if len(data) < 2:
        return False

    prev = data.iloc[-2]
    curr = data.iloc[-1]

    return (
        prev["Close"] > prev["Open"]
        and curr["Close"] < curr["Open"]
        and curr["Open"] > prev["Close"]
        and curr["Close"] < prev["Open"]
    )


def pin_bar(data):

    if len(data) < 1:
        return None

    candle = data.iloc[-1]

    body = abs(candle["Close"] - candle["Open"])
    upper = candle["High"] - max(candle["Close"], candle["Open"])
    lower = min(candle["Close"], candle["Open"]) - candle["Low"]

    if lower > body * 2 and upper < body:
        return "BULLISH"

    if upper > body * 2 and lower < body:
        return "BEARISH"

    return None
