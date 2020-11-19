#############################################################################
# Generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#  Nov 09, 2020 12:27:13 AM EST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top45 {base} {
    global vTcl
    if {$base == ""} {
        set base .top45
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1173x873+319+95
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    canvas $top.can46 \
        -background #3e3c55 -borderwidth 2 -closeenough 1.0 -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -relief ridge -selectbackground blue \
        -selectforeground white -width 125 
    vTcl:DefineAlias "$top.can46" "canvas_base" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.can46
    button $site_3_0.but47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -relief ridge -text Inventory 
    vTcl:DefineAlias "$site_3_0.but47" "button_Inventory" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but48 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -relief ridge -text {Shopping List} 
    vTcl:DefineAlias "$site_3_0.but48" "button_shoplist" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but49 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -relief ridge -text Recipies 
    vTcl:DefineAlias "$site_3_0.but49" "button_recipies" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent50 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 10 
    vTcl:DefineAlias "$site_3_0.ent50" "entry_barcode" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but51 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #36a35c -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Scan In} 
    vTcl:DefineAlias "$site_3_0.but51" "button_in" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but52 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #af0101 -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Scan Out} 
    vTcl:DefineAlias "$site_3_0.but52" "button_out" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent53 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 254 
    vTcl:DefineAlias "$site_3_0.ent53" "entry_addShopList" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but54 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Add To Shopping List} 
    vTcl:DefineAlias "$site_3_0.but54" "button_addShopList" vTcl:WidgetProc "Toplevel1" 1
    frame $site_3_0.fra85 \
        -borderwidth 2 -relief groove -background #737373 -height 75 \
        -width 125 
    vTcl:DefineAlias "$site_3_0.fra85" "frame_rec_menu" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra85
    ttk::combobox $site_4_0.tCo88 \
        -font TkTextFont -textvariable combobox -foreground {} -background {} \
        -takefocus {} 
    vTcl:DefineAlias "$site_4_0.tCo88" "TCombobox1" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_4_0.tCo90 \
        -font TkTextFont -textvariable combobox -foreground {} -background {} \
        -takefocus {} 
    vTcl:DefineAlias "$site_4_0.tCo90" "TCombobox2" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_0.but91 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Filter 
    vTcl:DefineAlias "$site_4_0.but91" "Button1" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.tCo88 \
        -in $site_4_0 -x 0 -relx 0.596 -y 0 -rely 0.3 -width 0 \
        -relwidth 0.145 -height 0 -relheight 0.42 -anchor nw \
        -bordermode ignore 
    place $site_4_0.tCo90 \
        -in $site_4_0 -x 0 -relx 0.752 -y 0 -rely 0.3 -width 0 \
        -relwidth 0.142 -height 0 -relheight 0.42 -anchor nw \
        -bordermode ignore 
    place $site_4_0.but91 \
        -in $site_4_0 -x 0 -relx 0.908 -y 0 -rely 0.3 -width 75 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    frame $site_3_0.fra86 \
        -borderwidth 2 -relief groove -background #585670 -height 75 \
        -width 125 
    vTcl:DefineAlias "$site_3_0.fra86" "frame_rec_main" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra86
    label $site_4_0.lab92 \
        -background #939393 -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Name 
    vTcl:DefineAlias "$site_4_0.lab92" "label_rec_name" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab93 \
        -background #939393 -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Time 
    vTcl:DefineAlias "$site_4_0.lab93" "label_rec_time" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab94 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -text X 
    vTcl:DefineAlias "$site_4_0.lab94" "label_rec_timeDate" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_0.but95 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -relief flat -text X 
    vTcl:DefineAlias "$site_4_0.but95" "button_rec_nameData" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.lab92 \
        -in $site_4_0 -x 0 -relx 0.186 -y 0 -rely 0.111 -width 0 \
        -relwidth 0.343 -height 0 -relheight 0.067 -anchor nw \
        -bordermode ignore 
    place $site_4_0.lab93 \
        -in $site_4_0 -x 0 -relx 0.586 -y 0 -rely 0.111 -width 0 \
        -relwidth 0.146 -height 0 -relheight 0.067 -anchor nw \
        -bordermode ignore 
    place $site_4_0.lab94 \
        -in $site_4_0 -x 0 -relx 0.586 -y 0 -rely 0.222 -width 0 \
        -relwidth 0.146 -height 0 -relheight 0.067 -anchor nw \
        -bordermode ignore 
    place $site_4_0.but95 \
        -in $site_4_0 -x 0 -relx 0.186 -y 0 -rely 0.222 -width 350 \
        -relwidth 0 -height 30 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but47 \
        -in $site_3_0 -x 0 -y 0 -width 341 -relwidth 0 -height 50 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but48 \
        -in $site_3_0 -x 0 -relx 0.332 -y 0 -width 342 -relwidth 0 -height 50 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but49 \
        -in $site_3_0 -x 0 -relx 0.664 -y 0 -width 341 -relwidth 0 -height 50 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent50 \
        -in $site_3_0 -x 0 -relx 0.801 -y 0 -rely 0.933 -width 84 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but51 \
        -in $site_3_0 -x 0 -relx 0.802 -y 0 -rely 0.917 -width 100 \
        -relwidth 0 -height 50 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but52 \
        -in $site_3_0 -x 0 -relx 0.899 -y 0 -rely 0.917 -width 100 \
        -relwidth 0 -height 50 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent53 \
        -in $site_3_0 -x 0 -relx 0.039 -y 0 -rely 0.933 -width 254 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but54 \
        -in $site_3_0 -x 0 -relx 0.303 -y 0 -rely 0.933 -width 200 \
        -relwidth 0 -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.fra85 \
        -in $site_3_0 -x 0 -y 0 -rely 0.083 -width 0 -relwidth 1 -height 0 \
        -relheight 0.083 -anchor nw -bordermode ignore 
    place $site_3_0.fra86 \
        -in $site_3_0 -x 0 -y 0 -rely 0.167 -width 0 -relwidth 1 -height 0 \
        -relheight 0.75 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.can46 \
        -in $top -x 0 -relx 0.06 -y 0 -rely 0.126 -width 0 -relwidth 0.873 \
        -height 0 -relheight 0.687 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top45 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
