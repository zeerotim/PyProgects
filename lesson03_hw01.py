# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(a:int, b:int):
    if b == 0:
        print("Ошибка: Деление на 0 ")
        return
    return a/b

try:
    a = int(input("Введе делимое a: "))
    b = int(input("Введе делитель b: "))
    print(f"{a}/{b} = {division(a, b)}")
except:
    print("Введено нечисловое значение")



