import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
import os
import sys
kivy.require('1.10.1')

class ScrollabelLabel(ScrollView):
    
    def update_chat_history(self,message):
        self.chat_history.text += '\n' + message
#        self.layout.height = self.chat_history.texture_size[1]+15 # for extra picell
        
#        
        
    

class connectPage(GridLayout):
#    in kivy file, firstName(link with python):firstName(kivy ID)
    
    firstName = ObjectProperty(None) #the varible name need to be the same with the kivy label name. 
    lastName = ObjectProperty(None)
    email = ObjectProperty(None)
    
    btn = ObjectProperty(None)
    
        
    with open('prev_details.txt','r') as f:
        d = f.read().split(';')
        firstName = d[0]
        lastName = d[1]
        email = d[2]

    
    def pressed(self): # no instance arg this time
        #those name, email varibles already setup inside the mygraid class and kivy file
#        print('First Name: {}\n Last Name: {}\n Email: {} '.format(self.firstName.text, self.lastName.text, self.email.text))
        first_name = self.firstName.text #the varible name need to be the same with the kivy label name. 
        last_name = self.lastName.text
        email_text = self.email.text
        print(f'First Name: {first_name}\n Last Name: {last_name}\n Email: {email_text} ')

        with open('prev_details.txt','w') as f:
            f. write (f'{first_name};{last_name};{email_text}\n')
        
        info = f'{first_name};{last_name};{email_text}'
        chat_app.info_page.update_info(info)
        chat_app.screen_manager.current = 'Info'
        
        Clock.schedule_once(self.connect,1)
        
    
    def connect(self, _):
        first_name = self.firstName.text #the varible name need to be the same with the kivy label name. 
        last_name = self.lastName.text
        email_text = self.email.text
        
        chat_app.create_chat_page()
        chat_app.screen_manager.current = 'Chat'
    
class infoPage(GridLayout):
    message = ObjectProperty(None) #the varible name need to be the same with the kivy label name. 
        
    def update_info(self, message):
        self.message.text = message


class ChatPage(GridLayout):   
    def __init__(self, **warg):
        Clock.schedule_once(self.connect,1)

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40:
            self.send_message(None)
    def send_message(self, _):
        message = self.new_message.text
        self.new_message.text = ''
        
    
# name the file as the function name but remove App key word, also everything in file name is lowercases
class chatBoxApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        
        self.connect_page = connectPage()
        screen = Screen(name='Connect')
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)
        
        self.info_page = infoPage()
        screen = Screen(name='Info')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager
    
    def create_chat_page(self):
        self.chat_page = ChatPage()
        screen = Screen(name='Chat')
        screen.add_widget(self.chat_page)
        self.screen_manager.add_widget(screen)
        
def show_error(message):
    chat_app.info_page.update_info(message)
    chat_app.screen_manager.current = 'Info'
    Clock.schedule_one(sys.exit, 10)

if __name__ == '__main__':
    chat_app = chatBoxApp()
    chat_app.run()
