import Assets.BetterTkinter as tk


class Window(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("EmailSender")  # change the os title of window
        TitleFrame(self).grid(row=0, column=0)  # adds title inside the window

        NameEntryFrame('Your email').grid()
        NameEntryFrame('Your email password', EntryCh='*').grid()


# - - - - - - - - - - - - #
# L A B E L   F R A M E S #
# - - - - - - - - - - - - #

class EmailContentFrame(tk.LabelFrame):

    def __init__(self, Master, *args, **kwargs):
        tk.LabelFrame.__init__(self, Master, "Email info")

        self._EmailSubject = NameEntryFrame(self, 'Subject', width=30)
        self._EmailSubject.grid()

        self._EmailContent = NameTextFrame(self, 'Content', width=30)
        self._EmailContent.grid()

        tk.LabelFrame.grid(self, *args, **kwargs)

    def SubjectEntry(self):
        return self.__EmailSubject

    def ContentTextField(self):
        return self._EmailContent


class TitleFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        tk.BigLabel(self, text='EmailSender').BasicGrid()
        tk.SmallLabel(self, text='By RealA10N').BasicGrid()


class _DefaultNameFrame(tk.Frame):

    def __init__(self, Master, Name, *args, **kwargs):
        tk.Frame.__init__(self, Master, *args, **kwargs)
        tk.SmallLabel(self, text='{}:'.format(Name)).BasicGrid(sticky='w')


class NameEntryFrame(_DefaultNameFrame):

    def __init__(self, Master, Name, DefaultText='', EntryCh='', width=30, *args, **kwargs):
        _DefaultNameFrame.__init__(self, Master, Name, *args, **kwargs)

        self._value = tk.StringVar()
        self.set(DefaultText)
        tk.RegularEntry(self, textvariable=self._value, show=EntryCh).grid()

    def set(self, string):
        self._value.set(string)


class NameTextFrame(_DefaultNameFrame):

    def __init__(self, Master, Name,
                 width=30, height=10, *args, **kwargs):
        _DefaultNameFrame.__init__(self, Master, Name, *args, **kwargs)

        self._Text = tk.RegularText(self, width=width, height=height)
        self._Text.grid()

    def clear(self):
        self._Text.delete('1.0', 'end')

    def set(self, string):
        self.clear()
        self._Text.insert('end', string)

    def get(self):
        return self._Text.get('1,0', 'end')


if __name__ == "__main__":
    root = Window()
    root.mainloop()
