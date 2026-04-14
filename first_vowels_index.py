''' Write a function to find the index of the first vowel in a given string.
Return the index of the first vowel in the string. If there are no vowels, return -1.

input:'hello'
output:1
Reason: The first vowel in 'hello' is 'e', which is at index 1.

Input:world
Result:1

Input:PYTHON
Result:4

Input:cry
Result:No vowels found in String
'''

def first_vowel_index(s):
    vowels='aeiouAEIOU'
    for i in s:
        if i in vowels:
            return s.index(i)
    return "No vowels found in String"


print(first_vowel_index('ninehundreadnine'))