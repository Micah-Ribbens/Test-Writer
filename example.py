class Math:

    @staticmethod
    def add(number1, number2):
        return number1 + number2

    @staticmethod
    def subtract(number1, number2):
        return number1 - number2

    @staticmethod
    def quadratic(a, b, c):
        square_root_value = b ** 2 - 4 * a * c
        return [(-b + square_root_value) / (2 * a),
                (-b - square_root_value) / (2 * a)]

    @staticmethod
    def square(number):
        return number ** 2

    @staticmethod
    def cube(number):
        return number ** 3

    @staticmethod
    def square_root(number):
        return number ** 0.5

