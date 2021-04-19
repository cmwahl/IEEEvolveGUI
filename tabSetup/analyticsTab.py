from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 
from matplotlib.figure import Figure 
import pandas as pd
import numpy as np

xl_17_18 = pd.ExcelFile('IEEE_Member_App_17-18.xlsx') # work on reading all .xlsx files in directory (looping)
xl_20_21 = pd.ExcelFile('IEEE_Member_App_20-21.xlsx')

def setup(self):
    # self is of the Tab class
    # some useful members are:
    # self.tabName - the name of the tab
    # self.displayFrame - the root frame to build all content inside

    # Default Option: adds 'Select year' or 'Select event' to beginning of list for default value
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
                  '2022-2023'],
                'Y')

    def pick_year(event):       
        if year_drop.get() == year[1]:
            event_drop.config(value=defop(xl_17_18.sheet_names,'E'))
            event_drop.current(0)
        if year_drop.get() == year[2]:
            event_drop.config(value=["No information available!"]) # write code to scan directory and check if this year's info is avaiable
            event_drop.current(0)
        if year_drop.get() == year[3]:
            event_drop.config(value=["No information available!"])
            event_drop.current(0)
        if year_drop.get() == year[4]:
            event_drop.config(value=defop(xl_20_21.sheet_names,'E'))
            event_drop.current(0)
        if year_drop.get() == year[5]:
            event_drop.config(value=["No information available!"])
            event_drop.current(0)

    # drop-down menu for years
    year_drop = ttk.Combobox(self.displayFrame, value = year)
    year_drop.current(0)
    year_drop.pack(pady=20)
    year_drop.bind("<<ComboboxSelected>>", pick_year)

    # drop-down menu for events
    event_drop = ttk.Combobox(self.displayFrame, value = defop([],'E'))
    event_drop.current(0)
    event_drop.pack()

    # checkbox configuration WIP
    def box_selection():
        if (major_var.get()): # if 'major' box is selected, return 'major' & disable 'class' box
            ttk.Checkbutton(self.displayFrame, variable=class_var, state=DISABLED)
            return 'major'
        if (class_var.get()): # if 'class' box is selected, return 'class' & disable 'major' box
            ttk.Checkbutton(self.displayFrame, variable=major_var, state=DISABLED)
            return 'class'
        if (major_var.get() == 0) & (class_var.get() == 0):
            return 'default'

    # checkbox for major category WIP
    major_var = IntVar()
    major_box = ttk.Checkbutton(self.displayFrame, text='Major',variable=major_var, command=box_selection)
    major_box.pack()

    # checkbox for class category WIP
    class_var = IntVar()
    class_box = ttk.Checkbutton(self.displayFrame, text='Class',variable=class_var, command=box_selection)
    class_box.pack()

    # Resize for bar: adds 0 to first & last index of list, needed because single bar graph will be THICC otherwise
    def resize_for_bar(array):
        array.insert(0,0) # add a zero to beginning of list
        array.insert(2,0) # add a zero to end of the list
        return array

    # Count Frequency: creates dictionary {'Target': # of appearances}
    def CountFrequency(list):
        # Creating an empty dictionary 
        freq = {}
        for item in list:
            if item in freq: # if item is already in dictionary, add count
                freq[item] += 1
            else: # if item is new, add it to the dictionary
                freq[item] = 1
        return freq

    # Attendees: returns an array containing a number of participants for an event, with 'type' returned by check box WIP
    def attendees(file,type):
        if type == 'default':
            fname_list = file['First_Name'].to_list() # EXCELFILE DOES NOT SUPPORT to_list(), need a function that returns column given the name of column
            return len(fname_list)
        if type == 'major': # WILL USE COUNTFREQUENCY
            pass
        if type == 'class': # WILL USE COUNTFREQUENCY 
            pass

    def plot():
        # set figure parameters
        fig = Figure(figsize = (4,5), dpi = 100) # sets parameters (size & dpi [dots per inch]) for the plot

        # function to be graphed
        chart = fig.add_subplot(111) # adding the bar graph (code = 111) to the subplot

        # NEEDS WORK, CASE #1: YEAR SELECTED, CASE #2 DEFAULT/MAJOR/CLASS WIP
        if year_drop.get() == year[1]:
            currentFile = xl_17_18
        if year_drop.get() == year[4]:
            currentFile = xl_20_21
        y = resize_for_bar([attendees(currentFile.parse(event_drop.get()),'default')]) # THIS WILL USE VALUE RETURNED BY attendees()


        x = np.arange(len(y))
        chart.bar(x, y) # plot (x,y)

        # configure axes of bar graph
        chart.set_xticks(x)
        chart.set_xticklabels([" ",event_drop.get()," "]) # REPLACE "TEST" WITH EVENT USER SELECTS FROM DROP-DOWN MENU WIP
        # RESIZE NEEDS TO ONLY HAPPEN FOR ATTENDEES_TOTAL NOT ATTENDEES_MAJOR OR ATTENDEES_CLASS
        chart.set_ylabel("Number of Participants")
        
        # creating the Tkinter canvas 
        # Go here for more info: https://tinyurl.com/yhol3h6s
        canvas = FigureCanvasTkAgg(fig, master = self.displayFrame)
        canvas.draw()
        canvas.get_tk_widget().pack() # placing the canvas on the Tkinter window
        
        # creating the matplotlib toolbar 
        toolbar = NavigationToolbar2Tk(canvas, self.displayFrame) 
        toolbar.update()
        canvas.get_tk_widget().pack() # placing the toolbar on the Tkinter window

    plot_button = Button(self.displayFrame, command = plot, text = "Plot")
    plot_button.pack()
