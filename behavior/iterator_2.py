"""
	Паттерн Итератор
	Вариант 2 - использование функцией iter(Iterable, restricted_value) с двумя переменными
	Iterable - итерируемый объект, restricted_value - значение, ограничивающее вывод
	(если None - итератор доходит до конца)
"""
class Objects:

	__names = ('obj1', 'obj2', 'obj3', 'obj4', 'obj5')

	def __init__(self, first=None):
		self._index = (-1 if first is None else Objects.__names.index(first)-1)

	def __call__(self):
		self._index += 1
		if self._index < len(Objects.__names):
			return Objects.__names[self._index]
		raise StopIteration()


string = ''
for x in iter(Objects('obj2'), 'obj4'):
	string += x
	string += ' '
print(string)
