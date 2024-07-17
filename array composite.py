def is_composite(n):
    if n <= 1:
        return False
    if n == 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False
def count_composite_numbers(arr):
    return sum(1 for num in arr if is_composite(num))
array = [16, 18, 27, 16, 23, 21, 19]
print("Number of Composite Numbers =", count_composite_numbers(array))
