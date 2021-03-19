from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 
from matplotlib.figure import Figure 
import pandas as pd

df_17_18 = pd.ExcelFile('IEEE_Member_App_17-18.xlsx') # work on reading all .xlsx files in directory (looping)
df_20_21 = pd.ExcelFile('IEEE_Member_App_20-21.xlsx')

def setup(self):
    # self is of the Tab class
    # some useful members are:
    # self.tabName - the name of the tab
    # self.displayFrame - the root frame to build all content inside

    def plot(): 
        fig = Figure(figsize = (3, 3), dpi = 100) # the figure that will contain the plot
        y = [i**2 for i in range(101)] # list of squares 
        plot1 = fig.add_subplot(111) # adding the subplot 
        plot1.plot(y) # plotting the graph 

        canvas = FigureCanvasTkAgg(fig, master = self.displayFrame) # creating the Tkinter canvas 
        canvas.draw()
        canvas.get_tk_widget().pack() # placing the canvas on the Tkinter window 
        toolbar = NavigationToolbar2Tk(canvas, self.displayFrame) # creating the Matplotlib toolbar 
        toolbar.update()
        canvas.get_tk_widget().pack() # placing the toolbar on the Tkinter window

    # defop (DEFault OPtion): adds 'Select year' or 'Select event' to beginning of list for default value
    def defop(array,var):
        if var == 'Y':
            array.insert(0,'---Select year---')
        if var == 'E':
            array.insert(0,'---Select event---')
        return array

    year = defop(['2017-2018',
                  '2018-2019',
                  '2019-2020',
                  '2020-2021',
                  '2021-2022',
                  '2022-2023'],'Y')

    def pick_year(event):       
        if year_drop.get() == year[1]:
            event_drop.config(value=defop(df_17_18.sheet_names,'E'))
            event_drop.current(0)
        if year_drop.get() == year[2]:
            event_drop.config(value=["No information available!"]) # write code to scan directory and check if this year's info is avaiable
            event_drop.current(0)            
        if year_drop.get() == year[3]:
            event_drop.config(value=["No information available!"])
            event_drop.current(0)
        if year_drop.get() == year[4]:
            event_drop.config(value=defop(df_20_21.sheet_names,'E'))
            event_drop.current(0)            
        if year_drop.get() == year[5]:
            event_drop.config(value=["No information available!"])
            event_drop.current(0)            

    # drop-down menu for years
    year_drop = ttk.Combobox(self.displayFrame, value = year)
    year_drop.current(0)
    year_drop.pack(pady=20)
    year_drop.bind("<<ComboboxSelected>>", pick_year)

    # drop-down menu for event
    event_drop = ttk.Combobox(self.displayFrame, value = defop([],'E'))
    event_drop.current(0)
    event_drop.pack()

    plot_button = Button(self.displayFrame, command = plot, text = "Plot")
    plot_button.pack()
