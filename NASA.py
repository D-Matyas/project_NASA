from collections import Counter


def get_astronauts():
    with open('astronauts.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


def get_birth_months(lines):
    months = []
    for line in lines[1:]:
        parts = line.strip().split(",")
        if len(parts) >= 5:
            birth_date = parts[4]
            months.append(birth_date.strip().split("/")[0])
    return months


def count_most_common(months):
    counter = Counter(months)
    most_common = counter.most_common(3)
    print(f'A leggyakrabban a(z) {most_common[0][0]}. hónap fordul elő '
          f'{round((most_common[0][1] / len(months)) * 100, 1)}%-os arányban')
    print(f'A második leggyakrabban a(z) {most_common[1][0]}. hónap fordul elő '
          f'{round((most_common[1][1] / len(months)) * 100, 1)}%-os arányban')
    print(f'A harmadik leggyakrabban a(z) {most_common[2][0]}. hónap fordul elő '
          f'{round((most_common[2][1] / len(months)) * 100, 1)}%-os arányban')


def main():
    count_most_common(get_birth_months(get_astronauts()))


main()
