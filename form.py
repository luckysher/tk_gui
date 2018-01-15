

from Tkinter import *


class Form(Tk):
    def __init__(self):
        self.tk = Tk()
        print("Form  class")


    def arangeComponents(self):
        self.frame()

    def run(self):
        self.arangeComponents()
        self.mainloop()



