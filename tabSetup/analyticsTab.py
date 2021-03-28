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

    # Resize for bar: adds 0 to first & last index of list, needed because bar graph will be THICC otherwise
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

    # Attendees : returns an array containing a number of participants for an event, with specified type returned by 'check box'
    def attendees(file,type):
        if type == 'default':
            fname_list = file['First_Name'].to_list()
            return len(fname_list)
        if type == 'major':
            pass
        if type == 'class':
            pass

    def plot():
        # set figure settings
        fig = Figure(figsize = (4, 5), dpi = 100) # sets parameters (size & dpi [dots per inch]) for the plot

        # function to be graphed
        num_attend = resize_for_bar([attendees(xl_20_21,'default')]) # THIS WILL USE VALUE RETURNED BY attendees_t() # Y-VALUES
        chart = fig.add_subplot(111) # adding the bar graph (code = 111) to the subplot
        ind = np.arange(len(num_attend)) # X-VALUES, array with length of num_attend
        chart.bar(ind, num_attend) # plot (x,y)

        # configure axes of bar graph
        chart.set_xticks(ind)
        chart.set_xticklabels([" ",event_drop.get()," "]) # REPLACE "TEST" WITH EVENT USER SELECTS FROM DROP-DOWN MENU
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
