"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""

# Объявление классов
class Car:
    def __init__(self, name, color, is_police = False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Создан новый {'полицейский' if self.is_police else ''} автомобиль: {self.name}, цвет: {self.color}")

    def go(self):
        print(f"{'Полицейский автомобиль' if self.is_police else 'Автомобиль'} {self.name} цвет {self.color} едет cо скоростью {self.speed} км/ч")

    def stop(self):
        print(f"{'Полицейский автомобиль' if self.is_police else 'Автомобиль'} {self.name} цвет {self.color} остановился со скорости", self.speed)

    def turn(self, direction: str):
        print(f"{'Полицейский автомобиль' if self.is_police else 'Автомобиль'} {self.name} цвет {self.color} повернул ", direction)

    def show_speed(self):
        print(f"Текущая скорость автомобиля:", self.name, self.speed, "км/ч")


class TownCar(Car):
    def show_speed(self):
        print(f"Текущая скорость автомобиля:", self.name, self.speed, "км/ч",
              ",превышено ограничение 60 км/ч" if self.speed > 60 else "")


class WorkCar(Car):
    def show_speed(self):
        print(f"Текущая скорость автомобиля:", self.name, self.speed, "км/ч",
              ",превышено ограничение 40 км/ч" if self.speed > 40 else "")


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, True)

#  Сам скрипт

toyota = Car("Тойота", "Синий")
toyota.speed = 80
toyota.go()
toyota.turn("Налево")
toyota.speed = 90
toyota.show_speed()
toyota.stop()

truck = WorkCar("Камаз", "Оранжевый")
truck.speed = 80
truck.go()
truck.show_speed()

pol_car = PoliceCar("Шкода", "Бело-синний")
pol_car.speed = 180
pol_car.go()
pol_car.turn("Направо")
pol_car.speed = 190
pol_car.show_speed()