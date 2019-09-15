#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup




class Widgets(Widget):
    def button(self):
        show_popup()

class PopWindow(FloatLayout):
    pass


def show_popup():
    show = PopWindow()
    
    popup_window = Popup(title='I\'m the Popup Window, Hi!', content=show, size_hint=(None,None),size=(400,400))
    popup_window.open() 
    
    
class MyApp(App):
    def build(self):
        return Widgets()

if __name__ == '__main__':
    MyApp().run()
