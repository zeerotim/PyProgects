"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
from functools import reduce

class Matrix:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        str_array = ""
        for el in self.array:
            str_array += reduce(lambda x,y: str(x)+" "+str(y), el)+"\n"
        return str_array

    def __add__(self, other):
        if len(self.array) != len(other.array):
            print("Неравные размерности матриц")
            return
        new_array = []
        for i in range(len(self.array)):
            if len(self.array[i]) != len(other.array[i]):
                print("Неравные размерности матриц")
                return
            new_array.append(list(map(lambda x, y: x + y, self.array[i], other.array[i])))
        return Matrix(new_array)


# инициируем списки списков
ll1 = [[1,2],[3,2]]
ll2 = [[3,3],[1,1]]

# получаем экземплары классов
a = Matrix(ll1)
b = Matrix(ll2)

c = a + b

print(a)
print(b)
print(c)
