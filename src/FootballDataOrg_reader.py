import http.client
import json
import time

class FootballDataOrg_reader:
    def __init__(self):
        self.connection = http.client.HTTPConnection('api.football-data.org')
        self.headers = {'X-Auth-Token': '9c9d678684574becb181a16cb506c6f2'}

    def read_data(self, count_of_matchdays):
        for number_of_matchday in range(1, count_of_matchdays + 1):
            self.connection.request('GET', f'/v2/competitions/BL1/matches/?matchday={number_of_matchday}',
                               None, self.headers)
            response = json.loads(self.connection.getresponse().read().decode())
            if response.get('count', None) is None:
                time.sleep(11)
                self.connection.request('GET', f'/v2/competitions/BL1/matches/?matchday={number_of_matchday}',
                                        None, self.headers)
                response = json.loads(self.connection.getresponse().read().decode())

            str_response = json.dumps(response)
            with open(f"jsons/MatchDay{number_of_matchday}.json", "w") as f:
                f.write(str_response)
            print(f"{number_of_matchday} matchday rode")
            time.sleep(4)

    def getH2h(self, count_of_matchdays):
        list_of_H2H = []
        for number_of_matchday in range(1, count_of_matchdays + 1):
            with open(f"jsons/MatchDay{number_of_matchday}.json", "r") as f:
                data = json.loads(f.read())
            count_of_matches = data['count']
            for match in data['matches']:
                first_team = match['homeTeam']['name']
                second_team = match['awayTeam']['name']
                list_of_H2H.append((first_team, second_team))
        return list_of_H2H


# reader = FootballDataOrg_reader()
# reader.read_data(26)
# list_of_H2H = reader.getH2h(26)
#with open("h2h.txt", 'w') as f:
#    f.write(str(list_of_H2H))

with open("h2h.txt", 'r') as f:
    data = json.dumps(f.read())
counter = 0
for el in data:
    counter += 1
print(len(data), counter)
