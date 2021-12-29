# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

#  сделаем более универсальную функцию, не с 3-мя аргументами, а с произвольным количеством
def my_func(*args):
    list_args = list(args)
    list_args.sort(reverse=True) # первые 2 элемента списка и будут максимальными значениями
    len_list = len(list_args)
    if len_list == 0:
        return 0
    elif len_list == 1:
        return float(list_args[0])
    else:
        return float(list_args[0])+float(list_args[1])

print(my_func(23, 324, 234))

# print(my_func())