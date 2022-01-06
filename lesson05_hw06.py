"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

import re

with open("hw06_r.txt", 'r', encoding="utf-8") as file_r:
    my_dict = {}
    for line in file_r:
        # получим список только чисел в строке при помощи re и типизируем элементы списка
        digits_list = list(map(lambda x: int(x), re.findall("\d+", line)))
        # получим ключ: первый элемент сплитованной строки
        my_dict[line.split(":")[0]] = sum(digits_list)

print(f"Результат: {my_dict}")


