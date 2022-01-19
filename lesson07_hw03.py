"""
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка. class Cell
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). self.count_cells
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.

Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создаётся общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернёт строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""

class Cell:
    """
    КЛЕТКА
    """
    def __init__(self, count_cells: int):
        self.count_cells = count_cells

    def __str__(self):
        cells = ""
        for i in range(self.count_cells):
            cells += "*"
        return cells

    def __add__(self, other):
        return Cell(self.count_cells+other.count_cells)

    def __sub__(self, other):
        # посчитал лучшим решением: при любом исходе при вычитании возвращать экземпляр класса, а не выводить ошибку
        return Cell(max(self.count_cells-other.count_cells, 0))

    def __mul__(self, other):
        return Cell(self.count_cells * other.count_cells)

    def __truediv__(self, other):
        # будем считать, что деление на нулевую клетку тоже возвращает нулевую кетку
        return Cell(self.count_cells // other.count_cells if other.count_cell > 0 else 0)

    def make_order(self, split_count: int):
        my_str = str(self)
        # вычислим количество частей
        parts = self.count_cells // split_count if self.count_cells % split_count == 0 \
            else self.count_cells // split_count + 1
        new_str = ""
        for i in range(parts):
            # нарежем строку на части
            new_str += my_str[split_count*i: min(self.count_cells, split_count*(i+1))]+"\n"
        return new_str

# Работа с клетками

cell1 = Cell(7)
cell2 = Cell(5)
cell3 = cell1 + cell2
print(cell3)

cell4 = cell1 - cell2
print(cell4)
cell5 = cell2 - cell1
print(cell5)

print((cell1 / cell2).count_cells)
print((cell1 * cell2).make_order(10))
