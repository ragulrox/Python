def count_negative_numbers(lst):
    return sum(1 for num in lst if num < 0)
list_of_elements = [16, -18, 27, -16, 23, -21, 19]
negative_count = count_negative_numbers(list_of_elements)
print("Number of negative numbers in List of elements =", negative_count)
