import Assets.BetterTkinter as tk


class Window(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("EmailSender")  # change the os title of window

        TitleFrame(self, row=0, column=0, columnspan=2)
        EmailContentFrame(self, row=1, column=0)
        EmailSenderFrame(self, row=1, column=1, sticky='n')


# - - - - - - - - - - - - #
# L A B E L   F R A M E S #
# - - - - - - - - - - - - #

class _DefaultLabelFrames(tk.LabelFrame):

    def __init__(self, Master, Name, *args, **kwargs):
        tk.LabelFrame.__init__(self, Master, Name)
        tk.LabelFrame.grid(self, *args, **kwargs)


class EmailSenderFrame(_DefaultLabelFrames):

    def __init__(self, Master, *args, **kwargs):
        _DefaultLabelFrames.__init__(self, Master, "Sender info", *args, **kwargs)

        self._SenderEmail = NameEntryFrame(self, 'Sender address', width=20)
        self._SenderEmail.grid(columnspan=2)

        self._SenderPass = NameEntryFrame(
            self, 'Sender password', EntryCh='*', width=20)
        self._SenderPass.grid(columnspan=2)

    def EmailEntry(self):
        return self._SenderEmail

    def PasswordEntry(self):
        return self._SenderPass


class EmailContentFrame(_DefaultLabelFrames):

    def __init__(self, Master, *args, **kwargs):
        _DefaultLabelFrames.__init__(self, Master, "Email info", *args, **kwargs)

        self._EmailSubject = NameEntryFrame(self, 'Subject', width=30)
        self._EmailSubject.grid()

        self._EmailContent = NameTextFrame(self, 'Content', width=30)
        self._EmailContent.grid()

    def SubjectEntry(self):
        return self._EmailSubject

    def ContentTextField(self):
        return self._EmailContent


class TitleFrame(tk.Frame):

    def __init__(self, Master, *args, **kwargs):
        tk.Frame.__init__(self, Master)

        tk.BigLabel(self, text='EmailSender').BasicGrid()
        tk.SmallLabel(self, text='By RealA10N').BasicGrid()

        tk.Frame.grid(self, *args, **kwargs)


# - - - - - - - - - - - #
# N A M E   F R A M E S #
# - - - - - - - - - - - #

class _DefaultNameFrame(tk.Frame):

    def __init__(self, Master, Name, *args, **kwargs):
        tk.Frame.__init__(self, Master, *args, **kwargs)
        tk.SmallLabel(self, text='{}:'.format(Name)).BasicGrid(sticky='w')


class NameEntryFrame(_DefaultNameFrame):

    def __init__(self, Master, Name, DefaultText='', EntryCh='', width=30, *args, **kwargs):
        _DefaultNameFrame.__init__(self, Master, Name, *args, **kwargs)

        self._value = tk.StringVar()
        self.set(DefaultText)
        tk.RegularEntry(self, textvariable=self._value, show=EntryCh, width=width).grid()

    def set(self, string):
        self._value.set(string)

    def get(self):
        return self._value.get()


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


# - - - - #
# M A I N #
# - - - - #

if __name__ == "__main__":
    root = Window()
    root.mainloop()
