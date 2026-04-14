"""
Write a function to implement the Caesar Cipher.

This is a type of substitution cipher in which each letter in the plaintext is
'shifted' a certain number of places down the alphabet.and so on.

For example, with a shift of 1, A would be replaced by B, B would become C,
Keep in mind that Z should loop back to A and vice versa.
The function takes a string and an integer as inputs. eturn the encrypted string.
Hint: In this challenge, you should only consider uppercase letters.

input:'HELLO' 3
output:'KHOOR'
Reason: Each letter in 'HELLO' has been shifted three places to the right in the alphabet resulting in 'KHOOR:

Input:WORLD'2
Output:YQTNF

Input :PYTHON'5
Output:UDYMTS
"""

def caesar_cipher(text, shift):

    result= ''
    for char in text:
        if char.isalpha():
            key =65 if char.isupper() else 97
            result+= chr((ord(char) - key + shift ) %26 + key)
        else:
            result+=char
    return result