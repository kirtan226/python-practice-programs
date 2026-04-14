"""String Challenge
take the at parameter being passed, which will be a string containing letters
from the alphabet, and return a new string based on the following rules.
Whenever a capital M is encountered, duplicate the previous character (then remove the M),
and whenever a capital N is encountered remove the next character from the
string (then remove the N). All other characters in the string will be lowercase letters.
For example: "abcNdgM" should return "abcgg". The final string will never be empty.

Input: "MrtyNNgMM"
Output: rtyggg

Input: "oMoMkkNrrN"
Output: ooookkr                         """

def N_M_change(s):
    ch_1="M"
    ch_2="N"
    result=[]
    prev=None

    for char in s:
        if char.islower():
            result.append(char)
            prev=char

        elif char==ch_1:
            if prev:
                result.append(prev)

        elif char==ch_2:
            if prev:
                result.pop()

    return ''.join(result)


st= input("Enter a string :")
print(N_M_change(st))

