class Observable:
    def __init__(self):
        self.observers = []

    def notify(self):
        pass

    def attach(self, observer):
        pass

class Compressor(Observable):
    def __init__(self, name):
        super().__init__()
        self.name = name 
        self.gain = 0

    @property
    def gain(self):
        return self._gain
    
    @gain.setter
    def setGain(self, value):
        self._gain = value

class Kick:
    def __init__(self):
        self.name = "Kick"

    def update(self, subject):
        pass
