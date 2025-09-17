def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10   # get last digit
        n //= 10          # remove last digit
    return total

# Take input
num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))


#Enter a number: 12345
#Sum of digits: 15

#Alternate 
num = input("Enter a number: ")
digit_sum = sum(int(digit) for digit in num)
print("Sum of digits:", digit_sum)
