import os
import requests
from risk import calculate_lot, expiry_time

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

print("BOT_TOKEN Loaded:", BOT_TOKEN is not None)
print("CHAT_ID Loaded:", CHAT_ID is not None)
def send_signal(signal, confidence):

    if not BOT_TOKEN or not CHAT_ID:
        print("Telegram credentials not found.")
        return

    lot = calculate_lot(confidence)
    expiry = expiry_time(confidence)

    message = f"""
🤖 ISDORE AI BOT

📊 Signal: {signal}

🎯 Confidence: {confidence}%

💰 Lot Size: {lot}

⏱ Expiry: {expiry}

✅ Generated Automatically
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        },
        timeout=10
    )

    print("Telegram Response:")
    print(response.text)
