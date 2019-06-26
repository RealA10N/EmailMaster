import tkinter as tk
from tkinter import ttk, font


class DefaultValue():
    def Get(self):
        pass


# - - - - - - #
# C O L O R S #
# - - - - - - #

class DefaultColor(DefaultValue):
    pass


class SelectedColor(DefaultColor):
    def Get(self):
        return '#0078d7'


class DeselectedColor(DefaultColor):
    def Get(self):
        return '#7a7a7a'


class BackgroundColor(DefaultColor):
    def Get(self):
        return '#f3f3f3'


# - - - - #
# P A D S #
# - - - - #

class DefaultPad(DefaultValue):
    pass


class RegularPad(DefaultPad):
    def Get(self):
        return 6


class BigPad(DefaultPad):
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

class DefaultFont(font.Font):
    pass


class RegularFont(DefaultFont):
    def __init__(self):
        DefaultFont.__init__(self, size=12)


class BigFont(DefaultFont):
    def __init__(self):
        DefaultFont.__init__(self, size=16)


# - - - - - - - #
# B U T T O N S #
# - - - - - - - #

class DefaultButton(ttk.Button):
    pass


class RegularButton(DefaultButton):
    pass

# - - - - - - #
# E N T R Y S #
# - - - - - - #


class DefaultEntry(ttk.Entry):
    pass


class RegularEntry(DefaultEntry):
    def __init__(self, *args, **kwargs):
        DefaultEntry.__init__(self, font=RegularFont(), *args, **kwargs)


class BigEntry(DefaultEntry):
    def __init__(self, *args, **kwargs):
        DefaultEntry.__init__(self, font=BigFont(), *args, **kwargs)


# - - - - - #
# T E X T S #
# - - - - - #

class DefaultText(tk.Text):

    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self,
                         relief='flat',
                         highlightthickness=1,
                         highlightcolor=SelectedColor().Get(),
                         highlightbackground=DeselectedColor().Get(),
                         *args, **kwargs)


class RegularText(DefaultText):
    def __init__(self, *args, **kwargs):
        DefaultText.__init__(self,
                             font=RegularFont(),
                             *args, **kwargs)


# - - - - - - #
# L A B E L S #
# - - - - - - #

class DefaultLabel(tk.Label):
    pass


class RegularLabel(DefaultLabel):
    def __init__(self, *args, **kwargs):
        DefaultLabel.__init__(self,
                              font=RegularFont(),
                              *args, **kwargs)

    def grid(self, *args, **kwargs):
        DefaultLabel.grid(self,
                          padx=RegularPad().Get(),
                          pady=RegularPad().Get(),
                          *args, **kwargs)


class BigLabel(DefaultLabel):
    def __init__(self, *args, **kwargs):
        DefaultLabel.__init__(self,
                              font=BigFont(),
                              *args, **kwargs)

    def grid(self, *args, **kwargs):
        DefaultLabel.grid(self,
                          padx=BigPad().Get(),
                          pady=BigPad().Get(),
                          *args, **kwargs)
