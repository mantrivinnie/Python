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



'''
Explanation:

Quick Sort is a divide-and-conquer algorithm:

Pick a pivot element (here, the middle one).

Partition the array into:

left: elements smaller than pivot

middle: elements equal to pivot

right: elements greater than pivot

Recursively sort left and right, then combine.

Time Complexity:

Average Case → O(n log n)

Worst Case → O(n²) (when pivot selection is poor)
'''

#Alternative (In-place version using recursion):
#If you want to sort the array without creating new lists:

def quicksort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_inplace(arr, low, pi - 1)
        quicksort_inplace(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)
quicksort_inplace(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
