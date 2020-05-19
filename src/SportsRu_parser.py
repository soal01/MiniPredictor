import requests


class SportsRu_parser:
    def __init__(self):
        self.start_id = 1347220
        self.end_id = 1347454

    def parse_file(self, name):
        with open(name, 'r') as f:
            data = f.read()
        print(data)
        data = data[data.find('Владение мячом</'):]
        data = data[118:]
        data1 = data[:2]
        data = data[370:]
        data2 = data[:2]
        data = data[data.find('Удары по воротам</'):]
        data = data[120:]
        data3 = data[:data.find('<')]
        print(data)
        data = data[data.find('<'):]
        ind = 0
        for i in range(368):
            if data[i] == '<':
                ind +=1
            if data[i] == '>':
                ind -=1
        # индекс должен равняться 0
        print('ind=', ind)
        print(data)
        data = data[367:]
        data4 = data[:data.find('<')]
        print(data)
        print("poleznaya data", data1, data2, data3, data4)


parser = SportsRu_parser()
parser.parse_file('example.html')
