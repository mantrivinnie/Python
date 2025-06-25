#Given a list, write a Python program to swap the first and last element of the list using Python.

# method-1
my_list = [1, 2, 3, 4, 5]
my_list[0], my_list[-1] = my_list[-1], my_list[0]
print("List after swapping first and last elements:", my_list)

#method-2
def swapList(newList):
    size = len(newList)
    
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    
    return newList
    

newList = [12, 35, 9, 56, 24]
print(swapList(newList))

#method-3
def swapList(list):
    
    get = list[-1], list[0]
    
    list[0], list[-1] = get
    
    return list

newList = [12, 35, 9, 56, 24]
print(swapList(newList))
