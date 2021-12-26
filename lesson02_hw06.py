
#
count_goods = int(input("Укажите количество товаров: "))
good = dict.fromkeys(['Название','Цена', "Количество", "ед"]) # болванка товара
goods_list = []  # пустой список товаров
# Заполним структуру товаров
for i in range(count_goods):
    for key in good:
        value = input(f"Укажите {key} для {i+1} товара: ")
        if (key == 'Цена') or (key == "Количество"):
            good[key] = float(value)
        else:
            good[key] = value
        print(key)
    goods_list.append((i+1, good.copy()))

print(goods_list)

# Создаем словари характеристик
list_charct = [] # болванка для списка характеристик
# в качестве словаря характеристик будем использовать переменную good
for key in good:
    list_charct.clear()
    for i in range(count_goods):
        list_charct.append(goods_list[i][1][key])
    good[key] = list(set(list_charct))

print(good)





