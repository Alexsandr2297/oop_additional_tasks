from datetime import datetime
"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""


class Car:
    def __init__(self, brand, model, year):
        current_year = datetime.now().year
        if year > current_year:
            raise Exception('Эта машина еще не была выпущена')
        self.brand = brand
        self.model = model
        self.year = year

    def __add__(self, other):
        if isinstance(other, Car):
            return self.year == other.year
        return False

    # код для проверки


car = Car('Toyota', 'Corolla', 2022)
try:
    car2 = Car('Toyota', 'Corolla', 3000)
except Exception as e:
    print(e)
# raises Exception('Эта машина еще не была выпущена')

