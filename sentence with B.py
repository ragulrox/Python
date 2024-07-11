def count_sentences_starting_with_b(paragraph):
    # Split the paragraph into sentences using common sentence-ending punctuation
    sentences = paragraph.split('.')
    
    # Filter out empty strings that may occur due to trailing punctuation
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    # Count sentences that start with 'B'
    count = sum(1 for sentence in sentences if sentence.startswith('B'))
    
    return count

# Sample input paragraph
paragraph = """This is the first sentence. But this one starts with B. 
Another sentence here. Beautiful things start with B. This one does not start with B."""

# Calculating the number of sentences starting with 'B'
num_sentences_starting_with_b = count_sentences_starting_with_b(paragraph)

# Printing the result
print(f"Number of sentences starting with 'B': {num_sentences_starting_with_b}")
