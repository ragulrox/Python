import re

def count_special_characters(statement):
    special_characters_pattern = re.compile(r'[^a-zA-Z0-9\s]')
    special_characters = special_characters_pattern.findall(statement)
    count = len(special_characters)
    return count
statement = "#&$% is the wishes"
special_characters_count = count_special_characters(statement)
print(f"Special Characters: {special_characters_count}")
