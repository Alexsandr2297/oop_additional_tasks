"""
Создай класс `Number` c полем `value` (указывается при инициализации)

Создай экземпляр, например `x = Number(7)`

Добавь методы:

`.get()` возвращает текущее value

`.add(<значение>)` добавляет указанное число к value

`.substract(<значение>)` вычитает указанное число из value
"""


class Number:
    """Класс для номера"""
    value: int

    def __init__(self, value):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.value = value

    def get(self):
        """Возвращает нужное число"""
        return self.value

    def add(self, a):
        """Добовляет к нужному числу"""
        self.value += a

    def substract(self, b):
        """Вычитает указанное число из текущего значения."""
        self.value -= b


# код для проверки
n = Number(7)
print(n.get())  # 7
n.add(3)
print(n.get())  # 10
n.substract(5)
print(n.get())  # 5
