"""
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    def __init__(self, title: str):
        self.title = title
        print(f"Создан канцтовар: {self.title}")

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):
    def draw(self, color: str):
        print(f"{self.title} отрисовывает цвет {color}")


class Pencil(Stationery):
    def draw(self, color: str):
        print(f"Карандаш {self.title} отрисовывает цвет {color}")

class Handle(Stationery):
    def draw(self, color: str):
        print(f"Маркер {self.title} отрисовывает цвет {color}")

#  ничего особо в голову не лезет по поводу переопределения метода draw

stat = Stationery("Штрих")
stat.draw()

pen = Pen("Ручка шариковая")
pen.draw("синий")




