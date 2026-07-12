import pandas as pd

def get_trend(close):

    ema20 = close.ewm(span=20).mean()
    ema50 = close.ewm(span=50).mean()
    ema200 = close.ewm(span=200).mean()

    if (
        ema20.iloc[-1] > ema50.iloc[-1]
        and ema50.iloc[-1] > ema200.iloc[-1]
    ):
        return "UP"

    if (
        ema20.iloc[-1] < ema50.iloc[-1]
        and ema50.iloc[-1] < ema200.iloc[-1]
    ):
        return "DOWN"

    return "SIDEWAYS"
