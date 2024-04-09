from tkinter import *
from creational.singleton import Singleton
import eqswindow
import footerwindow

class Window(Tk, Singleton):
    def init(self):
        print('calling  from init')
        super().__init__()

        self.button = Button(self, text='Open EQs', command=self.create_eqs_window)
        self.button.pack(expand=True)

        self.button = Button(self, text='Show footer', command=self.create_eqs_footer)
        self.button.pack(expand=True)

    def create_eqs_window(self):
        global extraWindow
        extraWindow = eqswindow.Extra()

    def create_eqs_footer(self):
        global extraWindow
        extraWindow = footerwindow.Extra()
    
    def __init__(self):
        print('calling  from __init__')