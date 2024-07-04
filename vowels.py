def count_vowels_and_consonants(statement):
    # Define sets of vowels and consonants
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')

    # Initialize counters
    vowels_count = 0
    consonants_count = 0

    # Iterate through each character in the statement
    for char in statement:
        if char in vowels:
            vowels_count += 1
        elif char in consonants:
            consonants_count += 1

    return vowels_count, consonants_count

# Sample input
statement = "This is a sample statement"

# Count vowels and consonants
vowels_count, consonants_count = count_vowels_and_consonants(statement)

# Print the result
print(f"Number of Vowels: {vowels_count}")
print(f"Number of Consonants: {consonants_count}")
