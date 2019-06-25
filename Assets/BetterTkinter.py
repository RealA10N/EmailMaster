import tkinter
from tkinter import ttk, font


class DefaultFont(font.Font):
    pass


class RegularFont(DefaultFont):
    def __init__(self):
        DefaultFont.__init__(self, size=12)


class BigFont(DefaultFont):
    def __init__(self):
        DefaultFont.__init__(self, size=16)


class Tk(tkinter.Tk):
    pass


class Button(ttk.Button):
    pass


class Entry(ttk.Entry):
    def __init__(self, *args, **kwargs):
        ttk.Entry.__init__(self, font=BigFont(), *args, **kwargs)
