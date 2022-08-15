"""
    Реализация паттерна Singleton по методу "отложенная инициализация экземпляра"

    Например, в случае импорта модулей мы можем автоматически создать объект, даже если он не нужен.
    Отложенное создание экземпляра гарантирует, что объект создается, только тогда,
    когда он действительно необходим.

    Источник: https://webdevblog.ru/realizaciya-shablona-singleton-v-python/?
"""

class Singleton:

    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('__init__ method called...')
        else:
            print('Instance already created: ', self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s = Singleton()
print('Object created ', Singleton.getInstance())
s1 = Singleton()
