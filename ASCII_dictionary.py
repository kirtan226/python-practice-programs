'''
Write a function to create a dictionary with characters as keys and their ASCII codes as values.
Instructions
1. Define a function that takes a string as input.
2. Inside the function, iterate over each character in the string and add it to the dictionary with its ASCII code as the value.
3. Return the resulting dictionary.

input:"abc"
output:{'a': 97, 'b': 98, 'c': 99}
Reason: The ASCII codes for 'a', 'b', and 'c' are 97, 98, and 99 respectively. So, these are added to
       the dictionary as values with their corresponding characters as keys.

Input:'def'
Output: {'d': 100, 'e': 101, 'f': 102}

Input:ghi
Output:{'g': 103, 'h': 104, 'i': 105}
'''

def ascii_dictionary(string):
    d={}
    for i in string:
        d[i]=ord(i)
    return d
ascii_dictionary('abc')