#program to implement a basic calculator that performs +, -, *, /


def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error! Division by zero."
        return a / b
    else:
        return "Invalid operator."

# Take inputs
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    result = calculator(a, b, op)
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter numeric values.")

#Example 1
#Enter first number: 10
#Enter second number: 5
#Enter operator (+, -, *, /): *
#Result: 50.0

#Example 2
#Enter first number: 8
#Enter second number: 0
#Enter operator (+, -, *, /): /
#Result: Error! Division by zero.

