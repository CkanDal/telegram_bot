import json
import re
import aiogram
from aiogram.filters import Command
from aiogram.types import Message
import subprocess

users = {}

pattern = re.compile(r"(?:user|inbound)>>>(.*?)>>>traffic>>>(.*)")

result = subprocess.run(
    ["xray", "api", "statsquery", "--server=127.0.0.1:10085"],
    capture_output=True,
    text=True
)


with open("/root/bots/testBots/jsonOutput.txt", "w", encoding="utf-8") as out:
    data = json.loads(result.stdout)
    stat = data['stat']
    for i in stat:
        value = i['value']
        name = i['name']
        m = pattern.search(name)
        if m:
            mbit = value * 8 / 1_000_000
            if m.group(1) not in users:
                users[m.group(1)] = {}
            users[m.group(1)][m.group(2)] =  f'{mbit:.2f} Mbit'
    out.write(json.dumps(users, indent=4))



