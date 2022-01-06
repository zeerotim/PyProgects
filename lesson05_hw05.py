"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random

len_list = int(input("Укажите количество элементов списка: "))
# сгенерим список чисел
my_list = random.sample(range(0,100), len_list) # только тут значения списка никогда не повторятся
print(f"исходный список: {my_list}")
# превратим список в строку наборов чисел, разделенных пробелом
str_list = " ".join(list(map(lambda x: str(x), my_list))).lstrip(" ")
print(f"строка исходного списка: {str_list}")

with open("hw05_rw.txt", 'w+', encoding="utf-8") as file_rw:
    # запишeм строку в файл
    print(str_list, file=file_rw)
    # прочитаем строку из файла и вычислим сумму элементов
    file_rw.seek(0) # на всякий случай
    text = file_rw.read().replace("\n", " ").strip(" ") # хм, пока не убрал перевод строки, последнее слово не превращалось в элемент списка
    print(f"строка из файла: {text}")
    text_list = text.split(" ")
    # приведем к числовому значению
    number_list = list(map(lambda x: int(x) if x.isdigit() else 0, text_list))

print(f"Конечный список из файла: {number_list}")
print(f"Сумма элементов списка: {sum(number_list)}")
