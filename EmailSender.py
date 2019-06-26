import Assets.BetterTkinter as tk


class Window(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.title("EmailSender")
        TitleFrame(self).grid()


class TitleFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        tk.BigLabel(self, text='EmailSender').BasicGrid()
        tk.SmallLabel(self, text='By RealA10N').BasicGrid()


class NameEntry(tk.Frame):

    def __init__(self, Name, DefaultEntry='', EntryCh='', *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self._value = tk.StringVar()
        self.SetValue(DefaultEntry)

        self._Label = tk.SmallLabel(self, text='{}:'.format(Name))
        self._Label.BasicGrid(sticky='w')

        self._Entry = tk.RegularEntry(self, textvariable=self._value, show=EntryCh)
        self._Entry.grid()

    def GetValue(self):
        return self._value.get()

    def SetValue(self, string):
        self._value.set(string)


if __name__ == "__main__":
    root = Window()
    root.mainloop()
