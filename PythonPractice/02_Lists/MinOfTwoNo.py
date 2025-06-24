#method-1
a=5
b=9
print(min(a,b))

#method-2
a=5
b=9
print(a if a<b else b)

#method-3
a=5
b=9
if a<b:
    print(a)
else:
    print(b)

#method-4
a = 5
b = 9
num = [a, b]
num.sort()
print(num[0])