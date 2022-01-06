"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json
import re


firms_dict = {}
average_profit = 0
average_quantity = 0
with open("hw07_firms.txt", 'r', encoding="utf-8") as file_r:
    for i, line in enumerate(file_r):
        if i == 0: continue  # пропустим первую строку файла, т.к. там заголовок
        # получим список только чисел в строке при помощи re и типизируем элементы списка
        digits_list = list(map(lambda x: int(x), re.findall("\d+", line)))
        profit = digits_list[0] - digits_list[1]
        if profit > 0:
            average_profit += profit
            average_quantity += 1
        # получим ключ: первый элемент сплитованной строки
        firms_dict[line.split(" ")[0]] = profit

average_profit = average_profit/average_quantity if average_quantity > 0 else 0
result = [firms_dict, dict(average_profit=average_profit)]
print(result)

with open("hw07_firms_profit.json", "w+", encoding="utf-8") as write_f:
    # Серриализуем результат
    json.dump(result, write_f)
    # хм, чет не нравится json-у кириллица :(
    write_f.seek(0)
    print(write_f.read())

    # попробуем дессериализовать и посмотрим на буквы... типа все ок :)
    write_f.seek(0)
    data = json.load(write_f)
    print(data)
    print(type(data))

