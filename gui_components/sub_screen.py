from base.utility_functions import percentage_to_number
from base.important_variables import *
from gui_components.screen import Screen


class SubScreen(Screen):
    components = []

    def run(self):
        pass

    def __init__(self, length_used_up, height_used_up):
        pass

    def set_item_bounds(self, item, length_used_up, height_used_up, percent_right, percent_down, percent_length, percent_height):
        x_coordinate = percentage_to_number(percent_right, screen_length)
        y_coordinate = percentage_to_number(percent_down, screen_height)
        length = percentage_to_number(percent_length, screen_length)
        height = percentage_to_number(percent_height, screen_height)

        # Changes values to max_value to still be within bounds
        if x_coordinate < length_used_up:
            x_coordinate = length_used_up

        if y_coordinate < height_used_up:
            y_coordinate = height_used_up

        item.number_set_bounds(x_coordinate, y_coordinate, length, height)
