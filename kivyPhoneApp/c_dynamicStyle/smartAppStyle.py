import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
  
        
# name the file as the function name but remove App key word, also everything in file name is lowercases
class MyStyleApp(App):
    def build(self):
        return FloatLayout() #Label(text='Hello chenhao & Jason')
    
    

if __name__ == '__main__':
    MyStyleApp().run()
