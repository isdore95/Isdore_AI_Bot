from market import get_market_data
from strategy import calculate_signal
from signals import send_signal

print("====================================")
print("     ISDORE AI BOT STARTED")
print("====================================")

data = get_market_data()

if data.empty:
    print("No market data received.")
else:
    signal, confidence = calculate_signal(data)

    print(f"Signal: {signal}")
    print(f"Confidence: {confidence}%")

    if signal != "WAIT":
        send_signal(signal, confidence)
        print("Signal sent to Telegram.")
    else:
        print("No trading opportunity.")
