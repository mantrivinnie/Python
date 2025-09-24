#To find all the prime numbers between a given range (here from 1 to 100)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # check up to sqrt(n)
        if n % i == 0:
            return False
    return True

primes = [num for num in range(1, 101) if is_prime(num)]

print("Prime numbers between 1 and 100 are:")
print(primes)



#Prime numbers between 1 and 100 are:
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
