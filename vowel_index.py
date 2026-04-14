"""Write a program that gives the index of the first vowel obtained in a string.
1. Define a function that takes a single argument str.
2. Inside the function, calculate the index of the first vowel encountered in the string.
3. Return None if there are no vowels.

input:"apple"
output:0

input:"PYTHON"
output:4
"""

def get_first_vowel_index(str):
    # write your code here
    vowel='aeiouAEIOU'
    sl=list(str)
    for i in sl:
        if i in vowel:
            return sl.index(i)
        else:
            continue

s="pythOn"
print(get_first_vowel_index(s))