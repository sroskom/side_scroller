from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from lib import CusWid
from kivy.core.audio import SoundLoader
from os.path import join
import sys

class Manager(ScreenManager):
    
    def __init__(self, *args):
        super(Manager,self).__init__()
        self.ids.cuswid.startanim()
        self.startCampMusic()
        
    def startScrollerMusic(self, *args):
        try:
            self.scrolrSound = SoundLoader.load(join(App.get_running_app().user_data_dir,'background_song_01.mp3'))
            if self.scrolrSound:
                self.scrolrSound.loop = True
                self.scrolrSound.play()
        except:
            pass
        
    def startCampMusic(self, *args):
        try:
            self.campSound = SoundLoader.load(join(App.get_running_app().user_data_dir,'camp_song.mp3'))
            if self.campSound:
                self.campSound.loop = True
                self.campSound.play()
        except:
            pass
        
    def stopCampMusic(self, *args):
        try:
            if self.campSound and self.campSound.state != 'stop':
                print(self.campSound.state)
                self.campSound.stop()
                self.campSound.unload()
        except:
            pass

    def stopScrollerMusic(self, *args):
        try:
            if self.scrolrSound and self.scrolrSound.state != 'stop':
                self.scrolrSound.stop()
                self.scrolrSound.unload()
        except:
            pass
class TempApp(App):
    def on_pause(self, *args):
        return True
    def build(self, *args):
        manager = Manager()
        return manager

if __name__ == '__main__':
    try:
        app = TempApp()
        app.run()
    except:
        e = sys.exc_info()
        f = open('/sdcard/temp/exceptions.txt', 'w')
        f.write(str(e))
        f.close()
