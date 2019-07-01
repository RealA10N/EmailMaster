from SenderGUI import Window
from tkinter import messagebox


class EmailMaster():

    def __init__(self):

        self._Window = Window()
        self._Window.mainloop()

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
