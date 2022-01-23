from abc import ABC, abstractmethod
import re

from base.function import Parameter


class CodingLanguage(ABC):
    test_file = open("test.txt", "w+")
    @abstractmethod
    def is_function(self, line):
        pass

    @abstractmethod
    def get_parameters(self, function_line):
        pass

    @abstractmethod
    def get_output_type(self, function_line):
        pass

    @abstractmethod
    def write_function_tests(self, function):
        pass

    @abstractmethod
    def write_before_functions(self):
        pass

    @abstractmethod
    def write_after_functions(self):
        pass

    def write_function_body(self, line):
        """ summary: writes the function's body (code below function declaration) calls write_line with 2 as the indentation level

            params:
                line: String; the line that should be written

            returns: None
        """

        self.write_line(line, 2)

    def write_line(self, line, indentation_level):
        """ summary: writes the line with the indentation level provided

            params:
                line: String; the line that should be written
                indentation_level: int; the number of tabs before that line

            returns: None
        """

        indentation = ""

        for x in range(indentation_level):
            indentation += "    "

        self.test_file.write(f"\n{indentation}{line}")
