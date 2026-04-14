''' Write a function to capitalize first letter of a string based on it's ASCII value .
Input : hello
Output : Hello

Input : world
Output : World

Input : python
Output : Python

Input : challenge
Output : Challenge
'''


def capitalize_by_ascii(s):
    first = s[0]
    print(first)

    ascii = ord(first)
    print(ascii - 32)

    cap = chr(ascii - 32)
    print(cap + s[1:])
    return cap + s[1:]


print(capitalize_by_ascii('hello'))
