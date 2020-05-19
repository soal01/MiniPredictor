import requests
import json

req = requests.get('https://www.sports.ru/football/match/augsburg-vs-wolfsburg/')
print(req.status_code)
print(req.content)
with open("example.html", "w") as f:
    f.write(req.content.decode())


