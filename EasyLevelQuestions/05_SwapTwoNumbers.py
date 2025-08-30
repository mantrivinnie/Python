# --------------- Method-1 ------------------

def SwapNum(a, b):
    return b, a   # return swapped values

try:
    a = float(input("Enter num 1 : "))
    b = float(input("Enter num 2 : "))

    a, b = SwapNum(a, b)   # call the function and unpack the swapped values
    print("After swapping: a =", a, ", b =", b)

except ValueError:
    print("Invalid input. Please enter a valid number.")


# ---------------- Method -2 ---------------------

# Using arithmetic operations (without third variable)
# Be careful with floating-point precision and very large numbers.

def SwapNum(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

#--------------- Method -3 -----------------------

# Using XOR (works only for integers)
def SwapNum(a, b):
    a = int(a)  # ensure integers
    b = int(b)
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b