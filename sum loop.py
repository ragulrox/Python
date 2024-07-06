def sum_using_for_loop(lst):
    total = 0
    for element in lst:
        total += element
    return total

# Example usage
numbers = [1, 2, 3, 4, 5]
print("Sum using for loop:", sum_using_for_loop(numbers))
