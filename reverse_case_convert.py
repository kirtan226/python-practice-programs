"""Write a function to invert the case of each character in a string.
Return the inverted case string.
Example
input:'Hello'
output:'OLLEh'
Reason: The function reverses the string and inverts the case of 'Hello' to 'OLLEH'.

Input:World
Output:DLROw

Input:Python
Output:NOHTYp

Input:Case
Output:ESAc
"""

def invert_case_and_index(s):
    reverse=s[::-1]
    new=''
    for i in reverse:
        if i.isupper():
            new+=i.lower()
        elif i.islower():
            new+=i.upper()
    return new


print(invert_case_and_index('Hello'))