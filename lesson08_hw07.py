"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""

class Complex:
    def __init__(self, x = 0.0, y = 0.0):
        self.x, self.y = x, y

    # изменим строковое представление
    def __str__(self):
        if self.x == 0 and self.y == 0:
            return "0"
        elif self.x != 0 and self.y == 0:
            return f"{self.x}"
        elif self.x == 0 and self.y != 0:
            return f"{self.y}i"
        elif self.y > 0:
            return f"{self.x}+{self.y}i"
        elif self.y < 0:
            return f"{self.x}{self.y}i"

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Complex(self.x*other.x-self.y*other.y, self.x*other.y+self.y*other.x)

    def __truediv__(self, other):
        return Complex((self.x*other.x+self.y*other.y)/(other.x**2+other.y**2),
                       (self.y*other.x-self.x*other.y)/(other.x**2+other.y**2))

# проверка работы класса

a = Complex(10, 4)
b = Complex(5, 2)

print(b)
print(a+b)
print(a*b)
print(a/b)
