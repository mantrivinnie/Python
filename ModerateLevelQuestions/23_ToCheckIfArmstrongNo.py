# Program to check if a number is an Armstrong number

def is_armstrong(num):
    # Convert number to string to easily count digits
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num

# Take input
num = int(input("Enter a number: "))

# Check and print result
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


#Enter a number: 153
#153 is an Armstrong number.

#Enter a number: 9474
#9474 is an Armstrong number.

#Enter a number: 125
#125 is not an Armstrong number.
