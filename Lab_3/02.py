# TODO Напишите функцию find_common_participants

def find_common_participants(str_1, str_2, divider = ","):
    set_str_1 = set(str_1.split(divider))
    set_str_2 = set(str_2.split(divider))
    common_names = list(set_str_1.intersection(set_str_2))
    common_names.sort()

    return common_names

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, divider = "|"))


# TODO Провеьте работу функции с разделителем отличным от запятой
