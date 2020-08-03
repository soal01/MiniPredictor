
from src.sportsRu_parser import SportsRu_parser
from src.sportsRu_recorder import SportsRu_recorder
from src.sportsRu_reader import SportsRu_reader
'''
загрузка страниц для парсинга

reader = SportsRu_reader()
reader.download()
print(reader.list_of_missed_matches)
'''

'''парсинг и запись в csv'''
parser = SportsRu_parser()
recorder = SportsRu_recorder('src/BL_matches.csv')
rows = parser.parse_files()
recorder.write_rows(rows)
