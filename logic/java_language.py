from base.function import Parameter, TestCase
from logic.coding_langauge import CodingLanguage
import re


class JavaLanguage(CodingLanguage):
    def write_before_functions(self):
        """ summary: writes the code that goes before the functions that test the code
            params: None
            returns: None
        """

        self.test_file.write("import org.testng.annotations.Test;")
        self.write_line("class Test {", 0)

    def write_after_functions(self):
        """ summary: writes the code that goes after the functions that test the code
            params: None
            returns: None
        """

        self.write_line("}", 0)

    def is_function(self, line):
        """ summary: sees if the line is a function by using a regular expression

            params:
                line: String; the line that will be tested to see if it is a function

            returns: boolean; if the line is a function
        """

        regular_expression = "^.*(public|static|private).*\(.*{$"
        return re.search(regular_expression, line) is not None

    def get_parameters(self, function_line):
        """ summary: finds the parameters within the parentheses of the function declaration

            params:
                function_line: String; the line that declares the function

            returns: List of Parameter; the parameters that the function has
        """

        parameters_have_started = False
        is_finding_parameter_name = False
        parameter_name = ""
        parameter_type = ""
        parameters = []
        invalid_characters = "()"

        for ch in function_line:
            # TODO find another way to not have to use continue
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

    def write_function_tests(self, function):
        """ summary: writes the tests of the function provided
            params:
                function: Function; the function that should be tested
            returns: None
        """

        self.write_function_declaration_statement(function.name)
        self.write_function_body(f"ArrayList<{function.output_type}> wanted_outputs = new ArrayList<>();")
        self.write_function_body(f"ArrayList<{function.output_type}> gotten_outputs = new ArrayList<>();")

        for x in range(len(function.test_cases)):
            test_case: TestCase = function.test_cases[x]

            wanted_output_name = f"wanted_output{x}"
            self.write_function_body(f"{wanted_output_name} = {test_case.output}")
            gotten_output_name = f"gotten_output{x}"
            function_call = f"{gotten_output_name} = {function.name}("

            for j in range(len(test_case.inputs)):
                # Includes all the inputs, index would be the number of previous functions * the length
                # of parameters (aka inputs); the "+ j" because that is the current input number
                input = test_case.inputs[j]

                function_call += f"{input}"

                # The last parameter in a function doesn't have ", " after it
                if j != len(test_case.inputs) - 1:
                    function_call += ", "

            self.write_function_body(f"{function_call})")
            self.write_function_body(f"wanted_outputs.add({wanted_output_name});")
            self.write_function_body(f"gotten_outputs.add({gotten_output_name});")

            self.write_function_body("for (var i = 0; i < inputs.size(); i++) {")
            self.write_line("if (wanted_outputs.get(i) != gotten_outputs.get(i) {", 3)

            error_start = "throw new AssertionError(\"Test Case i out of wanted_outputs.size() Failed; wanted\""
            self.write_line(f"{error_start} + wanted_outputs.get(i) + \" gotten\" + gotten_outputs.get(i));", 4)

    def write_function_declaration_statement(self, function_name):
        """ summary: writes the declaration statement of a function
            params:
                function_name: String; the name of the function
            returns: None
        """

        self.write_line("@Test", 1)
        self.write_line(f"public void {function_name}()" + "{", 1)