# Program to print the multiplication table of a number

def print_table(n):
    print(f"\nMultiplication Table of {n}:")
    for i in range(1, 11):    # Table up to 10
        print(f"{n} x {i} = {n * i}")

# Take input
num = int(input("Enter a number: "))

# Print the table
print_table(num)
