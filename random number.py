import random
def generate_random_number():
    random_number = random.randint(1, 99)
    return random_number
random_num = generate_random_number()
print(f"Generated random number: {random_num}")
