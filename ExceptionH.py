##Vincent OChieng  SCT211-0070/2022

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        try:
            result = x / y
            return result
        except ZeroDivisionError:
            return "Cannot divide by zero"


calculator = Calculator()

result_addition = calculator.add(5, 3)
result_subtraction = calculator.subtract(10, 4)
result_multiplication = calculator.multiply(6, 2)
result_division = calculator.divide(8, 2)

print("Addition:", result_addition)
print("Subtraction:", result_subtraction)
print("Multiplication:", result_multiplication)
print("Division:", result_division)