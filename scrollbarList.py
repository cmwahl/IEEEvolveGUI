from tkinter import *

# simple class to make scroll bar setup easier to manage
class scrollbarList():
    def __init__(self, root):
        self.scrollbar = Scrollbar(root)
        self.scrollbar.pack( side = RIGHT, fill = Y )

        self.list = Listbox(root, yscrollcommand = scrollbar.set )
        self.scrollbar.config( command = mylist.yview )

    # insert and delete behavior identical to Listbox
    # see https://www.tutorialspoint.com/python/tk_listbox.htm

    #example: scrollbarList.insert(END, "This is a new text")
    def insert(*args):
        self.list.insert(*args)

    def delete(*args):
        self.list.insert(*args)

    def getList():
        return self.list

    def pack(*args):
        mylist.pack(*args)
