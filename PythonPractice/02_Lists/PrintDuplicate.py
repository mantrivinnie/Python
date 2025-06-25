#code to print the duplicate in the list of integers in python

a = [1,2,3,1,5,6,1,2,5,3,9,4]
s = []
dup = []

for x in a:
    if x in s:
        dup.append(x)
    else:
        s.append(x)
print(dup)