
# Program to implement Binary Search

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid   # target found, return index
        elif arr[mid] < target:
            low = mid + 1   # search in right half
        else:
            high = mid - 1  # search in left half

    return -1   # target not found


# Input: sorted list
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = int(input("Enter the number to search: "))

# Perform search
result = binary_search(arr, target)

# Display result
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list.")



#Example
#Enter the number to search: 23
#Element found at index 5
