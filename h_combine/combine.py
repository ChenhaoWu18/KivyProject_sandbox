#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:07:39 2019

@author: wuchenhao

to do
edge testing, .@ can be a email; have to have a . after @
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
import sys

class CreateAccountWindow(Screen):
    firstName = ObjectProperty(None) #the varible name need to be the same with the kivy label name. 
    lastName = ObjectProperty(None)
    email = ObjectProperty(None)
    
    def submit(self):
        if self.firstName.text !='' and self.email.text != '' and self.email.text.count('@') == 1 and self.email.text.count('.')>0 :
            if self.password != '':
                db.add_user(self.email.text, self.password.text, self.firstName.text)
                
                self.reset()
                
                wM.current = 'login'
            
            else: 
                invalidForm()
        
        else:
            invalidForm()
        
    def login(self):
        self.reset()
        wM.current = 'login'
        
    def reset(self):
        self.password.text = ''
        self.firstName.text = ''
        self.email.text = ''
        
class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            wM.current = 'main'
        else:
            invalidLogin()
            
    def createBtn(self):
        self.reset()
        wM.current = 'create'
    
    def reset(self):
        self.email.text = ''
        self.password.text = ''

class MainWindow(Screen):
    n = ObjectProperty(None)
    createdDate = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ''
    
    def logOut(self):
        wM.current = 'login'
        
    def on_enter(self, *args):
        password, firstName, createdDate = db.get_user(self.current)
        self.n.text = 'Account Name: ' + firstName
        self.email.text = 'Email: ' + self.current
        self.createdDate.text = 'created On: ' + createdDate
        
class WindowManager(ScreenManager):
    pass

def invalidLogin():
    pop = Popup(title = 'Invalid Login',
                content = Label(text='Invalid email or password'),
                size_hint = (None, None), size = (400, 400))
    pop.open()
    
def invalidForm():
    pop = Popup(title = 'Invalid Form',
                content = Label(text='Please fill in all input\nwith valid information.'),
                size_hint = (None, None), size = (400, 400))
    pop.open()

kv = Builder.load_file('my.kv')

wM = WindowManager()
db = DataBase('users.txt')

screens = [LoginWindow(name='login'),
           CreateAccountWindow(name='create'),
           MainWindow(name='main')]
for screen in screens:
    wM.add_widget(screen)
    
wM.current = 'login'
    
class MyMainApp(App):
    def build(self):
        return wM

if __name__ == '__main__':
    MyMainApp().run()
