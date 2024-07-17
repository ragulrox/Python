def remove_duplicates(arr):
    from collections import Counter
    sorted_arr = sorted(arr)
    element_count = Counter(sorted_arr)
    result = [element for element in sorted_arr if element_count[element] == 1]
    return result
array = [15, 14, 25, 14, 32, 14, 31]
print("Sorted Array =", remove_duplicates(array))
