def normalize_string(input_string):
    # 1. Remove extra spaces from the beginning and end of the string
    cleaned_string = input_string.strip()
    
    # 2. Remove any special characters and punctuation (keeping only alphanumeric and spaces)
    allowed_chars = []
    for char in cleaned_string:
        if char.isalnum() or char.isspace():
            allowed_chars.append(char)
    
    # Join allowed characters back into a string
    cleaned_string = ''.join(allowed_chars)
    
    # 3. Replace multiple spaces with a single space
    words = cleaned_string.split()
    cleaned_string = ' '.join(words)
    
    # 4. Convert the string to camel case (capitalize the first letter of each word)
    camel_case_string = ' '.join([word.capitalize() for word in words])
    
    return camel_case_string

# Example input
input_string = " He@llo! World@ This is a Test!   . "
output_string = normalize_string(input_string)
print(output_string)


# Time Complexity

# O(n)

# Space Complexity

# O(n)