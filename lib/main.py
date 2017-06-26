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
from functools import partial

class FullImage(Image):
    pass
class TempBackground(Image):
    pass

class CusWid(Widget):
    init = True
    fps = 3.0/60.0
    def slide(self, *args):
        print('img pos: ',self.ids.img.pos,' size: ',self.ids.img.size)
        print('img2 pos: ',self.ids.img2.pos,' size: ',self.ids.img2.size)
        if self.ids.img.pos[0] > self.width:
            self.ids.img.pos[0] = self.ids.img2.pos[0] - self.ids.img2.width
        
        self.ids.img.pos[0] = self.ids.img.pos[0]+1
        
        if self.init:
            print('img pos: ',self.ids.img.pos,' size: ',self.ids.img.size)
            print('img2 pos: ',self.ids.img2.pos,' size: ',self.ids.img2.size)
            self.ids.img2.pos[0] = self.ids.img2.pos[0] - self.ids.img2.size[0]
            self.init = False
        if self.ids.img2.pos[0] > self.width:
            self.ids.img2.pos[0] = self.ids.img.pos[0] - self.ids.img.width
        else:
            self.ids.img2.pos[0] = self.ids.img2.pos[0]+1
    def startanim(self, *args):
        Clock.schedule_interval(self.slide, self.fps)

    def getTail(self, *args):
        if self.ids.img.pos[0] > self.ids.img2.pos[0]:
            return self.ids.img2
        else:
            return self.ids.img

    def getNextAvail(self, *args):
        img = self.ids.img.pos[0]
        img2 = self.ids.img2.pos[0]
        tmp1 = self.ids.tmp1.pos[0]
        if img<=0 and img>self.ids.img.width*(-1):
            return self.ids.img
        elif img2<= 0 and img2>self.ids.img2.width*(-1):
            return self.ids.img2
        else:
            return self.ids.tmp1
    
    def slideTmpBkgrd(self, *args):
        if self.ids.tmp1.pos[0] == 0:
            self.ids.img.source = self.ids.tmp1.source
            self.ids.img2.source = self.ids.tmp1.source
        self.ids.tmp1.pos[0] = self.ids.tmp1.pos[0]+1
        if self.ids.tmp1.pos[0] > self.width:
            return False
        else:
            return True
        
    def slideTmpBkgrdLoop(self, *args):
        pass
    
    def buttonPress(self, *args):
        if self.ids.tmp1.pos[0] >= self.width:
            self.ids.tmp1.pos[0] = self.getNextAvail().pos[0] - self.getNextAvail().width
            Clock.schedule_interval(self.slideTmpBkgrd, self.fps)
            print('temp now coming')
        else:
            print('button doing nothing')
        
    
    
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
