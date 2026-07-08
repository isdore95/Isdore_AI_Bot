from market import get_market_data
from strategy import calculate_signal
from signals import send_signal
from risk import calculate_lot, expiry_time

print("=" * 40)
print("     ISDORE AI BOT STARTED")
print("=" * 40)

data = get_market_data()

if data.empty:
    print("No market data received.")
else:
    signal, confidence = calculate_signal(data)

    lot = calculate_lot(confidence)
    expiry = expiry_time(confidence)

    print(f"Signal     : {signal}")
    print(f"Confidence : {confidence}%")
    print(f"Lot Size   : {lot}")
    print(f"Expiry     : {expiry}")

    send_signal(signal, confidence)
    print("Telegram signal sent.")
