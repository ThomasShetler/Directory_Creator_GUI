from tkinter import *
import phonebook_func
import phonebook_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500, 300)
        self.master.maxsize(500, 400)
        phonebook_func.center_window(self, 500, 500)
        self.master.title('Tkinter Phone book Demo')
        self.master.config(bg='#f0f0f0')

        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func)
        arg = self.master
        phonebook_gui.load_gui(self)


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
