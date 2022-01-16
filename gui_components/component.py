from abc import ABC, abstractmethod

from base.important_variables import screen_length, screen_height
from base.utility_functions import percentage_to_number


class Component(ABC):
    is_visible = True
    is_runnable = True
    is_selected = False

    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def render(self):
        pass

    def percentage_set_bounds(self, percent_right, percent_down, percent_length, percent_height):
        self.x_coordinate = percentage_to_number(percent_right, screen_length)
        self.y_coordinate = percentage_to_number(percent_down, screen_height)
        self.length = percentage_to_number(percent_length, screen_length)
        self.height = percentage_to_number(percent_height, screen_height)

    def number_set_bounds(self, x, y, length, height):
        self.x_coordinate, self.y_coordinate = x, y
        self.length, self.height = length, height

    def set_dimensions(self, dimensions):
        """ summary: sets the object's dimensions to the dimension's of the parameter dimensions

            params:
                dimensions: Dimension; the dimensions that this object should be

            returns: None
        """
        self.x_coordinate = dimensions.x_coordinate
        self.y_coordinate = dimensions.y_coordinate
        self.length = dimensions.length
        self.height = dimensions.height
