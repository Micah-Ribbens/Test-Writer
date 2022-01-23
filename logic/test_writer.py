from base.function import TestCase
from gui.function_testing_screen import FunctionField
from logic.coding_langauge import CodingLanguage


class TestWriter:
    """Writes tests"""
    coding_language: CodingLanguage = None

    def __init__(self, coding_language):
        """ summary: initializes the object

            params:
                coding_language: CodingLanguage; the language of the file being tested

            returns: None
        """

        self.coding_language = coding_language

    def write_tests(self, functions):
        """ summary: writes the tests for each function in functions in a file called 'test.txt'

            params:
                functions: List of Function; the functions that should be tested

            returns: None
        """

        self.coding_language.write_before_functions()
        for function in functions:
            if (len(function.test_cases) != 0):
                self.coding_language.write_function_tests(function)

        self.coding_language.write_after_functions()




