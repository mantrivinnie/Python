#Check if element exists in list in Python

#method-1
list= [10,20,30,40,50]
for x in list:
    if(x==40):
        print("element exists")
    else:
        print("element does not exists")

#method-2
list= [10,20,30,40,50]
key=40
flag = False

for x in list:
    if x == key:
        flag = True
        break

if flag:
    print("Element exists in the list")
else:
    print("Element does not exist")

#method-3
list = [10, 20, 30, 40, 50]
if a.count(40) > 0:
    print("Element exists in the list")
else:
    print("Element does not exist")