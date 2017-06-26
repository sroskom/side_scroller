from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from lib.main import CusWid
from kivy.core.audio import SoundLoader
from os.path import join

class Manager(ScreenManager):
    
    def __init__(self, *args):
        super(Manager,self).__init__()
        self.ids.cuswid.startanim()
        self.startCampMusic()
        
    def startScrollerMusic(self, *args):
        self.scrolrSound = SoundLoader.load(join(App.get_running_app().user_data_dir,'background_song_01.mp3'))
        if self.scrolrSound:
            self.scrolrSound.loop = True
            self.scrolrSound.play()
            
    def startCampMusic(self, *args):
        self.campSound = SoundLoader.load(join(App.get_running_app().user_data_dir,'camp_song.mp3'))
        if self.campSound:
            self.campSound.loop = True
            self.campSound.play()

    def stopCampMusic(self, *args):
        if self.campSound and self.campSound.state != 'stop':
            print(self.campSound.state)
            self.campSound.stop()
            self.campSound.unload()

    def stopScrollerMusic(self, *args):
        if self.scrolrSound and self.scrolrSound.state != 'stop':
            self.scrolrSound.stop()
            self.scrolrSound.unload()
        
class TempApp(App):
    def on_pause(self, *args):
        return True
    def build(self, *args):
        manager = Manager()
        return manager

if __name__ == '__main__':
    app = TempApp()
    app.run()
    
