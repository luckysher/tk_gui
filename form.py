

from Tkinter import *


class Form(Tk):
    def __init__(self):
        self.tk = Tk()
        print("Form  class")

    def frame(self):
        frm = Frame(self, width=60, height=50, bg="green")
        frm.pack()

    def arangeComponents(self):
        self.frame()

    def run(self):
        self.arangeComponents()
        self.mainloop()



