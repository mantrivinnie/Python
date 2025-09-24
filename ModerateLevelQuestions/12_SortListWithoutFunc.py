#to sort a list without using sort() function 

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                # swap
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

# Take input
numbers = [64, 25, 12, 22, 11]
print("Original list:", numbers)

sorted_list = bubble_sort(numbers)
print("Sorted list:", sorted_list)


#Original list: [64, 25, 12, 22, 11]
#Sorted list: [11, 12, 22, 25, 64]
