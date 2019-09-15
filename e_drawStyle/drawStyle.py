import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
#from kivy.graphics import Line

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(0, 1, 0, 0.5, mode='rgba')  #line color
#            Line(points = (20, 30, 200, 400, 600))
            
            Color(1, 1, 0, 0.5, mode='rgba') #change the color of whole rectangle
            self.rect = Rectangle(pos=(0,0), size=(30,30)) # init start position, 
            
#            Color(1, 1, 0, 0.5, mode='rgba') 
#            self.rect = Rectangle(pos=(200,300), size=(100,50)) # fixed statis position, those are not dynamic position using roots
    
    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        print('Mouse Down', touch)
#        self.btn.opacity = 0.5 #background colour change when click range 0 to 1, 0 dark1 light
    
    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print('Mouse Move', touch)
    
#    def on_touch_up(self, touch):
#        print('Mouse Up', touch)
#        self.btn.opacity = 1 #background colour change when left click
        
# name the file as the function name but remove App key word, also everything in file name is lowercases
class MyStyleApp(App):
    def build(self):
        return Touch() #Label(text='Hello chenhao & Jason')
    
    

if __name__ == '__main__':
    MyStyleApp().run()
