import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

class MyGrid(Widget):
#    in kivy file, firstName(link with python):firstName(kivy ID)
    firstName = ObjectProperty(None) #the varible name need to be the same with the kivy label name. 
    lastName = ObjectProperty(None)
    email = ObjectProperty(None)
    
    btn = ObjectProperty(None)
    
    def pressed(self): # no instance arg this time
        #those name, email varibles already setup inside the mygraid class and kivy file
#        print('First Name: {}\n Last Name: {}\n Email: {} '.format(self.firstName.text, self.lastName.text, self.email.text))
        first_name = self.firstName.text #the varible name need to be the same with the kivy label name. 
        last_name = self.lastName.text
        email_text = self.email.text
        print(f'First Name: {first_name}\n Last Name: {last_name}\n Email: {email_text} ')
        with open('prev_details.txt','w') as f:
            f. write (f'{first_name};{last_name};{email_text}')

        self.firstName.text = ""
        self.lastName.text = ""
        self.email.text = ""
    
# name the file as the function name but remove App key word, also everything in file name is lowercases
class MyStyleApp(App):
    def build(self):
        return MyGrid() #Label(text='Hello chenhao & Jason')

if __name__ == '__main__':
    MyStyleApp().run()
