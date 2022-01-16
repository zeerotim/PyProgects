"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("text_file_hw02.txt", 'r', encoding="utf-8") as file_obj:
    list_of_str = file_obj.readlines()
    print(list_of_str)
    print(f"Количество строк в файле {file_obj.name}: {len(list_of_str)}")
    # оказались в конце файла, перенесемся в начало
    file_obj.seek(0)
    # прочитаем файл целиком и избавимся от переноса строк, заменим их на пробел, обрежем лишние пробелы
    # , и разобьем строку
    list_of_text = file_obj.read().replace("\n", " ").strip(" ").split(" ")
    print(list_of_text)
    print(f"Количество слов в файле {file_obj.name}: {len(list_of_text)}")