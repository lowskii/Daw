from tkinter import *
from creational.singleton import Singleton
import eqswindow
import footerwindow
import convererwindow
import decoratorwindow
import renderwindow
import iteratorwindow

class Window(Tk, Singleton):
    def init(self):
        print('calling  from init')
        super().__init__()

        self.button = Button(self, text='Open EQs', command=self.create_eqs_window)
        self.button.pack(expand=True)

        self.button = Button(self, text='Play audio', command=self.convert_audio_to_midi)
        self.button.pack(expand=True)

        self.button = Button(self, text='Show footer', command=self.create_eqs_footer)
        self.button.pack(expand=True)

        self.button = Button(self, text='Show decorator', command=self.create_decorator)
        self.button.pack(expand=True)

        self.button = Button(self, text='Rendering', command=self.open_render)
        self.button.pack(expand=True)

        self.button = Button(self, text='Search', command=self.create_iterator_window)
        self.button.pack(expand=True)


    def create_eqs_window(self):
        global extraWindow
        extraWindow = eqswindow.Extra()
    
    def convert_audio_to_midi(self):
        global extraWindow
        extraWindow = convererwindow.Extra()

    def create_eqs_footer(self):
        global extraWindow
        extraWindow = footerwindow.Extra()

    def create_decorator(self):
        global extraWindow
        extraWindow = decoratorwindow.Extra()
    
    def open_render(self):
        global extraWindow
        extraWindow = renderwindow.Extra()

    def create_iterator_window(self):
        global extraWindow
        extraWindow = iteratorwindow.Extra()
    
    def __init__(self):
        print('calling  from __init__')