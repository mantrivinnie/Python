# Program to find the GCD of two numbers

def gcd(a, b):
    while b != 0:
        a, b = b, a % b   # Euclidean algorithm
    return a

# Take input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"GCD of {num1} and {num2} is {gcd(num1, num2)}")


#Enter first number: 48
#Enter second number: 18
#GCD of 48 and 18 is 6

#Alternate Method 
import math
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("GCD is:", math.gcd(num1, num2))

