#Find Sum and Average of List in Python

#method-1
a = [10,20,30,40,50]
sums = sum(a)
length = len(a)
avg = sums/length
print("Sum is :" , sums , "Avg is:" , avg)

#method-2
a = [10,20,30,40,50]
sum=0
length=0
for x in a :
    sum += x
    length += 1 

print("Sum:", sum)
avg = sum/length
print("Avg = ", avg)
