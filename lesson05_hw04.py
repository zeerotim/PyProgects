"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
# функция словаря чисел 0-9
def translete_numbers(number):
    dict = {1: ['one', 'один'],
            2: ['two', 'два'],
            3: ['three', 'три'],
            4: ['four', 'четыре'],
            5: ['five', 'пять'],
            6: ['six', 'шесть'],
            7: ['seven', 'семь'],
            8: ['eight', 'восемь'],
            9: ['nine', 'девять'],
            0: ['zero', 'ноль']}
    return dict[number]
# тест функции
# print(translete_numbers(5))

with open("hw04_read_file.txt", 'r', encoding="utf-8") as file_r, open("hw04_write_file.txt", 'w', encoding="utf-8") as file_w:

    for line in file_r:
        loc_line = line.replace("\n", "") # избавимся от переноса строк
        str_number_en, number = loc_line.split(" — ") # получим значения слева и справа от разделителя
        number = int(number.strip(" ")) if number.strip(" ").isdigit() else 0 # приведем к числу
        str_number_ru = translete_numbers(number)[1].capitalize()
        new_line = loc_line.replace(str_number_en, str_number_ru)
        print(new_line)
        print(new_line, file=file_w)
