import tkinter as tk # For the UI
from tkinter import filedialog, Text
import os # this is uneccisary >>> for opening a program

root  = tk.Tk()
barcodes = []   #stores a list of barcodes that have been scanned

#--------------------------------
# Function Definitions
#--------------------------------

# 
def startRead():
    # refreshes list so values are not repeated in the label
    for widget in frame.winfo_children():
        widget.destroy()

    # Clear the textbox
    tb.delete(0,20)
    # Put cursor in the textbox
    
    tb.focus_set()
    

def addCode(event):
    barcodes.append(tb.get())
    for code in barcodes:
        label = tk.Label(frame, text=code, bg="gray")
        label.pack()
    # Clear the textbox
    tb.delete(0,20)
    # Remove focus from the textbox
    scanBut.focus_set()

#
# UI FORMATING AND COMPONENTS
#
# canvas will hold the screen contents decided by the nav buttons at the top
canvas = tk.Canvas(root, height=600, width=1024, bg="#263D42")  # Size is same as screen

# BEGIN NAVIGATION BUTTONS
inventory = tk.Button(root, text="Inventory", fg ="White", bg="#73489C", width=40, height=5)
shopList = tk.Button(root, text="Shopping List", fg ="White", bg="#73489C", width=40, height=5)
recipies = tk.Button(root, text="Recipies", fg ="White", bg="#73489C", width=40, height=5)


# Scan out barcode button
scanOUT = tk.Button(root, text="Scan OUT", width=10, height=5, fg="White", bg="#C74040")

# Scan in barcode Button
#   when button presses barcode is read (starREad) then barcode is searched for in database
#   if barcode exists in the database increment the count value by 1
#   if barcode does not exist in the database create a new entry
scanIN = tk.Button(root, text="Scan IN", width=10, height=5, fg ="White", bg="#3EC95A", command=startRead)
#scanIN.pack(side=tk.RIGHT, padx=5, pady=5)

# Textbox that read in the barcode from the scanner
tb = tk.Entry(root, width=20)
tb.bind('<Return>', addCode)

# Grid Layout
inventory.grid(row=0, column=0, columnspan=2, sticky="nesw")
shopList.grid(row=0, column=2, columnspan=2, sticky="nesw")
recipies.grid(row=0, column=4, columnspan=2, sticky="nesw")

canvas.grid(row=1,column=0, columnspan=9)

tb.grid(row=8, column=3)
scanIN.grid(row=8, column=5, sticky="nesw")
scanOUT.grid(row=8, column=5, sticky="nesw")

root.mainloop() # makes the UI
# AFTER THIS POINT OCCURS WHEN CLOSING PROGRAM