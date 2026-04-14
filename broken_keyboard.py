"""Write a function to check if a given string can be typed using a broken keyboard.
The broken keyboard can only type certain characters.
The function takes two strings as input. The first string represents the working keys,
and the second string is the word to be typed. Check if each character in the word is present in the working keys.
Return True if the word can be typed with the existing keys, otherwise, return False.
Input:'abc' 'bad'
Output:False

Input:abcdefg' 'bag
Output:True

Input:xyz''yzzx
Output:True

Input:mnop''pop
Output:True
"""

def key_check(keys ,word):
    # key_list=list(keys)
    # word_list=list(word)
    for item in word:
        if item not in keys:
            return False

    return True

keys=input("Enter working keys of keyboed : ")
word=input("Enter a word :")
print(key_check(keys, word))