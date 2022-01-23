import re

from base.function import Parameter, Function


class FunctionFinder:
    """Finds all the functions in the file"""
    # Testing RegEx ^.*(public|static|private).*(int|double|boolean).*$
    lines = []
    function_starts = []
    functions = []
    coding_language = None

    def __init__(self, coding_language):
        """ summary: initializes the object

            params:
                coding_language: CodingLangauge; the coding langauge that is being used

            returns: None
        """

        self.coding_language = coding_language

    def get_all_functions(self, lines):
        """ summary: iterates over each line in lines to find all the functions

            params:
                lines: List of String; the lines in the file

            returns: List of Function; the functions that are in the file
        """
        
        self.lines = lines

        for x in range(len(lines)):
            line = lines[x]
            if self.coding_language.is_function(line):
                self.function_starts.append(x)

        for function_start in self.function_starts:
            parameters = self.coding_language.get_parameters(self.lines[function_start])
            function = Function(parameters, self.get_function_name(self.lines[function_start]))
            function.output_type = self.coding_language.get_output_type(self.lines[function_start])
            self.functions.append(function)

        return self.functions

    def get_function_name(self, function_declaration_line):
        """ summary: finds the function's name

            params:
                function_declaration_line: String; the line that declares the function

            returns: String; the name of the function
        """

        function_name = ""
        for ch in function_declaration_line:
            # There can't be any spaces in the function name meaning if there is a space then its not the function name
            if ch == " ":
                function_name = ""

            elif ch == "(":
                break

            # If the ch isn't equal to '(' or a space then the function_name should have a ch added to it
            else:
                function_name += ch

        return function_name



