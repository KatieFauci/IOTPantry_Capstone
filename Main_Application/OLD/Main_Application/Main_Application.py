#from tkinter import *
import tkinter as tk # For the UI
import mysql.connector
from tkinter import filedialog, Text
import os # this is uneccisary >>> for opening a program

root  = tk.Tk()
root.title("IOT Pantry System")
barcodes = []   #stores a list of barcodes that have been scanned

db = mysql.connector.conect(user="root",
                            passowrd="password",
                            host='localhost',
                            database='test_inventory')

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

def sw_i():
    raise i

def sw_s():
    raise s

def sw_r():
    raise r



#------------------------------------
# UI FORMATING AND COMPONENTS
#------------------------------------

# canvas will hold the screen contents decided by the nav buttons at the top
sho = tk.Frame(root, height=550, width=1024, bg="blue")# bg="#6a9164")
rec = tk.Frame(root, height=550, width=1024, bg="green")#bg="#7c5487")
inv = tk.Frame(root, height=550, width=1024, bg="red")# bg="#263D42")  # Size is same as screen


# BEGIN NAVIGATION BUTTONS
#self.controller = controller **
inventory = tk.Button(root, text="Inventory", fg ="White", bg="#73489C", height=5)#, command=lambda: controller.show_frame("i"))
shopList = tk.Button(root, text="Shopping List", fg ="White", bg="#73489C", height=5)#, command=lambda: controller.show_frame("s"))
recipies = tk.Button(root, text="Recipies", fg ="White", bg="#73489C", height=5)#, command=lambda: controller.show_frame("r"))

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






#--------------------------------
# UI Grid Layout
#--------------------------------

# Main Screens (stacked)
inv.grid(row=1,column=0, columnspan=6)
sho.grid(row=1,column=0, columnspan=6)
rec.grid(row=1,column=0, columnspan=6)

# Navigation Buttons
inventory.grid(row=0, column=0, columnspan=2, sticky="nesw")
shopList.grid(row=0, column=2, columnspan=2, sticky="nesw")
recipies.grid(row=0, column=4, columnspan=2, sticky="nesw")

# Barcode controls
tb.grid(row=8, column=3)
scanIN.grid(row=8, column=4, sticky="nesw")
scanOUT.grid(row=8, column=5, sticky="nesw")

#---------------------------------
# Inventory Screen
#---------------------------------
lab = Label(i, text = "THIS IS THE INVENTORY SCREEN", bg = "gray", pady=20, padx=20)
lab.pack()
for r in range(5):
    for c in range(4):
        l = Label(inv, text="Test", padx=10)
        l.grid(row=r,column=r)


#---------------------------------
# Shopping List Screen
#---------------------------------
for r in range(5):
    for c in range(4):
        e = Entry(sho, width=20, fg='blue', font=('Arial',12,'bold'))
        e.grid(row=r,column=c)
        e.insert("Test")

#---------------------------------
# Recipies Screen
#---------------------------------
for r in range(5):
    for c in range(4):
        e = Entry(rec, width=20, fg='blue', font=('Arial',12,'bold'))
        e.grid(row=r,column=c)
        e.insert("Test")



root.mainloop() # makes the UI
# AFTER THIS POINT OCCURS WHEN CLOSING PROGRAM
