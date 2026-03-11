def get_ips() -> str:
     with open("ips.txt", 'r', encoding="utf-8") as ips:
         text = ips.read()
     return text
