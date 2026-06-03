from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import requests
from serpapi import GoogleSearch
from urllib.request import urlretrieve

Builder.load_file('frontend.kv')

class FirstScreen(Screen):

    def get_img_link(self):
        # get user query from text
        query = self.manager.current_screen.ids.user_query.text

        # get serp gogle images
        params = {
            "engine": "google_images",
            "q": query,
            "api_key": "bf26c7972491579a88e7e16b2f0be4d5f2bfb3ed2bf98f684c8071d4341aa536"
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        image_url = results["images_results"][0]["original"]
        return image_url


    def download_image(self):

        # download image in local directory
        response = requests.get(self.get_img_link())

        imagepath = "image.jpg"
        with open(imagepath, "wb") as f:
            f.write(response.content)
        return imagepath

    def set_image(self):
        # set image in the Image widget
        self.manager.current_screen.ids.img.source = self.download_image()
        self.ids.img.reload()

class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()