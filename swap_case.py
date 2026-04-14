"""The SwapCase function you provided is a Python program designed to swap
the case of each character in a given string. That is, it converts uppercase characters
to lowercase and lowercase characters to uppercase."""
#ex: input:AbCdeFg , output:aBcDEfG

def swapcase(str):
    l=[]

    for char in str:
        if char.isupper():
            l.append(char.lower())
        elif char.islower():
            l.append(char.upper())

    return ''.join(l)

s=input("Enter a string : ")
print(swapcase(s))