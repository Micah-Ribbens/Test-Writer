import re

from base.function import Parameter, Function

class FunctionFinder:
    """Finds all the functions in the file"""
    # Testing RegEx ^.*(public|static|private).*(int|double|boolean).*$
    lines = []
    function_starts = []
    functions = []

    def get_all_functions(self, lines):
        """ summary: iterates over each line in lines to find all the functions

            params:
                lines: List of String; the lines in the file

            returns: List of Function; the functions that are in the file
        """
        
        self.lines = lines

        for x in range(len(lines)):
            line = lines[x]
            if self.is_function(line):
                self.function_starts.append(x)

        for function_start in self.function_starts:
            parameters = self.get_parameters(self.lines[function_start])
            function = Function(parameters, self.get_function_name(self.lines[function_start]))
            function.output_type = self.get_output_type(self.lines[function_start])
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

    def get_parameters(self, function_declaration_line):
        """ summary: finds the parameters within the parentheses of the function declaration

            params:
                function_declaration_line: String; the line that declares the function

            returns: List of Parameter; the parameters that the function has
        """
        parameters_have_started = False
        is_finding_parameter_name = False
        parameter_name = ""
        parameter_type = ""
        parameters = []
        invalid_characters = "()"

        for ch in function_declaration_line:
            # TODO find another way to note have to use continue
            if not parameters_have_started and ch != "(":
                continue

            if ch == "(":
                parameters_have_started = True



            if not is_finding_parameter_name and ch == " ":
                is_finding_parameter_name = True
                # TODO figure out a way to not use continue
                continue


            if is_finding_parameter_name and ch == " ":
                parameter = Parameter(parameter_type, parameter_name)
                parameters.append(parameter)

            if ch == ",":
                parameter_name = ""
                parameter_type = ""
                is_finding_parameter_name = False

            if not is_finding_parameter_name and ch != " " and not invalid_characters.__contains__(ch):
                parameter_type += ch

            if is_finding_parameter_name and ch != " " and not invalid_characters.__contains__(ch):
                parameter_name += ch


        return parameters

    def find_function_end(self, function_start):
        """ summary: finds the line of the function's ending '}'

            params:
                function_start: int; the line that the function starts on
                lines: List of String; the lines of the file being tested

            returns: int; the line that the function ends on
        """

        outer_curly_braces_needed = 1

        for x in range(len(self.lines)):
            line = self.lines[x + function_start]

            for ch in line:
                if ch == "{":
                    outer_curly_braces_needed += 1

                if ch == "}":
                    outer_curly_braces_needed -= 1

            if outer_curly_braces_needed <= 0:
                return x + function_start

        raise ValueError("Couldn't find the function's end")

    def is_function(self, line):
        """ summary: sees if the line is a function by using a regular expression

            params:
                line: String; the line that will be tested to see if it is a function

            returns: boolean; if the line is a function
        """
        regular_expression = "^.*(public|static|private).*\(.*{$"
        return re.search(regular_expression, line) is not None

    def get_output_type(self, line):
        """ summary: goes over the line and returns the first word that isn't public, static, or void

            params:
                line: String; the line that function is declared on

            returns: String; the output type of the function
        """

        tokens_before_output_type = ["public", "static", "void"]
        output_type = ""
        letters = "abcdefghijklmnopqrstuvwxyz"

        for ch in line:
            if ch == " " and tokens_before_output_type.__contains__(output_type):
                output_type = ""

            elif ch == " " and not tokens_before_output_type.__contains__(output_type) and output_type != "":
                break

            elif letters.__contains__(ch.lower()):
                output_type += ch

        return output_type


    # TODO assert methods validity maybe just ask user for number of outputs?
    # def get_number_of_outputs(self, function_start, function_end):
    #     """ summary: gets all the possible outputs (number of if statements + 1) for a function
    #
    #         params:
    #             function_start: int; the line number for the start of the function
    #             function_end: int; the line number for the end of the function
    #             lines: List of String; the self.lines in the file
    #
    #         returs: int; the number of outputs of the function
    #     """
    #     number_of_outputs = 1
    #     for x in range(function_end - function_start):
    #         if self.is_if_statement(self.lines[x + function_start]):
    #             number_of_outputs += 1
    #
    #     return number_of_outputs

    # def is_if_statement(self, line):
    #     """ summary: sees if the line is an if statement by using a regular expression
    #
    #         params:
    #             line: String; the line that will be tested to see if it is a function
    #
    #         returns: boolean; if the line is an if statement
    #     """
    #
    #     regular_expression = "^if \(.*{$"
    #     return re.search(regular_expression, line)