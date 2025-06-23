#Given a positive integer N, the task is to write a Python program to check if the number is Prime or not in Python. 
# For example, given a number 29, it has no divisors other than 1 and 29 itself. Hence, it is a prime number.

import math

n = 11
if n <= 1:
    print(False)
else:
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    print(is_prime)