# TODO решите задачу

import json #подключаем модуль
FILE = 'input.json' #путь к файлу, в данном случае лежит в папке проекта

def task() -> float:
    with open(FILE) as f: # открываем используя менеджер
        data = json.load(f)
        summ = sum([item["score"] * item["weight"] for item in data]) #вычисляем используя cписковое включение
    return round(summ, 3)

print(task())