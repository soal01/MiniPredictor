metrics = ['Владение мячом', 'Удары по воротам', 'Удары в створ', 'Удары мимо', 'Заблокированные удары',
                   'Сэйвы', 'Фолы', 'Угловые удары', 'Штрафные удары', 'Вне игры', 'Удары от ворот',
                   'Автоголы', 'Забитые пенальти', 'Незабитые пенальти', 'Вбрасывания']


class SportsRu_parser:
    def __init__(self):
        self.start_id = 1347220
        self.end_id = 1347454
        self.current_str = ""

    def set_new_str(self, new_str):
        self.current_str = new_str

    def parse_value(self):
        balance = 0
        ind = 0
        while True:
            if self.current_str[ind] == '<':
                balance += 1
            if self.current_str[ind] == '>':
                balance -= 1
            if ('9' >= self.current_str[ind] >= '0') and balance == 0:
                break
            ind += 1
        self.current_str = self.current_str[ind:]
        value = self.current_str[:self.current_str.find('<')]
        self.current_str = self.current_str[self.current_str.find('<'):]
        return value

    def get_metric(self, name):
        self.current_str = self.current_str[self.current_str.find(name):]
        self.current_str = self.current_str[self.current_str.find('<'):]
        first_value = self.parse_value()
        second_value = self.parse_value()
        return first_value, second_value

    def parse_teams(self):
        self.current_str = self.current_str[self.current_str.find('<title>'):]
        self.current_str = self.current_str[7:]
        first_team = self.current_str[:self.current_str.find(' - ')]
        self.current_str = self.current_str[self.current_str.find(' - '):]
        self.current_str = self.current_str[3:]
        second_team = self.current_str[:self.current_str.find(':')]
        return first_team, second_team

    def parse_goals(self):
        self.current_str = self.current_str[self.current_str.find('matchboard__card-game'):]
        self.current_str = self.current_str[self.current_str.find('>') + 1:]
        value = self.current_str[:self.current_str.find('<')]
        return value

    def parse_score(self):
        first_value = self.parse_goals()
        second_value = self.parse_goals()
        first_value.strip()
        second_value.strip()
        return first_value, second_value

    def parse(self):
        ans = []
        first_team, second_team = self.parse_teams()
        ans.extend([first_team, second_team])
        first_value, second_value = self.parse_score()
        ans.extend([first_value, second_value])
        #print(first_team, second_team)
        #print(first_value, second_value)
        for metric in metrics:
            first_value, second_value = self.get_metric(metric)
            ans.extend([first_value, second_value])
            #print(first_value, second_value)
        return ans


'''parser = SportsRu_parser()
with open('example.html', 'r') as f:
    data = f.read()
parser.set_new_str(data)
parser.parse()'''