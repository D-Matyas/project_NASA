import gspread
from collections import Counter


def get_worksheet():
    gc = gspread.service_account(filename='creds.json')
    sh = gc.open("astronauts")
    worksheet = sh.get_worksheet(0)
    return worksheet


def get_list_of_birth_months(worksheet):
    months = []
    data = worksheet.get_all_values()
    header = data[0]
    birth_date_index = header.index("Birth Date")
    for row in data[1:]:
        try:
            month = int(row[birth_date_index].split('/')[0])
            months.append(month)
        except (ValueError, IndexError):
            continue
    return months


def count_months_and_percentages(months):
    counter = Counter(months)
    most_common = counter.most_common(3)
    print(f'A leggyakrabban a(z) {most_common[0][0]}. hónap fordul elő '
          f'{round((most_common[0][1] / len(months)) * 100, 1)}%-os arányban')
    print(f'A második leggyakrabban a(z) {most_common[1][0]}. hónap fordul elő '
          f'{round((most_common[1][1] / len(months)) * 100, 1)}%-os arányban')
    print(f'A harmadik leggyakrabban a(z) {most_common[2][0]}. hónap fordul elő '
          f'{round((most_common[2][1] / len(months)) * 100, 1)}%-os arányban')


def main():
    print('A program kiírja, hogy a NASA űrhajósainak szülinapi hónapjai közül melyik a 3 leggyakoribb')
    count_months_and_percentages(get_list_of_birth_months(get_worksheet()))


main()
