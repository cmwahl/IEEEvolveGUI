from tkinter import *
import tabSetup.util as util
import math

# data fields pulled from the IEEE Server Blueprint Google Docs
# Field Types:
# Text - any alphanumeric characters, NO SYMBOLS/PUNCTUATION
# Number - numeric characters only, auto converts leading 0s
# Bool - true or false only
# Enum - sort of like radio box, will need to provide options

dataFields = []

dataFields.append({
    "Field": "Name", # name of field, will be displayed next to input
    "Type": "Text", # field type, see above
    "Default": "NAME", # if there's an error in the input, or there's no input, default to this
})
dataFields.append({
    "Field": "Membership Status",
    "Type": "Bool",
    "Default": False,
})
dataFields.append({
    "Field": "Birthday",
    "Type": "Text",
    "Default": "01/01/1900",
})
dataFields.append({
    "Field": "Classification",
    "Type": "Enum",
    "Default": "Others",
    "Options": ["Freshman","Sophomore","Junior","Senior","Graduate","Others"]
})

def setup(self):
    # self is of the Tab class
    # some useful members are:
    # self.tabName - the name of the tab
    # self.displayFrame - the root frame to build all content inside

    columns = 3
    rows = math.ceil(len(dataFields) / columns)

    rowFrames = []
    for i in range(rows):
        frame = Frame(self.displayFrame)
        frame.pack(side=TOP,fill=BOTH,expand='yes')
        rowFrames.append(frame)
    
    counter = 0

    for x in dataFields:
        options = None
        if "Options" in x:
            options = x["Options"]
            
        r = math.floor(counter / 3)
        c = counter % 3
        counter = counter + 1
            
        label = util.newEntryLabel(rowFrames[r], x["Field"], x["Type"], x["Default"], options)

        label.pack(side=LEFT,fill='x',expand='yes')

    button = util.newButton(self.displayFrame, "Submit")
    button.pack(side=BOTTOM,expand='yes')
