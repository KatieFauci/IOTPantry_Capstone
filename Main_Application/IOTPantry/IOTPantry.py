#!/usr/bin/env python3
import sys
import tkinter as tk
import Tcl
import sqlite3
from datetime import date
import math
import addfunc
import delfunc
import invfunc
import slfunc
import rfunc

# GLOBAL Constants
END = 50

# Global Control VARIABLES
CURRENTSCREEN = 1

# Global inventory Variables
NUMPAGES_INV = 0
FIRSTLIST_INV = 0
CURRENTPAGE_INV = 0
MAXPERPAGE_INV = 8
curInv = []
inv_widgets = []

# Global SL VARIABLES
sl_widgets = []
FIRSTLIST_SL = 0;
CURRENTPAGE_SL = 0
NUMPAGES_SL = 0
LASTNUMPAGES_SL = 0
MAXPERPAGE_SL = 10
CURRENT_SL_ITEM = 0

# Global recipie variables
MAXPERPAGE_R = 5
r_widgets = []
FIRSTLIST_R = 0
CURRENTPAGE_R = 0
NUMPAGES_R = 0
CURRENT_R = 0

# Connect to databases
invdb = sqlite3.connect('inventory.db')
refdb = sqlite3.connect('ref.db')

#------------------------------------
# Screen Configuration Functions
#------------------------------------
def configure_root():
    # Build componrnts
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    root.geometry("1173x873+319+95")
    root.minsize(1024,600)
    root.maxsize(1024,600)
    root.resizable(1,  1)
    root.configure(background="#d9d9d9")
    root.configure(highlightbackground="#d9d9d9")
    root.configure(highlightcolor="black")
def configure_base():
    canvas_base.place(relx=0, rely=0, relheight=1, relwidth=1)
    canvas_base.configure(background="#3e3c55")
    canvas_base.configure(borderwidth="2")
    canvas_base.configure(highlightbackground="#d9d9d9")
    canvas_base.configure(highlightcolor="black")
    canvas_base.configure(insertbackground="black")
    canvas_base.configure(relief="ridge")
    canvas_base.configure(selectbackground="blue")
    canvas_base.configure(selectforeground="white")

    button_Inventory.place(relx=0.0, rely=0.0, height=50, width=341)
    button_Inventory.configure(activebackground="#ececec")
    button_Inventory.configure(activeforeground="#000000")
    button_Inventory.configure(background="#d9d9d9")
    button_Inventory.configure(disabledforeground="#a3a3a3")
    button_Inventory.configure(foreground="#000000")
    button_Inventory.configure(highlightbackground="#d9d9d9")
    button_Inventory.configure(highlightcolor="black")
    button_Inventory.configure(pady="0")
    button_Inventory.configure(relief="ridge")
    button_Inventory.configure(text='''Inventory''')
    button_Inventory.configure(command=focus_inv)

    button_shoplist.place(relx=0.332, rely=0.0, height=50, width=342)
    button_shoplist.configure(activebackground="#ececec")
    button_shoplist.configure(activeforeground="#000000")
    button_shoplist.configure(background="#d9d9d9")
    button_shoplist.configure(disabledforeground="#a3a3a3")
    button_shoplist.configure(foreground="#000000")
    button_shoplist.configure(highlightbackground="#d9d9d9")
    button_shoplist.configure(highlightcolor="black")
    button_shoplist.configure(pady="0")
    button_shoplist.configure(relief="ridge")
    button_shoplist.configure(text='''Shopping List''')
    button_shoplist.configure(command=focus_sl)

    button_recipies.place(relx=0.664, rely=0.0, height=50, width=341)
    button_recipies.configure(activebackground="#ececec")
    button_recipies.configure(activeforeground="#000000")
    button_recipies.configure(background="#d9d9d9")
    button_recipies.configure(disabledforeground="#a3a3a3")
    button_recipies.configure(foreground="#000000")
    button_recipies.configure(highlightbackground="#d9d9d9")
    button_recipies.configure(highlightcolor="black")
    button_recipies.configure(pady="0")
    button_recipies.configure(relief="ridge")
    button_recipies.configure(text='''Recipies''')
    button_recipies.configure(command=focus_rec)

    entry_barcode.place(relx=0.811, rely=0.933, height=20, relwidth=0.082)
    entry_barcode.configure(background="white")
    entry_barcode.configure(disabledforeground="#a3a3a3")
    entry_barcode.configure(font="TkFixedFont")
    entry_barcode.configure(foreground="#000000")
    entry_barcode.configure(highlightbackground="#d9d9d9")
    entry_barcode.configure(highlightcolor="black")
    entry_barcode.configure(insertbackground="black")
    entry_barcode.configure(selectbackground="blue")
    entry_barcode.configure(selectforeground="white")
    entry_barcode.bind('<Return>',scan_out)

    button_in.place(relx=0.801, rely=0.917, height=50, width=100)
    button_in.configure(activebackground="#ececec")
    button_in.configure(activeforeground="#000000")
    button_in.configure(background="#36a35c")
    button_in.configure(disabledforeground="#a3a3a3")
    button_in.configure(foreground="#000000")
    button_in.configure(highlightbackground="#d9d9d9")
    button_in.configure(highlightcolor="black")
    button_in.configure(pady="0")
    button_in.configure(text='''Scan In''')
    button_in.configure(command=focus_barEntry)

    button_out.place(relx=0.899, rely=0.917, height=50, width=100)
    button_out.configure(activebackground="#ececec")
    button_out.configure(activeforeground="#000000")
    button_out.configure(background="#af0101")
    button_out.configure(disabledforeground="#a3a3a3")
    button_out.configure(foreground="#000000")
    button_out.configure(highlightbackground="#d9d9d9")
    button_out.configure(highlightcolor="black")
    button_out.configure(pady="0")
    button_out.configure(text='''Scan Out''')
    button_out.configure(command=focus_delEntry)

    entry_addShopList.place(relx=0.04, rely=0.933, height=20, relwidth=0.19)
    entry_addShopList.configure(background="white")
    entry_addShopList.configure(disabledforeground="#a3a3a3")
    entry_addShopList.configure(font="TkFixedFont")
    entry_addShopList.configure(foreground="#000000")
    entry_addShopList.configure(highlightbackground="#d9d9d9")
    entry_addShopList.configure(highlightcolor="black")
    entry_addShopList.configure(insertbackground="black")
    entry_addShopList.configure(selectbackground="blue")
    entry_addShopList.configure(selectforeground="white")
    entry_addShopList.configure(text="Item")

    entry_notesShopList.place(relx=0.24, rely=0.933, height=20, relwidth=0.15)
    entry_notesShopList.configure(background="white")
    entry_notesShopList.configure(disabledforeground="#a3a3a3")
    entry_notesShopList.configure(font="TkFixedFont")
    entry_notesShopList.configure(foreground="#000000")
    entry_notesShopList.configure(highlightbackground="#d9d9d9")
    entry_notesShopList.configure(highlightcolor="black")
    entry_notesShopList.configure(insertbackground="black")
    entry_notesShopList.configure(selectbackground="blue")
    entry_notesShopList.configure(selectforeground="white")
    entry_notesShopList.configure(text="Notes")

    button_addShopList.place(relx=0.4, rely=0.933, height=24, width=200)
    button_addShopList.configure(activebackground="#ececec")
    button_addShopList.configure(activeforeground="#000000")
    button_addShopList.configure(background="#d9d9d9")
    button_addShopList.configure(disabledforeground="#a3a3a3")
    button_addShopList.configure(foreground="#000000")
    button_addShopList.configure(highlightbackground="#d9d9d9")
    button_addShopList.configure(highlightcolor="black")
    button_addShopList.configure(pady="0")
    button_addShopList.configure(text='''Add To Shopping List''')
    button_addShopList.configure(command=add_sl)
def configure_inv():
    label_inv_name = tk.Label(frame_invMain)
    label_inv_quan = tk.Label(frame_invMain)
    label_inv_fg = tk.Label(frame_invMain)
    label_inv_end = tk.Label(frame_invMain)
    label_inv_exd = tk.Label(frame_invMain)
    label_inv_bar = tk.Label(frame_invMain)
    button_inv_del = tk.Button(frame_invMain)
    button_inv_nameAct = tk.Button(frame_invMain)
    Checkbutton1 = tk.Checkbutton(frame_invMain)
    label_inv_quanData = tk.Label(frame_invMain)
    label_inv_fgData = tk.Label(frame_invMain)
    label_inv_endData = tk.Label(frame_invMain)
    label_inv_exdData = tk.Label(frame_invMain)
    label_inv_barcData = tk.Label(frame_invMain)

    frame_inv_search.place(relx=0.0, rely=0.083, relheight=0.083, relwidth=1.0)
    frame_inv_search.configure(relief='groove')
    frame_inv_search.configure(borderwidth="2")
    frame_inv_search.configure(relief="groove")
    frame_inv_search.configure(background="#737373")
    frame_inv_search.configure(highlightbackground="#d9d9d9")
    frame_inv_search.configure(highlightcolor="black")

    button_inv_filter = tk.Button(frame_inv_search)
    button_inv_CLfilter = tk.Button(frame_inv_search)

    frame_invMain.place(relx=0.0, rely=0.167, relheight=0.75, relwidth=1.0)
    frame_invMain.configure(relief='groove')
    frame_invMain.configure(borderwidth="2")
    frame_invMain.configure(relief="groove")
    frame_invMain.configure(background="#585670")
    frame_invMain.configure(highlightbackground="#d9d9d9")
    frame_invMain.configure(highlightcolor="black")

    label_inv_name = tk.Label(frame_invMain)
    label_inv_name.place(relx=0.065, rely=0.044, height=30, width=190)
    label_inv_name.configure(activebackground="#f9f9f9")
    label_inv_name.configure(activeforeground="black")
    label_inv_name.configure(background="#939393")
    label_inv_name.configure(disabledforeground="#a3a3a3")
    label_inv_name.configure(foreground="#000000")
    label_inv_name.configure(highlightbackground="#d9d9d9")
    label_inv_name.configure(highlightcolor="black")
    label_inv_name.configure(text='''Name''')

    label_inv_quan = tk.Label(frame_invMain)
    label_inv_quan.place(relx=0.264, rely=0.044, height=30, width=125)
    label_inv_quan.configure(activebackground="#f9f9f9")
    label_inv_quan.configure(activeforeground="black")
    label_inv_quan.configure(background="#939393")
    label_inv_quan.configure(disabledforeground="#a3a3a3")
    label_inv_quan.configure(foreground="#000000")
    label_inv_quan.configure(highlightbackground="#d9d9d9")
    label_inv_quan.configure(highlightcolor="black")
    label_inv_quan.configure(text='''Quantity''')

    label_inv_fg = tk.Label(frame_invMain)
    label_inv_fg.place(relx=0.4, rely=0.044, height=30, width=125)
    label_inv_fg.configure(activebackground="#f9f9f9")
    label_inv_fg.configure(activeforeground="black")
    label_inv_fg.configure(background="#939393")
    label_inv_fg.configure(disabledforeground="#a3a3a3")
    label_inv_fg.configure(foreground="#000000")
    label_inv_fg.configure(highlightbackground="#d9d9d9")
    label_inv_fg.configure(highlightcolor="black")
    label_inv_fg.configure(text='''Food Group''')

    label_inv_end = tk.Label(frame_invMain)
    label_inv_end.place(relx=0.537, rely=0.044, height=30, width=125)
    label_inv_end.configure(activebackground="#f9f9f9")
    label_inv_end.configure(activeforeground="black")
    label_inv_end.configure(background="#939393")
    label_inv_end.configure(disabledforeground="#a3a3a3")
    label_inv_end.configure(foreground="#000000")
    label_inv_end.configure(highlightbackground="#d9d9d9")
    label_inv_end.configure(highlightcolor="black")
    label_inv_end.configure(text='''Entry Date''')

    label_inv_exd = tk.Label(frame_invMain)
    label_inv_exd.place(relx=0.674, rely=0.044, height=30, width=125)
    label_inv_exd.configure(activebackground="#f9f9f9")
    label_inv_exd.configure(activeforeground="black")
    label_inv_exd.configure(background="#939393")
    label_inv_exd.configure(disabledforeground="#a3a3a3")
    label_inv_exd.configure(foreground="#000000")
    label_inv_exd.configure(highlightbackground="#d9d9d9")
    label_inv_exd.configure(highlightcolor="black")
    label_inv_exd.configure(text='''Exp. Date''')

    label_inv_bar = tk.Label(frame_invMain)
    label_inv_bar.place(relx=0.811, rely=0.044, height=30, width=125)
    label_inv_bar.configure(activebackground="#f9f9f9")
    label_inv_bar.configure(activeforeground="black")
    label_inv_bar.configure(background="#939393")
    label_inv_bar.configure(disabledforeground="#a3a3a3")
    label_inv_bar.configure(foreground="#000000")
    label_inv_bar.configure(highlightbackground="#d9d9d9")
    label_inv_bar.configure(highlightcolor="black")
    label_inv_bar.configure(text='''Barcode''')

    entry_inv_search.place(relx=0.02, rely=0.3, height=20, relwidth=0.17)
    entry_inv_search.configure(background="white")
    entry_inv_search.configure(disabledforeground="#a3a3a3")
    entry_inv_search.configure(font="TkFixedFont")
    entry_inv_search.configure(foreground="#000000")
    entry_inv_search.configure(highlightbackground="#d9d9d9")
    entry_inv_search.configure(highlightcolor="black")
    entry_inv_search.configure(insertbackground="black")
    entry_inv_search.configure(selectbackground="blue")
    entry_inv_search.configure(selectforeground="white")

    button_inv_search = tk.Button(frame_inv_search)
    button_inv_search.place(relx=0.205, rely=0.3, height=24, width=47)
    button_inv_search.configure(activebackground="#ececec")
    button_inv_search.configure(activeforeground="#000000")
    button_inv_search.configure(background="#d9d9d9")
    button_inv_search.configure(disabledforeground="#a3a3a3")
    button_inv_search.configure(foreground="#000000")
    button_inv_search.configure(highlightbackground="#d9d9d9")
    button_inv_search.configure(highlightcolor="black")
    button_inv_search.configure(pady="0")
    button_inv_search.configure(text='''Search''')
    button_inv_search.configure(command = search_inv)

    button_NextPage.place(relx=0.947, rely=0.889, height=40, width=45)
    button_NextPage.configure(activebackground="#ececec")
    button_NextPage.configure(activeforeground="#000000")
    button_NextPage.configure(background="#d9d9d9")
    button_NextPage.configure(disabledforeground="#a3a3a3")
    button_NextPage.configure(foreground="#000000")
    button_NextPage.configure(highlightbackground="#d9d9d9")
    button_NextPage.configure(highlightcolor="black")
    button_NextPage.configure(pady="0")
    button_NextPage.configure(text='''>>''')
    button_NextPage.configure(command=next_page_inv)

    button_lastPage.place(relx=0.01, rely=0.889, height=40, width=45)
    button_lastPage.configure(activebackground="#ececec")
    button_lastPage.configure(activeforeground="#000000")
    button_lastPage.configure(background="#d9d9d9")
    button_lastPage.configure(disabledforeground="#a3a3a3")
    button_lastPage.configure(foreground="#000000")
    button_lastPage.configure(highlightbackground="#d9d9d9")
    button_lastPage.configure(highlightcolor="black")
    button_lastPage.configure(pady="0")
    button_lastPage.configure(text='''<<''')
    button_lastPage.configure(command=last_page_inv)

    button_clear_search = tk.Button(frame_inv_search)
    button_clear_search.place(relx=0.264, rely=0.3, height=24, width=76)
    button_clear_search.configure(activebackground="#ececec")
    button_clear_search.configure(activeforeground="#000000")
    button_clear_search.configure(background="#d9d9d9")
    button_clear_search.configure(disabledforeground="#a3a3a3")
    button_clear_search.configure(foreground="#000000")
    button_clear_search.configure(highlightbackground="#d9d9d9")
    button_clear_search.configure(highlightcolor="black")
    button_clear_search.configure(pady="0")
    button_clear_search.configure(text='''Clear Search''')
    button_clear_search.configure(command = fill_inv)

def configure_sl():
    frame_sl_main.place(relx=0.0, rely=0.083, relheight=0.833, relwidth=1.0)
    frame_sl_main.configure(relief='groove')
    frame_sl_main.configure(borderwidth="2")
    frame_sl_main.configure(relief="groove")
    frame_sl_main.configure(background="#585670")
    frame_sl_main.configure(highlightbackground="#d9d9d9")
    frame_sl_main.configure(highlightcolor="black")

    button_sl_delete.place(relx=0.059, rely=0.04, height=34, width=127)
    button_sl_delete.configure(activebackground="#ececec")
    button_sl_delete.configure(activeforeground="#000000")
    button_sl_delete.configure(background="#af0101")
    button_sl_delete.configure(disabledforeground="#a3a3a3")
    button_sl_delete.configure(foreground="#000000")
    button_sl_delete.configure(highlightbackground="#d9d9d9")
    button_sl_delete.configure(highlightcolor="black")
    button_sl_delete.configure(pady="0")
    button_sl_delete.configure(text='''Clear List''')
    button_sl_delete.configure(command=clear_sl)


    button_NextPage_sl.place(relx=0.947, rely=0.889, height=40, width=45)
    button_NextPage_sl.configure(activebackground="#ececec")
    button_NextPage_sl.configure(activeforeground="#000000")
    button_NextPage_sl.configure(background="#d9d9d9")
    button_NextPage_sl.configure(disabledforeground="#a3a3a3")
    button_NextPage_sl.configure(foreground="#000000")
    button_NextPage_sl.configure(highlightbackground="#d9d9d9")
    button_NextPage_sl.configure(highlightcolor="black")
    button_NextPage_sl.configure(pady="0")
    button_NextPage_sl.configure(text='''>>''')
    button_NextPage_sl.configure(command=next_page_sl)

    button_lastPage_sl.place(relx=0.01, rely=0.889, height=40, width=45)
    button_lastPage_sl.configure(activebackground="#ececec")
    button_lastPage_sl.configure(activeforeground="#000000")
    button_lastPage_sl.configure(background="#d9d9d9")
    button_lastPage_sl.configure(disabledforeground="#a3a3a3")
    button_lastPage_sl.configure(foreground="#000000")
    button_lastPage_sl.configure(highlightbackground="#d9d9d9")
    button_lastPage_sl.configure(highlightcolor="black")
    button_lastPage_sl.configure(pady="0")
    button_lastPage_sl.configure(text='''<<''')
    button_lastPage_sl.configure(command=last_page_sl)

    entry_addShopList.insert(0, "Item")
    entry_notesShopList.insert(0, "Notes")
def configure_recipies():
    frame_rec_menu.place(relx=0.0, rely=0.083, relheight=0.083, relwidth=1.0)
    frame_rec_menu.configure(relief='groove')
    frame_rec_menu.configure(borderwidth="2")
    frame_rec_menu.configure(relief="groove")
    frame_rec_menu.configure(background="#737373")

    frame_rec_main.place(relx=0.0, rely=0.167, relheight=0.75, relwidth=1.0)
    frame_rec_main.configure(relief='groove')
    frame_rec_main.configure(borderwidth="2")
    frame_rec_main.configure(relief="groove")
    frame_rec_main.configure(background="#585670")

    label_rec_name = tk.Label(frame_rec_main)
    label_rec_name.place(relx=0.186, rely=0.111, height=30, width=352)
    label_rec_name.configure(background="#939393")
    label_rec_name.configure(disabledforeground="#a3a3a3")
    label_rec_name.configure(foreground="#000000")
    label_rec_name.configure(text='''Name''')

    label_rec_time = tk.Label(frame_rec_main)
    label_rec_time.place(relx=0.586, rely=0.111, height=30, width=150)
    label_rec_time.configure(background="#939393")
    label_rec_time.configure(disabledforeground="#a3a3a3")
    label_rec_time.configure(foreground="#000000")
    label_rec_time.configure(text='''Time''')

    label_rec_timeDate = tk.Label(frame_rec_main)
    label_rec_timeDate.place(relx=0.586, rely=0.222, height=30, width=150)
    label_rec_timeDate.configure(background="#d9d9d9")
    label_rec_timeDate.configure(disabledforeground="#a3a3a3")
    label_rec_timeDate.configure(foreground="#000000")
    label_rec_timeDate.configure(text='''X''')

    button_rec_nameData = tk.Button(frame_rec_main)
    button_rec_nameData.place(relx=0.186, rely=0.222, height=30, width=350)
    button_rec_nameData.configure(activebackground="#ececec")
    button_rec_nameData.configure(activeforeground="#000000")
    button_rec_nameData.configure(background="#d9d9d9")
    button_rec_nameData.configure(cursor="fleur")
    button_rec_nameData.configure(disabledforeground="#a3a3a3")
    button_rec_nameData.configure(foreground="#000000")
    button_rec_nameData.configure(highlightbackground="#d9d9d9")
    button_rec_nameData.configure(highlightcolor="black")
    button_rec_nameData.configure(pady="0")
    button_rec_nameData.configure(relief="flat")
    button_rec_nameData.configure(text='''X''')

def configure_recEntry():
    frame_addrec.place(relx=0.0, rely=0.083, relheight=0.833, relwidth=1.0)
    frame_addrec.configure(relief='groove')
    frame_addrec.configure(borderwidth="2")
    frame_addrec.configure(relief="groove")
    frame_addrec.configure(background="#585670")

    label_recEnt_title.place(relx=0.078, rely=0.08, height=30, width=350)
    label_recEnt_title.configure(background="#939393")
    label_recEnt_title.configure(disabledforeground="#a3a3a3")
    label_recEnt_title.configure(foreground="#000000")
    label_recEnt_title.configure(text='''Title''')

    label_recEnt_time.place(relx=0.078, rely=0.16, height=30, width=100)
    label_recEnt_time.configure(background="#939393")
    label_recEnt_time.configure(disabledforeground="#a3a3a3")
    label_recEnt_time.configure(foreground="#000000")
    label_recEnt_time.configure(text='''Time''')

    label_rec_ins = tk.Label(frame_addrec)
    label_rec_ins.place(relx=0.449, rely=0.28, height=21, width=149)
    label_rec_ins.configure(background="#939393")
    label_rec_ins.configure(cursor="fleur")
    label_rec_ins.configure(disabledforeground="#a3a3a3")
    label_rec_ins.configure(foreground="#000000")
    label_rec_ins.configure(text='''Instructions''')

    label_rec_ing = tk.Label(frame_addrec)
    label_rec_ing.place(relx=0.088, rely=0.28, height=21, width=150)
    label_rec_ing.configure(background="#939393")
    label_rec_ing.configure(disabledforeground="#a3a3a3")
    label_rec_ing.configure(foreground="#000000")
    label_rec_ing.configure(text='''Ingredients''')

    button_rec_addin.place(relx=0.146, rely=0.9, height=30, width=175)
    button_rec_addin.configure(activebackground="#ececec")
    button_rec_addin.configure(activeforeground="#000000")
    button_rec_addin.configure(background="#d9d9d9")
    button_rec_addin.configure(disabledforeground="#a3a3a3")
    button_rec_addin.configure(foreground="#000000")
    button_rec_addin.configure(highlightbackground="#d9d9d9")
    button_rec_addin.configure(highlightcolor="black")
    button_rec_addin.configure(pady="0")
    button_rec_addin.configure(text='''Add Ingredients To List''')
    button_rec_addin.configure(command = add_ing_sl)

    label_ing_list.place(relx=0.088, rely=0.34, height=271, width=344)
    label_ing_list.configure(background="#ffffff")
    label_ing_list.configure(disabledforeground="#a3a3a3")
    label_ing_list.configure(foreground="#000000")
    label_ing_list.configure(justify='left')
    label_ing_list.configure(text='''Ingredients''')
    label_ing_list.configure(wraplength="300")

    label_steps.place(relx=0.449, rely=0.34, height=271, width=533)
    label_steps.configure(background="#ffffff")
    label_steps.configure(disabledforeground="#a3a3a3")
    label_steps.configure(foreground="#000000")
    label_steps.configure(justify="left")
    label_steps.configure(text='''Steps''')
    label_steps.configure(wraplength="500")
    label_steps.configure(pady = 0)
def configure_addEntry():
    frame_addEntry.place(relx=0.381, rely=0.15, relheight=0.658, relwidth=0.243)
    frame_addEntry.configure(relief='groove')
    frame_addEntry.configure(borderwidth="2")
    frame_addEntry.configure(relief="groove")
    frame_addEntry.configure(background="#d9d9d9")

    entry_code.place(relx=0.1, rely=0.152, height=20, relwidth=0.803)
    entry_code.configure(background="white")
    entry_code.configure(cursor="fleur")
    entry_code.configure(disabledforeground="#a3a3a3")
    entry_code.configure(font="TkFixedFont")
    entry_code.configure(foreground="#000000")
    entry_code.configure(insertbackground="black")
    entry_code.bind('<Return>',scan_in)

    Entry_prod_name.place(relx=0.1, rely=0.278, height=20, relwidth=0.803)
    Entry_prod_name.configure(background="white")
    Entry_prod_name.configure(disabledforeground="#a3a3a3")
    Entry_prod_name.configure(font="TkFixedFont")
    Entry_prod_name.configure(foreground="#000000")
    Entry_prod_name.configure(insertbackground="black")

    label_code = tk.Label(frame_addEntry)
    label_code.place(relx=0.1, rely=0.101, height=21, width=201)
    label_code.configure(background="#d9d9d9")
    label_code.configure(disabledforeground="#a3a3a3")
    label_code.configure(foreground="#000000")
    label_code.configure(justify='left')
    label_code.configure(text='''Barcode''')

    label_prodName = tk.Label(frame_addEntry)
    label_prodName.place(relx=0.1, rely=0.228, height=21, width=201)
    label_prodName.configure(background="#d9d9d9")
    label_prodName.configure(disabledforeground="#a3a3a3")
    label_prodName.configure(foreground="#000000")
    label_prodName.configure(justify='left')
    label_prodName.configure(text='''Product Name''')


    Entry_foodGroup.place(relx=0.1, rely=0.405, height=20, relwidth=0.803)
    Entry_foodGroup.configure(background="white")
    Entry_foodGroup.configure(disabledforeground="#a3a3a3")
    Entry_foodGroup.configure(font="TkFixedFont")
    Entry_foodGroup.configure(foreground="#000000")
    Entry_foodGroup.configure(insertbackground="black")

    Entry_expd.place(relx=0.1, rely=0.532, height=20, relwidth=0.803)
    Entry_expd.configure(background="white")
    Entry_expd.configure(disabledforeground="#a3a3a3")
    Entry_expd.configure(font="TkFixedFont")
    Entry_expd.configure(foreground="#000000")
    Entry_expd.configure(insertbackground="black")

    Label_foodGroup = tk.Label(frame_addEntry)
    Label_foodGroup.place(relx=0.1, rely=0.354, height=21, width=201)
    Label_foodGroup.configure(background="#d9d9d9")
    Label_foodGroup.configure(disabledforeground="#a3a3a3")
    Label_foodGroup.configure(foreground="#000000")
    Label_foodGroup.configure(text='''Food Group''')

    Label_enterexp = tk.Label(frame_addEntry)
    Label_enterexp.place(relx=0.1, rely=0.481, height=21, width=201)
    Label_enterexp.configure(background="#d9d9d9")
    Label_enterexp.configure(disabledforeground="#a3a3a3")
    Label_enterexp.configure(foreground="#000000")
    Label_enterexp.configure(text='''Expiration Date''')

    entry_numItems.place(relx=0.1, rely=0.658, height=20, relwidth=0.803)
    entry_numItems.configure(background="white")
    entry_numItems.configure(disabledforeground="#a3a3a3")
    entry_numItems.configure(font="TkFixedFont")
    entry_numItems.configure(foreground="#000000")
    entry_numItems.configure(insertbackground="black")

    label_numitems = tk.Label(frame_addEntry)
    label_numitems.place(relx=0.1, rely=0.608, height=21, width=201)
    label_numitems.configure(background="#d9d9d9")
    label_numitems.configure(disabledforeground="#a3a3a3")
    label_numitems.configure(foreground="#000000")
    label_numitems.configure(justify='left')
    label_numitems.configure(text='''Quantity''')

    button_add.place(relx=0.201, rely=0.81, height=30, width=150)
    button_add.configure(activebackground="#ececec")
    button_add.configure(activeforeground="#000000")
    button_add.configure(background="#d9d9d9")
    button_add.configure(disabledforeground="#a3a3a3")
    button_add.configure(foreground="#000000")
    button_add.configure(highlightbackground="#d9d9d9")
    button_add.configure(highlightcolor="black")
    button_add.configure(pady="0")
    button_add.configure(text='''Add to Inventory''')
    button_add.configure(command = add_inv)

    button_closeAdd = tk.Button(frame_addEntry)
    button_closeAdd.place(relx=0.863, rely=0.025, height=25, width=25)
    button_closeAdd.configure(activebackground="#ececec")
    button_closeAdd.configure(activeforeground="#000000")
    button_closeAdd.configure(background="#9e9e9e")
    button_closeAdd.configure(disabledforeground="#a3a3a3")
    button_closeAdd.configure(foreground="#000000")
    button_closeAdd.configure(highlightbackground="#d9d9d9")
    button_closeAdd.configure(highlightcolor="black")
    button_closeAdd.configure(pady="0")
    button_closeAdd.configure(text='''X''')
    button_closeAdd.configure(command = return_curScreen)
def configure_delEntry():
    frame_del.place(relx=0.371, rely=0.183, relheight=0.542, relwidth=0.271)
    frame_del.configure(relief='groove')
    frame_del.configure(borderwidth="2")
    frame_del.configure(relief="groove")
    frame_del.configure(background="#d9d9d9")

    button_delete.place(relx=0.181, rely=0.831, height=24, width=175)
    button_delete.configure(activebackground="#ececec")
    button_delete.configure(activeforeground="#000000")
    button_delete.configure(background="#d9d9d9")
    button_delete.configure(disabledforeground="#a3a3a3")
    button_delete.configure(foreground="#000000")
    button_delete.configure(highlightbackground="#d9d9d9")
    button_delete.configure(highlightcolor="black")
    button_delete.configure(pady="0")
    button_delete.configure(text='''Remove Item From Inventory''')
    button_delete.configure(command = delete_inv)

    label_delName.place(relx=0.144, rely=0.154, height=21, width=200)
    label_delName.configure(background="#d9d9d9")
    label_delName.configure(disabledforeground="#a3a3a3")
    label_delName.configure(foreground="#000000")
    label_delName.configure(justify='left')
    label_delName.configure(text='''''')

    entry_numDelete.place(relx=0.578, rely=0.646, height=20, relwidth=0.159)
    entry_numDelete.configure(background="white")
    entry_numDelete.configure(disabledforeground="#a3a3a3")
    entry_numDelete.configure(font="TkFixedFont")
    entry_numDelete.configure(foreground="#000000")
    entry_numDelete.configure(insertbackground="black")

    label_barDelete.place(relx=0.144, rely=0.215, height=21, width=200)
    label_barDelete.configure(background="#d9d9d9")
    label_barDelete.configure(disabledforeground="#a3a3a3")
    label_barDelete.configure(foreground="#000000")
    label_barDelete.configure(justify='left')
    label_barDelete.configure(text='''''')

    label_expDel.place(relx=0.144, rely=0.277, height=21, width=200)
    label_expDel.configure(background="#d9d9d9")
    label_expDel.configure(disabledforeground="#a3a3a3")
    label_expDel.configure(foreground="#000000")
    label_expDel.configure(justify='left')
    label_expDel.configure(text='''''')

    label_entDate.place(relx=0.144, rely=0.338, height=21, width=200)
    label_entDate.configure(background="#d9d9d9")
    label_entDate.configure(disabledforeground="#a3a3a3")
    label_entDate.configure(foreground="#000000")
    label_entDate.configure(justify='left')
    label_entDate.configure(text='''''')

    label_curNum.place(relx=0.144, rely=0.4, height=21, width=200)
    label_curNum.configure(background="#d9d9d9")
    label_curNum.configure(disabledforeground="#a3a3a3")
    label_curNum.configure(foreground="#000000")
    label_curNum.configure(justify='left')
    label_curNum.configure(text='''''')

    label_numDel = tk.Label(frame_del)
    label_numDel.place(relx=0.144, rely=0.646, height=21, width=114)
    label_numDel.configure(background="#d9d9d9")
    label_numDel.configure(cursor="fleur")
    label_numDel.configure(disabledforeground="#a3a3a3")
    label_numDel.configure(foreground="#000000")
    label_numDel.configure(text='''Amount To Remove:''')

    button_closeDel = tk.Button(frame_del)
    button_closeDel.place(relx=0.884, rely=0.031, height=25, width=25)
    button_closeDel.configure(activebackground="#ececec")
    button_closeDel.configure(activeforeground="#000000")
    button_closeDel.configure(background="#acacac")
    button_closeDel.configure(disabledforeground="#a3a3a3")
    button_closeDel.configure(foreground="#000000")
    button_closeDel.configure(highlightbackground="#d9d9d9")
    button_closeDel.configure(highlightcolor="black")
    button_closeDel.configure(pady="0")
    button_closeDel.configure(text='''X''')
    button_closeDel.configure(command = return_curScreen)

    label_userInst.place(relx=0.144, rely=0.062, height=21, width=200)
    label_userInst.configure(background="#d9d9d9")
    label_userInst.configure(disabledforeground="#a3a3a3")
    label_userInst.configure(foreground="#000000")
    label_userInst.configure(text='''Scan An Item''')
def configure_sl_veiw():
    frame_sl_veiw.place(relx=0.371, rely=0.183, relheight=0.408, relwidth=0.271)
    frame_sl_veiw.configure(relief='groove')
    frame_sl_veiw.configure(borderwidth="2")
    frame_sl_veiw.configure(relief="groove")
    frame_sl_veiw.configure(background="#d9d9d9")
    frame_sl_veiw.configure(highlightbackground="#d9d9d9")
    frame_sl_veiw.configure(highlightcolor="black")

    button_delete_sl.place(relx=0.181, rely=0.833, height=24, width=175)
    button_delete_sl.configure(activebackground="#ececec")
    button_delete_sl.configure(activeforeground="#000000")
    button_delete_sl.configure(background="#d9d9d9")
    button_delete_sl.configure(disabledforeground="#a3a3a3")
    button_delete_sl.configure(foreground="#000000")
    button_delete_sl.configure(highlightbackground="#d9d9d9")
    button_delete_sl.configure(highlightcolor="black")
    button_delete_sl.configure(pady="0")
    button_delete_sl.configure(text='''Remove From Shopping List''')
    button_delete_sl.configure(command = remove_sl)

    label_sld_name.place(relx=0.144, rely=0.155, height=16, width=200)
    label_sld_name.configure(activebackground="#f9f9f9")
    label_sld_name.configure(activeforeground="black")
    label_sld_name.configure(background="#d9d9d9")
    label_sld_name.configure(disabledforeground="#a3a3a3")
    label_sld_name.configure(foreground="#000000")
    label_sld_name.configure(highlightbackground="#d9d9d9")
    label_sld_name.configure(highlightcolor="black")
    label_sld_name.configure(justify='left')
    label_sld_name.configure(text='''Name''')

    label_sld_n = tk.Label(frame_sl_veiw)
    label_sld_n.configure(justify='left')
    label_sld_n.place(relx=0.144, rely=0.260, height=16, width=200)
    label_sld_n.configure(activebackground="#f9f9f9")
    label_sld_n.configure(activeforeground="black")
    label_sld_n.configure(background="#d9d9d9")
    label_sld_n.configure(disabledforeground="#a3a3a3")
    label_sld_n.configure(foreground="#000000")
    label_sld_n.configure(highlightbackground="#d9d9d9")
    label_sld_n.configure(highlightcolor="black")
    label_sld_n.configure(text='''Notes:''')

    label_sld_notes.place(relx=0.144, rely=0.342, height=16, width=200)
    label_sld_notes.configure(activebackground="#f9f9f9")
    label_sld_notes.configure(activeforeground="black")
    label_sld_notes.configure(background="#d9d9d9")
    label_sld_notes.configure(disabledforeground="#a3a3a3")
    label_sld_notes.configure(foreground="#000000")
    label_sld_notes.configure(highlightbackground="#d9d9d9")
    label_sld_notes.configure(highlightcolor="black")
    label_sld_notes.configure(justify='left')
    label_sld_notes.configure(text='''X''')

    button_closeDel_sl.place(relx=0.884, rely=0.033, height=25, width=25)
    button_closeDel_sl.configure(activebackground="#ececec")
    button_closeDel_sl.configure(activeforeground="#000000")
    button_closeDel_sl.configure(background="#acacac")
    button_closeDel_sl.configure(disabledforeground="#a3a3a3")
    button_closeDel_sl.configure(foreground="#000000")
    button_closeDel_sl.configure(highlightbackground="#d9d9d9")
    button_closeDel_sl.configure(highlightcolor="black")
    button_closeDel_sl.configure(pady="0")
    button_closeDel_sl.configure(text='''X''')
    button_closeDel_sl.configure(command = return_curScreen)

#-------------------------------------
# Lift screens
#-------------------------------------
def focus_inv():
    global CURRENTSCREEN
    global CURRENTPAGE_INV
    frame_invMain.lift()
    frame_inv_search.lift()
    CURRENTSCREEN = 1
    fill_inv()
    if (NUMPAGES_INV == 1):
        button_NextPage.place_forget()
        button_lastPage.place_forget()
    else:
        CURRENTPAGE_INV = 0
        button_lastPage.place_forget()
        button_NextPage.place(relx=0.947, rely=0.889, height=40, width=45)
def focus_rec():
    global CURRENTSCREEN
    frame_rec_menu.lift()
    frame_rec_main.lift()
    CURRENTSCREEN = 2
    update_r()
def focus_sl():
    global CURRENTSCREEN
    frame_sl_main.lift()
    CURRENTSCREEN = 3
    entry_addShopList.delete(0, END)
    entry_notesShopList.delete(0, END)
    entry_addShopList.insert(0, "Item")
    entry_notesShopList.insert(0, "Notes")
    update_sl()
    if (NUMPAGES_SL == 1):
        button_NextPage_sl.place_forget()
        button_lastPage_sl.place_forget()
    else:
        CURRENTPAGE_INV = 0
        button_lastPage_sl.place_forget()
        button_NextPage_sl.place(relx=0.947, rely=0.889, height=40, width=45)

    update_sl()
def return_curScreen():
    global CURRENTSCREEN
    print("RETURN TO >> "+str(CURRENTSCREEN))
    clear_pop()
    if (CURRENTSCREEN == 1):
        focus_inv()
    elif (CURRENTSCREEN == 2):
        focus_rec()
    elif (CURRENTSCREEN == 3):
        focus_sl()

#------------------------------------
# Formating Functions
#------------------------------------
def clear_pop():
    entry_code.delete(0, END)
    Entry_prod_name.delete(0, END)
    Entry_foodGroup.delete(0, END)
    Entry_expd.delete(0, END)
    entry_numItems.delete(0, END)
    label_delName.configure(text ="")
    label_barDelete.configure(text = "")
    label_entDate.configure(text = "")
    label_expDel.configure(text = "")
    label_curNum.configure(text = "")
    entry_barcode.delete(0, END)
def clear_widgets(list_of_widgets):
    for widget in list_of_widgets:
        widget.destroy()

#-------------------------------
# Inventory Control Functions
#-------------------------------
def focus_barEntry():
    return_curScreen()
    frame_addEntry.lift()
    # Clear the entry box
    entry_code.delete(0,20)
    # put the cursor in the text box
    entry_code.focus_set()
    # Clear entries
    entry_code.delete(0, END)
    Entry_prod_name.delete(0, END)
    Entry_foodGroup.delete(0, END)
    Entry_expd.delete(0, END)
    entry_numItems.delete(0, END)
def focus_delEntry():
    return_curScreen()
    frame_del.lift()
    # Clear the entry box
    entry_barcode.delete(0,20)
    # put the cursor in the text box
    entry_barcode.focus_set()
    entry_numDelete.delete(0, END)
    label_userInst.configure(text = '''Scan An Item''')
    label_userInst.configure(foreground = "#000000")
def scan_out(event):
    # Get Scanned Code
    code = entry_barcode.get()
    label_delName.configure(text = code)
    # Check if already in Inventory
    data = addfunc.check_inv("items", entry_barcode.get(), invdb)
    print("\nITEM FOUND? >> "+str(data[0][0]))
    if (data[0][0] == 1):
        label_userInst.configure(text='''ITEM FOUND''')
        label_userInst.configure(foreground = "#008006")
        # Pull Data
        data = addfunc.get_info("*","items","barcode_num",str(code), invdb)
        # Fill Information
        label_delName.configure(text = str(data[0][2]))
        label_barDelete.configure(text = str(data[0][3]))
        label_entDate.configure(text = "Entry Date: "+str(data[0][5]))
        label_expDel.configure(text = "Exp Date: "+str(data[0][6]))
        label_curNum.configure(text = "Current Quantity:"+str(data[0][7]))
        # Default number to remove to 1
        entry_numDelete.insert(0,"1")
    else:
        # Alert user the item was not FOUND
        label_userInst.configure(text = '''ITEM NOT FOUND''')
        label_userInst.configure(foreground = "#df0005")
    fill_inv()
def scan_in(event):
    # Get code scanned
    code = entry_code.get()
    entry_code.configure(text=code)
    # Pull data from ref_database
    data = addfunc.get_info("*", "items", "barcode", code, refdb)
    # Fill entries
    Entry_prod_name.insert(0, str(data[0][1]))
    Entry_foodGroup.insert(0, str(data[0][2]))
    Entry_expd.insert(0, str(data[0][3]))
    entry_numItems.insert(0,"1")
def add_inv():
    # Check if already in Inventory
    data = addfunc.check_inv("items", entry_code.get(), invdb)
    if(data[0][0] == 0): # Add as a new item
        print("\nITEM NOT IN INVENTORY\n")
        # get new id
        newID = addfunc.get_new_id("items",invdb,"item_id")
        print("Next ID >>> " + str(newID))
        # get food_group # ID
        fgID = addfunc.get_fg_id(Entry_foodGroup.get(),invdb)
        print("FOOD GROUP >> " + str(fgID))
        # pull UID
        UID = addfunc.pull_UID(refdb, entry_code.get())
        # build add
        addfunc.add_inv(invdb, newID, fgID, Entry_prod_name.get(), entry_code.get(), UID, Entry_expd.get(), entry_numItems.get())
        print(" << item added >> ")
    else:   # increment count acordint to amount entered
        addfunc.inc_count(invdb, entry_code.get(), entry_numItems.get())
    # Clear entries
    entry_code.delete(0, END)
    Entry_prod_name.delete(0, END)
    Entry_foodGroup.delete(0, END)
    Entry_expd.delete(0, END)
    entry_numItems.delete(0, END)
    # Clear the entry box
    entry_code.delete(0,20)
    # Lift the inventory
    frame_invMain.lift()
def delete_inv():
    data = addfunc.check_inv("items", entry_barcode.get(), invdb)
    # if the items exists
    if(data[0][0] == 1):
        print("\n ITEM FOUND \n")
        # get current number
        data = addfunc.get_info("num_items","items","barcode_num", str(entry_barcode.get()), invdb)
        curNum = int(data[0][0])
        incNum = int(entry_numDelete.get())
        code = str(entry_barcode.get())
        # if Quantity = 1 OR quantity = numRemove
        if ((curNum == 1) or (incNum >= curNum)):
            delfunc.remove_entry("items", "barcode_num",code, invdb)
            return_curScreen()
        else: #increment count
            delfunc.inc_count(invdb,entry_barcode.get(),incNum)
            print(" \n\n DELETE DONE \n\n")
            return_curScreen()
    else:
        print("\nITEM NOT IN INVENTORY \n")
def next_page_inv():
    global CURRENTPAGE_INV
    global NUMPAGES_INV
    print("CURRENT PAGE >> "+str(CURRENTPAGE_INV))
    print("NUM PAGES >> "+str(NUMPAGES_INV))
    if (CURRENTPAGE_INV < NUMPAGES_INV-1):
        CURRENTPAGE_INV+=1
        fill_inv()
        button_lastPage.place(relx=0.01, rely=0.889, height=40, width=45)
    if (CURRENTPAGE_INV == NUMPAGES_INV-1):
        button_NextPage.place_forget()
def last_page_inv():
    global CURRENTPAGE_INV
    global NUMPAGES_INV

    print("CURRENT PAGE >> "+str(CURRENTPAGE_INV))
    print("NUM PAGES >> "+str(NUMPAGES_INV))
    if (CURRENTPAGE_INV > 0):
        CURRENTPAGE_INV-=1
        fill_inv()
        button_NextPage.place(relx=0.947, rely=0.889, height=40, width=45)
    if (CURRENTPAGE_INV == 0):
        button_lastPage.place_forget()
def fill_inv():
    global FIRSTLIST_INV
    global inv_widgets
    global NUMPAGES_INV
    global CURRENTPAGE_INV
    global FIRSTLIST_INV
    global MAXPERPAGE_INV
    # after the inital setup
    #print("FIRSTLIST_INV PAGE >> "+str(CURRENTPAGE_INV))
    if (FIRSTLIST_INV != 0):
        clear_widgets(inv_widgets)
    FIRSTLIST_INV = 1
    # clear widgets
    inv_widgets = []
    # get current inventory
    curInv = invfunc.get_inv(invdb)
    # get starting point for pagenum
    totalRow = len(curInv)
    totalCol = len(curInv[0])
    # Calculate the number of pages
    NUMPAGES_INV = math.ceil(totalRow/MAXPERPAGE_INV)
    #print("NUMPAGES_INV >>"+str(NUMPAGES_INV))
    numEntries = 0
    curRow = CURRENTPAGE_INV*MAXPERPAGE_INV
    curCol = 0
    H = 30
    W = 125
    X = 0.264 #inc by 0.137
    Y = 0.156 #inc by .065
    #print("TOTAL ROWs >> "+str(totalRow))
    for row in range(totalRow):
        row += curRow
        #print("ROW >> "+str(row))
        if ((numEntries == MAXPERPAGE_INV) or (row == totalRow+1)):
            break;
        #current_row = curInv[curRow]
        # Make Item button
        button_inv_nameAct = tk.Button(frame_invMain)
        button_inv_nameAct.place(relx=0.065, rely=Y, height=H, width=190)
        button_inv_nameAct.configure(text=curInv[row][0])
        invfunc.configure_nameButton(button_inv_nameAct)
        button_inv_nameAct.configure(command = lambda name=curInv[row][0]: remove_manual(name))
        inv_widgets.append(button_inv_nameAct)
        # reset the x position
        X = 0.264
        for col in range (totalCol-1):
            col+=1
            invlabel = tk.Label(frame_invMain)
            invlabel.place(relx=X, rely=Y, height=H, width=W)
            invlabel.configure(text=curInv[row][col])
            invfunc.configure_label(invlabel)
            inv_widgets.append(invlabel)
            # increment the x position
            X+=0.137
        # increment y position
        Y+=0.1
        numEntries+=1
def remove_manual(name):
    print("Remove Manualy")
    focus_delEntry()
    # pull Info
    data = addfunc.get_info("*","items","product_name",name, invdb)
    # Fill Information
    label_userInst.configure(text='''''')
    label_delName.configure(text = str(data[0][2]))
    label_barDelete.configure(text = str(data[0][3]))
    label_entDate.configure(text = "Entry Date: "+str(data[0][5]))
    label_expDel.configure(text = "Exp Date: "+str(data[0][6]))
    label_curNum.configure(text = "Current Quantity:"+str(data[0][7]))
    # Default number to remove to 1
    entry_numDelete.insert(0,"1")
    entry_barcode.insert(0,str(data[0][3]))
def remove_by_rfid(id):
    # find item in Inventory
    inInv = check_rfid_exists(id)
    # remove item
    if(data[0][0] == 1):
        print("\n ITEM FOUND \n")
        # get current number
        data = addfunc.get_info("num_items","items","UID", str(id), invdb)
        curNum = int(data[0][0])
        # if Quantity = 1 remove entry
        if (curNum == 1):
            delfunc.remove_by_rfid(id)
        else: #increment count
            delfunc.inc_count_rfid(id, invdb, curNum)
            print(" \n\n DELETE DONE \n\n")
    else:
        print("\nITEM NOT IN INVENTORY \n")
def search_inv():
    global FIRSTLIST_INV
    global inv_widgets
    global NUMPAGES_INV
    global CURRENTPAGE_INV
    global FIRSTLIST_INV
    global MAXPERPAGE_INV
    key = entry_inv_search.get()
    entry = entry_addShopList.get()
    print(entry)
    print("KEY 1 >> "+ entry_inv_search.get())
    # get entries related to key
    result = invfunc.get_inv_search(invdb, key)
    # display results-----
    print(result)
    clear_widgets(inv_widgets)
    inv_widgets = []
    # get starting point for pagenum
    totalRow = len(result)
    print("TOTAL ROW >> "+ str(totalRow))
    totalCol = len(result[0])
    # Calculate the number of pages
    NUMPAGES_INV = math.ceil(totalRow/MAXPERPAGE_INV)
    #print("NUMPAGES_INV >>"+str(NUMPAGES_INV))
    numEntries = 0
    curRow = CURRENTPAGE_INV*MAXPERPAGE_INV
    curCol = 0
    H = 30
    W = 125
    X = 0.264 #inc by 0.137
    Y = 0.156 #inc by .065
    #print("TOTAL ROWs >> "+str(totalRow))
    for row in range(totalRow):
        row += curRow
        print("ROW >> "+str(row))
        if ((numEntries == MAXPERPAGE_INV) or (row == totalRow+1)):
            break;
        #current_row = curInv[curRow]
        # Make Item button
        button_inv_nameAct = tk.Button(frame_invMain)
        button_inv_nameAct.place(relx=0.065, rely=Y, height=H, width=190)
        button_inv_nameAct.configure(text=result[row][0])
        invfunc.configure_nameButton(button_inv_nameAct)
        button_inv_nameAct.configure(command = lambda name=result[row][0]: remove_manual(name))
        inv_widgets.append(button_inv_nameAct)
        # reset the x position
        X = 0.264
        for col in range (totalCol-1):
            col+=1
            invlabel = tk.Label(frame_invMain)
            invlabel.place(relx=X, rely=Y, height=H, width=W)
            invlabel.configure(text=result[row][col])
            invfunc.configure_label(invlabel)
            inv_widgets.append(invlabel)
            # increment the x position
            X+=0.137
        # increment y position
        Y+=0.1
        numEntries+=1

#----------------------------------------
# Shopping List Control Functions
#----------------------------------------
def update_sl():
    global MAXPERPAGE_SL
    global sl_widgets
    global FIRSTLIST_SL
    global CURRENTPAGE_SL
    global NUMPAGES_SL
    global LASTNUMPAGES_SL
    print("CURRENT PAGE >> "+str(CURRENTPAGE_SL))
    if (FIRSTLIST_SL != 0):
        clear_widgets(sl_widgets)
    FIRSTLIST_SL = 1
    print("MAX PER PAGE >> " + str(MAXPERPAGE_SL))
    # pull info from he database
    sl = slfunc.get_sl_data(invdb)
    #print(sl)
    # get total number of entries
    totalRow = len(sl)
    print("LENGTH OF SL >> "+str(totalRow))
    numEntries = 0
    curRow = CURRENTPAGE_SL*MAXPERPAGE_SL+1
    # Calculate the number of pages
    if (totalRow == 1):
        NUMPAGES_SL = 1
    else:
        NUMPAGES_SL = math.ceil((totalRow-1)/MAXPERPAGE_SL)
    print("NUMBER OF PAGES >> "+str(NUMPAGES_SL))
    Y = 0.156
    yinc = .08
    sl_widgets = []
    # print labels
    print("TOTAL ROW >> "+str(totalRow))
    for row in range(totalRow):
        row += curRow
        #print("ROW >> "+str(row))
        #print("SL ROW >> "+str(row))
        if ((numEntries == MAXPERPAGE_SL) or (row+1 == totalRow+1)):
            break;
        #current_row = curInv[curRow]
        # make Checkbox
        checkbox_sl = tk.Checkbutton(frame_sl_main)
        checkbox_sl.place(relx=0.059, rely=Y, relheight=0.056, relwidth=0.061)
        slfunc.configure_slCheckbox(checkbox_sl)
        sl_widgets.append(checkbox_sl)
        # Make Item button
        button_slEntry = tk.Button(frame_sl_main)
        button_slEntry.place(relx=0.1, rely=Y, height=34, width=250)
        button_slEntry.configure(text=sl[row][0])
        slfunc.configure_slEntry(button_slEntry)
        button_slEntry.configure(command = lambda name=sl[row][0]: remove_sl_veiw(name))
        sl_widgets.append(button_slEntry)
        # make notes label
        label_slNotes = tk.Label(frame_sl_main)
        label_slNotes.place(relx=0.35, rely=Y, height=34, width=400)
        label_slNotes.configure(text=sl[row][1])
        slfunc.configure_slEntry(label_slNotes)
        sl_widgets.append(label_slNotes)
        # Count entry
        numEntries+=1dis
        Y+=yinc
    # check if page number increased
    check_nav()
    print("\n------------\n")
def add_sl():
    #get textbox input
    entry = entry_addShopList.get()
    note = entry_notesShopList.get()
    #if the entry is not empty
    if ((entry != "") and (entry != "Item")):
        # Get a new ID
        newID = addfunc.get_new_id("shopping_list", invdb, "list_id")
        if (note == "Notes"):
            note = ""
        # add the text to the shopping list
        slfunc.add_sl_db(invdb, entry, newID, note)
    # clear textbox
    entry_addShopList.delete(0, END)
    entry_notesShopList.delete(0, END)
    entry_addShopList.insert(0, "Item")
    entry_notesShopList.insert(0, "Notes")
    # update the shopping list
    update_sl()
def next_page_sl():
    global CURRENTPAGE_SL
    global NUMPAGES_SL
    print("CURRENT PAGE >> "+str(CURRENTPAGE_SL))
    print("NUM PAGES >> "+str(NUMPAGES_SL))
    if (CURRENTPAGE_SL < NUMPAGES_SL-1):
        CURRENTPAGE_SL+=1
        button_lastPage_sl.place(relx=0.01, rely=0.889, height=40, width=45)
    if (CURRENTPAGE_SL == NUMPAGES_SL-1):
        button_NextPage_sl.place_forget()
    update_sl()
def last_page_sl():
    global CURRENTPAGE_SL
    global NUMPAGES_SL
    print("CURRENT PAGE >> "+str(CURRENTPAGE_SL))
    print("NUM PAGES >> "+str(NUMPAGES_SL))
    if (CURRENTPAGE_SL > 0):
        CURRENTPAGE_SL-=1
        button_NextPage_sl.place(relx=0.947, rely=0.889, height=40, width=45)
    if (CURRENTPAGE_SL == 0):
        button_lastPage_sl.place_forget()
    update_sl()
def clear_sl():
    global CURRENTPAGE_SL
    command = "DELETE FROM shopping_list WHERE list_id != 0"
    c = invdb.cursor()
    c.execute(command)
    invdb.commit()
    CURRENTPAGE_SL = 0
    update_sl()
def add_from_rec(entry, note):
    if ((entry != "") and (entry != "Item")):
        # Get a new ID
        newID = addfunc.get_new_id("shopping_list", invdb, "list_id")
        if (note == "Notes"):
            note = ""
        # add the text to the shopping list
        slfunc.add_sl_db(invdb, entry, newID, note)
    # clear textbox
    entry_addShopList.delete(0, END)
    entry_notesShopList.delete(0, END)
    entry_addShopList.insert(0, "Item")
    entry_notesShopList.insert(0, "Notes")
def remove_sl_veiw(name):
    global CURRENT_SL_ITEM
    frame_sl_veiw.lift()
    # fill Information
    notes = addfunc.get_info("list_id, notes", "shopping_list", "product_name", name, invdb)
    label_sld_name.configure(text=name)
    label_sld_notes.configure(text=str(notes[0][1]))
    CURRENT_SL_ITEM = notes[0][0]
def remove_sl():
    global CURRENT_SL_ITEM
    command = 'DELETE FROM shopping_list WHERE list_id = "'+str(CURRENT_SL_ITEM)+'";'
    c = invdb.cursor()
    c.execute(command)
    invdb.commit()
    update_sl()
    return_curScreen()
def check_nav():
    global CURRENTPAGE_SL
    global NUMPAGES_SL
    if (CURRENTPAGE_SL < NUMPAGES_SL-1):
        #button_lastPage_sl.place(relx=0.01, rely=0.889, height=40, width=45)
        button_NextPage_sl.place(relx=0.947, rely=0.889, height=40, width=45)
    if (CURRENTPAGE_SL == NUMPAGES_SL-1):
        button_NextPage_sl.place_forget()
    if (CURRENTPAGE_SL > 0):
        #button_NextPage_sl.place(relx=0.947, rely=0.889, height=40, width=45)
        button_lastPage_sl.place(relx=0.01, rely=0.889, height=40, width=45)
    if (CURRENTPAGE_SL == 0):
        button_lastPage_sl.place_forget()


#----------------------------------------
# Recipies Control Functions
#----------------------------------------
def update_r():
    global MAXPERPAGE_R
    global r_widgets
    global FIRSTLIST_R
    global CURRENTPAGE_R
    global NUMPAGES_R
    print("CURRENT PAGE >> "+str(CURRENTPAGE_R))
    print("FIRSTLIST_INV PAGE >> "+str(CURRENTPAGE_R))
    if (FIRSTLIST_R != 0):
        clear_widgets(r_widgets)
    FIRSTLIST_R = 1
    print("MAX PER PAGE >> " + str(MAXPERPAGE_R))
    # pull info from he database
    r = rfunc.get_r_data(invdb)
    print(r)
    # get total number of entries
    totalRow = len(r)
    print("LENGTH OF SL >> "+str(totalRow))
    numEntries = 0
    curRow = CURRENTPAGE_R*MAXPERPAGE_R
    # Calculate the number of pages
    NUMPAGES_R = math.ceil(totalRow/MAXPERPAGE_R)
    print("NUMBER OF PAGES >> "+str(NUMPAGES_R))
    Y = 0.222
    yinc = .08
    r_widgets = []
    # print labels
    print("TOTAL ROW >> "+str(totalRow))
    for row in range(totalRow):
        row += curRow
        print("R ROW >> "+str(row))
        if ((numEntries == MAXPERPAGE_R) or (row == totalRow+1)):
            break;

        button_rec_nameData = tk.Button(frame_rec_main)
        button_rec_nameData.place(relx=0.186, rely=Y, height=30, width=350)
        rfunc.configure_rButton(button_rec_nameData)
        button_rec_nameData.configure(text=r[row][0])
        sl_widgets.append(button_rec_nameData)
        button_rec_nameData.configure(command = lambda name=r[row][0]: get_recipe(name))

        label_rec_timeDate = tk.Label(frame_rec_main)
        label_rec_timeDate.place(relx=0.586, rely=Y, height=30, width=150)
        rfunc.configure_timeLabel(label_rec_timeDate)
        label_rec_timeDate.configure(text=r[row][1])
        sl_widgets.append(label_rec_timeDate)

        numEntries+=1
        Y+=yinc
def get_recipe(name):
    print("GET RECIPE >> "+name)
    # get recipe id
    rID = addfunc.get_info("recipe_id", "recipe", "recipe_name", name, invdb)
    print("RID >> "+str(rID[0][0]))
    # pull Instructions
    r_steps = addfunc.get_info("step_id, step", "steps","recipe_id", str(rID[0][0]), invdb)
    # pull Ingredients
    #r_ing = addfunc.get_info("")
    #print("STEPS >>")
    fill_recipe(rID[0][0])
def fill_recipe(id):
    global CURRENT_R
    CURRENT_R = id
    frame_addrec.lift()
    # pull Info
    r = addfunc.get_info("*", "recipe", "recipe_id", id, invdb)
    #print(r)
    r_steps = addfunc.get_info("step", "steps", "recipe_id", id, invdb)
    print("STEPS >> ")
    print(r_steps)
    r_ingr = addfunc.get_info("ingredient, amount","ingredients", "recipe_id", id, invdb)
    print("ING >>")
    print(r_ingr)
    label_recEnt_title.configure(text = r[0][1])
    label_recEnt_time.configure(text = r[0][2])

    totalRow_steps = len(r_steps)
    totalRow_ingr = len(r_ingr)
    #totalCol = len(r_steps[0])-1
    entry = 1
    steps = ""
    ingr = ""
    stepNum = 1
    for row in range(totalRow_steps):
        steps = steps+str(stepNum)+". "+r_steps[row][0] + "\n"
        print("\n"+str(r_steps[row][0]))
        stepNum+=1

    for row in range(totalRow_ingr):
        ingr = ingr + r_ingr[row][1] + " " + r_ingr[row][0] + "\n"
        print("\n"+str(r_ingr[row][0]))


    print(steps)
    print(ingr)

    label_steps.configure(text = steps)
    label_ing_list.configure(text = ingr)
def add_ing_sl():
    global CURRENT_R
    # get Ingredients
    i = addfunc.get_info("ingredient, amount","ingredients", "recipe_id", CURRENT_R, invdb)
    totalRow = len(i)
    for row in range(totalRow):
        add_from_rec(i[row][0],i[row][1])

#----------------------------------------
# DRIVING CODE
#----------------------------------------
# make root
root = tk.Tk()
root.title("IOT Pantry System")
configure_root()

# Screen frames
canvas_base = tk.Canvas(root)
frame_sl_main = tk.Frame(canvas_base)
frame_rec_menu = tk.Frame(canvas_base)
frame_rec_main = tk.Frame(canvas_base)
frame_addEntry = tk.Frame(canvas_base)
frame_invMain = tk.Frame(canvas_base)
frame_inv_search = tk.Frame(canvas_base)
frame_del = tk.Frame(canvas_base)

# Base components used on all the screens
button_Inventory = tk.Button(canvas_base)
button_shoplist = tk.Button(canvas_base)
button_recipies = tk.Button(canvas_base)
entry_barcode = tk.Entry(canvas_base)
button_in = tk.Button(canvas_base)
button_out = tk.Button(canvas_base)
entry_addShopList = tk.Entry(canvas_base)
entry_notesShopList = tk.Entry(canvas_base)
button_addShopList = tk.Button(canvas_base)

# functional components of delete entry Delete popup
button_delete = tk.Button(frame_del)
label_delName = tk.Label(frame_del)
entry_numDelete = tk.Entry(frame_del)
label_barDelete = tk.Label(frame_del)
label_expDel = tk.Label(frame_del)
label_entDate = tk.Label(frame_del)
label_curNum = tk.Label(frame_del)
label_userInst = tk.Label(frame_del)

# Functional Components of the item entry popup
entry_code = tk.Entry(frame_addEntry)
Entry_prod_name = tk.Entry(frame_addEntry)
Entry_foodGroup = tk.Entry(frame_addEntry)
Entry_expd = tk.Entry(frame_addEntry)
entry_numItems = tk.Entry(frame_addEntry)
button_add = tk.Button(frame_addEntry)

# Functional Components on the inventory screens
button_NextPage = tk.Button(frame_invMain)
button_lastPage = tk.Button(frame_invMain)
entry_inv_search = tk.Entry(frame_inv_search)
button_inv_search = tk.Button(frame_inv_search)

# Functional Components on the Shopping List
button_NextPage_sl= tk.Button(frame_sl_main)
button_lastPage_sl = tk.Button(frame_sl_main)
button_sl_delete = tk.Button(frame_sl_main)

# functional components of the manual remove from sl popup
frame_sl_veiw = tk.Frame(canvas_base)
button_delete_sl = tk.Button(frame_sl_veiw)
label_sld_name = tk.Label(frame_sl_veiw)
label_sld_notes = tk.Label(frame_sl_veiw)
button_closeDel_sl = tk.Button(frame_sl_veiw)

# Functional components of the Recipies
frame_addrec = tk.Frame(canvas_base)
label_recEnt_title = tk.Label(frame_addrec)
label_recEnt_time = tk.Label(frame_addrec)
button_rec_addin = tk.Button(frame_addrec)
label_steps = tk.Label(frame_addrec)
label_ing_list = tk.Label(frame_addrec)



# configure the separate screens
configure_base()
configure_sl()
configure_recipies()
configure_recEntry()
configure_addEntry()
configure_inv()
configure_delEntry()
configure_sl_veiw()
# pick start screen
focus_inv()

# Start GUI
root.mainloop()
