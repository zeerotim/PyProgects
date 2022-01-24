"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
import re

class MyData:
    parts_of_data = ['day', 'month', 'year']
    def __init__(self, str_data: str):
        self.str_data = str_data
        #  изначально моя регулярка
        # if not re.match(r'^[0-3]\d-[0-1][0-2]-\d{4}$', self.str_data):
        # скопировал, и немного упростил эту регулярку
        # if not re.match(r'^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$', self.str_data):
        if not re.match(r'^(0?[1-9]|[12][0-9]|3[01])-(0?[1-9]|1[012])-\d{4}$', self.str_data):
            print(f'Параметр str_data ={str_data} не соответствует формату даты')

    @classmethod
    def get_number(cls, str_data: str, part_of_data = "year"):
        num_list = list(map(lambda x: int(x), str_data.split('-')))
        dict_data = dict(zip(cls.parts_of_data, num_list))
        return dict_data[part_of_data]

    @staticmethod
    def valid_number(num_of_part, part_of_data = "month"):
        # num_of_part = MyData.get_number(part_of_data)
        if part_of_data == 'day' and (num_of_part >31 or num_of_part < 1):
            print(f"День {num_of_part}, не может быть больше 31 и меньше 1")

        elif part_of_data == 'month' and (num_of_part >12 or num_of_part < 1):
            print(f"Месяц {num_of_part}, не может быть больше 12 и меньше 1")


my_data = MyData("32-12-2002")

print(my_data.get_number(my_data.str_data, "month"))

my_data.valid_number(my_data.get_number(my_data.str_data, "number"), "number")
my_data.valid_number(my_data.get_number(my_data.str_data, "month"), "month")
