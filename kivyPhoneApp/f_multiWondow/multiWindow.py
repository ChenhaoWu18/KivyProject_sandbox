#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.lang import Builder #no matter what is the name of .kv file it will find it
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen):
    pass

class SecionWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('my.kv')

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    MyMainApp().run()
