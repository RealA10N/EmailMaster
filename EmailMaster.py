from Assets.SenderGUI import Window
from threading import Thread
from tkinter import messagebox
import Assets.EmailSender as Sender


class EmailMaster():

    def __init__(self):

        self._Window = Window()

        self.Window().ConfigSendButtonFunc(self.SendButtonClick)

        self.Window().mainloop()

    def Window(self):
        return self._Window

    def SendButtonClick(self):
        self.Window().SetSendingProfile()
        SendThread = Thread(target=self.SendEmail)
        SendThread.start()  # self.SendEmail()

    def SendEmail(self):
        email = Sender.Email(SenderEmail=self.Window().GetSenderAddress(),
                             SenderPassword=self.Window().GetSenderPassword(),
                             Addressee=self.Window().GetAddressee(),
                             Subject=self.Window().GetSubject(),
                             Content=self.Window().GetContent(),
                             FilePaths=self.Window().GetFilePaths())

        try:
            email.Send()
        except Sender.FailedToSendEmail as Messege:
            self._RaiseErrorPopup(Messege)

        self.Window().SetSendProfile()

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
