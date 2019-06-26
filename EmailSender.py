import Assets.BetterTkinter as tk


class Window(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.title("EmailSender")
        TitleFrame(self).grid()


class TitleFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        tk.BigLabel(self, text='EmailSender').BasicGrid()
        tk.SmallLabel(self, text='By RealA10N').BasicGrid()


if __name__ == "__main__":
    root = Window()
    root.mainloop()
