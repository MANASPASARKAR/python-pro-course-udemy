from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
from filesharer import FileSharer
import time
import webbrowser

Builder.load_file('frontend.kv')

class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.start_stop_cam.text = "Stop Camera"
        self.ids.camera.opacity = 1

    def stop(self):
        self.ids.camera.play = False
        self.ids.start_stop_cam.text = "Start Camera"
        self.ids.camera.texture = None
        self.ids.camera.opacity = 1

    def capture(self):
        current_time = time.strftime('%d%m%Y-%H%M%S')
        self.filepath = f"files/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.captured_image.source = self.filepath

class ImageScreen(Screen):
    link_message = "Create a link first"
    def create_link(self):
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        filesharer = FileSharer(filepath=file_path)
        self.url = filesharer.share()
        self.ids.link.text = self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()