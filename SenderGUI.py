import Assets.BetterTkinter as tk


class Window(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Email Sender")  # change the os title of window
        self.resizable(False, False)

        TitleFrame(self, row=0, column=0, columnspan=2)

        LeftFrame = tk.Frame(self)
        LeftFrame.BasicGrid(row=1, column=0, sticky='n')

        RightFrame = tk.Frame(self)
        RightFrame.BasicGrid(row=1, column=1, sticky='n')

        self._EmailContentFrame = EmailContentFrame(LeftFrame, row=0, column=0)
        self._SendEmailFrame = SendEmailFrame(LeftFrame, row=1, column=0)
        self._EmailSenderFrame = EmailSenderFrame(RightFrame, row=0, column=0)
        self._AttachFilesFrame = AttachFilesFrame(RightFrame, row=1, column=0)

    def ConfigSendButtonFunc(self, func):
        self._SendEmailFrame.ConfigSendButtonFunc(func)

    def GetSubject(self):
        return self._EmailContentFrame.GetSubject()

    def GetContent(self):
        return self._EmailContentFrame.GetContent()

    def GetSenderAddress(self):
        return self._EmailSenderFrame.GetSenderAddress()

    def GetSenderPassword(self):
        return self._EmailSenderFrame.GetSenderPassword()

    def GetAddressee(self):
        return self._SendEmailFrame.GetAddressee()


# - - - - - - - - - - - - #
# L A B E L   F R A M E S #
# - - - - - - - - - - - - #

class _DefaultLabelFrames(tk.LabelFrame):

    def __init__(self, Master, Name, *args, **kwargs):
        tk.LabelFrame.__init__(self, Master, Name)
        tk.LabelFrame.grid(self, *args, **kwargs)


class AttachFilesFrame(_DefaultLabelFrames):

    def __init__(self, Master, *args, **kwargs):
        _DefaultLabelFrames.__init__(self, Master, "Attach Files", *args, **kwargs)

        self._FilesListbox = tk.RegularListox(self, selectmode='extended', width=20)
        self._FilesListbox.grid()

        self._FileButtons = AttachFilesButtons(self)
        self._FileButtons.BasicGrid()


class AttachFilesButtons(tk.Frame):

    def __init__(self, Master, *args, **kwargs):
        tk.Frame.__init__(self, Master, *args, **kwargs)

        self._AddButton = tk.RegularButton(self, text="Add files", width=10)
        self._AddButton.grid(row=0, column=0)

        self._DeleteButton = tk.RegularButton(self, text="Delete selected", width=15)
        self._DeleteButton.grid(row=0, column=1)

    def _AddButton(self):
        return self._AddButton

    def _DeleteButton(self):
        return self._DeleteButton


class EmailSenderFrame(_DefaultLabelFrames):

    def __init__(self, Master, *args, **kwargs):
        _DefaultLabelFrames.__init__(self, Master, "Sender info", *args, **kwargs)

        self._SenderEmail = NameEntryFrame(self, 'Sender address', width=20)
        self._SenderEmail.grid()

        self._SenderPass = NameEntryFrame(
            self, 'Sender password', EntryCh='*', width=20)
        self._SenderPass.grid()

    def _AddressEntry(self):
        return self._SenderEmail

    def _PasswordEntry(self):
        return self._SenderPass

    def GetSenderAddress(self):
        return self._AddressEntry().get()

    def GetSenderPassword(self):
        return self._PasswordEntry().get()


class SendEmailFrame(_DefaultLabelFrames):
    def __init__(self, Master, *args, **kwargs):
        _DefaultLabelFrames.__init__(self, Master, "Send", *args, **kwargs)

        self._EmailAddressee = NameEntryFrame(self, 'Addressee', width=30)
        self._EmailAddressee.grid()

        self._SendButton = SendButton(self)

    def ConfigSendButtonFunc(self, func):
        self._SendButton.ConfigFunc(func)

    def _AddresseeEntry(self):
        return self._EmailAddressee

    def GetAddressee(self):
        return self._AddresseeEntry().get()


class EmailContentFrame(_DefaultLabelFrames):

    def __init__(self, Master, *args, **kwargs):
        _DefaultLabelFrames.__init__(self, Master, "Email info", *args, **kwargs)

        self._EmailSubject = NameEntryFrame(self, 'Subject', width=30)
        self._EmailSubject.grid()

        self._EmailContent = NameTextFrame(self, 'Content', width=30)
        self._EmailContent.grid()

    def _SubjectEntry(self):
        return self._EmailSubject

    def _ContentTextField(self):
        return self._EmailContent

    def GetSubject(self):
        return self._SubjectEntry().get()

    def GetContent(self):
        return self._ContentTextField().get()


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

    def get(self):
        return self._Text.get()


# - - - - - - - - - - - - - - - #
# C U S T O M   E L E M E N T S #
# - - - - - - - - - - - - - - - #

class SendButton(tk.RegularButton):

    def __init__(self, master, *args, **kwargs):
        tk.RegularButton.__init__(self, master, command=lambda: self.ButtonClick())
        tk.RegularButton.grid(self, *args, **kwargs)

        self._Enabled = None
        self._ClickFunc = None

        self.SetSendProfile()

    def ButtonClick(self):
        if self._Enabled:
            self.SetSendingProfile()
            if self._ClickFunc is not None:
                self._ClickFunc()

    def ConfigFunc(self, FuncPointer):
        self._ClickFunc = FuncPointer

    def SetSendProfile(self):
        self.config(text="Send!", state='normal')
        self._Enabled = True

    def SetSendingProfile(self):
        self.config(text="Sending...", state='disabled')
        self._Enabled = False


# - - - - #
# M A I N #
# - - - - #

if __name__ == "__main__":
    root = Window()
    root.mainloop()
