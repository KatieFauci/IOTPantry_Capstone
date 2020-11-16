import kivy


from kivy.app import App
from kivy.uix.button import Button

class Myapp(App):
    def build(self):
        return Button(text = 'Hello kivy')


if __name__ == '__main__':
    Myapp().run()
