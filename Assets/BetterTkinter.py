import tkinter as tk
from tkinter import ttk, font


class _DefaultValue():
    def Get(self):
        pass


# - - - - - - #
# C O L O R S #
# - - - - - - #

class _DefaultColor(_DefaultValue):
    pass


class SelectedColor(_DefaultColor):
    def Get(self):
        return '#0078d7'


class DeselectedColor(_DefaultColor):
    def Get(self):
        return '#7a7a7a'


class BackgroundColor(_DefaultColor):
    def Get(self):
        return '#f3f3f3'


# - - - - #
# P A D S #
# - - - - #

class _DefaultPad(_DefaultValue):
    pass


class SmallPad(_DefaultPad):
    def Get(self):
        return 3


class RegularPad(_DefaultPad):
    def Get(self):
        return 6


class BigPad(_DefaultPad):
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
    def __init__(self, Master, *args, **kwargs):
        tk.Frame.__init__(self, Master,
                          bg=BackgroundColor().Get(),
                          *args, **kwargs)

    def BasicGrid(self, *args, **kwargs):
        tk.Frame.grid(self, *args, **kwargs)

    def grid(self, *args, **kwargs):
        tk.Frame.grid(self,
                      padx=RegularPad().Get(),
                      pady=RegularPad().Get(),
                      *args, **kwargs)


class LabelFrame(tk.LabelFrame):
    def __init__(self, Master, Text, *args, **kwargs):
        tk.LabelFrame.__init__(self, Master,
                               bg=BackgroundColor().Get(),
                               text=" {} ".format(Text),
                               relief='ridge',
                               font=RegularFont(),
                               *args, **kwargs)

    def BasicGrid(self, *args, **kwargs):
        tk.LabelFrame.grid(self, *args, **kwargs)

    def grid(self, *args, **kwargs):
        tk.LabelFrame.grid(self,
                           padx=RegularPad().Get(),
                           pady=RegularPad().Get(),
                           *args, **kwargs)


# - - - - - #
# F O N T S #
# - - - - - #

class _DefaultFont(font.Font):
    pass


class RegularFont(_DefaultFont):
    def __init__(self):
        _DefaultFont.__init__(self, size=12)


class SmallFont(_DefaultFont):
    def __init__(self):
        _DefaultFont.__init__(self, size=8)


class BigFont(_DefaultFont):
    def __init__(self):
        _DefaultFont.__init__(self, size=16)


# - - - - - - - #
# B U T T O N S #
# - - - - - - - #

class _DefaultButton(ttk.Button):

    def BasicGrid(self, *args, **kwargs):
        ttk.Button.grid(self, *args, **kwargs)


class RegularButton(_DefaultButton):

    def grid(self, *args, **kwargs):
        _DefaultButton.grid(self,
                            padx=RegularPad().Get(),
                            pady=RegularPad().Get(),
                            *args, **kwargs)

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

    def BasicGrid(self, *args, **kwargs):
        tk.Label.grid(self, *args, **kwargs)


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


class SmallLabel(_DefaultLabel):
    def __init__(self, *args, **kwargs):
        _DefaultLabel.__init__(self,
                               font=SmallFont(),
                               *args, **kwargs)

    def grid(self, *args, **kwargs):
        _DefaultLabel.grid(self,
                           padx=SmallPad().Get(),
                           pady=SmallPad().Get(),
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


# - - - - #
# V A R S #
# - - - - #

class StringVar(tk.StringVar):
    pass


class IntVar(tk.IntVar):
    pass


# - - - - - - - #
# L I S T B O X #
# - - - - - - - #

class _DefaultListbox(tk.Listbox):

    def DeleteSelected(self):
        Selection = reversed(self.curselection())
        for SelectedIndex in Selection:
            self.delete(SelectedIndex)

    def AddItem(self, String):
        self.insert('end', String)

    def AddItems(self, StringsList):
        for String in StringsList:
            self.AddItem(String)

    def DeleteAll(self):
        self.delete(0, 'end')

    def BasicGrid(self, *args, **kwargs):
        tk.Label.grid(self, *args, **kwargs)


class RegularListox(_DefaultListbox):

    def __init__(self, Master, *args, **kwargs):
        _DefaultListbox.__init__(self, Master,
                                 font=RegularFont(),
                                 relief='flat',
                                 highlightthickness=1,
                                 highlightcolor=SelectedColor().Get(),
                                 highlightbackground=DeselectedColor().Get(),
                                 *args, **kwargs)

    def grid(self, *args, **kwargs):
        _DefaultListbox.grid(self,
                             padx=RegularPad().Get(),
                             pady=RegularPad().Get(),
                             *args, **kwargs)
