# Program to implement Insertion Sort

def insertion_sort(arr):
    # Traverse from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]          # current element to insert
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key      # place key at correct position

    return arr


# Input list
arr = [12, 11, 13, 5, 6]

print("Original array:", arr)
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)


#Example
#Original array: [12, 11, 13, 5, 6]
#Sorted array: [5, 6, 11, 12, 13]

#Explanation:
#Insertion sort works like sorting cards in your hand.
#It picks one element at a time and inserts it into the correct position among already-sorted elements.

#Time Complexity:
#Worst Case: O(n²)
#Best Case (already sorted): O(n)
