from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty


class my_layout(FloatLayout):
    screen_mngr = ObjectProperty(None)


class myapp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("View/MainScreen/Screen.kv")

    def logger(self):
        if self.root.ids.user.text == 'admin' and self.root.ids.password.text=='admin':
            self.root.ids.welcome_label.text = f'Sup {self.root.ids.user.text}!'
            screen = Screen(name='screen2')
        else:
            self.root.ids.welcome_label.text = 'Wrong credentials'

if __name__ == "__main__":
    myapp().run()
