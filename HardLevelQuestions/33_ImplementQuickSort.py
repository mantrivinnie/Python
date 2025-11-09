# Program to implement Quick Sort

def quicksort(arr):
    # Base case: a list of 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # choose middle element as pivot
        left = [x for x in arr if x < pivot]       # elements less than pivot
        middle = [x for x in arr if x == pivot]    # elements equal to pivot
        right = [x for x in arr if x > pivot]      # elements greater than pivot
        return quicksort(left) + middle + quicksort(right)


# Input list
arr = [10, 7, 8, 9, 1, 5]

print("Original array:", arr)
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)


#Original array: [10, 7, 8, 9, 1, 5]
#Sorted array: [1, 5, 7, 8, 9, 10]
