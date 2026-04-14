"""
Write a function to calculate the sum of the harmonic series up to a given number.
Return the sum of the harmonic series rounded off to two decimal places.
Hint: The harmonic series is defined as '1+ 1/2 + 1/3 + 1/4 +....+ 1/п ' .

input:5
output:2.28
Reason: The sum of the first five terms of the harmonic series is 2.28. This is calculated as
follows : 1+ 1/2 + 1/3 + 1/4 + 1/5 = 2.28

Input:4
Output:2.08
"""

def harmonic_sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=float(1/i)
        # print(i , 1/i)
        # print(sum)

    return round(sum,2)

n = int(input(" Enter a number :"))
print(harmonic_sum(n))