def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0

    # Traverse both lists and append the smaller element to merged_list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append remaining elements from list1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Append remaining elements from list2
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
result = merge_sorted_lists(list1, list2)
print("Merged Sorted List:", result)