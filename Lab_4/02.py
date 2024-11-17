# TODO импортировать необходимые молули

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

# TODO считать содержимое csv файла

    with open(INPUT_FILENAME) as f:
        data = [inf for inf in csv.DictReader(f)] # считываем содержимое файла используя cписковое включение

# TODO Сериализовать в файл с отступами равными 4

    with open(OUTPUT_FILENAME, "w") as f: #создаем / перезаписываем файл
        json.dump(data, f, indent=4) # собственно сама запись в файл

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
