from base.important_variables import game_window, screen_length, screen_height, background_color


def change_attributes(modified_object, object):
    """ summary: modifies modified_object's attributes so they reflect the object's attributes
        (only the attributes in modified_object.attributes will be modified)

        params:
            modified_object: Object; the object which will have its properties modified
            object: Object; the object which the modified_object's attributes will reflect

        returns: None
    """
    for key in modified_object.attributes:
        modified_object.__dict__[key] = object.__dict__[key]

    return modified_object


def percentage_to_number(percentage, percentage_of_number):
    """ summary: turns the percentage into a fraction which is multiplied by percentage_of_number

        params:
            percentage: int; the percentage (fraction * 100)
            percentage_of_number: int; the number that the percentage is of

        returns: int; the number that is gotten from the percentage (as a fraction) multiplied by percentage_of_number
    """
    return (percentage / 100) * percentage_of_number


def validate_kwargs_has_all_fields(kwargs_fields, kwargs):
    """ summary: raises an error if a kwarg field was not provided

        params:
            kwargs_fields: dictionary; the needed kwargs fields
            kwargs: dictionary: the provided kwargs fields

        returns: None
    """
    for field in kwargs_fields:
        if not kwargs.__contains__(field):
            raise ValueError(f"Field {field} was not provided for kwargs")


def render_words(message, font, **kwargs):
    """ summary: draws words onto the screen; either x_coordinate, y_coordinate, and text_is_center
        must be provided or is_center_of_screen

        params:
            x_coordinate: int; the x_coordinate of the text
            y_coordinate: int; the y_coordinate of the text
            text_is_centered: boolean; the x and y coordinates are the center of the text (if True) otherwise start of text
            is_center_of_screen: boolean; the text is in the center of the screen
            text_color (optional): tuple; the (Red, Green, Blue) values of text color; is (255, 255, 255) if not specified
            text_background (optional) tuple; the (Red, Green, Blue) values of the background of the text; is background_color if not specified

        returns: None
    """

    # Getting all the variables
    text_color = (255, 255, 255) if not kwargs.get("text_color") else kwargs.get("text_color")
    text_background = background_color if not kwargs.get("text_background") else kwargs.get("text_background")
    is_center_of_screen = False if not kwargs.get("is_center_of_screen") else kwargs.get("is_center_of_screen")
    is_center = False if not kwargs.get("is_center") else kwargs.get("is_center")
    text = font.render(message, True, text_color, text_background)
    text_rect = text.get_rect()

    if is_center_of_screen:
        text_rect.center = (screen_length / 2, screen_height / 2)

    else:
        validate_kwargs_has_all_fields(["x_coordinate", "y_coordinate"], kwargs)
        text_rect.left = kwargs.get("x_coordinate")
        text_rect.top = kwargs.get("y_coordinate")

    if is_center:
        text_rect.center = (kwargs.get("x_coordinate"), kwargs.get("y_coordinate"))

    game_window.get_window().blit(text, text_rect)


# length is what percent_right and percent_length are a percent of and height is what percent_down and percent_height are a percent of
def percentages_to_numbers(percent_right, percent_down, percent_length, percent_height, length, height):
    """ summary: turns the percentages into numbers

        params:
            percent_right: int; the percent it is to right (percentage of length)
            percent_down: int; the percent it is down (percentage of height)
            percent_length: int; the length (percentage of length)
            percent_height: int; the height (percentage of height)
            length: int; the number that percent_right and percent_length are based off of
            height: int; the number that percent_down

        returns: None
    """
    return [
        percentage_to_number(percent_right, length),
        percentage_to_number(percent_down, height),
        percentage_to_number(percent_length, length),
        percentage_to_number(percent_height, height)
    ]


def lists_share_an_item(list1, list2):
    """ summary: iterates over list1 to see if list2 contains one of those item

        params:
            list1: list; the first list (is iterated over)
            list2: list; the second list (used to check if it shares an item with list1)

        returns: boolean; if list1 and list2 share an item
    """
    is_true = False
    for item in list1:
        if list2.__contains__(item):
            is_true = True

    return is_true

def remove_last_ch(string):
    """ summary: removes the last character from a string

        params:
            string: String; the string which will have its last character removed

        returns: String; the string without the last character
    """
    return string[0:len(string) - 1]
