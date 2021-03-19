from tkinter import *
import tab
import tabSetup.tabInformation as tabInformation

def main():
    root = Tk()
    root.title("IEEEvolve Admin")
    root.minsize(800,200)
    root.geometry("600x500")

    tabObjects = []

    tabFrame = Frame(root, bg="#808080")
    tabFrame.pack(side=TOP)

    contentFrame = LabelFrame(root)
    contentFrame.pack(side=TOP, fill='both', expand='yes')

    def updateTabOnClick(tabName): # hide all other tabs and show the one with tabName only
        for x in tabObjects:
            if x.tabName == tabName:
                x.showFrame()
            else:
                x.hideFrame()

    for tabDict in tabInformation.tabs:
        newTab = tab.Tab(tabFrame, contentFrame, tabDict["TabName"], tabDict["Description"])
        newTab.tabClickFunction(updateTabOnClick)
        newTab.passSetupFunction(tabDict["Function"])
        tabObjects.append(newTab)

    tabObjects[0].showFrame()

    mainloop()

main()
