"""
Write a function to repeat the last character of a string n times.
Return the new string with the repeated character.
input:'hello' 3
output:'hellooo'
Reason: The last character of the string 'hello' is 'o'. Repeating it 3 times. gives 'ooo. Appending this to the original string gives 'hellooo.

Input:world' 2
Output:worlddd

Input:python' 4
Output:pythonnnnn
"""

def repeat_last_char(string, n):
    st= string[-1]
    # print(st)

    # return string[:-1]+st*3
    return string+st*n


s='python'
n=4
print(repeat_last_char(s, n))