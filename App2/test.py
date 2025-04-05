import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Layout1(BoxLayout):
    pass

class Test(App):
    def build(self):
        return Layout1()
Test().run()