import tkinter as tk # For the UI
from tkinter import filedialog, Text, ttk

root  = tk.Tk()
root.title("Test 3")


Canvas1 = tk.Canvas(root)
Canvas1.place(relx=0.2, rely=0.222, relheight=0.451, relwidth=0.772)
Canvas1.configure(background="#fab8db")
Canvas1.configure(borderwidth="2")
Canvas1.configure(insertbackground="black")
Canvas1.configure(relief="ridge")
Canvas1.configure(selectbackground="blue")
Canvas1.configure(selectforeground="white")


root.mainloop()
