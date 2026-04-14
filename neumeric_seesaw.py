"""
Write a function to create a numeric seesaw.
For an integer as input, return a list of numbers from 1 to that number and then back down to 1.

input:5
output:[1, 2, 3, 4, 5, 4, 3, 2, 1]
Reason: The function returns numbers from 1 up to the input number 5, then back down to 1. Hence, the output is '123454321.

Input:3
Output:[1, 2, 3, 2, 1]

Input:7
Output:[1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
"""

def numeric_seesaw(n):
    new=[]
    for i in range(1,n+1):
        new.append(i)
        if i==n:
            for i in range(n - 1, 0, -1):
                new.append(i)
    return new

    # for i in range(n-1,0,-1):
    #     new.append(i)
    # return new

n=7
print(numeric_seesaw(n))