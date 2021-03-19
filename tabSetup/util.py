# UTILITY MODULE USED BY OTHER TABS

from tkinter import *


# this function creates a label-entry box, such as Name: [  TEXT  ]
def newEntryLabel(root, labelText, labelType, labelDefault, labelOptions):
    frame = Frame(root)
    
    label = Label(frame, text=(labelText + ": "), relief=FLAT)
    label.pack(side = LEFT)
    
    entry = Entry(frame, bd=2)
    entry.pack(side = LEFT)

    return frame

# dummy function
def dummyFunction():
    pass

# this function creates a clickable button
def newButton(root, name, function = dummyFunction):
    button = Button(root, command = dummyFunction, text = name)

    return button
