''' Write a function to calculate the maximum value using '+' or '*' sign
between two numbers in a string.

Return the maximum value that can be obtained by either adding or
multiplying two numbers in the string.

Example
input:'3 4'
output:12
Reason: The two numbers in the string are 3 and 4. The maximum value that
can be obtained by either adding(7) or multiplying(12) these numbers is 12.

Input:5 6
Result:30

Input:7 8
Result:56

'''

def max_value(s):
    add=0
    mul=1
    new=s.split(' ')
    # print(new)
    for i in new:
        add+=int(i)
        mul*=int(i)

    return add if add>mul else mul


print(max_value('9 10'))