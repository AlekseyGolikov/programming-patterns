"""
	Итератор (Iterator) - паттерн поведения объектов, предоставляющий способ последовательного доступа
	ко всем элементам составного объекта, не раскрывая его внутреннего представления.

	Вариант 1 предполагает переопределение магических методов __getitem__, __len__, __setitem__, __delitem__,
	__iter__, __reversed__, __contains__, __missing__
"""

class L:
	def __init__(self):
		self._books = []

	def __getitem__(self, item):
		return self._books[item]


	def __setitem__(self, key, value):
		self._books[key] = value

	def __delitem__(self, key):
		del self._books[key]

	def __len__(self):
		return len(self._books)

	def __iter__(self):
		return iter(self._books)

	def __reversed__(self):
		return reversed(self._books)

	def __contains__(self, item):
		if self._books[item] is not None:
			return True
		return False

	def __missing__(self, key):
		if self._books[key] is None:
			raise ValueError('unable value!')

	def add(self, val):
		self._books.append(val)

	def __str__(self):
		string = ''
		for x in self._books:
			string += str(x)
			string += '; '
		return string


l = L()
l.add('aaa')
l.add('bbb')
l.add('ccc')
l[4]='ddd'

