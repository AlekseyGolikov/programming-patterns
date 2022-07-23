"""
	Паттерн Mediator (посредник) предоставляет средства для создания объекта-посредника, который инкапсулирует взаимоедйствия между другими объектами.
	Это позволяет осуществлять взаимодействия между другими объектами, которые ничего не знают друг о друге.
	Когда используется паттерн Посредник?
	1) Когда имеется множество взаимосвязаных объектов, связи между которыми сложны и запутаны.
	2) Когда необходимо повторно использовать объект, однако повторное использование затруднено в силу сильных связей с другими объектами.
	Широко применяется при создании GUI
"""
class WindowBase:
	def show(self):
		raise NotImplementedError()

	def hide(self):
		raise NotImplementedError()

class MainWindow(WindowBase):
	def show(self):
		print('Show MainWindow')

	def hide(self):
		print('Hide MainWindow')

class SettingWindow(WindowBase):
	def show(self):
		print('Show SettingWindow')

	def hide(self):
		print('Hide SettingWindow')

class HelpWindow(WindowBase):
	def show(self):
		print('Show HelpWindow')

	def hide(self):
		print('Hide HelpWindow')

class WindowMediator:
	def __init__(self):
		self.windows = dict.fromkeys(['main', 'setting', 'help'])

	def show(self, win):
		for window in self.windows.values():
			if not window is win:
				window.hide()
		win.show()

	def set_main(self, win):
		self.windows['main'] = win

	def set_setting(self, win):
		self.windows['setting'] = win

	def set_help(self, win):
		self.windows['help'] = win

main_win = MainWindow()
setting_win = SettingWindow()
help_win = HelpWindow()

med = WindowMediator()
med.set_main(main_win)
med.set_setting(setting_win)
med.set_help(help_win)

main_win.show()

med.show(setting_win)

med.show(help_win)
