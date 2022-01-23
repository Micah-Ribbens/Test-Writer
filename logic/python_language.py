import re

from base.function import Parameter, TestCase
from logic.coding_langauge import CodingLanguage


class PythonLanguage(CodingLanguage):
    def write_wanted_outputs(self, function):
        """ summary: writes all the wanted outputs in list form

            params:
                function: Function; the function being tested

            returns: None
        """

        self.write_function_body("wanted_outputs = [")
        for x in range(len(function.test_cases)):
            test_case = function.test_cases[x]

            # The last item of the list should not have a comma after it
            if x != len(function.test_cases) - 1:
                self.write_line(f"{test_case.output}, ", 3)

            else:
                self.write_line(f"{test_case.output}", 3)

        self.write_function_body("]")

    def write_gotten_outputs(self, function):
        """ summary: writes all the wanted outputs in list form

            params:
                function: Function; the function being tested

            returns: None
        """
        self.write_function_body("gotten_outputs = [")
        for x in range(len(function.test_cases)):
            test_case = function.test_cases[x]
            function_call = f"{function.name}("

            for j in range(len(test_case.inputs)):
                # Includes all the inputs, index would be the number of previous functions * the length
                # of parameters (aka inputs); the "+ j" because that is the current input number
                input = test_case.inputs[j]

                function_call += f"{input}"

                # The last parameter in a function doesn't have ", " after it
                if j != len(test_case.inputs) - 1:
                    function_call += ", "

            # The last item in a list shouldn't have a ',' after it
            if x != len(function.test_cases) - 1:
                self.write_line(f"{function_call}),", 3)

            else:
                self.write_line(f"{function_call})", 3)

        self.write_function_body("]")

    def write_function_tests(self, function):
        """ summary: writes the tests of the function provided

            params:
                function: Function; the function that should be tested

            returns: None
        """

        self.write_line(f"def {function.name}(self):", 1)
        self.write_wanted_outputs(function)
        self.write_gotten_outputs(function)

        self.write_function_body("for x in range(len(wanted_outputs)):")
        error_message = 'f"Test Case number {x} out of {len(wanted_outputs)} is being tested"'
        self.write_line(f'self.assertEqual(gotten_outputs[x], wanted_outputs[x], {error_message})', 3)

    def write_after_functions(self):
        """ summary: writes the code that goes after the functions that test the code
            params: None
            returns: None
        """

        self.write_line("if __name__ == '__main__':", 0)
        self.write_line("unittest.main()", 1)


    def write_before_functions(self):
        """ summary: writes the code that goes before the functions that test the code
            params: None
            returns: None
        """

        self.test_file.write("import unittest")
        self.write_line("class Test(unittest.TestCase):", 0)

    def is_function(self, line):
        """ summary: sees if the line is a function by using a regular expression

            params:
                line: String; the line that will be tested to see if it is a function

            returns: boolean; if the line is a function
        """

        regular_expression = "^.*def.*:.*$"
        return re.search(regular_expression, line) is not None

    def get_parameters(self, function_line):
        """ summary: finds the parameters within the parentheses of the function declaration

            params:
                function_line: String; the line that declares the function

            returns: List of Parameter; the parameters that the function has
        """

        parameters_have_started = False
        parameter_type = ""
        parameter_name = ""
        parameters = []
        invalid_characters = "(),"

        for ch in function_line:
            if ch == ")":
                break

            if not parameters_have_started and ch != "(":
                continue

            if ch == "(":
                parameters_have_started = True

            # Self isn't a parameter that you can pass in for Python really; it is something used when
            # Calling a method using an instance of the class
            if ch == " " and parameter_name != "self":
                parameters.append(Parameter(parameter_type, self.space_out_words(parameter_name)))
                parameter_name = ""

            elif ch == " ":
                parameter_name = ""

            elif not invalid_characters.__contains__(ch):
                parameter_name += ch

        # The last parameter in a function doesn't have a space after it
        # A space is what adds the parameter_name to parameters
        parameters.append(Parameter(parameter_type, self.space_out_words(parameter_name)))

        return parameters

    def get_output_type(self, function_line):
        """ summary: its impossible to find the output type in Python so it returns ''

            params:
                function_line: String; the line the function was declared on

            returns: String; ''
        """

        return ""

    def space_out_words(self, parameter_name):
        """ summary: goes over each character in parameter_name and turns each '_' into a space (' ')

            params:
                parameter_name: String; the name of the parameter

            returns: String; the parameter_name with spaces between words
        """

        words = ""

        for ch in parameter_name:
            if ch == "_":
                words += " "

            else:
                words += ch

        return words
