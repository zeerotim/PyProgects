"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
 базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

+5 + 6 задания
"""

class Warehouse:
    '''
    goods - словарь, у которого клчем будет элемент класса/подкласса
    OfficeEquipment, а значением - количество
    '''
    goods = dict()
    def __init__(self, name: str):
        self.name = name

    def add_good(self, good, count):
        if self.valid_count(count):
            if self.goods.get(good) is None:
                self.goods[good] = count
            else:
                self.goods[good] += count
            print(f"На склад {self.name} оприходован {good} в кол-ве {count} шт")

    def sub_good(self, good, count):
        if self.valid_count(count):
            if self.goods.get(good) is None:
                self.goods[good] = -count
            else:
                self.goods[good] -= count
            print(f"Со склада {self.name} списан {good} в кол-ве {count} шт")

    def get_good(self, good):
        return 0 if self.goods.get(good) is None else self.goods[good]

    def get_goods(self):
        print(f"На складе {self.name}")
        for key, value in self.goods.items():
            print(f"{key} в количестве {value} шт.")

    @staticmethod
    def valid_count(count):
        return str(count).isdigit()



class OfficeEquipment:
    def __init__(self, name: str, trade_mark ="",is_color = True):
        self.name, self.trade_mark, self.is_color = name, trade_mark, is_color
        # print(f"Создано офисное оборудование: {self.name}")

    def __hash__(self):
        return hash((self.name, self.trade_mark, self.is_color))

    def __str__(self):
        return f"{self.name} {self.trade_mark}"


class Printer(OfficeEquipment):
    def __init__(self, name, trade_mark, is_color, type: str):
        super().__init__(name, trade_mark, is_color)
        # type = матричный, струйный, лазерный
        self.type = type
        # print(f"Создан {self.type} принтер: {self.name} {self.trade_mark}")
        print(f"Создан {self.type} принтер: {self}")

class Scanner(OfficeEquipment):
    def __init__(self, name, trade_mark, is_color,type: str):
        # type = ручной, планшетный
        super().__init__(name, trade_mark, is_color)
        self.type = type
        print(f"Создан {self.type} сканер: {self.name} {self.trade_mark}")

class Xerox(OfficeEquipment):
    def __init__(self, name, trade_mark, is_color,type: str):
        super().__init__(name, trade_mark, is_color)
        # type = ручной, планшетный
        self.type = type
        print(f"Создан {self.type} ксерокс: {self.name} {self.trade_mark}")

# работа с классами

printer = Printer(name = "Принтер 1015", trade_mark = "HP", is_color= False,  type = "Струйный")
xerox = Xerox(name = "Ксерокс 354", trade_mark = "Canon", is_color= True,  type = "Планшетный")


wh1 = Warehouse("Центральный")

wh1.add_good(printer, 5)
wh1.add_good(printer, 1)
wh1.sub_good(printer, 2)
wh1.add_good(xerox, 8)

wh1.get_goods()
