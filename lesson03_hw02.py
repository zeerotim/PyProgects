# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(name, surname, birth_year, city, email, phone):
    return {"Имя": name, "Фамилия": surname, "Год рождения": birth_year,
            "Город проживания": city, "email": email, "Телефон": phone}

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
birth_year = int(input('Введите год рождения: '))
city = input('Введите город проживания: ')
email = input('Введите email: ')
phone = input('Введите телефон: ')

user = user_data(surname=surname, name=name, birth_year=birth_year, email=email, phone=phone, city=city)
# специально поменяд порядок параметров функции, чтобы понять, что он не важен в поименованных аргументах
# print(user)
for key, value in user.items():
    print(f"{key}: {value}", end=" ")




