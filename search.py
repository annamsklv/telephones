from constants import DATA_BASE
import csv


def search_by(atr: str, search_data: str):
    with open(DATA_BASE, "r", newline='', encoding='windows-1251') as csvfile:
        reader = csv.DictReader(csvfile, delimiter="|")
        data = []
        for row in reader:
            if search_data in row[atr]:
                data.append(row)
        for i in data:
            print(*i.values())
