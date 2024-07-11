def count_matching_characters(s1, s2):
    # Determine the length of the shorter string
    min_length = min(len(s1), len(s2))
    
    # Count matches
    matches = 0
    for i in range(min_length):
        if s1[i] == s2[i]:
            matches += 1
            
    return matches

# Sample input
s1 = "what"
s2 = "watch"

# Calculating and printing the number of matches
matches = count_matching_characters(s1, s2)
print(f"Number of matches: {matches}")
