"""
The standard form is defined as a sentence with the first letter of each word
capitalized and all other letters in lowercase.

Example
input :'this IS A test sentence'
output:'This Is A Test Sentence'

Reason: The function capitalizes the first letter of each word and converts all
other letters to lowercase. Thus, 'this IS A test sentence' becomes 'This Is A Test Sentence'.

Input: hELLO wORLD
Output: Hello World
"""

def standard_form(sentence):
    a=sentence.lower()
    l=a.split()
    new=[]
    for char in l:
        new.append(char.title())
    return ' '.join(new)

string = "this IS A test sentence"
print(standard_form(string))