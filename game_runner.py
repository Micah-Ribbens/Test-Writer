import time

import pygame.key

from base.important_variables import *
from base.velocity_calculator import VelocityCalculator
from gui.home_screen import HomeScreen
from logic.python_language import PythonLanguage
from logic.test_writer import TestWriter
from set_upper import SetUpper

home_screen = HomeScreen()
game_window.add_screen(home_screen)

coding_langauge = PythonLanguage()

while True:
    controls = pygame.key.get_pressed()
    mods = pygame.key.get_mods()
    start_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if home_screen.submit_button.got_clicked():
        SetUpper.set_up(home_screen.file_location_field.text, coding_langauge)

    if controls[pygame.K_d] and pygame.KMOD_CTRL & mods:
        test_writer = TestWriter(coding_langauge)
        functions = SetUpper.functions
        test_writer.write_tests(functions)
        pygame.quit()

    game_window.run()

    if controls[pygame.K_LEFT]:
        game_window.display_screen(SetUpper.all_functions_screen)

    VelocityCalculator.time = time.time() - start_time
