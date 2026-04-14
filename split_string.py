"""
Write a function to split a string into two parts: one containing all the vowels and the other containing all the consonants.

Return two strings: one containing all vowels and another containing all consonants from the input string.
input:'hello'
output:('eo', 'hll')
Reason: of the word 'hello', 'e' and 'o' are vowels and 'h', 'I', and 'l' are consonants.
So, we get two strings: 'eo' (vowels) and 'hll' (consonants).
"""

def split_string(s):
    vowels='aeiou'
    vo=''
    constant=''

    for char in s:
        if char in vowels:
            vo+=char
        else:
            constant+=char
    return (vo , constant)




    # for char in s:
    #     if char in vowels:
    #         vo+=char
    #     else:
    #         constant+=char
    #
    # # print(vo)
    # # print(constant)
    # li=[]
    # li.append(vo)
    # li.append(constant)
    # # print(li)
    # tup=tuple(li)
    # # print(tup)
    # return tup


print(split_string("abcdefg"))