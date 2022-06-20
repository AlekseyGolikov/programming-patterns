"""
    Шаблон проектирования Builder инкапсулирует создание объекта и позволяет разделить его на различные этапы.

    Когда использовать паттерн Строитель

    1) Когда процесс создания нового объекта не должен зависеть от того,
       из каких частей этот объект состоит и как эти части связаны между собой;
    2) Когда необходимо обеспечить получение различных вариаций объекта в процессе его создания

    Шаблон Builder не имеет большого смысла для небольших, простых классов, поскольку добавленная логика для их построения просто добавляет сложности.

    Хотя, когда дело доходит до больших, сложных классов с многочисленными областями, такими как многослойные нейронные сети — паттерн Builder реально выручает.
"""
class Robot:
    """
        Определение класса, экземпляр которого необходимо создать руководствуясь паттерном Строитель
    """
    def __init__(self):
        self.bipedal = False
        self.quadripedal = False
        self.wheeled = False
        self.flying = False
        self.traversal = []
        self.detection_systems = []

    def __str__(self):
        string = ''
        if self.bipedal:
            string += 'BIPEDAL '
        if self.quadripedal:
            string += 'QUADRIPEDAL '
        if self.flying:
            string += 'FLYING ROBOT'
        if self.wheeled:
            string += 'ROBOT ON WHEELS\n'
        else:
            string += 'ROBOT\n'

        if self.traversal:
            string += 'Traversal modules installed: \n'

        for module in self.traversal:
            string += '- ' + str(module) + '\n'

        if self.detection_systems:
            string += 'Detection system installed: \n'

        for system in self.detection_systems:
            string += '- '+str(system)+'\n'

        return string

class BipedalLegs:
    def __str__(self):
        return 'two legs'

class QuadripedalLegs:
    def __str__(self):
        return 'four legs'

class Arms:
    def __str__(self):
        return 'two arms'

class Wings:
    def __str__(self):
        return 'wings'

class Blades:
    def __str__(self):
        return 'blades'

class TwoWheels:
    def __str__(self):
        return 'two wheels'

class CameraDetectionSystem:
    def __str__(self):
        return 'cameras'

class InfraredDetectionSystem:
    def __str__(self):
        return 'infrared'

from abc import ABC, abstractmethod

class RobotBuilder(ABC):
    """
        Определение абстрактного класса, который реализует интерфейс для создания классов конкретных объектов
    """
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_traversal(self):
        pass

    @abstractmethod
    def build_detection_system(self):
        pass

class AndroidBuilder(RobotBuilder):
    """
        Определение класса, который создает экземпляры конкретного объекта Android
    """
    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    def get_product(self):
        return self.product

    def build_traversal(self):
        self.product.bipedal = True
        self.product.traversal.append(BipedalLegs())
        self.product.traversal.append(Arms())

    def build_detection_system(self):
        self.product.detection_systems.append(CameraDetectionSystem())

class AutonomousCarBuilder(RobotBuilder):
    """
        Определение класса, который создает экземпляры конкретного объекта AutonomousCar
    """
    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    def get_product(self):
        return self.product

    def build_traversal(self):
        self.product.wheeled = True
        self.product.traversal.append(TwoWheels())

    def build_detection_system(self):
        self.product.detection_systems.append(InfraredDetectionSystem())

# builder =AndroidBuilder()
# builder.build_traversal()
# builder.build_detection_system()
# print(builder.get_product())

# builder = AutonomousCarBuilder()
# builder.build_traversal()
# builder.build_detection_system()
# print(builder.get_product())

class Director:
    """
        Если в полях нашего продукта спользуются относительно стандартные конструкторы,
        мы можем даже создать так называемого директора для управления конкретными сборщиками
    """
    def make_android(self, builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()

    def make_autonomouscar(self, builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()

director = Director()
builder = AndroidBuilder()
print(director.make_android(builder))
