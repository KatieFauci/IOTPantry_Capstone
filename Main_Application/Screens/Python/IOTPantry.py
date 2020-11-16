import sys
import tkinter as tk
import Tcl
import mysql.connector
from datetime import date

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
    canvas_base.place(relx=0, rely=0, relheight=1
            , relwidth=1)
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
    button_Inventory.configure(command=create_inv)

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
    button_shoplist.configure(command=create_sl)

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
    button_recipies.configure(command=create_recipies)

    entry_barcode.place(relx=0.811, rely=0.933, height=20
            , relwidth=0.082)
    entry_barcode.configure(background="white")
    entry_barcode.configure(disabledforeground="#a3a3a3")
    entry_barcode.configure(font="TkFixedFont")
    entry_barcode.configure(foreground="#000000")
    entry_barcode.configure(highlightbackground="#d9d9d9")
    entry_barcode.configure(highlightcolor="black")
    entry_barcode.configure(insertbackground="black")
    entry_barcode.configure(selectbackground="blue")
    entry_barcode.configure(selectforeground="white")
    entry_barcode.bind('<Return>',scan_in)

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
    button_out.configure(command=focus_barEntry)

    entry_addShopList.place(relx=0.039, rely=0.933, height=20
            , relwidth=0.248)
    entry_addShopList.configure(background="white")
    entry_addShopList.configure(disabledforeground="#a3a3a3")
    entry_addShopList.configure(font="TkFixedFont")
    entry_addShopList.configure(foreground="#000000")
    entry_addShopList.configure(highlightbackground="#d9d9d9")
    entry_addShopList.configure(highlightcolor="black")
    entry_addShopList.configure(insertbackground="black")
    entry_addShopList.configure(selectbackground="blue")
    entry_addShopList.configure(selectforeground="white")

    button_addShopList.place(relx=0.303, rely=0.933, height=24
            , width=200)
    button_addShopList.configure(activebackground="#ececec")
    button_addShopList.configure(activeforeground="#000000")
    button_addShopList.configure(background="#d9d9d9")
    button_addShopList.configure(disabledforeground="#a3a3a3")
    button_addShopList.configure(foreground="#000000")
    button_addShopList.configure(highlightbackground="#d9d9d9")
    button_addShopList.configure(highlightcolor="black")
    button_addShopList.configure(pady="0")
    button_addShopList.configure(text='''Add To Shopping List''')


def create_inv():
    frame_invMain = tk.Frame(canvas_base)
    frame_invMain.place(relx=0.0, rely=0.167, relheight=0.75
            , relwidth=1.0)
    frame_invMain.configure(relief='groove')
    frame_invMain.configure(borderwidth="2")
    frame_invMain.configure(relief="groove")
    frame_invMain.configure(background="#585670")
    frame_invMain.configure(highlightbackground="#d9d9d9")
    frame_invMain.configure(highlightcolor="black")

    label_inv_name = tk.Label(frame_invMain)
    label_inv_name.place(relx=0.127, rely=0.044, height=30, width=125)
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

    button_inv_del = tk.Button(frame_invMain)
    button_inv_del.place(relx=0.049, rely=0.044, height=24, width=47)
    button_inv_del.configure(activebackground="#ececec")
    button_inv_del.configure(activeforeground="#000000")
    button_inv_del.configure(background="#af0101")
    button_inv_del.configure(disabledforeground="#a3a3a3")
    button_inv_del.configure(foreground="#000000")
    button_inv_del.configure(highlightbackground="#d9d9d9")
    button_inv_del.configure(highlightcolor="black")
    button_inv_del.configure(pady="0")
    button_inv_del.configure(text='''Delete''')

    button_inv_nameAct = tk.Button(frame_invMain)
    button_inv_nameAct.place(relx=0.127, rely=0.156, height=30
            , width=125)
    button_inv_nameAct.configure(activebackground="#ececec")
    button_inv_nameAct.configure(activeforeground="#000000")
    button_inv_nameAct.configure(background="#d3d3d3")
    button_inv_nameAct.configure(disabledforeground="#a3a3a3")
    button_inv_nameAct.configure(foreground="#000000")
    button_inv_nameAct.configure(highlightbackground="#d9d9d9")
    button_inv_nameAct.configure(highlightcolor="black")
    button_inv_nameAct.configure(pady="0")
    button_inv_nameAct.configure(relief="flat")
    button_inv_nameAct.configure(text='''NAME BUTTON''')

    Checkbutton1 = tk.Checkbutton(frame_invMain)
    Checkbutton1.place(relx=0.049, rely=0.156, relheight=0.056
            , relwidth=0.061)
    Checkbutton1.configure(activebackground="#ececec")
    Checkbutton1.configure(activeforeground="#000000")
    Checkbutton1.configure(background="#585670")
    Checkbutton1.configure(disabledforeground="#a3a3a3")
    Checkbutton1.configure(foreground="#000000")
    Checkbutton1.configure(highlightbackground="#d9d9d9")
    Checkbutton1.configure(highlightcolor="black")
    Checkbutton1.configure(justify='left')
    #Checkbutton1.configure(variable=Inventory_support.che72)

    label_inv_quanData = tk.Label(frame_invMain)
    label_inv_quanData.place(relx=0.264, rely=0.156, height=30
            , width=124)
    label_inv_quanData.configure(activebackground="#f9f9f9")
    label_inv_quanData.configure(activeforeground="black")
    label_inv_quanData.configure(background="#d9d9d9")
    label_inv_quanData.configure(disabledforeground="#a3a3a3")
    label_inv_quanData.configure(foreground="#000000")
    label_inv_quanData.configure(highlightbackground="#d9d9d9")
    label_inv_quanData.configure(highlightcolor="black")
    label_inv_quanData.configure(text='''X''')

    label_inv_fgData = tk.Label(frame_invMain)
    label_inv_fgData.place(relx=0.4, rely=0.156, height=30, width=125)
    label_inv_fgData.configure(activebackground="#f9f9f9")
    label_inv_fgData.configure(activeforeground="black")
    label_inv_fgData.configure(background="#d9d9d9")
    label_inv_fgData.configure(disabledforeground="#a3a3a3")
    label_inv_fgData.configure(foreground="#000000")
    label_inv_fgData.configure(highlightbackground="#d9d9d9")
    label_inv_fgData.configure(highlightcolor="black")
    label_inv_fgData.configure(text='''X''')

    label_inv_endData = tk.Label(frame_invMain)
    label_inv_endData.place(relx=0.537, rely=0.156, height=30
            , width=125)
    label_inv_endData.configure(activebackground="#f9f9f9")
    label_inv_endData.configure(activeforeground="black")
    label_inv_endData.configure(background="#d9d9d9")
    label_inv_endData.configure(disabledforeground="#a3a3a3")
    label_inv_endData.configure(foreground="#000000")
    label_inv_endData.configure(highlightbackground="#d9d9d9")
    label_inv_endData.configure(highlightcolor="black")
    label_inv_endData.configure(text='''X''')

    label_inv_exdData = tk.Label(frame_invMain)
    label_inv_exdData.place(relx=0.674, rely=0.156, height=30
            , width=125)
    label_inv_exdData.configure(activebackground="#f9f9f9")
    label_inv_exdData.configure(activeforeground="black")
    label_inv_exdData.configure(background="#d9d9d9")
    label_inv_exdData.configure(disabledforeground="#a3a3a3")
    label_inv_exdData.configure(foreground="#000000")
    label_inv_exdData.configure(highlightbackground="#d9d9d9")
    label_inv_exdData.configure(highlightcolor="black")
    label_inv_exdData.configure(text='''X''')

    label_inv_barcData = tk.Label(frame_invMain)
    label_inv_barcData.place(relx=0.811, rely=0.156, height=30
            , width=125)
    label_inv_barcData.configure(activebackground="#f9f9f9")
    label_inv_barcData.configure(activeforeground="black")
    label_inv_barcData.configure(background="#d9d9d9")
    label_inv_barcData.configure(disabledforeground="#a3a3a3")
    label_inv_barcData.configure(foreground="#000000")
    label_inv_barcData.configure(highlightbackground="#d9d9d9")
    label_inv_barcData.configure(highlightcolor="black")
    label_inv_barcData.configure(text='''X''')

    frame_inv_search = tk.Frame(canvas_base)
    frame_inv_search.place(relx=0.0, rely=0.083, relheight=0.083
            , relwidth=1.0)
    frame_inv_search.configure(relief='groove')
    frame_inv_search.configure(borderwidth="2")
    frame_inv_search.configure(relief="groove")
    frame_inv_search.configure(background="#737373")
    frame_inv_search.configure(highlightbackground="#d9d9d9")
    frame_inv_search.configure(highlightcolor="black")

    entry_inv_search = tk.Entry(frame_inv_search)
    entry_inv_search.place(relx=0.02, rely=0.3, height=20
            , relwidth=0.17)
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
    #
    #combo_inv_type = tk.Combobox(frame_inv_search)
    #combo_inv_type.place(relx=0.508, rely=0.3, relheight=0.42
    #        , relwidth=0.146)
    #combo_inv_type.configure(textvariable=Inventory_support.combobox)
    #combo_inv_type.configure(takefocus="")

    #combo_inv_crit = tk.Combobox(frame_inv_search)
    #combo_inv_crit.place(relx=0.664, rely=0.3, relheight=0.42
    #        , relwidth=0.14)
    #combo_inv_crit.configure(textvariable=Inventory_support.combobox)
    #combo_inv_crit.configure(takefocus="")

    button_inv_filter = tk.Button(frame_inv_search)
    button_inv_filter.place(relx=0.82, rely=0.3, height=24, width=70)
    button_inv_filter.configure(activebackground="#ececec")
    button_inv_filter.configure(activeforeground="#000000")
    button_inv_filter.configure(background="#d9d9d9")
    button_inv_filter.configure(disabledforeground="#a3a3a3")
    button_inv_filter.configure(foreground="#000000")
    button_inv_filter.configure(highlightbackground="#d9d9d9")
    button_inv_filter.configure(highlightcolor="black")
    button_inv_filter.configure(pady="0")
    button_inv_filter.configure(text='''Filter''')

    button_inv_CLfilter = tk.Button(frame_inv_search)
    button_inv_CLfilter.place(relx=0.908, rely=0.3, height=24, width=70)

    button_inv_CLfilter.configure(activebackground="#ececec")
    button_inv_CLfilter.configure(activeforeground="#000000")
    button_inv_CLfilter.configure(background="#d9d9d9")
    button_inv_CLfilter.configure(disabledforeground="#a3a3a3")
    button_inv_CLfilter.configure(foreground="#000000")
    button_inv_CLfilter.configure(highlightbackground="#d9d9d9")
    button_inv_CLfilter.configure(highlightcolor="black")
    button_inv_CLfilter.configure(pady="0")
    button_inv_CLfilter.configure(text='''Clear Filter''')
def create_sl():

    frame_sl_main = tk.Frame(canvas_base)
    frame_sl_main.place(relx=0.0, rely=0.083, relheight=0.833
            , relwidth=1.0)
    frame_sl_main.configure(relief='groove')
    frame_sl_main.configure(borderwidth="2")
    frame_sl_main.configure(relief="groove")
    frame_sl_main.configure(background="#585670")
    frame_sl_main.configure(highlightbackground="#d9d9d9")
    frame_sl_main.configure(highlightcolor="black")

    button_sl_delete = tk.Button(frame_sl_main)
    button_sl_delete.place(relx=0.059, rely=0.068, height=24, width=47)
    button_sl_delete.configure(activebackground="#ececec")
    button_sl_delete.configure(activeforeground="#000000")
    button_sl_delete.configure(background="#af0101")
    button_sl_delete.configure(disabledforeground="#a3a3a3")
    button_sl_delete.configure(foreground="#000000")
    button_sl_delete.configure(highlightbackground="#d9d9d9")
    button_sl_delete.configure(highlightcolor="black")
    button_sl_delete.configure(pady="0")
    button_sl_delete.configure(text='''Delete''')

    label_sl_item = tk.Label(frame_sl_main)
    label_sl_item.place(relx=0.117, rely=0.156, height=34, width=198)
    label_sl_item.configure(activebackground="#f9f9f9")
    label_sl_item.configure(activeforeground="black")
    label_sl_item.configure(background="#d9d9d9")
    label_sl_item.configure(disabledforeground="#a3a3a3")
    label_sl_item.configure(foreground="#000000")
    label_sl_item.configure(highlightbackground="#d9d9d9")
    label_sl_item.configure(highlightcolor="black")
    label_sl_item.configure(text='''X''')

    Checkbutton2 = tk.Checkbutton(frame_sl_main)
    Checkbutton2.place(relx=0.059, rely=0.156, relheight=0.056
            , relwidth=0.061)
    Checkbutton2.configure(activebackground="#ececec")
    Checkbutton2.configure(activeforeground="#000000")
    Checkbutton2.configure(background="#585670")
    Checkbutton2.configure(disabledforeground="#a3a3a3")
    Checkbutton2.configure(foreground="#000000")
    Checkbutton2.configure(highlightbackground="#d9d9d9")
    Checkbutton2.configure(highlightcolor="black")
    Checkbutton2.configure(justify='left')
def create_recipies():
    frame_rec_menu = tk.Frame(canvas_base)
    frame_rec_menu.place(relx=0.0, rely=0.083, relheight=0.083
            , relwidth=1.0)
    frame_rec_menu.configure(relief='groove')
    frame_rec_menu.configure(borderwidth="2")
    frame_rec_menu.configure(relief="groove")
    frame_rec_menu.configure(background="#737373")

    #TCombobox1 = ttk.Combobox(frame_rec_menu)
    #TCombobox1.place(relx=0.596, rely=0.3, relheight=0.42
    #        , relwidth=0.146)
    #TCombobox1.configure(textvariable=Recipies_support.combobox)
    #TCombobox1.configure(takefocus="")

    #TCombobox2 = ttk.Combobox(frame_rec_menu)
    #TCombobox2.place(relx=0.752, rely=0.3, relheight=0.42
    #        , relwidth=0.142)
    #TCombobox2.configure(textvariable=Recipies_support.combobox)
    #TCombobox2.configure(takefocus="")

    Button1 = tk.Button(frame_rec_menu)
    Button1.place(relx=0.908, rely=0.3, height=24, width=75)
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#d9d9d9")
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(foreground="#000000")
    Button1.configure(highlightbackground="#d9d9d9")
    Button1.configure(highlightcolor="black")
    Button1.configure(pady="0")
    Button1.configure(text='''Filter''')

    frame_rec_main = tk.Frame(canvas_base)
    frame_rec_main.place(relx=0.0, rely=0.167, relheight=0.75
            , relwidth=1.0)
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
    label_rec_timeDate.place(relx=0.586, rely=0.222, height=30
            , width=150)
    label_rec_timeDate.configure(background="#d9d9d9")
    label_rec_timeDate.configure(disabledforeground="#a3a3a3")
    label_rec_timeDate.configure(foreground="#000000")
    label_rec_timeDate.configure(text='''X''')

    button_rec_nameData = tk.Button(frame_rec_main)
    button_rec_nameData.place(relx=0.186, rely=0.222, height=30
            , width=350)
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
def create_recEntry():
    Frame1 = tk.Frame(canvas_base)
    Frame1.place(relx=0.0, rely=0.083, relheight=0.833, relwidth=1.0)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief="groove")
    Frame1.configure(background="#585670")

    label_recEnt_title = tk.Label(Frame1)
    label_recEnt_title.place(relx=0.078, rely=0.08, height=30
            , width=350)
    label_recEnt_title.configure(background="#939393")
    label_recEnt_title.configure(disabledforeground="#a3a3a3")
    label_recEnt_title.configure(foreground="#000000")
    label_recEnt_title.configure(text='''Title''')

    label_recEnt_time = tk.Label(Frame1)
    label_recEnt_time.place(relx=0.078, rely=0.16, height=30, width=50)
    label_recEnt_time.configure(background="#939393")
    label_recEnt_time.configure(disabledforeground="#a3a3a3")
    label_recEnt_time.configure(foreground="#000000")
    label_recEnt_time.configure(text='''Time''')

    label_rec_ins = tk.Label(Frame1)
    label_rec_ins.place(relx=0.449, rely=0.28, height=21, width=149)
    label_rec_ins.configure(background="#939393")
    label_rec_ins.configure(cursor="fleur")
    label_rec_ins.configure(disabledforeground="#a3a3a3")
    label_rec_ins.configure(foreground="#000000")
    label_rec_ins.configure(text='''Instructions''')

    label_rec_ing = tk.Label(Frame1)
    label_rec_ing.place(relx=0.088, rely=0.28, height=21, width=150)
    label_rec_ing.configure(background="#939393")
    label_rec_ing.configure(disabledforeground="#a3a3a3")
    label_rec_ing.configure(foreground="#000000")
    label_rec_ing.configure(text='''Ingredients''')

    button_rec_addin = tk.Button(Frame1)
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

    listbox_rec_ing = tk.Listbox(Frame1)
    listbox_rec_ing.place(relx=0.088, rely=0.34, relheight=0.544
            , relwidth=0.316)
    listbox_rec_ing.configure(background="white")
    listbox_rec_ing.configure(cursor="fleur")
    listbox_rec_ing.configure(disabledforeground="#a3a3a3")
    listbox_rec_ing.configure(font="TkFixedFont")
    listbox_rec_ing.configure(foreground="#000000")

    Llistbox_rec_ins = tk.Listbox(Frame1)
    Llistbox_rec_ins.place(relx=0.449, rely=0.34, relheight=0.544
            , relwidth=0.512)
    Llistbox_rec_ins.configure(background="white")
    Llistbox_rec_ins.configure(disabledforeground="#a3a3a3")
    Llistbox_rec_ins.configure(font="TkFixedFont")
    Llistbox_rec_ins.configure(foreground="#000000")
def create_addEntry():

    Frame1.place(relx=0.381, rely=0.15, relheight=0.658, relwidth=0.243)

    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief="groove")
    Frame1.configure(background="#d9d9d9")


    entry_code.place(relx=0.1, rely=0.152, height=20, relwidth=0.803)
    entry_code.configure(background="white")
    entry_code.configure(cursor="fleur")
    entry_code.configure(disabledforeground="#a3a3a3")
    entry_code.configure(font="TkFixedFont")
    entry_code.configure(foreground="#000000")
    entry_code.configure(insertbackground="black")
    entry_code.bind('<Return>',scan_in)

    Entry_prod_name.place(relx=0.1, rely=0.278, height=20
            , relwidth=0.803)
    Entry_prod_name.configure(background="white")
    Entry_prod_name.configure(disabledforeground="#a3a3a3")
    Entry_prod_name.configure(font="TkFixedFont")
    Entry_prod_name.configure(foreground="#000000")
    Entry_prod_name.configure(insertbackground="black")

    label_code = tk.Label(Frame1)
    label_code.place(relx=0.1, rely=0.101, height=21, width=201)
    label_code.configure(background="#d9d9d9")
    label_code.configure(disabledforeground="#a3a3a3")
    label_code.configure(foreground="#000000")
    label_code.configure(justify='left')
    label_code.configure(text='''Barcode''')

    label_prodName = tk.Label(Frame1)
    label_prodName.place(relx=0.1, rely=0.228, height=21, width=201)
    label_prodName.configure(background="#d9d9d9")
    label_prodName.configure(disabledforeground="#a3a3a3")
    label_prodName.configure(foreground="#000000")
    label_prodName.configure(justify='left')
    label_prodName.configure(text='''Product Name''')


    Entry_foodGroup.place(relx=0.1, rely=0.405, height=20
            , relwidth=0.803)
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

    Label_foodGroup = tk.Label(Frame1)
    Label_foodGroup.place(relx=0.1, rely=0.354, height=21, width=201)
    Label_foodGroup.configure(background="#d9d9d9")
    Label_foodGroup.configure(disabledforeground="#a3a3a3")
    Label_foodGroup.configure(foreground="#000000")
    Label_foodGroup.configure(text='''Food Group''')

    Label_enterexp = tk.Label(Frame1)
    Label_enterexp.place(relx=0.1, rely=0.481, height=21, width=201)
    Label_enterexp.configure(background="#d9d9d9")
    Label_enterexp.configure(disabledforeground="#a3a3a3")
    Label_enterexp.configure(foreground="#000000")
    Label_enterexp.configure(text='''Expiration Date''')

    entry_numItems.place(relx=0.1, rely=0.658, height=20
            , relwidth=0.803)
    entry_numItems.configure(background="white")
    entry_numItems.configure(disabledforeground="#a3a3a3")
    entry_numItems.configure(font="TkFixedFont")
    entry_numItems.configure(foreground="#000000")
    entry_numItems.configure(insertbackground="black")

    label_numitems = tk.Label(Frame1)
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

#-------------------------------
# Control Functions
#-------------------------------
def focus_barEntry():
    END = 50
    Frame1.lift()
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


def scan_in(event):
    # Get code scanned
    code = entry_code.get()
    entry_code.configure(text=code)

    # Pull information from ref_database
    mycursor = refdb.cursor()
    command = "SELECT * FROM items WHERE barcode="+code+";"
    print(command)
    mycursor.execute(command)
    info = mycursor.fetchall()
    print(info)

    # Fill entries
    #entry_code.insert(0,code)
    Entry_prod_name.insert(0, str(info[0][1]))
    Entry_foodGroup.insert(0, str(info[0][2]))
    Entry_expd.insert(0, str(info[0][3]))
    entry_numItems.insert(0,"1")

def add_inv():
    # Check if already in Inventory
    mycursor = invdb.cursor()
    command = "SELECT EXISTS(SELECT * FROM items WHERE barcode_num="+str(entry_code.get())+");"
    mycursor.execute(command)
    info = mycursor.fetchall()
    print(info)

    if(info[0][0] == 0): # Add as a new item
        # get new id
        mycursor = invdb.cursor()
        mycursor.execute("SELECT MAX(item_id)+1 FROM items;")
        nextid = mycursor.fetchall()
        print("Next ID >>> " + str(nextid[0][0]))
        # build add
        add_item = ("INSERT INTO items "
                    "(product_name, input_date, expiration_date, frequency_tag, barcode_num, num_items, food_group)"
                    "VALUES(%s,%s,%s,%s,%s,%s,%s)")
        data_item = (Entry_prod_name.get(), date.today(), Entry_expd.get(), entry_code.get(), entry_numItems.get(), Entry_foodGroup.get())
        # Execute command
        mycursor.execute(add_item, data_item)
        invdb.commit()
        print(" << item added >> ")

    #else:   # increment count acordint to amount entered




def scan_out(event):

    print("CONNECTED TO  >>>  " + mydb)
    mycusor = mydb.cursor()
    # build command
    code = entry_barcode.get()
    command = "Delete_Barcode("+code+");"
    mycusor = mydb.cursor()
    mycursor.execute(command)


#----------------------------------------
# DRIVING CODE
#----------------------------------------
global val, w, root
# make root
root = tk.Tk()
root.title("IOT Pantry System")
configure_root()

# Base components used on all the screens
canvas_base = tk.Canvas(root)
button_Inventory = tk.Button(canvas_base)
button_shoplist = tk.Button(canvas_base)
button_recipies = tk.Button(canvas_base)
entry_barcode = tk.Entry(canvas_base)
button_in = tk.Button(canvas_base)
button_out = tk.Button(canvas_base)
entry_addShopList = tk.Entry(canvas_base)
button_addShopList = tk.Button(canvas_base)
configure_base()

# Functional Components of the item entry popup
Frame1 = tk.Frame(canvas_base)
entry_code = tk.Entry(Frame1)
Entry_prod_name = tk.Entry(Frame1)
Entry_foodGroup = tk.Entry(Frame1)
Entry_expd = tk.Entry(Frame1)
entry_numItems = tk.Entry(Frame1)
button_add = tk.Button(Frame1)

# Connect to databases
invdb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="inventory"
)
refdb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="ref_database"
)

# Creates the separate screens
create_sl()
create_recipies()
create_recEntry()
create_addEntry()
create_inv()
# Start GUI
root.mainloop()
