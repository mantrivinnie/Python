def common_elements(list1, list2):
    return list(set(list1) & set(list2))   # use set intersection

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = common_elements(list1, list2)

print("List 1:", list1)
print("List 2:", list2)
print("Common elements:", common)
