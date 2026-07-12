from market import get_market_data
from strategy import calculate_signal
from signals import send_signal
from trend import trend_filter
from risk import calculate_lot, expiry_time

print("=" * 40)
print("     ISDORE AI BOT STARTED")
print("=" * 40)

data = get_market_data()

if data.empty:
    print("No market data received.")

else:
    trend = trend_filter(data)

    signal, confidence = calculate_signal(data)

    if trend == "UP" and signal == "SELL":
        signal = "WAIT"

    elif trend == "DOWN" and signal == "BUY":
        signal = "WAIT"

    lot = calculate_lot(confidence)
    expiry = expiry_time(confidence)

    print(f"Trend      : {trend}")
    print(f"Signal     : {signal}")
    print(f"Confidence : {confidence}%")
    print(f"Lot Size   : {lot}")
    print(f"Expiry     : {expiry}")

    if signal != "WAIT":
        send_signal(signal, confidence)
        print("Telegram signal sent.")
    else:
        print("No trade setup found.")
