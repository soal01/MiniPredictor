import requests
import json

req = requests.get('https://www.sports.ru/football/match/1347220/stat/')
print(req.status_code)
print(req.content)
with open("example1.html", "w") as f:
    f.write(req.content.decode())


