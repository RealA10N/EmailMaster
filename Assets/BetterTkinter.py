import tkinter as tk
from tkinter import ttk, font


class __DefaultValue():
    def Get(self):
        pass


# - - - - - - #
# C O L O R S #
# - - - - - - #

class __DefaultColor(__DefaultValue):
    pass


class SelectedColor(__DefaultColor):
    def Get(self):
        return '#0078d7'


class DeselectedColor(__DefaultColor):
    def Get(self):
        return '#7a7a7a'


class BackgroundColor(__DefaultColor):
    def Get(self):
        return '#f3f3f3'


# - - - - #
# P A D S #
# - - - - #

class __DefaultPad(__DefaultValue):
    pass


class RegularPad(__DefaultPad):
    def Get(self):
        return 6


class BigPad(__DefaultPad):
    def Get(self):
        return 10


# - - - - - - - #
# W I N D O W S #
# - - - - - - - #

class Tk(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.config(bg=BackgroundColor().Get())


class TopLevel(tk.Toplevel):
    pass


class Frame(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self,
                          bg=BackgroundColor().Get(),
                          *args, **kwargs)


# - - - - - #
# F O N T S #
# - - - - - #

class _DefaultFont(font.Font):
    pass


class RegularFont(_DefaultFont):
    def __init__(self):
        _DefaultFont.__init__(self, size=12)


class BigFont(_DefaultFont):
    def __init__(self):
        _DefaultFont.__init__(self, size=16)


# - - - - - - - #
# B U T T O N S #
# - - - - - - - #

class _DefaultButton(ttk.Button):
    pass


class RegularButton(_DefaultButton):
    pass

# - - - - - - #
# E N T R Y S #
# - - - - - - #


class _DefaultEntry(ttk.Entry):
    pass


class RegularEntry(_DefaultEntry):
    def __init__(self, *args, **kwargs):
        _DefaultEntry.__init__(self, font=RegularFont(), *args, **kwargs)


class BigEntry(_DefaultEntry):
    def __init__(self, *args, **kwargs):
        _DefaultEntry.__init__(self, font=BigFont(), *args, **kwargs)


# - - - - - #
# T E X T S #
# - - - - - #

class _DefaultText(tk.Text):

    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self,
                         relief='flat',
                         highlightthickness=1,
                         highlightcolor=SelectedColor().Get(),
                         highlightbackground=DeselectedColor().Get(),
                         *args, **kwargs)


class RegularText(_DefaultText):
    def __init__(self, *args, **kwargs):
        _DefaultText.__init__(self,
                              font=RegularFont(),
                              *args, **kwargs)


# - - - - - - #
# L A B E L S #
# - - - - - - #

class _DefaultLabel(tk.Label):
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self,
                          bg=BackgroundColor().Get(),
                          *args, **kwargs)


class RegularLabel(_DefaultLabel):
    def __init__(self, *args, **kwargs):
        _DefaultLabel.__init__(self,
                               font=RegularFont(),
                               *args, **kwargs)

    def grid(self, *args, **kwargs):
        _DefaultLabel.grid(self,
                           padx=RegularPad().Get(),
                           pady=RegularPad().Get(),
                           *args, **kwargs)


class BigLabel(_DefaultLabel):
    def __init__(self, *args, **kwargs):
        _DefaultLabel.__init__(self,
                               font=BigFont(),
                               *args, **kwargs)

    def grid(self, *args, **kwargs):
        _DefaultLabel.grid(self,
                           padx=BigPad().Get(),
                           pady=BigPad().Get(),
                           *args, **kwargs)

