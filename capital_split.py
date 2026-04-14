"""
Write a function to split a string at each capital letter.
If there are no capital letters in the string return an empty list.
input:'Helloworld'
output:['Hello', 'World']
Reason: The input string is split at each capital letter, resulting in two strings: 'Hello' and 'World'.

Input:'ThisIsATest'
Output:['This', 'Is', 'A', 'Test']
"""

def split_at_capitals_iterative(s):
    if not any(c.isupper() for c in s):
        return []
    result = []
    current_word = ''
    for char in s:
        if char.isupper():
            if current_word:
                result.append(current_word)
            current_word = char
        else:
            current_word += char
    if current_word:
        result.append(current_word)
    return result

# Example usage:
input_string = 'HelloWorld'
output = split_at_capitals_iterative(input_string)
print(output)  # Output: ['Hello', 'World']


# Using re
# import re
# def split_at_capitals_regex(s):
#     if not any(c.isupper() for c in s):
#         return []
#     return re.findall(r'[A-Z][a-z]*', s)
#
# # Example usage:
# input_string = 'HelloWorld'
# output = split_at_capitals_regex(input_string)
# print(output)  # Output: ['Hello', 'World']