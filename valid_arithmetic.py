''' Write a function to check if a given string is valid arithmmetic expression .
1. Define a function that takes a string as input.
2. Return True if the string is a valid arithmetic expression, otherwise return False.
    A valid arithmetic expression contains only numbers, arithmetic operators (+, -, *, /)
    and parenthesis () and no alphabets.

Input : 'abc123'
Output : False

Input : '(4+5)*6/7-8'
Output : True

Input : '10/2+xyz'
Output : False

Input : '2+3*4/5'
Output : True

'''

def is_math_expression(s):
    validations ='0123456789+-*/()'

    for i in s:
        if i not in validations:
            return False
    return True


print(is_math_expression('2+3*4/5'))