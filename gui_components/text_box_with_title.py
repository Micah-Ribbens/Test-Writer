from base.colors import white
from base.drawable_objects import GameObject
from base.important_variables import background_color, screen_length
from base.function import Parameter
from gui_components.clickable_component import ClickableComponent
from gui_components.component import Component
from gui_components.text_box import TextBox

class TextBoxWithTitle(ClickableComponent):
    """A textbox that has a title before the input portion"""
    title_portion = None
    input_portion = None

    def __init__(self, font_size, default_text, title, text_color, text_background_color):
        """ summary: initializes the object

            parameters:
                font_size: int; the font size of the text that will be displayed on the screen
                default_text: String; the default text for the input field
                title: String; the title that is displayed before the input field
                text_color: tuple; the (Red, Green, Blue) values of the text's color
                text_background_color: tuple: the (Red, Green, Blue) values of the text's background color

            returns: None
        """

        self.title_portion = TextBox(title, font_size, False, text_color, text_background_color)
        self.input_portion = TextBox(default_text, font_size, True, text_color, text_background_color)
        super().__init__()

    def number_set_bounds(self, x, y, length, height):
        title_portion_length = self.get_title_portion_length()
        buffer = screen_length * .01
        input_portion_length = length - title_portion_length - buffer

        self.title_portion.number_set_bounds(x, y, title_portion_length, height)
        self.input_portion.number_set_bounds(x + title_portion_length + buffer, y, input_portion_length, height)
        # Can't use self.number_set_bounds() because that ends in infinite recursion
        Component.number_set_bounds(self, x, y, length, height)

    def get_title_portion_length(self):
        """ summary: uses get_rect() to figure out the title portion's length (length is get_rect().length)
            params: None
            returns: int; the percentage length that the title portion takes up in relation to the screen's length
        """
        title_text = self.title_portion.font.render(self.title_portion.text, True, background_color, background_color)
        title = title_text.get_rect()

        return title.width * 1.2

    def run(self):
        self.title_portion.run()
        self.input_portion.run()

        # All the subcomponents should be the same selection state as the entire component
        self.input_portion.is_selected = self.is_selected
        self.title_portion.is_selected = self.is_selected
        ClickableComponent.run(self)

    def render(self):
        self.title_portion.render()
        self.input_portion.render()