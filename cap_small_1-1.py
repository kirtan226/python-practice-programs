"""Write a function to convert a given string to Spongecase.
Spongecase is a style of text where letters alternately appear in lower and upper case.
For example, the word Spongecase in spongecase would be sPoNgEcAsE.

input :"programizpro123"
output:pRoGrAmTzPr0123

Input:learn to code
output:lEaRn To CoDe
"""

# def Spongecase(string):
#     new=''
#     for i in range(0 , len(string)):
#         if (i%2!=0):
#             new=new+string[i].upper()
#
#         else:
#             new =new+string[i].lower()
#
#     return new
# s=input("Enter a string :")

# print(Spongecase(s))
# s="hello"
# print(s[2])

def Spongecase(text):
    result = []
    i = 0
    for char in text:
        if char.isalpha():
            if i % 2 == 0:
                result.append(char.lower())
            else:
                result.append(char.upper())
            i += 1
        else:
            result.append(char)
    return ''.join(result)
s=input("Enter a string :")

print(Spongecase(s))