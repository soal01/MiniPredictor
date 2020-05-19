import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '9c9d678684574becb181a16cb506c6f2'}
connection.request('GET', '/v2/competitions/BL1/matches/?matchday=22', None, headers)
response = json.loads(connection.getresponse().read().decode())

print(response)

str_response = json.dumps(response)
with open("Example.json", "w") as f:
    f.write(str_response)

# url ="https://api.football-data.org/v2/competitions/BL/matches?matchday=11"


