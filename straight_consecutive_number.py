"""
Write a function to check if a number is a straight digital number.

A straight digital number is one where the difference between two consecutive digits is constant.

input:12345
output:True
Reason: The difference between each pair of consecutive digits in 12345 is 1, so it's a straight digital number.

Input:13579
Output:True

Input:24680
Output:False
"""

def is_straight_digital(n):
    new = str(n)
    order = True
    # print(len(new))
    difference = int(new[1])-int(new[0])
    for num in range(0,len(new)-1):
        if int(new[num+1])- int(new[num]) != difference:
            order =False
    return True if order else False
no = 24680
print(is_straight_digital(no))