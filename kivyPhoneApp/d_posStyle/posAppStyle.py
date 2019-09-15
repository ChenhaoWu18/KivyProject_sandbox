import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Touch(Widget):
    btn = ObjectProperty(None)
    def on_touch_down(self, touch):
        print('Mouse Down', touch)
        self.btn.opacity = 0.5 #background colour change when click range 0 to 1, 0 dark1 light
    
    def on_touch_move(self, touch):
        print('Mouse Move', touch)
    
    def on_touch_up(self, touch):
        print('Mouse Up', touch)
        self.btn.opacity = 1 #background colour change when left click
        
# name the file as the function name but remove App key word, also everything in file name is lowercases
class MyStyleApp(App):
    def build(self):
        return Touch() #Label(text='Hello chenhao & Jason')
    
    

if __name__ == '__main__':
    MyStyleApp().run()
