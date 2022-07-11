"""
    Создание класса по методу Singleton с помощью функции-декоратора
"""
def singleton(cls):
    def wrapper(*args, **kwargs):
        if not wrapper.inst:
            wrapper.inst = cls(*args, **kwargs)
        return wrapper.inst
    wrapper.inst = None
    return wrapper

@singleton
class Obj:
    pass

o = Obj()
o1 = Obj()
print(o == o1)