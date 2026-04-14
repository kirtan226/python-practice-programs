""" take the str parameter being passed and return the string in reversed order.
For example: if the input string is "Hello World and Coders" then your program should
return the string sredoC dna dlroW olleH."""

'''Input: "coderbyte"
Output: etybredoc

Input: "I Love Code"
Output: edoC evoL I'''

def reverse(string):

    reverse_string=string[::-1]

    return reverse_string

s=input("Enter a string :")
print(reverse(s))