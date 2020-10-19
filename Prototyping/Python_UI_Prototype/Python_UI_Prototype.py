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


# UI FORMATING AND COMPONENTS
canvas = tk.Canvas(root, height=600, width=1024, bg="#263D42")  # Size is same as screen
canvas.pack()

frame = tk.Frame(root, bg="Gray")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

scanBut = tk.Button(root, text="Scan Barcode", padx=10, pady=5, fg ="White", bg="#263D42", command=startRead)
scanBut.pack();

tb = tk.Entry(root, width=20)
tb.bind('<Return>', addCode)
tb.pack()

root.mainloop() # makes the UI
# AFTER THIS POINT OCCURS WHEN CLOSING PROGRAM