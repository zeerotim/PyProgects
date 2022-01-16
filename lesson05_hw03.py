"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open("text_file_hw03.txt", 'r', encoding="utf-8") as file_obj:
    # сначала хотел запихать все содержисое фала в одну переменную и работать с ней,
    # но потом решил, что построковое чтение должно быть менее емким для памяти
        # text = file_obj.readlines()
        # print(text)
        # # file_obj.seek(0)
        # for line in text[1:]:
        #     print(line)
        # избавимся от переноса строк
        # text = list(map(lambda x: x.replace("\n", ""), text))
        # print(text)

    # попробуем все сделать за 1 проход цикла
    list_names_less20k = []
    sum_salary = 0
    for i, line in enumerate(file_obj):
        if i == 0: continue # пропустим первую строку файла, т.к. там заголовок
        name, salary = line.split(",")
        # приведем значение оклада к числу: очистим от переноса строк и пробелов, проверим на число
        salary = int(salary.replace("\n", "").strip(" ")) if salary.replace("\n", "").strip(" ").isdigit() else 0
        print(i, name, salary)
        sum_salary += salary
        if salary < 20000:
            list_names_less20k.append(name)
        # print(line)]
print(f"Сотрудники с окладом менее 20000: {list_names_less20k}")
print(f"Среднее значение окладов сотрудников: {sum_salary/i}")



