# Program to implement Merge Sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2      # find the middle
        left_half = arr[:mid]    # divide into left half
        right_half = arr[mid:]   # divide into right half

        # Recursive calls to sort each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two halves
        i = j = k = 0

        # Compare and merge
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements from left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements from right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)

merge_sort(arr)

print("Sorted array:", arr)



#Original array: [38, 27, 43, 3, 9, 82, 10]
#Sorted array: [3, 9, 10, 27, 38, 43, 82]


'''
Explanation:
Merge Sort is a classic Divide and Conquer algorithm:
Divide the array into halves recursively until you reach single elements.
Merge the halves back in sorted order.
The merge_sort() function splits and merges until the array is fully sorted.
'''

#Time Complexity	: O(n log n)
#Space Complexity : O(n)
