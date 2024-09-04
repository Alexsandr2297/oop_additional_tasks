"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Так как данный класс используется в большом каталоге, его необходимо оптимизировать и создать класс, который использует коллекции slots

Сравните скорость работы двух классов: с коллекциями slots и без них. Для этого каждому классу напишите метод get_set_del, 
в котором происходи получение, присваивание и удаление значения.
"""


class Car:
    brand: str
    model: str
    year_manufacture: int

    def __init__(self, brand, model, year_manufacture):
        self.brand = brand
        self.model = model
        self.year_manufacture = year_manufacture

    def get_set_del(self):
        self.brand = "Toyota"
        self.model = "Corola"
        del self.model


class CarSlots:
    __slots__ = ("brand", "model", "year_manufacture")

    def __init__(self, brand, model, year_manufacture):
        self.brand = brand
        self.model = model
        self.year_manufacture = year_manufacture

    def get_sel_del(self):
        self.brand = "Toyota"
        self.model = "Corola"
        del self.model


car = Car('Toyota', 'Corolla', 2022)
car_slots = Car('Toyota', 'Crown', 1990)

import timeit

t1 = timeit.timeit(car.get_set_del)
t2 = timeit.timeit(car_slots.get_set_del)
print(t1)
print(t2)
print((t1 - t2) / t1 * 100)
