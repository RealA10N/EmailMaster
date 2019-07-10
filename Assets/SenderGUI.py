import Assets.BetterTkinter as tk
from os import path


class Window(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("EmailMaster")  # change the os title of window
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

    def Subject(self):
        return self._EmailContentFrame.Subject()

    def Content(self):
        return self._EmailContentFrame.Content()

    def SenderAddress(self):
        return self._EmailSenderFrame.SenderAddress()

    def SenderPassword(self):
        return self._EmailSenderFrame.SenderPassword()

    def Addressee(self):
        return self._SendEmailFrame.Addressee()

    def GetFilePaths(self):
        return self._AttachFilesFrame.GetFilePaths()

    def SetSendProfile(self):
        self._SendEmailFrame.SetSendProfile()

    def SetSendingProfile(self):
        self._SendEmailFrame.SetSendingProfile()

    def GetWidgetConfigsList(self):
        return [self.SenderAddress(),
                self.SenderPassword(),
                self.Addressee(),
                self.Subject(),
                self.Content()]


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

        self._FileButtons.ConfigAddButtonFunc(lambda: self.AddFiles())
        self._FileButtons.ConfigDeleteButtonFunc(lambda: self.DeleteSelectedFile())

        self._FilePaths = []

    def _GetFilesListbox(self):
        return self._FilesListbox

    def AddFiles(self):
        NewFiles = tk.askopenfilenames(title="Selecte files")

        for FilePath in NewFiles:
            self._GetFilesListbox().AddItem(path.basename(FilePath))  # add basename to gui
            self._FilePaths.append(FilePath)  # add full path to list

    def DeleteSelectedFile(self):
        SelectedIndexes = reversed(self._GetFilesListbox().GetSelectedIndexes())

        for Index in SelectedIndexes:
            self._GetFilesListbox().delete(Index)  # remove basename from gui
            self._FilePaths.pop(Index)  # remove full path from list

    def GetFilePaths(self):
        return self._FilePaths


class AttachFilesButtons(tk.Frame):

    def __init__(self, Master, *args, **kwargs):
        tk.Frame.__init__(self, Master, *args, **kwargs)

        self._AddButton = tk.RegularButton(self, text="Add files", width=10)
        self._AddButton.grid(row=0, column=0)

        self._DeleteButton = tk.RegularButton(self, text="Delete selected", width=15)
        self._DeleteButton.grid(row=0, column=1)

    def _GetAddButton(self):
        return self._AddButton

    def _GetDeleteButton(self):
        return self._DeleteButton

    def ConfigAddButtonFunc(self, func):
        self._GetAddButton().config(command=func)

    def ConfigDeleteButtonFunc(self, func):
        self._GetDeleteButton().config(command=func)


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

    def SenderAddress(self):
        return self._AddressEntry().GetConfig()

    def SenderPassword(self):
        return self._PasswordEntry().GetConfig()


class SendEmailFrame(_DefaultLabelFrames):
    def __init__(self, Master, *args, **kwargs):
        _DefaultLabelFrames.__init__(self, Master, "Send", *args, **kwargs)

        self._EmailAddressee = NameEntryFrame(self, 'Addressee', width=30)
        self._EmailAddressee.grid()

        self._SendButton = SendButton(self)

    def _GetSendButton(self):
        return self._SendButton

    def ConfigSendButtonFunc(self, func):
        self._GetSendButton().ConfigFunc(func)

    def SetSendProfile(self):
        self._GetSendButton().SetSendProfile()

    def SetSendingProfile(self):
        self._GetSendButton().SetSendingProfile()

    def _AddresseeEntry(self):
        return self._EmailAddressee

    def Addressee(self):
        return self._AddresseeEntry().GetConfig()


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

    def Subject(self):
        return self._SubjectEntry().GetConfig()

    def Content(self):
        return self._ContentTextField().GetConfig()


class TitleFrame(tk.Frame):

    def __init__(self, Master, *args, **kwargs):
        tk.Frame.__init__(self, Master)

        tk.BigLabel(self, text='EmailMaster').BasicGrid()
        tk.SmallLabel(self, text='By RealA10N').BasicGrid()

        tk.Frame.grid(self, *args, **kwargs)


# - - - - - - - - - - - #
# N A M E   F R A M E S #
# - - - - - - - - - - - #

class _DefaultNameFrame(tk.Frame):

    def __init__(self, Master, Name, *args, **kwargs):
        tk.Frame.__init__(self, Master, *args, **kwargs)
        tk.SmallLabel(self, text='{}:'.format(Name)).BasicGrid(sticky='w')

    def GetConfig(self):
        return self._Widget.GetConfig()


class NameEntryFrame(_DefaultNameFrame):

    def __init__(self, Master, Name, DefaultText='', EntryCh='', width=30, *args, **kwargs):
        _DefaultNameFrame.__init__(self, Master, Name, *args, **kwargs)

        self._Widget = tk.RegularEntry(self, show=EntryCh, width=width)
        self._Widget.grid()

        self.GetConfig().set(DefaultText)


class NameTextFrame(_DefaultNameFrame):

    def __init__(self, Master, Name,
                 width=30, height=10, *args, **kwargs):
        _DefaultNameFrame.__init__(self, Master, Name, *args, **kwargs)

        self._Widget = tk.RegularText(self, width=width, height=height)
        self._Widget.grid()

    def get(self):
        return self._Widget.get()


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
        if self._Enabled and self._ClickFunc is not None:
            self._ClickFunc()

    def ConfigFunc(self, FuncPointer):
        self._ClickFunc = FuncPointer

    def SetSendProfile(self):
        self.config(text="Send!", state='normal')
        self._Enabled = True

    def SetSendingProfile(self):
        self.config(text="Sending...", state='disabled')
        self._Enabled = False
