#!/usr/bin/env python
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
import mysql.connector
from mysql.connector import errorcode

#import sqlite3 as sql

import os
import threading

config = {
    'user': 'root',
    'password': 'RamR3b3l4297',
    'host': 'localhost',
    'database': 'inventory',
    'raise_on_warnings': True
}
invdb = mysql.connector.connect(**config)

#Login Screen to access personal database
class LoginScreen(BoxLayout):

    orientation = "vertical"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Screen background color
        Window.clearcolor = (0.40, 0.40, 0.40, 1)

        self.add_widget(Label())

        self.add_widget(Label(text='Smart Pantry',
                              font_size='40sp',
                              size_hint=(1, .36),
                              bold=True))
        self.add_widget(Label())

        #Username Widget
        self.add_widget(Label(
            text='Username:',
            font_size='20sp',
            size_hint=(.25, .46),
            pos_hint={'right': .62}))
        self.username = TextInput(multiline=False,
                                  size_hint=(.25, .66),
                                  pos_hint={'right': .62})
        self.add_widget(self.username)

        #Password Widget
        self.add_widget(Label(
            text='Password:',
            font_size='20sp',
            size_hint=(.25, .46),
            pos_hint={'right': .62}))
        self.password = TextInput(password=True,
                                  multiline=False,
                                  size_hint=(.25, .66),
                                  pos_hint={'right': .62})
        self.add_widget(self.password)

        #Login Button Widget
        self.login = Button(
            text="Log In",
            size_hint=(.25, .46),
            pos_hint={'right': .62})
        self.login.bind(on_press=self.login_button)
        self.add_widget(Label())
        self.add_widget(self.login)
        self.add_widget(Label())

    #Function of button
    def login_button(self, instance):
        username = self.username.text
        password = self.password.text

        if username == "IOTPantry":
            if password == "smartpantry":
                IOT_app.screen_manager.current = "HomePage"
            else:
                IOT_app.screen_manager.current = "Error"
        else:
            IOT_app.screen_manager.current = "Error"



#Screen if user inputs wrong account
class Error(BoxLayout):

    orientation = "vertical"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Label())
        self.add_widget(Label())

        #Error Message Displayed To User
        self.add_widget(Label(text='Invalid username or password. Please try again.',
                              size_hint=(1, .36),
                              font_size='32sp'))

        #Return To Login Page Button
        self.ReturnBut = Button(text="Try Again",
                                size_hint=(.25, .46),
                                pos_hint={'right': .62})
        self.ReturnBut.bind(on_press=self.ReturnButton)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.ReturnBut)

        self.add_widget(Label())
        self.add_widget(Label())

    #Switches Screen
    def ReturnButton(self, instance):
        IOT_app.screen_manager.current = "LoginScreen"



#Home Page Screen
class HomePage(BoxLayout):

    orientation = "vertical"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Label())

        #Screen Header
        self.add_widget(Label(text="Welcome to your pantry",
                              font_size='40sp',
                              size_hint=(1, .36),
                              bold=True))

        #Define Inventory button
        self.Invent = Button(text="Pantry Inventory",
                             size_hint=(.25, .46),
                             pos_hint={'right': .62})
        self.Invent.bind(on_press=self.InventoryButton)
        self.add_widget(Label())
        self.add_widget(self.Invent)

        # Define Shopping List button
        self.Shop_Button = Button(text="Shopping List",
                                  size_hint=(.25, .46),
                                  pos_hint={'right': .62})
        self.Shop_Button.bind(on_press=self.ShoppingButton)
        self.add_widget(Label())
        self.add_widget(self.Shop_Button)

        # Define Recipe Book button
        self.Recipes = Button(text="Recipe Book",
                              size_hint=(.25, .46),
                              pos_hint={'right': .62})
        self.Recipes.bind(on_press=self.RecipeButton)
        self.add_widget(Label())
        self.add_widget(self.Recipes)

        self.add_widget(Label())

    #Create button function
    def InventoryButton(self, instance):
        info1 = "Loading Inventory"
        IOT_app.screen_manager.current = "Inventory"

    # Create button function
    def ShoppingButton(self, instance):
        info2 = "Loading Shopping List"
        IOT_app.screen_manager.current = "Shopping List"

    # Create button function
    def RecipeButton(self, instance):
        info3 = "Loading Recipes"
        IOT_app.screen_manager.current = "Recipe Book"



#Pantry Inventory Screen
class InventoryPage(FloatLayout):
    # Updates info on HomePage

    def update_info(self, message):
        self.message.text = message

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.word_dict = {}

        self.add_widget(Label())

        self.add_widget(Label(text="Inventory",
                              font_size='40sp',
                              size_hint=(1, 2),
                              pos_hint={'center_x': .5, 'center_y': .95},
                              bold=True))

        self.add_widget(Label())

        self.add_widget(Label(text="Product Name",
                              size_hint=(1, 2),
                              pos_hint={'center_x': .25, 'center_y': .85},
                              bold=True))

        self.add_widget(Label(text="Quantity",
                              size_hint=(.25, .46),
                              pos_hint={'center_x': .55, 'center_y': .85},
                              bold=True))

        self.add_widget(Label(text="Expiration",
                              size_hint=(.25, .46),
                              pos_hint={'center_x': .75, 'center_y': .85},
                              bold=True))

        #invdb = sql.connect('C:\\Users\\erod4\\Documents\\GitHub\\IOTPantry_Capstone\\Main_Application\\IOTPantry\\inventory.db')
        c = invdb.cursor()
        c.execute("SELECT product_name FROM items")
        data = c.fetchall()
        length = len(data)
        prod_name = []
        for x in range(length):
            prod_name.append(data[x][0])

        prod_name = '\n'.join(str(line)for line in prod_name)
        print(prod_name)

        c.execute("SELECT num_items FROM items")
        data2 = c.fetchall()
        length2 = len(data2)
        quant = []
        for y in range(length2):
            quant.append(data2[y][0])


        quant = '\n'.join(str(line) for line in quant)


        c.execute("SELECT expiration_date FROM items")
        data3 = c.fetchall()
        length3 = len(data3)
        exp = []
        for z in range(length3):
            exp.append(data3[z][0])

        exp = '\n'.join(str(line) for line in exp)



        self.add_widget(Label(text=str(prod_name),
                              size_hint_x= None,
                              halign= 'left',
                              valign= 'middle',
                              pos_hint={'center_x': .25},
                              padding_x=20))

        self.add_widget(Label(text=str(quant),
                              pos_hint={'center_x': .55}))

        self.add_widget(Label(text=str(exp),
                              pos_hint={'center_x': .75}))

        self.add_widget(Label())
        self.add_widget(Label())

        self.Re_Button = Button(text="Return",
                                size_hint=(.25, .26),
                                text_size=self.size,
                                pos_hint={'center_x': .5, 'center_y': .1},
                                padding_x=20)
        self.Re_Button.bind(on_press=self.ReturnBack)
        self.add_widget(Label())
        self.add_widget(self.Re_Button)

    def ReturnBack(self, instance):
        info1 = "Loading Inventory"
        IOT_app.screen_manager.current = "HomePage"


#Shopping List Screen
class ShoppingListPage(GridLayout):

    cols= 3

    # Updates info on HomePage
    def update_info(self, message):
        self.message.text = message

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Label())

        self.add_widget(Label(text="Shopping List",
                              font_size='40sp',
                              size_hint=(1, .36),
                              bold=True))

        self.add_widget(Label())

        self.add_widget(Label(text="Item List Number",
                              size_hint=(1, 2),
                              pos_hint={'center_x': .25, 'center_y': .9},
                              bold=True))

        self.add_widget(Label(text="Product Name",
                              size_hint=(.25, .46),
                              pos_hint={'center_x': .55, 'center_y': .9},
                              bold=True))

        self.add_widget(Label(text="Notes",
                              size_hint=(.25, .46),
                              pos_hint={'center_x': .75, 'center_y': .9},
                              bold=True))

        #invdb = sql.connect('C:\\Users\\erod4\\Documents\\GitHub\\IOTPantry_Capstone\\Main_Application\\IOTPantry\\inventory.db')
        c = invdb.cursor()
        c.execute("SELECT list_id FROM shopping_list")
        data = c.fetchall()
        length = len(data)
        listnum = []
        for x in range(length):
            listnum.append(data[x][0])

        listnum = '\n'.join(str(line) for line in listnum)
        print(data)

        c.execute("SELECT product_name FROM shopping_list")
        data2 = c.fetchall()
        length = len(data2)
        prod_name = []
        for x in range(length):
            prod_name.append(data2[x][0])

        prod_name = '\n'.join(str(line) for line in prod_name)

        c.execute("SELECT notes FROM shopping_list")
        data3 = c.fetchall()
        length = len(data3)
        note = []
        for x in range(length):
            note.append(data3[x][0])

        note = '\n'.join(str(line) for line in note)

        self.add_widget(Label(text=str(listnum),
                              pos_hint={'center_x': .25}))

        self.add_widget(Label(text=str(prod_name),
                              pos_hint={'center_x': .55}))

        self.add_widget(Label(text=str(note),
                              pos_hint={'center_x': .75}))

        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.Re_Button = Button(text="Return",
                                size_hint=(.25, .26),
                                pos_hint={'center_x': .5, 'center_y': .1})
        self.Re_Button.bind(on_press=self.ReturnBack)
        self.add_widget(Label())
        self.add_widget(self.Re_Button)
        self.add_widget(Label())



    def ReturnBack(self, instance):
        info1 = "Loading Inventory"
        IOT_app.screen_manager.current = "HomePage"



#Recipe Screen
class RecipePage(BoxLayout):

    orientation = "vertical"

    # Updates info on HomePage
    def update_info(self, message):
        self.message.text = message

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Label())

        self.add_widget(Label(text="Recipes",
                              font_size='40sp',
                              size_hint=(1, .36),
                              bold=True))

        #invdb = sql.connect('C:\\Users\\erod4\\Documents\\GitHub\\IOTPantry_Capstone\\Main_Application\\IOTPantry\\inventory.db')
        c = invdb.cursor()
        c.execute("SELECT recipe_name FROM recipe;")
        data4 = c.fetchall()
        length = len(data4)
        reci = []
        for x in range(length):
            reci.append(data4[x][0])

        for x in range(length):
            self.recipe = Button(
                text=str(reci[x]),
                size_hint=(.25, .46),
                pos_hint={'right': .62})
            self.recipe.bind(on_press=self.steps_button)
            self.add_widget(Label())
            self.add_widget(self.recipe)
            self.add_widget(Label())

        self.add_widget(Label())

        self.Re_Button = Button(text="Return",
                                size_hint=(.25, .46),
                                pos_hint={'center_x': .5})
        self.Re_Button.bind(on_press=self.ReturnBack)
        self.add_widget(Label())
        self.add_widget(self.Re_Button)
        self.add_widget(Label())
        self.add_widget(Label())

    def steps_button(self, instance):
        IOT_app.screen_manager.current = "Steps"

    def ReturnBack(self, instance):
        info1 = "Loading Inventory"
        IOT_app.screen_manager.current = "HomePage"


class Steps(BoxLayout):
    orientation = "vertical"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Label())

        self.add_widget(Label(text="Recipes",
                            font_size='40sp',
                            size_hint=(1, .36),
                            bold=True))

        self.add_widget(Label())

        #invdb = sql.connect('C:\\Users\\erod4\\Documents\\GitHub\\IOTPantry_Capstone\\Main_Application\\IOTPantry\\inventory.db')
        c = invdb.cursor()
        c.execute("SELECT step FROM steps WHERE recipe_id = 1;")
        data5 = c.fetchall()
        length = len(data5)
        step = []
        for x in range(length):
            step.append(data5[x][0])

        step = '\n\n'.join(str(line) for line in step)

        self.steps = Label(text=str(step),
                           pos_hint={'center_x': .5})
        self.add_widget(self.steps)
        self.steps.bind(size=self.setting_function)

        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.Re_Button = Button(text="Return",
                                size_hint=(.25, .46),
                                pos_hint={'center_x': .5})
        self.Re_Button.bind(on_press=self.ReturnBack)

        self.add_widget(Label())
        self.add_widget(self.Re_Button)
        self.add_widget(Label())

    def ReturnBack(self, instance):
        info5 = "Loading Recipes"
        IOT_app.screen_manager.current = "Recipe Book"

    def setting_function(self, *args):
        self.steps.pos_hint = {'center_x': 0.5, 'center_y': .85}
        self.steps.text_size = self.size



#Main code
class PantryApp(App):
    def build(self):
        self.screen_manager = ScreenManager() #Screen Object Declaration

        self.LoginScreen = LoginScreen() #Define new screen object
        screen = Screen(name="LoginScreen") #Name Screen
        screen.add_widget(self.LoginScreen) #Add Screen
        self.screen_manager.add_widget(screen) #Allow for switching through screen manager class

        self.HomePage = HomePage() #Define new screen object
        screen1 = Screen(name="HomePage") #Name Screen
        screen1.add_widget(self.HomePage) #Add Screen
        self.screen_manager.add_widget(screen1) #Allow for switching through screen manager class

        self.InventoryPage = InventoryPage() #Define new screen object
        screen2 = Screen(name="Inventory") #Name Screen
        screen2.add_widget(self.InventoryPage) #Add Screen
        self.screen_manager.add_widget(screen2) #Allow for switching through screen manager class

        self.ShoppingListPage = ShoppingListPage() #Define new screen object
        screen3 = Screen(name="Shopping List") #Name Screen
        screen3.add_widget(self.ShoppingListPage) #Add Screen
        self.screen_manager.add_widget(screen3) #Allow for switching through screen manager class

        self.RecipePage = RecipePage() #Define new screen object
        screen4 = Screen(name="Recipe Book") #Name Screen
        screen4.add_widget(self.RecipePage) #Add Screen
        self.screen_manager.add_widget(screen4) #Allow for switching through screen manager class

        self.Error = Error()  # Define new screen object
        screen5 = Screen(name="Error")  # Name Screen
        screen5.add_widget(self.Error)  # Add Screen
        self.screen_manager.add_widget(screen5)  # Allow for switching through screen manager class

        self.steps = Steps()  # Define new screen object
        screen6 = Screen(name="Steps")  # Name Screen
        screen6.add_widget(self.steps)  # Add Screen
        self.screen_manager.add_widget(screen6)

        return self.screen_manager #Returns screens



if __name__ == "__main__":
    IOT_app = PantryApp()
    IOT_app.run() #Run application
