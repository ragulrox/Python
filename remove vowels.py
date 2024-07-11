def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in input_string if char not in vowels])

# Accepting a string from the user
user_input = input("Enter a string: ")

# Removing vowels from the input string
result_string = remove_vowels(user_input)

# Displaying the result
print(f"String after removing vowels: {result_string}")
