from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.storage.jsonstore import JsonStore
import os.path
import sys
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.image import Image

class FullImage(Image):
    pass

class CusWid(Widget):
    init = True
    def slide(self, *args):
        if self.ids.img.pos[0] > self.width:
            self.ids.img.pos[0] = self.ids.img2.pos[0] - self.ids.img2.width
           
        self.ids.img.pos[0] = self.ids.img.pos[0]+2
        
        if self.init:
            self.ids.img2.pos[0] = self.ids.img2.width*(-1)
            self.init = False
        if self.ids.img2.pos[0] > self.width:
            self.ids.img2.pos[0] = self.ids.img.pos[0] - self.ids.img.width
        else:
            self.ids.img2.pos[0] = self.ids.img2.pos[0]+2
    def startanim(self, *args):
        Clock.schedule_interval(self.slide, 1.0/60)

class TempApp(App):
    def on_pause(self, *args):
        return True
    def build(self, *args):
        cuswid = CusWid()
        cuswid.startanim()
        return cuswid

if __name__ == '__main__':
    app = TempApp()
    app.run()
