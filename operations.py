def arithmetic_operations(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    int_div = a // b
    floor_div = a // b
    mod_div = a % b
    return add, sub, mul, int_div, floor_div, mod_div
int_a = 10
int_b = 3
print("Integer operations:")
int_results = arithmetic_operations(int_a, int_b)
print(f"Addition: {int_results[0]}")
print(f"Subtraction: {int_results[1]}")
print(f"Multiplication: {int_results[2]}")
print(f"Integer Division: {int_results[3]}")
print(f"Floor Division: {int_results[4]}")
print(f"Modulo Division: {int_results[5]}")
float_a = 10.5
float_b = 3.2
print("\nFloat operations:")
float_results = arithmetic_operations(float_a, float_b)
print(f"Addition: {float_results[0]}")
print(f"Subtraction: {float_results[1]}")
print(f"Multiplication: {float_results[2]}")
print(f"Integer Division: {float_results[3]}")
print(f"Floor Division: {float_results[4]}")
print(f"Modulo Division: {float_results[5]}")
