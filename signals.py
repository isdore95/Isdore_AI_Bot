import os
import requests
from risk import calculate_lot, expiry_time

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

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

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        },
        timeout=10
    )
