from base.utility_functions import percentage_to_number, percentages_to_numbers
from base.important_variables import *
from gui_components.screen import Screen


class SubScreen(Screen):
    """A part of a screen"""

    components = []
    dimensions = None

    def run(self):
        pass

    def __init__(self, dimensions):
        """ summary: initializes the object

            params:
                length_used_up: int; the length that the main screen, the screen that the sub screen is a part of, uses up
                height_used_up: int; the height that the main screen, the screen that the sub screen is a part of, uses up

            returns: None
        """
        self.dimensions = dimensions
