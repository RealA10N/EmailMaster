from SenderGUI import Window
from threading import Thread
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os import path


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
        email = Email(SenderEmail=self.Window().GetSenderAddress(),
                      SenderPassword=self.Window().GetSenderPassword(),
                      Addressee=self.Window().GetAddressee(),
                      Subject=self.Window().GetSubject(),
                      Content=self.Window().GetContent(),
                      FilePaths=self.Window().GetFilePaths())

        try:
            email.Send()
        except FailedToSendEmail as Messege:
            self._RaiseErrorPopup(Messege)

        self.Window().SetSendProfile()

    def _RaiseErrorPopup(self, ErrorMessege):
        GrapicPopup("Failed to send email", ErrorMessege).ShowError()


class Email():

    def __init__(self, SenderEmail, SenderPassword,
                 Addressee, Subject, Content="", FilePaths=[]):

        self._SenderEmail = SenderEmail
        self._SenderPassword = SenderPassword
        self._Addressee = Addressee
        self._Subject = Subject
        self._Content = Content
        self._FilePaths = FilePaths

        self._Server = None

    def _GetHost(self):
        try:
            Host = self._SenderEmail[self._SenderEmail.index('@') + 1:].lower()
        except ValueError:
            raise FailedToSendEmail(f'Sender email "{self._SenderEmail}" is invalid')

        return Host

    def _ConnectToHost(self):
        try:
            self._Server = smtplib.SMTP(f"smtp.{self._GetHost()}", 587)
        except smtplib.socket.gaierror:
            raise FailedToSendEmail(
                f'Can not connect to host "{self._GetHost()}", or host not supported')

        self._Server.starttls()

    def _Login(self):
        self._ConnectToHost()

        try:
            self._Server.login(self._SenderEmail, self._SenderPassword)
        except smtplib.SMTPAuthenticationError:
            raise FailedToSendEmail(f'Failed to login to "{self._SenderEmail}"')

    def _QuitServer(self):
        if self._Server is not None:
            self._Server.quit()
            self._Server = None

    def _GetMsg(self):
        Msg = MIMEMultipart()

        Msg['From'] = self._SenderEmail                 # sender
        Msg['To'] = self._Addressee                     # addressee
        Msg['Subject'] = self._Subject                  # subject
        Msg.attach(MIMEText(self._Content, 'plain'))    # contect

        for FilePath in self._FilePaths:                # files
            FilePart = self._GetFilePart(FilePath)
            Msg.attach(FilePart)

        return Msg.as_string()

    def _GetFilePart(self, FilePath):
        file = open(FilePath, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " +
                        path.basename(FilePath))
        return part

    def Send(self):
        self._Login()
        Msg = self._GetMsg()
        self._Server.sendmail(self._SenderEmail, self._Addressee, Msg)


class GrapicPopup():

    def __init__(self, Title, Desc):
        self._TitleDescArgs = [Title, Desc]

    def ShowError(self):
        messagebox.showerror(*self._TitleDescArgs)

    def ShowWarning(self):
        messagebox.showwarning(*self._TitleDescArgs)

    def ShowInfo(self):
        messagebox.showinfo(*self._TitleDescArgs)


class FailedToSendEmail(Exception):
    pass  # Exception class


if __name__ == "__main__":
    EmailMaster()
