"""have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word.
Words will be separated by only one space."""

def up_string(s):

    for char in s:
        if s[0].isupper():
            return s
        else:
            return s[0].upper()+s[1:]

st=input("Enter a string :")
print(up_string(st))


"""If we have to convert first letter of every word in capital then use title() method"""
# str=s=input("Enter a text :")
# cap_str=str.title()
# print(cap_str)