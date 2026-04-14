''' Write a function to check if number is harshed or not .
Return True if the number is a Harshad number, else return False.
A Harshad number in a given number base is an integer that is divisible by
the sum of its digits when written in that base.

Input:18
Output:True
Reason: The sum of digits of 18 is 9. Since 18 is divisible by 9, it's a Harshad number.

Input:12
Output :True

Input: 11
Output :False

Input:20
Output:True
'''


def is_harshad(n):
    s=str(n)
    sum=0
    for i in s:
        sum+=int(i)

    a=n/sum
    print(a)
    print(type(a))

    return True if a.is_integer() else False

n=25
print(is_harshad(n))