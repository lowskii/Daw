from tkinter import Toplevel, Button
from creational.singleton import Singleton
from creational.abstractfactory import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("EQs")
        self.geometry("600x600")
        self.button = Button(self, text='Show EQs', command=self.showEQs)
        self.button.pack(expand=True)

    def showEQs(self):
        eqsFactory = EQsFactory()

        eqs = eqsFactory.eqs

        for e in eqs:
            self.button = Button(self, text=f'{e.name}')
            self.button.pack(expand=True)

