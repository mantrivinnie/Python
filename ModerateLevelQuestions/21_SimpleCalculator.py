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
