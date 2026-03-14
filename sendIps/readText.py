import os
import subprocess
import re
import json


path = "/var/log/xray/access.log"
pathIps = "/root/bots/testBots/sendIps/ips.txt"

seen = {}


with open(pathIps, "r", encoding="utf-8") as db:
    seen = json.load(db)


with open(path, "r", encoding="utf-8") as f, \
     open(pathIps, "w", encoding="utf-8") as out:
    for line in f:
        if "accepted" in line and "from " in line:
            m = re.search(r'\bfrom\s+(\d{1,3}(?:\.\d{1,3}){3}):\d+.*?email:\s*(\S+)', line)
            if not m:
                continue

            ip = m.group(1)
            name = m.group(2)
            
            if name not in seen:
                seen[name] = {}
            
            if ip not in seen[name]:
                seen[name] = ip
    json.dump(seen, out, indent=2)
