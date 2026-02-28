import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKENSENDIP")

print(BOT_TOKEN)
with open("ips.txt", "r", encoding="utf-8") as ips:
    print(requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id=1648413619&text={ips.read()}").json())
