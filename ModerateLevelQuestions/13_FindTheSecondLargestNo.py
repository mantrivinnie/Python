def second_largest(lst):
    # Remove duplicates to handle repeated values
    unique_lst = list(set(lst))
    
    if len(unique_lst) < 2:
        return None   # Not enough unique numbers
    
    largest = max(unique_lst)
    unique_lst.remove(largest)
    return max(unique_lst)

# Example usage
numbers = [12, 35, 1, 10, 34, 1]
print("List:", numbers)

result = second_largest(numbers)
if result is None:
    print("List doesn't have a second largest element.")
else:
    print("Second largest number is:", result)
