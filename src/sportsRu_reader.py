import requests


class SportsRu_reader:
    def __init__(self):
        self.start_id = 1347220
        self.end_id = 1347454
        self.list_of_missed_matches = range(self.start_id, self.end_id + 1)

    def download_match(self, id):
        url = f"https://www.sports.ru/football/match/{id}/stat/"
        req = requests.get(url)
        if req.status_code == 200:
            with open(f"html_files/{id}.html", "w") as f:
                f.write(req.content.decode())
            print(id, "successfully downloaded")
            return 0
        else:
            return id

    def download(self):
        new_list_of_missed_matches = []
        for id in self.list_of_missed_matches:
            status = self.download(id)
            if status:
                new_list_of_missed_matches.append(id)
        self.list_of_missed_matches = new_list_of_missed_matches


