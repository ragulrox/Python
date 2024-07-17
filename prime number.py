def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True 
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
def find_primes(arr):
    return [num for num in arr if is_prime(num)]
array = [26, 28, 47, 26, 43, 51, 29]
primes_in_array = find_primes(array)
print("Prime numbers in Array elements =", primes_in_array)
