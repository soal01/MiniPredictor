import http.client
import json
import time

class FootballDataOrg_reader:
    def __init__(self):
        self.connection = http.client.HTTPConnection('api.football-data.org')
        self.headers = {'X-Auth-Token': '9c9d678684574becb181a16cb506c6f2'}

    def read_data(self):
        for number_of_matchday in range(1, 20):
            self.connection.request('GET', f'/v2/competitions/BL1/matches/?matchday={number_of_matchday}',
                               None, self.headers)
            response = json.loads(self.connection.getresponse().read().decode())
            str_response = json.dumps(response)
            with open(f"jsons/MatchDay{number_of_matchday}.json", "w") as f:
                f.write(str_response)
            time.sleep(4)


reader = FootballDataOrg_reader()
reader.read_data()