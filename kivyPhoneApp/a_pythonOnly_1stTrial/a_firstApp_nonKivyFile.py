import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

#       create a inner grid to seprate input sections and button  
        self.inside = GridLayout()
        self.inside.cols = 2
        
#       add label text 
        self.inside.add_widget(Label(text='First Name: '))
        
#        design a varible for save input text, then add the text input function to a widget box
        self.firstName = TextInput(multiline=False)
        self.inside.add_widget(self.firstName)
        
        self.inside.add_widget(Label(text='Last Name: '))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)
        
        self.inside.add_widget(Label(text='Email: '))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)
        
#        add the inside grid to main Widget (nested Widget)
        self.add_widget(self.inside)
        
#         add the button box to main Widget below the inner widget
        self.submit = Button(text='Submit', font_size=40)
#        add funcion to the button to interact after press
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
        
    def pressed(self, instance):
        firstName = self.firstName.text
        lastName = self.lastName.text
        email = self.email.text
        
        print('First Name: {}\n Last Name: {}\n Email: {} '.format(firstName,lastName,email))
#        print(type(instance))
        self.firstName.text = ""
        self.lastName.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyGrid() #Label(text='Hello chenhao & Jason')

if __name__ == '__main__':
    MyApp().run()
