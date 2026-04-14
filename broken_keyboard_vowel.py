"""The broken keyboard toggles the case of letters every time a vowel is pressed.
def type_with_broken_keyboard(word):
So, the case changes every time a vowel is encountered.
Return the string as typed by the keyboard.
Note: Assume that the keyboard starts from lowercase.

Example
input:'banana
output:bANanA
Reason: The word 'banana' starts with a lowercase. The first "A" toggles it to uppercase,
the second 'A' toggles it to lowercase and the final A toggles it to uppercase again.
The keyboard types 'bANanA'.

Input:'mississippi'
Output:mISSissIPPi

Input:'oooooooo'
Output:OoOoOoOo
"""


def type_with_broken_keyboard(word):
    new=''
    v = 'aeiou'
    word = word.lower()
    v_count=0
    for char in word:
        if char in v:
            v_count+=1

        if v_count%2==0:
            new =new+char.lower()
        else:
           new =new+char.upper()
    return new
word = input("Enter a Word : ")
print(type_with_broken_keyboard(word))


"""

___________FOR case change on only vowels__________
def type_with_broken_keyboard(word):
    new=''
    v='aeiou'
    word=word.lower()

    for char in word:
        if char in v:
            new = new+char.upper()

        else:
            new=new+char

    return new

word=input("Enter a Word : ")
print(type_with_broken_keyboard(word))
"""