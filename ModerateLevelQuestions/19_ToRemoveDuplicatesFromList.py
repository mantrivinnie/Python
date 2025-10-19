#program to remove duplicates from a list.


#Using set()
def remove_duplicates(lst):
    return list(set(lst))

# Example
numbers = [1, 2, 2, 3, 4, 4, 5]
print("Original list:", numbers)
print("After removing duplicates:", remove_duplicates(numbers))

#Alternate Method 
def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example
numbers = [1, 2, 2, 3, 4, 4, 5]
print("Original list:", numbers)
print("After removing duplicates:", remove_duplicates(numbers))


#Output 
#Original list: [1, 2, 2, 3, 4, 4, 5]
#After removing duplicates: [1, 2, 3, 4, 5]


