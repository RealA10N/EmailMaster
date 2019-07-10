from Assets.SenderGUI import Window
from threading import Thread
from tkinter import messagebox
import Assets.EmailSender as Sender
import pickle


class EmailMaster():

    def __init__(self):

        self._Window = Window()

        self.GetWindow().ConfigSendButtonFunc(self.SendButtonClick)
        self.LoadSettings()

        self.GetWindow().mainloop()

    def GetWindow(self):
        return self._Window

    def SendButtonClick(self):
        self.GetWindow().SetSendingProfile()
        self.SaveSettings()
        SendThread = Thread(target=self.SendEmail)
        SendThread.start()  # self.SendEmail()

    def _SettingsPath(self):
        return 'Saves.EmailMaster'

    def LoadSettings(self):
        SaveLoad = SaveAndLoad(*self.GetWindow().GetWidgetConfigsList())
        try:
            SaveLoad.Load(self._SettingsPath())
        except LoadNotFound:
            pass
        except LoadCorrupted:
            self._RaiseErrorPopup(
                f'The saved fields file has been corrupted. All the fiels are back to default.')

    def SaveSettings(self):
        SaveLoad = SaveAndLoad(*self.GetWindow().GetWidgetConfigsList())
        SaveLoad.Save(self._SettingsPath())

    def SendEmail(self):
        email = Sender.Email(SenderEmail=self.GetWindow().SenderAddress().get(),
                             SenderPassword=self.GetWindow().SenderPassword().get(),
                             Addressee=self.GetWindow().Addressee().get(),
                             Subject=self.GetWindow().Subject().get(),
                             Content=self.GetWindow().Content().get(),
                             FilePaths=self.GetWindow().GetFilePaths())

        try:
            email.Send()
        except Sender.FailedToSendEmail as Messege:
            self._RaiseErrorPopup(Messege)

        self.GetWindow().SetSendProfile()

    def _RaiseErrorPopup(self, ErrorMessage, Title='Failed to send email'):
        GrapicPopup(Title, ErrorMessage).ShowError()


class SaveAndLoad():

    def __init__(self, *WidgetConfigs):
        self._AllElements = WidgetConfigs

    def Save(self, Path):
        Saved = list()
        for Widget in self._AllElements:
            Saved.append(Widget.get())

        with open(Path, 'wb') as File:
            pickle.dump(Saved, File)

    def _Open(self, Path):
        try:
            with open(Path, 'rb') as File:
                Saved = pickle.load(File)
        except FileNotFoundError:
            raise LoadNotFound(F"File '{Path}' doesn't exict")
        except pickle.UnpicklingError:
            raise LoadCorrupted(F"File '{Path}' is corrupted")
        return Saved

    def Load(self, Path):
        Saved = self._Open(Path)

        for Widget, Value in zip(self._AllElements, Saved):
            Widget.set(Value)


class LoadNotFound(FileNotFoundError):
    pass  # Exception class


class LoadCorrupted(Exception):
    pass  # Exception class


class GrapicPopup():

    def __init__(self, Title, Desc):
        self._TitleDescArgs = [Title, Desc]

    def ShowError(self):
        messagebox.showerror(*self._TitleDescArgs)

    def ShowWarning(self):
        messagebox.showwarning(*self._TitleDescArgs)

    def ShowInfo(self):
        messagebox.showinfo(*self._TitleDescArgs)


if __name__ == "__main__":
    EmailMaster()
