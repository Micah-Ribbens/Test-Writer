from base.colors import white, green
from base.drawable_objects import Dimensions
from base.important_variables import screen_length, screen_height, game_window
from gui.function_testing_screen import FunctionTestingScreen
from gui_components.button import Button
from gui_components.grid import Grid
from gui_components.screen import Screen
from base.utility_functions import percentages_to_numbers
from gui_components.text_box_with_title import TextBoxWithTitle
class AllFunctionsScreen(Screen):
    """The screen that shows all the functions that are in the file"""
    functions = []
    buttons = []
    function_screens = []
    function_names = []
    inputs = []
    outputs = []

    def run(self):
        for button in self.buttons:
            if button.got_clicked():
                self.display_screen(button.text, self.function_screens)

    def __init__(self, functions):
        """ summary: initializes the object

            params:
                functions: List of Function; the functions that are going to be tested

            returns: None

        """
        self.functions = functions
        buttons = []
        function_screens = []

        for function in self.functions:
            function_screen = FunctionTestingScreen(function)
            function_screens.append(function_screen)
            game_window.add_screen(function_screen)

        for x in range(len(function_screens)):
            name = functions[x].name
            function_button = Button(name, 14, white, green)
            self.components.append(function_button)
            self.function_names.append(name)
            buttons.append(function_button)

            # TODO why doesn't this work?
            # function_button.add_click_action(lambda: (game_window.display_screens([function_screens[x]]),
            #                                           print(x)))

        grid = Grid(Dimensions(0, 0, screen_length, screen_height), 4, None, True)
        grid.turn_into_grid(buttons, None, None)
        game_window.display_screens([self])
        self.buttons = buttons
        self.function_screens = function_screens

    def display_screen(self, function, function_screens):
        """ summary: displays the screen that is tied to that function name onto the screen (calls game_window.display_screens)

            params:
                button_name: String; the name of the button was clicked that will change the screen

            returns: None
        """
        index = self.function_names.index(function)
        game_window.display_screens([function_screens[index]])




