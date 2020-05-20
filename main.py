
from src.sportsRu_parser import SportsRu_parser
from src.sportsRu_recorder import SportsRu_recorder


parser = SportsRu_parser()
recorder = SportsRu_recorder()
with open('src/example.html', 'r') as f:
    data = f.read()
parser.set_new_str(data)
row = parser.parse()
df = recorder.convert_to_dataframe(row)
print(df)
