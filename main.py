from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton # adding button
from kivy.lang import Builder 
from kivymd.uix.dialog import MDDialog
from helpers import *
from kivy.core.window import Window
from kivy.uix.image import Image

# set window size
Window.size=(320,480)
dialog = None


class GLDNFApp(MDApp):

    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"

        self.image = Builder.load_string(image_helper)
        
        # adding button

        button = MDRectangleFlatButton(text='Login', pos_hint = {'center_x': 0.5, 'center_y': 0.2}, on_release=self.login)
        
        
        self.username = Builder.load_string(username_helper)
        self.password = Builder.load_string(password_helper)
        screen.add_widget(self.image)
        screen.add_widget(self.username)
        screen.add_widget(self.password)
        screen.add_widget(button)
        return screen



    # function of the button
    def login(self):
        # check entered username and password
        if self.root.ids.user.text=='admin' and self.root.ids.password.text=='admin123':
            if not self.dialog:
                # create dialog
                self.dialog = MDDialog(
                    title="Login",
                    text=f"Welcome {self.root.ids.user.text}!",
                    buttons=[
                        MDRectangleFlatButton(
                            text="Ok", text_color=self.theme_cls.primary_color,
                            on_release=self.close
                        ),
                    ],
                )
            # open and display dialog
            self.dialog.open()

    def close(self, instance):
        # close dialog
        self.dialog.dismiss()




if __name__ == "__main__":
    GLDNFApp().run()


        

