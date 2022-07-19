"""
    Паттерн "Команда" (Command) позволяет инкапсулировать запрос на выполнение определенного действия
    в виде отдельного объекта. Этот объект запроса на действие и называется командой.
    При этом объекты, инициирующие запросы на выполнение действия, отделяются от объектов,
    которые выполняют это действие.

    Команды могут использовать параметры, которые передают ассоциированную с командой информацию.
    Кроме того, команды могут ставиться в очередь и также могут быть отменены.

    Когда использовать команды?
    1) Когда надо передавать в качестве параметров определенные действия, вызываемые в ответ на другие действия.
       То есть когда необходимы функции обратного действия в ответ на определенные действия.
    2) Когда необходимо обеспечить выполнение очереди запросов, а также их возможную отмену.
    3) Когда надо поддерживать логгирование изменений в результате запросов.
       Использование логов может помочь восстановить состояние системы - для этого необходимо
       будет использовать последовательность запротоколированных команд.
"""
class Light:
    def turn_on(self):
        print('turn on')

    def turn_off(self):
        print('turn_off')

class CommandBase:
    def execute(self):
        raise NotImplementedError()

class LightCommandBase(CommandBase):
    def __init__(self, light):
        self._light = light

class TurnOnLightCommand(LightCommandBase):
    def execute(self):
        self._light.turn_on()

class TurnOffLightCommand(LightCommandBase):
    def execute(self):
        self._light.turn_off()

class Switch:
    def __init__(self, on_cmd, off_cmd):
        self._on_cmd = on_cmd
        self._off_cmd = off_cmd

    def on(self):
        self._on_cmd.execute()

    def off(self):
        self._off_cmd.execute()

light = Light()
switch = Switch(
    on_cmd=TurnOnLightCommand(light),
    off_cmd=TurnOffLightCommand(light)
)
switch.on()
switch.off()
