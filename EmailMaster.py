from Assets.SenderGUI import Window
from threading import Thread
from tkinter import messagebox
import Assets.EmailSender as Sender


class EmailMaster():

    def __init__(self):

        self._Window = Window()

        self.GetWindow().ConfigSendButtonFunc(self.SendButtonClick)

        self.GetWindow().mainloop()

    def GetWindow(self):
        return self._Window

    def SendButtonClick(self):
        self.GetWindow().SetSendingProfile()
        SendThread = Thread(target=self.SendEmail)
        SendThread.start()  # self.SendEmail()

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

    def _RaiseErrorPopup(self, ErrorMessege):
        GrapicPopup("Failed to send email", ErrorMessege).ShowError()


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
