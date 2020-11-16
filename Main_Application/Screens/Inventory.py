#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#    Nov 08, 2020 11:54:31 PM EST  platform: Windows NT

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

import Inventory_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    Inventory_support.set_Tk_var()
    top = Toplevel1 (root)
    Inventory_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    Inventory_support.set_Tk_var()
    top = Toplevel1 (w)
    Inventory_support.init(w, top, *args, **kwargs)
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
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1173x873+319+95")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.canvas_base = tk.Canvas(top)
        self.canvas_base.place(relx=0.06, rely=0.126, relheight=0.687
                , relwidth=0.873)
        self.canvas_base.configure(background="#3e3c55")
        self.canvas_base.configure(borderwidth="2")
        self.canvas_base.configure(highlightbackground="#d9d9d9")
        self.canvas_base.configure(highlightcolor="black")
        self.canvas_base.configure(insertbackground="black")
        self.canvas_base.configure(relief="ridge")
        self.canvas_base.configure(selectbackground="blue")
        self.canvas_base.configure(selectforeground="white")

        self.button_Inventory = tk.Button(self.canvas_base)
        self.button_Inventory.place(relx=0.0, rely=0.0, height=50, width=341)
        self.button_Inventory.configure(activebackground="#ececec")
        self.button_Inventory.configure(activeforeground="#000000")
        self.button_Inventory.configure(background="#d9d9d9")
        self.button_Inventory.configure(disabledforeground="#a3a3a3")
        self.button_Inventory.configure(foreground="#000000")
        self.button_Inventory.configure(highlightbackground="#d9d9d9")
        self.button_Inventory.configure(highlightcolor="black")
        self.button_Inventory.configure(pady="0")
        self.button_Inventory.configure(relief="ridge")
        self.button_Inventory.configure(text='''Inventory''')

        self.button_shoplist = tk.Button(self.canvas_base)
        self.button_shoplist.place(relx=0.332, rely=0.0, height=50, width=342)
        self.button_shoplist.configure(activebackground="#ececec")
        self.button_shoplist.configure(activeforeground="#000000")
        self.button_shoplist.configure(background="#d9d9d9")
        self.button_shoplist.configure(disabledforeground="#a3a3a3")
        self.button_shoplist.configure(foreground="#000000")
        self.button_shoplist.configure(highlightbackground="#d9d9d9")
        self.button_shoplist.configure(highlightcolor="black")
        self.button_shoplist.configure(pady="0")
        self.button_shoplist.configure(relief="ridge")
        self.button_shoplist.configure(text='''Shopping List''')

        self.button_recipies = tk.Button(self.canvas_base)
        self.button_recipies.place(relx=0.664, rely=0.0, height=50, width=341)
        self.button_recipies.configure(activebackground="#ececec")
        self.button_recipies.configure(activeforeground="#000000")
        self.button_recipies.configure(background="#d9d9d9")
        self.button_recipies.configure(disabledforeground="#a3a3a3")
        self.button_recipies.configure(foreground="#000000")
        self.button_recipies.configure(highlightbackground="#d9d9d9")
        self.button_recipies.configure(highlightcolor="black")
        self.button_recipies.configure(pady="0")
        self.button_recipies.configure(relief="ridge")
        self.button_recipies.configure(text='''Recipies''')

        self.entry_barcode = tk.Entry(self.canvas_base)
        self.entry_barcode.place(relx=0.811, rely=0.933, height=20
                , relwidth=0.082)
        self.entry_barcode.configure(background="white")
        self.entry_barcode.configure(disabledforeground="#a3a3a3")
        self.entry_barcode.configure(font="TkFixedFont")
        self.entry_barcode.configure(foreground="#000000")
        self.entry_barcode.configure(highlightbackground="#d9d9d9")
        self.entry_barcode.configure(highlightcolor="black")
        self.entry_barcode.configure(insertbackground="black")
        self.entry_barcode.configure(selectbackground="blue")
        self.entry_barcode.configure(selectforeground="white")

        self.button_in = tk.Button(self.canvas_base)
        self.button_in.place(relx=0.802, rely=0.917, height=50, width=100)
        self.button_in.configure(activebackground="#ececec")
        self.button_in.configure(activeforeground="#000000")
        self.button_in.configure(background="#36a35c")
        self.button_in.configure(disabledforeground="#a3a3a3")
        self.button_in.configure(foreground="#000000")
        self.button_in.configure(highlightbackground="#d9d9d9")
        self.button_in.configure(highlightcolor="black")
        self.button_in.configure(pady="0")
        self.button_in.configure(relief="ridge")
        self.button_in.configure(text='''Scan In''')

        self.button_out = tk.Button(self.canvas_base)
        self.button_out.place(relx=0.9, rely=0.917, height=50, width=100)
        self.button_out.configure(activebackground="#ececec")
        self.button_out.configure(activeforeground="#000000")
        self.button_out.configure(background="#af0101")
        self.button_out.configure(disabledforeground="#a3a3a3")
        self.button_out.configure(foreground="#000000")
        self.button_out.configure(highlightbackground="#d9d9d9")
        self.button_out.configure(highlightcolor="black")
        self.button_out.configure(pady="0")
        self.button_out.configure(relief="ridge")
        self.button_out.configure(text='''Scan Out''')

        self.entry_addShopList = tk.Entry(self.canvas_base)
        self.entry_addShopList.place(relx=0.039, rely=0.933, height=20
                , relwidth=0.248)
        self.entry_addShopList.configure(background="white")
        self.entry_addShopList.configure(disabledforeground="#a3a3a3")
        self.entry_addShopList.configure(font="TkFixedFont")
        self.entry_addShopList.configure(foreground="#000000")
        self.entry_addShopList.configure(highlightbackground="#d9d9d9")
        self.entry_addShopList.configure(highlightcolor="black")
        self.entry_addShopList.configure(insertbackground="black")
        self.entry_addShopList.configure(selectbackground="blue")
        self.entry_addShopList.configure(selectforeground="white")

        self.button_addShopList = tk.Button(self.canvas_base)
        self.button_addShopList.place(relx=0.303, rely=0.933, height=24
                , width=200)
        self.button_addShopList.configure(activebackground="#ececec")
        self.button_addShopList.configure(activeforeground="#000000")
        self.button_addShopList.configure(background="#d9d9d9")
        self.button_addShopList.configure(disabledforeground="#a3a3a3")
        self.button_addShopList.configure(foreground="#000000")
        self.button_addShopList.configure(highlightbackground="#d9d9d9")
        self.button_addShopList.configure(highlightcolor="black")
        self.button_addShopList.configure(pady="0")
        self.button_addShopList.configure(text='''Add To Shopping List''')

        self.frame_invMain = tk.Frame(self.canvas_base)
        self.frame_invMain.place(relx=0.0, rely=0.167, relheight=0.75
                , relwidth=1.0)
        self.frame_invMain.configure(relief='groove')
        self.frame_invMain.configure(borderwidth="2")
        self.frame_invMain.configure(relief="groove")
        self.frame_invMain.configure(background="#585670")
        self.frame_invMain.configure(highlightbackground="#d9d9d9")
        self.frame_invMain.configure(highlightcolor="black")

        self.label_inv_name = tk.Label(self.frame_invMain)
        self.label_inv_name.place(relx=0.127, rely=0.044, height=30, width=125)
        self.label_inv_name.configure(activebackground="#f9f9f9")
        self.label_inv_name.configure(activeforeground="black")
        self.label_inv_name.configure(background="#939393")
        self.label_inv_name.configure(disabledforeground="#a3a3a3")
        self.label_inv_name.configure(foreground="#000000")
        self.label_inv_name.configure(highlightbackground="#d9d9d9")
        self.label_inv_name.configure(highlightcolor="black")
        self.label_inv_name.configure(text='''Name''')

        self.label_inv_quan = tk.Label(self.frame_invMain)
        self.label_inv_quan.place(relx=0.264, rely=0.044, height=30, width=125)
        self.label_inv_quan.configure(activebackground="#f9f9f9")
        self.label_inv_quan.configure(activeforeground="black")
        self.label_inv_quan.configure(background="#939393")
        self.label_inv_quan.configure(disabledforeground="#a3a3a3")
        self.label_inv_quan.configure(foreground="#000000")
        self.label_inv_quan.configure(highlightbackground="#d9d9d9")
        self.label_inv_quan.configure(highlightcolor="black")
        self.label_inv_quan.configure(text='''Quantity''')

        self.label_inv_fg = tk.Label(self.frame_invMain)
        self.label_inv_fg.place(relx=0.4, rely=0.044, height=30, width=125)
        self.label_inv_fg.configure(activebackground="#f9f9f9")
        self.label_inv_fg.configure(activeforeground="black")
        self.label_inv_fg.configure(background="#939393")
        self.label_inv_fg.configure(disabledforeground="#a3a3a3")
        self.label_inv_fg.configure(foreground="#000000")
        self.label_inv_fg.configure(highlightbackground="#d9d9d9")
        self.label_inv_fg.configure(highlightcolor="black")
        self.label_inv_fg.configure(text='''Food Group''')

        self.label_inv_end = tk.Label(self.frame_invMain)
        self.label_inv_end.place(relx=0.537, rely=0.044, height=30, width=125)
        self.label_inv_end.configure(activebackground="#f9f9f9")
        self.label_inv_end.configure(activeforeground="black")
        self.label_inv_end.configure(background="#939393")
        self.label_inv_end.configure(disabledforeground="#a3a3a3")
        self.label_inv_end.configure(foreground="#000000")
        self.label_inv_end.configure(highlightbackground="#d9d9d9")
        self.label_inv_end.configure(highlightcolor="black")
        self.label_inv_end.configure(text='''Entry Date''')

        self.label_inv_exd = tk.Label(self.frame_invMain)
        self.label_inv_exd.place(relx=0.674, rely=0.044, height=30, width=125)
        self.label_inv_exd.configure(activebackground="#f9f9f9")
        self.label_inv_exd.configure(activeforeground="black")
        self.label_inv_exd.configure(background="#939393")
        self.label_inv_exd.configure(disabledforeground="#a3a3a3")
        self.label_inv_exd.configure(foreground="#000000")
        self.label_inv_exd.configure(highlightbackground="#d9d9d9")
        self.label_inv_exd.configure(highlightcolor="black")
        self.label_inv_exd.configure(text='''Exp. Date''')

        self.label_inv_bar = tk.Label(self.frame_invMain)
        self.label_inv_bar.place(relx=0.811, rely=0.044, height=30, width=125)
        self.label_inv_bar.configure(activebackground="#f9f9f9")
        self.label_inv_bar.configure(activeforeground="black")
        self.label_inv_bar.configure(background="#939393")
        self.label_inv_bar.configure(disabledforeground="#a3a3a3")
        self.label_inv_bar.configure(foreground="#000000")
        self.label_inv_bar.configure(highlightbackground="#d9d9d9")
        self.label_inv_bar.configure(highlightcolor="black")
        self.label_inv_bar.configure(text='''Barcode''')

        self.button_inv_del = tk.Button(self.frame_invMain)
        self.button_inv_del.place(relx=0.049, rely=0.044, height=24, width=47)
        self.button_inv_del.configure(activebackground="#ececec")
        self.button_inv_del.configure(activeforeground="#000000")
        self.button_inv_del.configure(background="#af0101")
        self.button_inv_del.configure(disabledforeground="#a3a3a3")
        self.button_inv_del.configure(foreground="#000000")
        self.button_inv_del.configure(highlightbackground="#d9d9d9")
        self.button_inv_del.configure(highlightcolor="black")
        self.button_inv_del.configure(pady="0")
        self.button_inv_del.configure(text='''Delete''')

        self.button_inv_nameAct = tk.Button(self.frame_invMain)
        self.button_inv_nameAct.place(relx=0.127, rely=0.156, height=30
                , width=125)
        self.button_inv_nameAct.configure(activebackground="#ececec")
        self.button_inv_nameAct.configure(activeforeground="#000000")
        self.button_inv_nameAct.configure(background="#d3d3d3")
        self.button_inv_nameAct.configure(disabledforeground="#a3a3a3")
        self.button_inv_nameAct.configure(foreground="#000000")
        self.button_inv_nameAct.configure(highlightbackground="#d9d9d9")
        self.button_inv_nameAct.configure(highlightcolor="black")
        self.button_inv_nameAct.configure(pady="0")
        self.button_inv_nameAct.configure(relief="flat")
        self.button_inv_nameAct.configure(text='''NAME BUTTON''')

        self.Checkbutton1 = tk.Checkbutton(self.frame_invMain)
        self.Checkbutton1.place(relx=0.049, rely=0.156, relheight=0.056
                , relwidth=0.061)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#585670")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(variable=Inventory_support.che72)

        self.label_inv_quanData = tk.Label(self.frame_invMain)
        self.label_inv_quanData.place(relx=0.264, rely=0.156, height=30
                , width=124)
        self.label_inv_quanData.configure(activebackground="#f9f9f9")
        self.label_inv_quanData.configure(activeforeground="black")
        self.label_inv_quanData.configure(background="#d9d9d9")
        self.label_inv_quanData.configure(disabledforeground="#a3a3a3")
        self.label_inv_quanData.configure(foreground="#000000")
        self.label_inv_quanData.configure(highlightbackground="#d9d9d9")
        self.label_inv_quanData.configure(highlightcolor="black")
        self.label_inv_quanData.configure(text='''X''')

        self.label_inv_fgData = tk.Label(self.frame_invMain)
        self.label_inv_fgData.place(relx=0.4, rely=0.156, height=30, width=125)
        self.label_inv_fgData.configure(activebackground="#f9f9f9")
        self.label_inv_fgData.configure(activeforeground="black")
        self.label_inv_fgData.configure(background="#d9d9d9")
        self.label_inv_fgData.configure(disabledforeground="#a3a3a3")
        self.label_inv_fgData.configure(foreground="#000000")
        self.label_inv_fgData.configure(highlightbackground="#d9d9d9")
        self.label_inv_fgData.configure(highlightcolor="black")
        self.label_inv_fgData.configure(text='''X''')

        self.label_inv_endData = tk.Label(self.frame_invMain)
        self.label_inv_endData.place(relx=0.537, rely=0.156, height=30
                , width=125)
        self.label_inv_endData.configure(activebackground="#f9f9f9")
        self.label_inv_endData.configure(activeforeground="black")
        self.label_inv_endData.configure(background="#d9d9d9")
        self.label_inv_endData.configure(disabledforeground="#a3a3a3")
        self.label_inv_endData.configure(foreground="#000000")
        self.label_inv_endData.configure(highlightbackground="#d9d9d9")
        self.label_inv_endData.configure(highlightcolor="black")
        self.label_inv_endData.configure(text='''X''')

        self.label_inv_exdData = tk.Label(self.frame_invMain)
        self.label_inv_exdData.place(relx=0.674, rely=0.156, height=30
                , width=125)
        self.label_inv_exdData.configure(activebackground="#f9f9f9")
        self.label_inv_exdData.configure(activeforeground="black")
        self.label_inv_exdData.configure(background="#d9d9d9")
        self.label_inv_exdData.configure(disabledforeground="#a3a3a3")
        self.label_inv_exdData.configure(foreground="#000000")
        self.label_inv_exdData.configure(highlightbackground="#d9d9d9")
        self.label_inv_exdData.configure(highlightcolor="black")
        self.label_inv_exdData.configure(text='''X''')

        self.label_inv_barcData = tk.Label(self.frame_invMain)
        self.label_inv_barcData.place(relx=0.811, rely=0.156, height=30
                , width=125)
        self.label_inv_barcData.configure(activebackground="#f9f9f9")
        self.label_inv_barcData.configure(activeforeground="black")
        self.label_inv_barcData.configure(background="#d9d9d9")
        self.label_inv_barcData.configure(disabledforeground="#a3a3a3")
        self.label_inv_barcData.configure(foreground="#000000")
        self.label_inv_barcData.configure(highlightbackground="#d9d9d9")
        self.label_inv_barcData.configure(highlightcolor="black")
        self.label_inv_barcData.configure(text='''X''')

        self.frame_inv_search = tk.Frame(self.canvas_base)
        self.frame_inv_search.place(relx=0.0, rely=0.083, relheight=0.083
                , relwidth=1.0)
        self.frame_inv_search.configure(relief='groove')
        self.frame_inv_search.configure(borderwidth="2")
        self.frame_inv_search.configure(relief="groove")
        self.frame_inv_search.configure(background="#737373")
        self.frame_inv_search.configure(highlightbackground="#d9d9d9")
        self.frame_inv_search.configure(highlightcolor="black")

        self.entry_inv_search = tk.Entry(self.frame_inv_search)
        self.entry_inv_search.place(relx=0.02, rely=0.3, height=20
                , relwidth=0.17)
        self.entry_inv_search.configure(background="white")
        self.entry_inv_search.configure(disabledforeground="#a3a3a3")
        self.entry_inv_search.configure(font="TkFixedFont")
        self.entry_inv_search.configure(foreground="#000000")
        self.entry_inv_search.configure(highlightbackground="#d9d9d9")
        self.entry_inv_search.configure(highlightcolor="black")
        self.entry_inv_search.configure(insertbackground="black")
        self.entry_inv_search.configure(selectbackground="blue")
        self.entry_inv_search.configure(selectforeground="white")

        self.button_inv_search = tk.Button(self.frame_inv_search)
        self.button_inv_search.place(relx=0.205, rely=0.3, height=24, width=47)
        self.button_inv_search.configure(activebackground="#ececec")
        self.button_inv_search.configure(activeforeground="#000000")
        self.button_inv_search.configure(background="#d9d9d9")
        self.button_inv_search.configure(disabledforeground="#a3a3a3")
        self.button_inv_search.configure(foreground="#000000")
        self.button_inv_search.configure(highlightbackground="#d9d9d9")
        self.button_inv_search.configure(highlightcolor="black")
        self.button_inv_search.configure(pady="0")
        self.button_inv_search.configure(text='''Search''')

        self.combo_inv_type = ttk.Combobox(self.frame_inv_search)
        self.combo_inv_type.place(relx=0.508, rely=0.3, relheight=0.42
                , relwidth=0.146)
        self.combo_inv_type.configure(textvariable=Inventory_support.combobox)
        self.combo_inv_type.configure(takefocus="")

        self.combo_inv_crit = ttk.Combobox(self.frame_inv_search)
        self.combo_inv_crit.place(relx=0.664, rely=0.3, relheight=0.42
                , relwidth=0.14)
        self.combo_inv_crit.configure(textvariable=Inventory_support.combobox)
        self.combo_inv_crit.configure(takefocus="")

        self.button_inv_filter = tk.Button(self.frame_inv_search)
        self.button_inv_filter.place(relx=0.82, rely=0.3, height=24, width=70)
        self.button_inv_filter.configure(activebackground="#ececec")
        self.button_inv_filter.configure(activeforeground="#000000")
        self.button_inv_filter.configure(background="#d9d9d9")
        self.button_inv_filter.configure(disabledforeground="#a3a3a3")
        self.button_inv_filter.configure(foreground="#000000")
        self.button_inv_filter.configure(highlightbackground="#d9d9d9")
        self.button_inv_filter.configure(highlightcolor="black")
        self.button_inv_filter.configure(pady="0")
        self.button_inv_filter.configure(text='''Filter''')

        self.button_inv_CLfilter = tk.Button(self.frame_inv_search)
        self.button_inv_CLfilter.place(relx=0.908, rely=0.3, height=24, width=70)

        self.button_inv_CLfilter.configure(activebackground="#ececec")
        self.button_inv_CLfilter.configure(activeforeground="#000000")
        self.button_inv_CLfilter.configure(background="#d9d9d9")
        self.button_inv_CLfilter.configure(disabledforeground="#a3a3a3")
        self.button_inv_CLfilter.configure(foreground="#000000")
        self.button_inv_CLfilter.configure(highlightbackground="#d9d9d9")
        self.button_inv_CLfilter.configure(highlightcolor="black")
        self.button_inv_CLfilter.configure(pady="0")
        self.button_inv_CLfilter.configure(text='''Clear Filter''')

if __name__ == '__main__':
    vp_start_gui()





