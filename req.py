import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKENSENDIP")

with open("/root/bots/testBots/sendIps/ips.txt", "r", encoding="utf-8") as ips:
    print(requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id=1648413619&text={ips.read()}").json())
