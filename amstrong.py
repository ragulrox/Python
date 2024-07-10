def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == num
test_number = 143
if is_armstrong_number(test_number):
    print(f"{test_number} is an Armstrong number.")
else:
    print(f"{test_number} is not an Armstrong number.")
  
