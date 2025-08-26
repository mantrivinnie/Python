# This program checks whether a number is even or odd.

def check_even_or_odd(number):
    """
    This function checks if a number is even or odd.
    
    An even number is a number that is perfectly divisible by 2,
    leaving no remainder. The modulo operator (%) is used to
    find the remainder of a division.
    
    Args:
        number (int): The number to check.
    
    Returns:
        str: A string indicating whether the number is "Even" or "Odd".
    """
    # The modulo operator (%) gives the remainder of a division.
    # If a number divided by 2 has a remainder of 0, it is even.
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Get input from the user.
# The input() function returns a string, so we convert it to an integer.
try:
    user_number = int(input("Enter an integer: "))

    # Call the function to check the number.
    result = check_even_or_odd(user_number)

    # Display the result to the user.
    print(f"The number {user_number} is {result}.")

except ValueError:
    # Handle cases where the user enters non-integer input.
    print("Invalid input. Please enter a whole number (integer).")

