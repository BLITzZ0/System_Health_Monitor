import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Loads BOT_TOKEN and ROOM_ID from .env

BOT_TOKEN = os.getenv("BOT_TOKEN")
ROOM_ID = os.getenv("ROOM_ID")

def send_webex_alert(bot_token, room_id, message):
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {bot_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "roomId": room_id,
        "text": message
    }
    response = requests.post(url, headers=headers, json=payload)
    print("Status:", response.status_code)
    print(response.text)

send_webex_alert(BOT_TOKEN, ROOM_ID, "System Health Monitor Test Message")
