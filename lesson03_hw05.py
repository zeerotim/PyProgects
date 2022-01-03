# Функция возвращает сумму элементов,
def sum_string(numbers:str, end_simb = "end"):
    list_numbers = numbers.split(' ')
    len_list = len(list_numbers)
    if len_list == 0:
        return 0, False

    if list_numbers[-1] == end_simb:
        # по-хорошему надо бы обработать возможный некорректный ввод нечисловых значений
        return sum(list(map(lambda x: int(x) if x.isdigit() else 0, list_numbers[:len_list-1]))), True
    else:
        return sum(list(map(lambda x: int(x) if x.isdigit() else 0, list_numbers))), False

# Основная программа

quit = False
summa = 0
while not quit:
    buf_summ, quit = sum_string(input('Введите строку чисел разделенную пробелом, для остановки напишите quit: '),
                                'quit')
    summa +=buf_summ
    print(f"Сумма введенных чисел: {summa}")


