from base.function import TestCase
from gui.function_testing_screen import FunctionField


class TestWriter:
    """Writes tests"""
    import_statement = "import org.testng.annotations.Test;"
    test_file = open("test.java", "w+")

    def write_tests(self, functions):
        """ summary: writes the tests for each function in functions in a file called 'test.java'

            params:
                functions: List of Function; the functions that should be tested

            returns: None
        """

        self.test_file.write(self.import_statement)
        self.test_file.write("\n"+self.get_class_statement())

        for function in functions:
            if (len(function.test_cases) != 0):
                self.write_function_tests(function)

    def get_class_statement(self):
        """ summary: gets the class declaration statement
            params: None
            returns: the class declaration statement
        """
        return "class Test {"

    def write_function_declaration_statement(self, function_name):
        """ summary: writes the declaration statement of a function

            params:
                function_name: String; the name of the function

            returns: None
        """

        self.write_line("@Test", 1)
        self.write_line(f"public void {function_name}()" + "{", 1)

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
            self.write_function_body("wanted_outputs.add(wanted_output);")
            self.write_function_body("gotten_outputs.add(gotten_output);")

            self.write_function_body("for (var i = 0; i < inputs.size(); i++) {")
            self.write_line("if (wanted_outputs.get(i) != gotten_outputs.get(i) {", 3)

            error_start = "throw new AssertionError(\"Test Case i out of wanted_outputs.size() Failed; wanted\""
            self.write_line(f"{error_start} + wanted_outputs.get(i) + \" gotten\" + gotten_outputs.get(i));", 4)

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
