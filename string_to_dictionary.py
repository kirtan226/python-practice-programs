'''Write a function to map each letter in a string to its corresponding ASCII value.
- Return a dictionary where keys are characters from the input string and values are their
  corresponding ASCII values.
Input : 'abc'
Output : {'a': 97, 'b': 98, 'c': 99}
Reason: The ASCII value of a is 97,b is 98, and c is 99. So, the output {'a': 97, 'b': 98, 'c': 99} .

Input :'def'
Output :{'d': 100, 'e': 101, 'f': 102}
'''


def map_letters(string):
    new = {}
    for i in string:
        new[i] = ord(i)
    return new


print(map_letters('kirtan'))
