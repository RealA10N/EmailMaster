import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os import path


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
        try:
            file = open(FilePath, 'rb')
        except FileNotFoundError:
            raise FailedToSendEmail(f'Failed to load {path.basename(FilePath)}')

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


class FailedToSendEmail(Exception):
    pass  # Exception class
