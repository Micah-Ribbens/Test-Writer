import pygame.key

from base.important_variables import *
import time
from base.velocity_calculator import VelocityCalculator
from gui.all_functions_screen import AllFunctionsScreen
from base.function import Function, Parameter
from gui.function_testing_screen import FunctionTestingScreen
from gui.home_screen import HomeScreen
from logic.function_finder import FunctionFinder
from logic.line_finder import LineFinder
from logic.test_writer import TestWriter

home_screen = HomeScreen()
game_window.add_screen(home_screen)

class SetUpper:
    functions = []
    function_fields = []
    all_functions_screen: AllFunctionsScreen = None

    def set_up(file_path):
        lines = LineFinder.get_lines(file_path)
        function_finder = FunctionFinder()
        SetUpper.functions = function_finder.get_all_functions(lines)

        all_functions_screen = AllFunctionsScreen(SetUpper.functions)
        game_window.add_screen(all_functions_screen)
        game_window.display_screens([all_functions_screen])
        SetUpper.all_functions_screen = all_functions_screen

    def get_all_function_fields():
        return SetUpper.all_functions_screen.function_screens[0].function_fields



while True:
    controls = pygame.key.get_pressed()
    mods = pygame.key.get_mods()
    start_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if home_screen.submit_button.got_clicked():
        # try:
        SetUpper.set_up(home_screen.file_location_field.text)


        # except:
    #     print("File Path can't be found")
    #     home_screen.file_location_field.text = "File path doesn't exist"
    #     home_screen.file_location_field.default_text = "File path doesn't exist"

    if controls[pygame.K_d] and pygame.KMOD_CTRL & mods:
        test_writer = TestWriter()
        functions = SetUpper.functions
        function_fields = SetUpper.get_all_function_fields()
        test_writer.write_tests(functions)
        pygame.quit()

    game_window.run()

    if controls[pygame.K_LEFT]:
        game_window.display_screens([SetUpper.all_functions_screen])

    VelocityCalculator.time = time.time() - start_time
