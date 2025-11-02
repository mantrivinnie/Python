# Program to implement Selection Sort

def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Assume the current index has the minimum element
        min_index = i

        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Input list
arr = [64, 25, 12, 22, 11]

print("Original array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
