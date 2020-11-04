import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import test_2_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    test_2_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    test_2_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
      _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
      _fgcolor = '#000000'  # X11 color: 'black'
      _compcolor = '#d9d9d9' # X11 color: 'gray85'
      _ana1color = '#d9d9d9' # X11 color: 'gray85'
      _ana2color = '#ececec' # Closest X11 color: 'gray92'

      top.geometry("600x450+660+210")
      top.minsize(120, 1)
      top.maxsize(3844, 1061)
      top.resizable(1,  1)
      top.title("New Toplevel")
      top.configure(background="#d9d9d9")

      Canvas1 = tk.Canvas(top)
      Canvas1.place(relx=0.2, rely=0.222, relheight=0.451, relwidth=0.772)

      Canvas1.configure(background="#fab8db")
      Canvas1.configure(borderwidth="2")
      Canvas1.configure(insertbackground="black")
      Canvas1.configure(relief="ridge")
      Canvas1.configure(selectbackground="blue")
      Canvas1.configure(selectforeground="white")

if __name__ == '__main__':
    vp_start_gui()
