"""Write a function to sort a string in ginorts order.
Instructions
In ginorts, all sorted lowercase letters are ahead of uppercase letters, all sorted uppercase
letters are ahead of digits, and all sorted odd digits are ahead of sorted even digits.Return the sorted string.
FORMULA : <sorted_lower> <UPPER> <odd(1,3)> <even(2,4)>
Example

input : Sorting1234
output : ginortS1324

Input :PythonRules56
Output :ehlnostuyPR56

Input:HelloWorld1234
Output:dellloorHW1324

Input:Hackathon2021
Output:aachknotH1022

Reason: in the output, all lowercase letters are sorted and placed first,
followed by sorted uppercase letters, then odd digits, and finally even digits.
Hence, Sorting becomes ginort'S+13+24' 'ginort513241
"""


def ginortS(s):
    upper = []
    lower = []
    even = []
    odd = []
    zero = []
    for char in s:
        if char.isupper():
            upper.append(char)
        elif char.islower():
            lower.append(char)
        elif char.isdigit():
            if int(char) % 2 == 0:
                even.append(char)
            else:
                odd.append(char)
        elif char == '0':
            zero.append(char)

    lower.sort()
    upper.sort()
    even.sort()
    odd.sort()
    return ''.join(lower+upper+odd+zero+even)

s = "Hackathon2021"
print(ginortS(s))