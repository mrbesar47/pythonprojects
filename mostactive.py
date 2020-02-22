import tkinter as tk
#import os
#os.system('python newdaydata.py')
from newdaydata import list_of_rows




window = tk.Tk()

# list of fruits
activeTickerList = list_of_rows

#action to be performed when button clicked
def clicked():
    for ind, ticker in enumerate(activeTickerList):
        # print names in the tkinter window
        # create a label widget
        names_label = tk.Label(window)
        # give it a position using grid
        names_label.grid(row=int(ind)+1, column=0)
        # print the fruit name in the label
        names_label.config(text=ticker)

btn = tk.Button(window, text="SEE", command=clicked)
btn.grid(column=0, row=0, padx=30, pady=2)


window.mainloop()