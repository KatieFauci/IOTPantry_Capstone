from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
#from kivy.config import Config
#from kivy.uix.anchorlayout import AnchorLayout
#from kivy.uix.floatlayout import FloatLayout
#from kivy.lang import Builder
#from datetime import date
#from kivy.properties import ObjectProperty, NumericProperty
#from kivy.properties import StringProperty

import sqlite3 as sql

import os
import threading

#Login Screen to access personal database
class LoginScreen(BoxLayout):

    orientation = "vertical"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Screen background color
        Window.clearcolor = (0.70, 0.70, 0.70, 1)

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

        if username == "Test":
            if password == "test":
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
class InventoryPage(GridLayout):
    # Updates info on HomePage

    cols = 3

    def update_info(self, message):
        self.message.text = message

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Label(text="Name"))
        self.add_widget(Label(text="Quantity"))
        self.add_widget(Label(text="Expiration"))

        invdb = sql.connect('C:\\Users\\erod4\\Documents\\GitHub\\IOTPantry_Capstone\\Databases\\inventory.db')
        c = invdb.cursor()
        c.execute("SELECT product_name FROM items;")
        data = c.fetchall()
        c.execute("SELECT num_items FROM items;")
        data1 = c.fetchall()
        c.execute("SELECT expiration_date FROM items;")
        data2 = c.fetchall()

        self.add_widget(Label(text=str(data),
                              size_hint=(1, .36)))

        self.add_widget((Label(text=str(data1),
                               size_hint=(1, .36))))


        self.add_widget(Label(text=str(data2),
                              size_hint=(1, .36)))

        self.Re_Button = Button(text="Return",
                                size_hint=(.25, .46),
                                pos_hint={'right': .62})
        self.Re_Button.bind(on_press=self.ReturnBack)
        self.add_widget(Label())
        self.add_widget(self.Re_Button)
        self.add_widget(Label())




    def ReturnBack(self, instance):
        info1 = "Loading Inventory"
        IOT_app.screen_manager.current = "HomePage"


#Shopping List Screen
class ShoppingListPage(GridLayout):

    cols= 1

    # Updates info on HomePage
    def update_info(self, message):
        self.message.text = message

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        invdbshop = sql.connect('C:\\Users\\erod4\\Documents\\GitHub\\IOTPantry_Capstone\\Databases\\inventory.db')
        c = invdbshop.cursor()
        c.execute("SELECT * FROM shopping_list;")
        data = c.fetchall()

        self.add_widget(Label(text=str(data),
                              size_hint=(1, .36)))

        self.Re_Button = Button(text="Return",
                                size_hint=(.25, .46),
                                pos_hint={'right': .62})
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

        invdbrec = sql.connect('C:\\Users\\erod4\\Documents\\GitHub\\IOTPantry_Capstone\\Databases\\inventory.db')
        c = invdbrec.cursor()
        c.execute("SELECT * FROM recipe;")
        data = c.fetchall()

        self.add_widget(Label(text=str(data)))

        self.add_widget(Label())

        self.Re_Button = Button(text="Return",
                                size_hint=(.25, .46),
                                pos_hint={'right': .42})
        self.Re_Button.bind(on_press=self.ReturnBack)
        self.add_widget(Label())
        self.add_widget(self.Re_Button)
        self.add_widget(Label())



    def ReturnBack(self, instance):
        info1 = "Loading Inventory"
        IOT_app.screen_manager.current = "HomePage"



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

        return self.screen_manager #Returns screens



if __name__ == "__main__":
    IOT_app = PantryApp()
    IOT_app.run() #Run application