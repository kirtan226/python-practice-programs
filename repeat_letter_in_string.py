''' write a function to check if a string contains two consecutive identical letters .

Input:hello
Output:True
reason: in word "Hello" 'l' is repeating , Thus True

Input:world
Output:False

Input:goodbye
Output:True

'''

def has_consecutive_letters(s):
    new = ''
    repeat = ''
    for i in s:
        if i in new:
            repeat += i
        else:
            new += i

    return True if len(repeat) >= 1 else False
