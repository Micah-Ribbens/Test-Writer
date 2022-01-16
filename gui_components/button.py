from gui_components.clickable_component import ClickableComponent
from gui_components.text_box import TextBox
class Button(TextBox):
    action = None

    def __init__(self, text, font_size, text_color, background_color):
        # Only difference is that a Button's text can't be edited
        super().__init__(text, font_size, False, text_color, background_color)

    def add_click_action(self, function):
        self.action = function

    def run(self):
        ClickableComponent.run(self)

        if self.got_clicked() and self.action is not None:
            self.action()
