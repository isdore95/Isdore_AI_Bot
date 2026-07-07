import requests
from config import BOT_TOKEN, CHAT_ID

def send_signal(signal, confidence):

    message = f"""
🤖 ISDORE AI BOT

Signal: {signal}

Confidence: {confidence}%

Pair: EUR/USD
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )
