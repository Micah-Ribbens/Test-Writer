from base.dimensions import Dimensions
from base.important_variables import screen_length, screen_height
from base.utility_functions import percentages_to_numbers
from base.function import Function, TestCase
from gui_components.button import Button
from gui_components.grid import Grid
from gui_components.text_box_with_title import TextBoxWithTitle
from gui_components.screen import Screen
from gui_components.text_box import TextBox
from base.colors import *


class FunctionField:
    """Stores all the components for each function field in FunctionTestingScreen"""
    components = []
    inputs = []
    output = None

    def __init__(self):
        """ summary: initializes the component
            params: None
            returns: None
        """
        # Have to reset this so it doesn't grow based off of other FunctionField objects
        self.components = []
        self.inputs = []
        self.outputs = []

    def add_component(self, component, is_input):
        """ summary: adds the component to FunctionField.components

            params:
                component: Component; the component which is going to be added to FunctionField.components
                is_input: boolean; the component is the input to a function

            returns: None
        """
        self.components.append(component)

        if is_input:
            self.inputs.append(component.input_portion)

        else:
            self.output = component.input_portion

    def add_components(self, components):
        """ summary: for each component in components it appends the component to components

            params:
                components: List of Component: the components which are going to be added to FunctionField.components

            returns: None
        """
        for component in components:
            self.components.append(component)


class FunctionTestingScreen(Screen):
    """Screen where the input(s) and output(s) are shown for testing"""
    function = None
    function_fields = []

    def __init__(self, function: Function):
        """ summary: initializes the object

            params:
                function; the function that is going to be displayed on the screen

            returns: None
        """
        self.function = function
        self.function_fields = []

        for x in range(1):
            self.add_function_field()

    def get_components(self):
        """ summary: gets all the screens components
            params: None
            returns: all the screens components
        """

        components = []
        for field in self.function_fields:
            for component in field.components:
                components.append(component)

        return components

    def delete_function_field(self):
        """ summary: deletes the last item in function_fields
            params: None
            returns: None
        """
        del self.function_fields[len(self.function_fields) - 1]
        self.function.number_of_outputs -= 1

    def add_function_field(self):
        """ summary: adds a function field

            params:
                number_of_function_fields: int; the number of function fields that are currently on the screen

            returns: None
        """

        parameter_field_height = 20

        parameter_fields = []
        function_field = FunctionField()
        number_of_function_fields = len(self.function_fields)
        for parameter in self.function.parameters:
            parameter_field = TextBoxWithTitle(18, parameter.name, parameter.type, parameter.color, white)
            parameter_fields.append(parameter_field)
            function_field.add_component(parameter_field, True)

        output_field = TextBoxWithTitle(18, "Expected Output", self.function.output_type, black, white)
        add_button = Button("+", 18, white, green)
        minus_button = Button("-", 18, white, red)
        add_button.percentage_set_dimensions(90, parameter_field_height * number_of_function_fields, 5, parameter_field_height)
        minus_button.percentage_set_dimensions(95, parameter_field_height * number_of_function_fields, 5, parameter_field_height)

        add_button.add_click_action(self.add_function_field)
        minus_button.add_click_action(self.delete_function_field)

        function_field.add_components([add_button, minus_button])
        function_field.add_component(output_field, False)

        x, y, length, height = percentages_to_numbers(0, parameter_field_height * number_of_function_fields,
                                                      90, parameter_field_height, screen_length, screen_height)

        grid = Grid(Dimensions(x, y, length, height), None, 1, True)
        grid.turn_into_grid(parameter_fields + [output_field], None, None)
        self.function_fields.append(function_field)
        self.function.number_of_outputs += 1

    def run(self):
        """ summary: changes the inputs and output for each test case based on the user's inputs
            params: None
            returns: None
        """
        for function_field in self.function_fields:
            self.function.test_cases = []
            inputs = []

            for input_field in function_field.inputs:
                inputs.append(input_field.text)

            test_case = TestCase(inputs, function_field.output.text)
            self.function.test_cases.append(test_case)














