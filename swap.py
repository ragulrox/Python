def swap_values(a, b):
    print(f"Original values - a: {a}, b: {b}")
    temp = a
    a = b
    b = temp    
    print(f"Swapped values - a: {a}, b: {b}")
    return a, b
a = 5
b = 10
a, b = swap_values(a, b)
