#################################################################
#                                                               #
# Form class for showing form with multiple components          #
#                                                               #
#################################################################

# imports for various components from TK
from Tkinter import *

# Form class
class Form(Tk):

    # form class constructor
    def __init__(self):
        self.tk = Tk()
        print("Form  class")

    # frame for handling various components
    def frame(self):
        frm = Frame(self, width=900, height=500, bg="green")
        frm.pack()

    # method for arranging various component
    def arangeComponents(self):
        self.frame()

    # Run method for running form
    def run(self):
        self.arangeComponents()
        self.mainloop()



