''' Write a function to find the first character in a string that repeats .
Repeating character means the character that occurs more than once in a
string.
For example,
"racecar"
1.'r'
2.'a'
3.'c'
The character that repeats first is  "c" Similarly, in the string "programiz" the only character
that repeats is ʹrꞌ
Return the first repeating character from the given string s
If no repeating characters are found, return 'C'
the only character that repeats is
so it is considered as the first repeating character here.
Input: "programiz"
Output:"r"

input = "rotator"
output: 't'

Input = "ice"
output : "No repeating characters"

Input:'hello'
output :"l"

Input:'abcdefg'
Output : "No repeating characters"
'''


def first_repeating_char(s):
    repeat=[]
    for i in s:
        if i in repeat:
            return i
        elif i not in repeat:
            repeat.append(i)

    return "No repeating characters"


print(first_repeating_char("racecar"))
