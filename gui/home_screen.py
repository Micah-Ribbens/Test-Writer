from base.important_variables import *
from base.colors import *
from gui_components.button import Button
from gui_components.screen import Screen
from gui_components.text_box import TextBox


class HomeScreen(Screen):
    """The main screen of the application where setting up the testing occurs"""
    file_location_field = TextBox("File location", 15, True, green, red)
    submit_button = Button("Submit", 14, white, green)
    components = [file_location_field, submit_button]


    def __init__(self):
        """ summary: initializes all the fields of the Home Screen
            params: None
            returns: None
        """
        self.file_location_field.percentage_set_bounds(20, 20, 50, 15)
        self.submit_button.percentage_set_bounds(0, 0, 100, 15)

    def un_setup(self):
        """ summary: makes the HomeScreen disappear
            params: None
            returns: None
        """
        game_window.set_screen_visible(self, False)

    def run(self):
        pass

