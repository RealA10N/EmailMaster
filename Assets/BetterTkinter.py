import tkinter
from tkinter import ttk, font

# - - - - - - #
# C O L O R S #
# - - - - - - #


class DefaultColor():
    def Get(self):
        pass


class SelectedColor():
    def Get(self):
        return '#0078d7'


class DeselectedColor(DefaultColor):
    def Get(self):
        return '#7a7a7a'


# - - - - - - - #
# W I N D O W S #
# - - - - - - - #

class Tk(tk.Tk):
    pass


class TopLevel(tk.Toplevel):
    pass


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
