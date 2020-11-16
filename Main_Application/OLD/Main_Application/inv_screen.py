#from tkinter import *
import tkinter as tk # For the UI
from tkinter import filedialog, Text, ttk
import os # this is uneccisary >>> for opening a program

root  = tk.Tk()
root.title("Inventory Screen")

# Create frame
inv_menu = tk.Frame(root, bg = "green")
inv_menu.pack()
inv = tk.Frame(root, bg = "blue", height = 400, width = 400)
inv.pack()

# Control Bar
filter_options = ['Quantity', 'Food Group', 'Entry Date', 'Exp. Date']
fopt.set('Entry Date')
filter_criteria = ['1','2','3','4'] #Place holder
fcrit.set('1')

search_box = tk.Entry(inv, width = 20)
search_box.grid(column = 0, row = 0)
search_but = tk.Button(inv, text = "Search")
search_but.grid(column = 1, row = 0)
filter_label = tk.Label(inv, text = "Filter:")
filter_label.grid(column = 2, row = 0)
filter_type = ttk.Combobox(inv, values = filter_options)
filter_type.grid(column = 3, row = 0)
filter_crit = ttk.Combobox(inv, values = filter_criteria) # Change depending on filter_type
filter_crit.grid(column = 4, row = 0)
filter_but = tk.Button(inv, text = "Filter")
filter_but.grid(column = 5, row = 0)



# Header Labels
item = tk.Label(inv, text = "Name", padx = 10, pady=10)
qua = tk.Label(inv, text = "Quantity", padx=10, pady=10)
type = tk.Lable(inv, text = "Food Group", padx=10, pady=10)
entry_date = tk.Label(inv, text = "Entry Date", padx=10, pady=10)
exp_date = tk.Label(inv, text = "Exp. Date", padx=10, pady=10)

# Make Grid
item.grid(column = 0, row = 1)
qua.grid(column = 1, row = 1)
type.grid(column = 2, row = 1)
entry_date.grid(column = 3, row = 1)
exp_date.grid(column = 4, row = 1)

root.mainloop()
