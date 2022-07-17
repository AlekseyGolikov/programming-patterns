"""
    Вариант 2 - Цепочка на основе сопрограмм

"""
import functools
import time

def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator
    return wrapper

@coroutine
def key_handler(successor=None):
    """
        Когда этой сопрограмме будет послано событие - напрямую или из другой сопрограммы в цепочке, -
        оно будет получено в виде значения переменной event. Если сопрограмма может обработать
        данное событие (то есть оно имеет тип Event.KEYPRESS), то обрабатывает - в данном случае
        просто печатает - и дальше не посылает. Если же сопрограмма о полученном событии ничего не знает
        и при условии, что имеется сопрограмма-преемник, то событие посылается преемнику.
        Если же преемника нет, то событие отбрасывается.
    """
    while True:
        event = (yield)
        if event == 'key pressed':
            print('Press: {}'.format(event))
        elif successor is not None:
            print('--key_handler')
            time.sleep(1)
            successor.send(event)

@coroutine
def mouse_handler(successor=None):
    while True:
        event = (yield)
        if event == 'mouse click':
            print('Press: {}'.format(event))
        elif successor is not None:
            print('--mouse_handler')
            time.sleep(1)
            successor.send(event)

@coroutine
def timer_handler(successor=None):
    while True:
        event = (yield)
        if event == 'timer tick':
            print(event)

@coroutine
def debug_handler(successor):
    while True:
        event = (yield)
        print('*DEBUG*: {}'.format(event))
        successor.send(event)

pipeline = debug_handler(key_handler(mouse_handler(timer_handler())))

pipeline.send('timer tick')
