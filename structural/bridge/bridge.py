"""
    Паттерн Bridge используется в ситуациях, когда требуется отделить абстракцию (интерфейс или алгоритм) от реализации.
    Паттерн мост позволяет создать две независимых иерархии классов: "абстрактную", которая определяет операции
    (интерфейс или алгоритм верхнего уровня) и конкретную, представляющую реализацию, которая в конечном итоге будет
    вызвана из абстрактных операций.

    Шаблон моста предотвращает то, что называется декартовой сложностью произведения взрывом.
    Проблема будет очевидна на примере. Предположим, вы реализуете Самолет . Это может быть военный или коммерческий самолет.
    Кроме того, это может быть пассажирский/военный или грузовой самолет. Одним из подходов к реализации этого является
    наличие Военного пассажирского , Военного грузового , Коммерческого пассажирского и Коммерческого грузового самолетов.
    Здесь декартово произведение сложности равно 2x.

    Источник: https://pythobyte.com/the-bridge-design-pattern-in-python-e61aa55f/
"""

from abc import ABC, abstractmethod

class Carrier(ABC):
    @abstractmethod
    def carry_military(self, items):
        pass
    @abstractmethod
    def carry_commercial(self, items):
        pass

class Cargo(Carrier):
    def carry_military(self, items):
        print('The plane carries %s military cargo goods.' % items)
    def carry_commercial(self, items):
        print('The plane carries %s commercial cargo goods.' % items)

class Passenger(Carrier):
    def carry_military(self, passengers):
        print('The plane carries %s military cargo goods.' % passengers)
    def carry_commercial(self, passengers):
        print('The plane carries %s commercial cargo goods.' % passengers)

class Plane(ABC):
    @abstractmethod
    def __init__(self, carrier):
        self.carrier = carrier

    @abstractmethod
    def display_description(self):
        pass

    @abstractmethod
    def add_objects(self):
        pass

class Commercial(Plane):
    def __init__(self, carrier, objects):
        super().__init__(carrier)
        self.objects = objects

    def display_description(self):
        self.carrier.carry_commercial(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects

class Military(Plane):
    def __init__(self, carrier, objects):
        super().__init__(carrier)
        self.objects = objects

    def display_description(self):
        self.carrier.carry_military(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects

cargo = Cargo()
passenger = Passenger()
military1 = Military(cargo, 100)
military1.display_description()
military1.add_objects(25)
military1.display_description()

military2 = Military(passenger, 250)
military2.display_description()
military2.add_objects(10)
military2.display_description()

commercial1 = Commercial(cargo, 110)
commercial1.display_description()
commercial1.add_objects(25)
commercial1.display_description()

commercial2 = Commercial(passenger, 200)
commercial2.display_description()
commercial2.add_objects(25)
commercial2.display_description()