numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

first_sub_number = numbers[0:4] # список до неизвестного
second_sub_number = numbers[5:] # список после неизвестного
chislo = (sum(first_sub_number) + sum(second_sub_number)) / len(numbers) # среднее по списку numbers
numbers[4] = chislo # замена на среднее

print("Измененный список:", numbers)


