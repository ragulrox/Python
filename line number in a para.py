def count_words_and_lines(paragraph):
    # Split the paragraph into lines
    lines = paragraph.split('\n')
    
    # Count the number of lines
    num_lines = len(lines)
    
    # Count the number of words in each line
    words_per_line = [len(line.split()) for line in lines]
    
    return words_per_line, num_lines

# Sample input paragraph
paragraph = """This is the first line.
This is the second line, which is a bit longer.
And this is the third line."""

# Calculating the number of words in each line and the number of lines
words_per_line, num_lines = count_words_and_lines(paragraph)

# Printing the results
print(f"Number of lines: {num_lines}")
for i, count in enumerate(words_per_line, start=1):
    print(f"Number of words in line {i}: {count}")
