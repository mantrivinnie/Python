# This program gives the squared value of the input provided by the user.

def SquareNum(x):
    return x*x
try:

    # Get input from the user.
    # The input() function returns a string, so we need to convert it to a float
    # to perform mathematical operations.
    x=float(input("Enter the number:\n"))

    # Call the function to get the sum.
    square = SquareNum(x)

    # Display the result to the user.
    # The f-string formats the output nicely.
    print(f"The square of {x} is {square}")

except ValueError:
    # Handle cases where the user enters non-numeric input.
    print("Invalid input. Please enter a valid number.")


