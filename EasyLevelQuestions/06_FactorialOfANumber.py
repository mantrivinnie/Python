# Factorial using loop
n = int(input("Enter a number: "))
fact = 1

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n} = {fact}")


#---------------Method-2-------------
# Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {n} = {factorial(n)}")


#----------------Method -3------------------
import math

n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {n} = {math.factorial(n)}")
