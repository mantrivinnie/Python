# This program adds two numbers provided by the user.

def add_two_numbers(num1, num2):
    """
    This function takes two numbers as arguments and returns their sum.
    
    Args:
        num1 (float): The first number.
        num2 (float): The second number.
    
    Returns:
        float: The sum of the two numbers.
    """
    return num1 + num2

# Get input from the user.
# The input() function returns a string, so we need to convert it to a float
# to perform mathematical operations.
try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    # Call the function to get the sum.
    sum_result = add_two_numbers(first_number, second_number)

    # Display the result to the user.
    # The f-string formats the output nicely.
    print(f"The sum of {first_number} and {second_number} is: {sum_result}")

except ValueError:
    # Handle cases where the user enters non-numeric input.
    print("Invalid input. Please enter a valid number.")

