''' Write a function to swap two character in a string .
1. Define a function that takes a string and two characters as input.
2. Inside the function, replace all occurrences of the first character with the
second, and vice versa.
3. Return the modified string.

Input:'hello world','h' , 'W'
Output: 'wello horld"
Reason: The function swaps all occurrences of 'h' with 'w' and vice versa in
the string 'hello world', resulting in 'wello horld'.

Input : 'abcd' ,'a', 'd'
Output : 'dbca'

Input :'1234567890', '1' ,'9'
Output : '9234567810'

Input : "hello world","a","w"
Output : 'hello aorld'
'''


def double_character_swap(text, char1, char2):
    new = ''
    for i in text:
        # print(i)
        if i == char1:
            new += char2
        elif i == char2:
            new += char1
        else:
            new += i

    print(new)

double_character_swap("hello world", "a", "w")
