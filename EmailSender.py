import Assets.BetterTkinter as tk


class Window(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.title("EmailSender")

        self.LoadWidgets()

    def LoadWidgets(self):

        SenderEmail = tk.RegularEntry(self)
        SenderEmail.grid()


if __name__ == "__main__":
    root = Window()
    root.mainloop()
