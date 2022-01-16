"""
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""

class Worker:
    def __init__(self, name: str, surname: str, position: str, _income = dict.fromkeys(["wage", "bonus"], 0)):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income
        print(f"Создан работник: {self.name} {self.surname}, должность: {self.position}, "
              f"c окладом {self._income['wage']} руб. и премией {self._income['bonus']} руб.")

class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return sum(self._income.values())
        # return self._income["wage"]+self._income["bonus"]


pos_worker = Position("Петя", "Васечкин", "Сварщик", _income={"wage": 100, "bonus": 50})
print(f"Суммарный доход {pos_worker.get_full_name()} = {pos_worker.get_total_income()} руб.")
