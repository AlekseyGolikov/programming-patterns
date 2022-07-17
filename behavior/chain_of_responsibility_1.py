"""
    Цепочка Обязанностей (Chain of responsibility) - поведенческий шаблон проектирования, который позволяет избежать жесткой привязки отправителя запроса к получателю. Все возможные обработчики запроса образуют цепочку, а сам запрос перемещается по этой цепочке. Каждый объект в этой цепочке при получении запроса выбирает, либо закончить обработку запроса, либо передать запрос на обработку следующему по цепочке объекту.
    Когда применяется цепочка обязанностей?
    •	Когда имеется более одного объекта, который может обработать определенный запрос
    •	Когда надо передать запрос на выполнение одному из нескольких объект, точно не определяя, какому именно объекту
    •	Когда набор объектов задается динамически
    Вариант 1 - Традиционная цепочка
"""
class HttpHandler:
    """Абстрактный класс обработчика"""
    def handle(self, code):
        raise NotImplementedError()

class Http404Handler(HttpHandler):
    """Обработчик для кода 404"""
    def handle(self, code):
        if code == 404:
            return 'Page is not found!'

class Http500Handler(HttpHandler):
    """Обработчик для кода 500"""
    def handle(self, code):
        if code == 500:
            return 'Server error!'

class Client:
    def __init__(self):
        self._handlers = []

    def add_handler(self, h):
        self._handlers.append(h)

    def response(self, code):
        for h in self._handlers:
            msg = h.handle(code)
            if msg:
                print(msg)
                break

client = Client()
client.add_handler(Http404Handler())
client.add_handler(Http500Handler())
client.response(400)
client.response(404)
client.response(500)