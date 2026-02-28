import os
import subprocess
import re

path = "/var/log/xray/access.log"

seen = set()

with open("ips.txt", "r", encoding="utf-8") as db:
    for line in db:
        seen.add(line.strip())


with open(path, "r", encoding="utf-8") as f, \
     open("ips.txt", "a", encoding="utf-8") as out:
    for line in f:
        if "accepted" in line and "from " in line:
            m = re.search(r'\bfrom\s+(\d{1,3}(?:\.\d{1,3}){3}):\d+\b', line)
            if not m:
                continue

            ip = m.group(1)

            if ip not in seen:
                seen.add(ip)
                out.write(ip + "\n")

