def sumsquare(l):
    odd_sum = sum(x**2 for x in l if x % 2 != 0)
    even_sum = sum(x**2 for x in l if x % 2 == 0)
    return [odd_sum, even_sum]
n = int(input("Enter the number of elements: "))
numbers = []
for _ in range(n):
    num = int(input("Enter the element: "))
    numbers.append(num)
result = sumsquare(numbers)
print(result)
