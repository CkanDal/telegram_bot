import os
import subprocess
import re
import json


path = "/var/log/xray/access.log"
pathIps = "/root/bots/testBots/sendIps/ips.txt"

seen = {}


try:
    with open(pathIps, "r", encoding="utf-8") as db:
        seen = json.load(db)
except (FileNotFoundError, json.JSONDecodeError):
    pass
    
with open(path, "r", encoding="utf-8") as f:
    for line in f:
        if "accepted" in line and "from " in line:
            m = re.search(r'\bfrom\s+(\d{1,3}(?:\.\d{1,3}){3}):\d+.*?email:\s*(\S+)', line)
            if not m:
                continue

            ip = m.group(1)
            name = m.group(2)
            
            if name not in seen:
                seen[name] = []
            
            if ip not in seen[name]:
                seen[name].append(ip)
with open(pathIps, "w", encoding="utf-8") as out:
    json.dump(seen, out, indent=2, sort_keys=True)
