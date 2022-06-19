"""
    Фабричный метод (Factory Method) - это паттерн, который определяет интерфейс для создания экземпляров
    некоторого класса, но непосредственное решение о том, экземпляр какого класса создавать происходит
    в подклассах. То есть паттерн предполагает, что базовый класс делегирует создание экземпляров
    классам-наследникам. (например, создание экземпляров объектов зависит от информации,
    прочитанной из файла или введённых пользователем данных)

    Когда надо применять паттерн:

    1) когда заранее неизвестно, объекты каких типов необходимо создавать;
    2) когда система должна быть независимой от процесса создания новых объектов и расширяемой:
    в нее можно легко вводить новые классы, объекты которых система должна создавать.
    3) когда создание новых объектов необходимо делегировать из базового класса классам наследникам

    Источник 1: https://webdevblog.ru/porozhdajushhie-shablony-v-python/
    Источник 2: https://metanit.com/sharp/patterns/2.1.php
"""
from abc import ABC, abstractmethod

class Product(ABC):
    """
        Абстрактный класс Product определяет интерфейс класса, объекты которого надо будет создавать
    """
    @abstractmethod
    def calculate_risk(self):
        pass

class Worker(Product):
    """
        Конкретный класс Worker представляет собой реализацию класса Product
    """
    def __init__(self, name, age, hours):
        self.name = name
        self.age = age
        self.hours = hours

    def calculate_risk(self):
        return self.age + 100/self.hours

    def __str__(self):
        return self.name + ' [' + str(self.age) + '] - ' + str(self.hours) + ' h/week'

class Unemployed(Product):
    """
        Конкретный класс Unemployed представляет собой реализацию класса Product
    """
    def __init__(self, name, age, able):
        self.name = name
        self.age = age
        self.able = able

    def calculate_risk(self):
        if self.able:
            return self.age+10
        else:
            return self.age+30

    def __str__(self):
        if self.able:
            return self.name+' ['+str(self.age)+' years old] - able to work.'
        else:
            return self.name+' ['+str(self.age)+' years old] - unable to work.'

# Класс PersonFactory, который в зависимости от значения параметра type_of_person
# выбирает фабричный метод из объявленных ранее Worder или Unemployed
class PersonFactory:

    def get_person(self, type_of_person):
        if type_of_person == 'worker':
            return Worker('Oliver', 22, 30)
        if type_of_person == 'unemployed':
            return Unemployed('Sophie', 33, False)

if __name__ == '__main__':

    factory = PersonFactory()

    product1 = factory.get_person('worker')
    print(product1)

    product2 = factory.get_person('unemployed')
    print(product2)
