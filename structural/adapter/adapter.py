"""
    Паттерн Adapter
"""
class ForkUSA:
    def power_usa(self):
        print('power on. USA')

class ForkEuro:
    def power_euro(self):
        print('power on. Euro')

class SocketUSA:
    def __init__(self, fork):
        self.fork = fork

    def connect(self):
        self.fork.power_usa()

class Adapter:
    def __init__(self):
        self.adapter = ForkEuro()

    def power_usa(self):
        self.adapter.power_euro()

# uf = ForkUSA()
# us = SocketUSA(uf)
# us.connect()

us = SocketUSA(Adapter())
us.connect()

