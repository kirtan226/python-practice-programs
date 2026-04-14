"""Codeland Username Validation
Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine
if the string is a valid username according to the following rules:
1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string false.
Examples
Input: "aa_"
Output: false

Input: "u__hello_world123"
Output: true                            """

# def username(s):
#     variables='abcdefghijklmnopqrstuvwxyz_1234567890'
#
#     for char in s:
#         if len(s) in range(4,25):
#             if char in variables:
#                 if s[0].isalpha():
#                     if s[-1] != '_':
#                         return True
#
#     return False
#
# st=input("Enter a string:")
# print(username(st))

"""using regular expression"""

import re
def username(s):

    op=re.findall(r'^[a-zA-Z][\w_0-9]{4,24}[^_]$',s)
    if op:
        return True
    else:
        return False

st = input("Enter a string:")
print(username(st))

