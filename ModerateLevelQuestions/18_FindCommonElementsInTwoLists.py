# Program to find common elements in two lists 

def common_elements(list1, list2):
    return list(set(list1) & set(list2))   # use set intersection

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = common_elements(list1, list2)

print("List 1:", list1)
print("List 2:", list2)
print("Common elements:", common)



#List 1: [1, 2, 3, 4, 5]
#List 2: [4, 5, 6, 7, 8]
#Common elements: [4, 5]


#Alternate Method ------------- without using set 
def common_elements(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common
