"""
Write a function to replace multiple different characters in a string at once.
1. Define a function that takes a string and a dictionary as input.
2. The dictionary keys are the characters to be replaced and the values are the characters to replace them with.
3. Inside the function, iterate over each character in the string. If it's in the dictionary, replace it with its corresponding value.
4. Return the modified string.

input:'hello world'
{'h': 'j', 'e': 'i', 'l': 'm'}
output:'jimmo wormd'
Reason: In the input string, 'h' is replaced by 'j', 'e' is replaced by 'i', and all instances of '1' are replaced by 'm.
 Therefore, 'hello world' becomes 'jimmo wormd'.

InputL'goodbye'
{'g': 'b', 'o': 'a', 'd': 'y'}
Output:baaybye

Input:'programming'
{'p': 'c', 'm': 'n'}
Output:crogranning
"""

def replace_chars(string, replacements):
    new=''
    for i in string:
        if i in replacements.keys():
            new+=replacements[i]
        else:
            new+=i
    return new

string = 'kirtan'
replacements={'k': 'j', 'e': 'i', 'l': 'm'}
print(replace_chars(string, replacements))