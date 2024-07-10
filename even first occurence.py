def print_even_before_20(lst):
    for num in lst:
        if num == 20:
            break
        if num % 2 == 0:
            print(num)
numbers = [10, 15, 8, 21, 14, 20, 30, 12]
print("Even numbers before the first occurrence of 20:")
print_even_before_20(numbers)
