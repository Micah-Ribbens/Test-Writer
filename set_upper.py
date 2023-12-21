from base.important_variables import *
from gui.all_functions_screen import AllFunctionsScreen
from logic.function_finder import FunctionFinder
from logic.line_finder import LineFinder


class SetUpper:
    """Has helper methods for transitioning between screens and stores needed data"""

    functions = []
    function_fields = []
    all_functions_screen: AllFunctionsScreen = None

    def set_up(file_path, coding_language):
        """ summary: sets up the screen with all the functions based on the information from the file

            params:
                file_path: String; the path to the file which will be tested

            returns: None
        """

        lines = LineFinder.get_lines(file_path)
        function_finder = FunctionFinder(coding_language)
        SetUpper.functions = function_finder.get_all_functions(lines)

        all_functions_screen = AllFunctionsScreen(SetUpper.functions)
        game_window.add_screen(all_functions_screen)
        game_window.display_screen(all_functions_screen)
        SetUpper.all_functions_screen = all_functions_screen

