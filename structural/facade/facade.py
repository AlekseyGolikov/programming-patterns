"""
	Фасад (Facade) представляет шаблон проектирования, который позволяет скрыть сложность системы
	с помощью предоставления упрощенного интерфейса для взаимодействия с ней.

	Когда использовать фасад?
	1) Когда имеется сложная система, и необходимо упростить с ней работу. Фасад позволит определить
		одну точку взаимодействия между клиентом и системой.
	2) Когда надо уменьшить количество зависимостей между клиентом и сложной системой.
		Фасадные объекты позволяют отделить, изолировать компоненты системы от клиента и развивать и
		работать с ними независимо.
	3) Когда нужно определить подсистемы компонентов в сложной системе. Создание фасадов для компонентов
		каждой отдельной подсистемы позволит упростить взаимодействие между ними и повысить
		их независимость друг от друга.
"""
class Paper:
	def __init__(self, count):
		self._count = count

	def write_(self, txt):
		print(txt)
		self._count -= 1

	def get_count(self):
		return self._count

class Printer:
	def error(self):
		print('Бумага закончилась!')

	def _print(self, paper, msg):
		if paper.get_count()>0:
			paper.write_(msg)
		else:
			self.error()


class Facade:
	def __init__(self):
		self.paper = Paper(1)
		self.printer = Printer()

	def write(self, msg):
		self.printer._print(self.paper, msg)

facade = Facade()
facade.write('Hello world!')
facade.write('Hello world!')
