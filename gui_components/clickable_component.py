from base.drawable_objects import GameObject
from base.events import Event
from base.utility_classes import HistoryKeeper
from base.utility_functions import percentage_to_number
from base.important_variables import *
import pygame


class ClickableComponent(GameObject):
    click_event = None
    amount_clicked = None

    def __init__(self):
        self.click_event = Event()
        self.amount_clicked = []

    # Things that inherit from it must call this method otherwise seeing if component got clicked won't work
    # Code won't see if this component got clicked in the past
    def run(self):
        mouse_clicked = pygame.mouse.get_pressed()[0]
        self.click_event.run(mouse_clicked)

    def got_clicked(self):
        is_clicked = True
        area = pygame.Rect(self.x_coordinate, self.y_coordinate, self.length,
                           self.height)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]
        # Otherwise if the mouse is held down this is going to be called over and over again
        if self.click_event.is_continuous(mouse_clicked):
            is_clicked = False

        if not area.collidepoint(mouse_x, mouse_y) or not mouse_clicked:
            is_clicked = False

        return is_clicked and self.is_visible


