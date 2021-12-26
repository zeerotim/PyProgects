# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
print(f"Начальный список: {my_list}")
my_list.sort(reverse = True) # на всякий случай отсортируем по-убыванию, вдруг изначально не отсортирован
new_el = int(input("Введите новый элемент списка: "))

if new_el in my_list:
    ind = my_list.index(new_el)
    my_list.insert(ind, new_el)
else:
    # max_value = my_list[0]
    max_value = max(my_list)
    min_value = min(my_list)
    if new_el > max_value:
        my_list.insert(0, new_el)
    elif new_el < min_value:
        my_list.append(new_el)
    else:
        ind = 0
        while new_el < my_list[ind]:
            ind += 1
        my_list.insert(ind, new_el)
# Можно было вообще не париться с кучей уcловий, а просто добавить новый элемент в список (append)
# и отсортировать его по убыванию :)

print(my_list)