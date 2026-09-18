class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero is undefined."


calc = Calculator()

try:
    x = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ").strip()
    y = float(input("Enter second number: "))

    if op == "+":
        result = calc.add(x, y)
    elif op == "-":
        result = calc.subtract(x, y)
    elif op == "*":
        result = calc.multiply(x, y)
    elif op == "/":
        result = calc.divide(x, y)
    else:
        result = "Error: Unsupported operator."

    print(f"Result: {result}")
except ValueError:
    print("Error: Invalid numeric input.")