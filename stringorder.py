# Using the Python language, have the function AlphabetSoup(str) take the str string parameter being passed
# and return the string with the letters in alphabetical order
# (ie. hello becomes ehllo). Assume numbers and punctuation symbols will not be included in the string.


def isorder(str):
    str_list=list(str)
    a=sorted(str_list)
    # print(a)

    return ''.join(a)

s=input("Enter any string to sort:")
print(isorder(s))