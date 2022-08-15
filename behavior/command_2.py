"""
	Вариант 2 - реализация паттерна Команда
	Этот вариант также соответствует паттерну Компановщик, т.к. и отдельные команды, и макрос команд имеют
	одинаковый интерфейс (методы do() и undo())
"""
import time


class Grid:
	def __init__(self, width: int, height: int) -> None:
		self._cells = [['white' for _ in range(height)] for _ in range(width)]

	def cell(self, x: int, y: int, color: str = None):
		if color is None:
			return self._cells[x][y]
		self._cells[x][y] = color

	def display(self):
		for y in range(self.columns):
			for x in range(self.rows):
				print(self._cells[y][x].center(13), end='')
			print('\n')
		print('--------------------')

	@property
	def rows(self):
		return len(self._cells[0])

	@property
	def columns(self):
		return len(self._cells)


class UndoableGrid(Grid):

	def create_cell_command(self, x, y, color):
		def undo():
			self.cell(x, y, undo.color)
		def do():
			undo.color = self.cell(x,y)
			self.cell(x, y, color)
		return Command(do, undo, 'Cell')
	def create_rectangle_macro(self, x0, y0, x1, y1, color):
		macro = Macro('Rectangle')
		for x in range(x0, x1+1):
			for y in range(y0, y1+1):
				macro.add(self.create_cell_command(x, y, color))
		return macro


class Command:
	def __init__(self, do, undo, description=''):
		assert callable(do) and callable(undo)
		self.do = do
		self.undo = undo
		self.description = description

	def __call__(self):
		self.do()

class Macro:
	def __init__(self, description=''):
		self.description = description
		self.__commands = []

	def add(self, command):
		if not isinstance(command, Command):
			raise TypeError('Expected object of type Command, got {}'.format(type(command).__name__))
		self.__commands.append(command)

	def __call__(self):
		for command in self.__commands:
			command()

	do = __call__

	def undo(self):
		for command in reversed(self.__commands):
			command.undo()

if __name__ == '__main__':
	grid = UndoableGrid(8, 3) 	# (1) пустая
	redLeft = grid.create_cell_command(2, 1, 'red')
	redRight = grid.create_cell_command(5, 0, 'red')
	grid.display()
	time.sleep(1)
	redLeft() 					# (2) вставить красные ячейки
	redRight.do() 				# ИЛИ: redRight()
	greenLeft = grid.create_cell_command(2, 1, 'lightgreen')
	greenLeft() 				# (3) вставить зеленую ячейку
	grid.display()
	time.sleep(1)
	rectangleLeft = grid.create_rectangle_macro(1,1,2,2, 'lightblue')
	rectangleRight = grid.create_rectangle_macro(5,0,6,1,'lightblue')
	grid.display()
	time.sleep(1)
	rectangleLeft() 			# (4) Вставить синие ячейки
	rectangleRight.do() 		# ИЛИ: rectangleRight()
	grid.display()
	time.sleep(1)
	rectangleLeft.undo() 		# (5) отменить левую синию ячейку
	greenLeft.undo() 			# (6) отменить левую зеленую ячейку
	rectangleRight.undo() 		# (7) отменить правую синюю ячейку
	redLeft.undo() 				# (8) отменить красные ячейки
	redRight.undo()
	grid.display()
	time.sleep(1)
