"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""
from builtins import float


class Road:
    #класс дорога с атрибутами длина и ширина в м.
    def __init__(self, _length: float, _width: float):
        self._length = _length
        self._width = _width
        print(f"Создана дорога, длиной: {self._length} м., шириной: {self._width} м.")

    def mass_asphalt(self, height: float): # толщину асфальта указываем в метрах
        return self._width*self._length*height*25

road_1 = Road(_length=1000, _width=15)
height = float(input("Укажите толщину асфальта (м): "))
print(f"Масса асфальта для дороги толщиной {height} м = {road_1.mass_asphalt(height)} кг")
