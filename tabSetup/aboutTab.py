from tkinter import *

def setup(self):
    # self is of the Tab class
    # some useful members are:
    # self.tabName - the name of the tab
    # self.displayFrame - the root frame to build all content inside

    #var = StringVar()
    text = Message(
        self.displayFrame,
        anchor='n',
        text = """About IEEEngage
IEEEngage is a newly-developed and digitized portion of IEEE UH.
It seeks to improve the organization through automation of many key tasks (announcements, membership updates), and through analytics."""
    )

    #var.set("About IEEEngage\n\nIEEEngage is a newly-developed and digitized portion of IEEE UH.\nIt seeks to improve the organization through automation of many key tasks (announcements, membership updates), and through analytics.")

    text.pack(fill='both', expand='yes')
