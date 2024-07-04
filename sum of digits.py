def sum(n):
    n = abs(n) 
    total = 0
    while n > 0:
        total += n % 10  
        n = n // 10  
    return total
number = int(input("Enter the number:"))
result = sum(number)
print(f"Sum of digits of {number} is {result}")
