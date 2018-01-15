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
        frm = Frame(self, width=500, height=700, bg="green")
        frm.pack(fill=BOTH)
        return frm


    def addLabel(self, master, col, row, text):
        lblName = Label(master, text=text, fg="black")
        lblName.config(width=20, height=2, font="Sans-serif, 17")


    # method for arranging various component
    def arangeComponents(self):
        frm = self.frame()

        # Add Label
        self.addLabel(frm, col=0, row=2, text="Name")

        # Add text field
        self.addTextField(frm, col=3, row=2)

        # Add Label
        self.addLabel(frm, col=0, row=4, text="Age")

        # Add text field
        self.addTextField(frm, col=3, row=4)

        # add Button
        bt = Button(frm, text="Submit", fg="black")
        bt.config(font="Sans-serif, 15", width=20, height=2)
        bt.grid(columnspan=5, row=6)

    # Run method for running form
    def run(self):
        self.arangeComponents()
        self.mainloop()



