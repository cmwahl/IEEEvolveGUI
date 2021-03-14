from tkinter import *

def emptyButtonFunction(): 
    print("BUTTON CLICKED")

class Tab:
    def __init__(self, tabFrame, contentFrame, tabName, tabDesc):
        self.tabName = tabName
        self.clickFunction = emptyButtonFunction

        tabButton = Button(tabFrame, text=tabName, command = lambda: self.clickFunction(tabName))
        tabButton.pack(side=LEFT)

        #create a frame for packing
        self.displayFrame = Frame(contentFrame)
        label = Label(self.displayFrame,text=tabDesc)
        label.pack(side=TOP)

    def tabClickFunction(self, function):
        self.clickFunction = function

    def passSetupFunction(self, function):
        function(self)

    def hideFrame(self):
        self.displayFrame.pack_forget()

    def showFrame(self):
        self.displayFrame.pack(fill='both', expand='yes')
