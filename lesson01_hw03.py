# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.

int_n = input("Введите чило n: ")
int_n = int(int_n)+int(int_n+int_n)+int(int_n+int_n+int_n)
print(F"Выражение n+nn+nnn = {int_n}")

# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

str_n = input("Введите целое чило n: ")
lenth_n = len(str_n)
i = 0
max_n = int(str_n[i])
while i < lenth_n-1:
    i += 1
    if max_n < int(str_n[i]):
        max_n = int(str_n[i])

print(f"Максимальное цифра в числе n = {max_n}")


