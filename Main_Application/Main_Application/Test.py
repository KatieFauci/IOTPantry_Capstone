import tkinter as tk

root = tk.Tk()

f = tk.Frame(root, bg = "orange", width = 500, height = 500)
f.pack(side=LEFT, expand = 1)

f3 = tk.Frame(f, bg = "red", width = 500)
f3.pack(side=LEFT, expand = 1, pady = 50, padx = 50)

f2 = tk.Frame(root, bg = "black", height=100, width = 100)
f2.pack(side=LEFT, fill = Y)

b = tk.Button(f2, text = "test")
b.pack()

b = tk.Button(f3, text = "1", bg = "red")
b.grid(row=1, column=3)
b2 = tk.Button(f3, text = "2")
b2.grid(row=1, column=4)
b3 = tk.Button(f3, text = "2")
b3.grid(row=2, column=0)

root.mainloop()
