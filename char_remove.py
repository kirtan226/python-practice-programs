"""Question: An array of characters and a string B is given. Write a function to
 return the string B with all the characters from the array removed."""

def char_set(l1,s1):

    s=''

    for char in s1:
        if char not in l1:
            s=s+char
    return s

l1=['h','e','w']
s1='hello world'
print(char_set(l1,s1))