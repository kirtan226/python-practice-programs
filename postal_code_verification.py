""" Write a function to valid Postal code .
A valid postal code must follow the pattern DDD-DDD, where D is a digit.
Hint: In Python, you can use the re module to work with regular expressions. The match() function can be used to
determine if an input string matches a particular pattern.
input:*123 456'
output:True
Reason: The input string '123-456' matches the pattern of a valid postal code, which is DDD-DDD.
Console

Input:123456
Output:False

Input:12-3456
Output:False
"""

import re
def validate_postal_code(code):
    a=re.match(r'[0-9]{3}-[0-9]{3}',code)
    return True if a else False

code = '987-654'
print(validate_postal_code(code))