'''Write a function to calculate the sum of all digits between two given numbers.
Return the sum of all digits between the two numbers(inclusive).

input:10 ,15
output:21
Reason: The numbers between 10 and 15 are 10, 11, 12, 13, 14, and 15. The sum of their digits is
(1+0) + (1+1) + (1+2) + (1+3) + (1+4) (1+5), which equals to 21.

Input:1 , 5
Output:15

Input:100 , 105
Output:21

Input:0 , 3
Output:6
'''


def sum_of_digits(start, end):
    sum=0
    for i in range(start , end+1):
        new=str(i)
        for i in new:
            for j in i:
                sum+=int(j)
    return sum



print(sum_of_digits(100, 105))