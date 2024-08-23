"""
Допишите код под условия в цикле так, чтобы вывод был корректным
"""


class Animal:

    def __init__(self, name):
        self.name = name

    def walk(self):
        pass


class Dog(Animal):

    def bark(self):
        print('Bark!')


class Cat(Animal):

    def meow(self):
        print('Meow!')


animals = [Dog('Dog1'), Dog('Dog2'), Cat('Cat1'), Dog('Dog3')]
# Должно выводиться Bark или Meow в зависимости от того какой класс
for i in animals:
    if issubclass(i.__class__, Dog):
        i.bark()
    else:
        i.meow()
