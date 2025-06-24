#Finding the maximum of two numbers in Python helps determine the larger of the two values.
# For example, given two numbers a = 7 and b = 3, you may want to extract the larger number, which in this case is 7.

#method-1
a = 7
b = 3
print(max(a, b))

#method-2
a=7
b=3
print(a if a>b else b)

#method-3
a = 7
b = 3
if a > b:
    print(a)
else:
    print(b)

#method-4
a = 7
b = 3
num = [a, b]
num.sort()
print(num[-1])