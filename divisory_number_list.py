"""
Write a function to find all the divisors of a given number.
Return a list of all divisors of the input number.

input:12
output:[1, 2, 3, 4, 6, 12]
Reason: The numbers 1, 2, 3, 4, 6, and 12 are all divisors of 12.

Input:7
Output:[1, 7]

"""

def find_divisors(n):
    divisors_list=[]
    for i in range(1,n+1):
        if n%i==0:
            divisors_list.append(i)
    return divisors_list


print(find_divisors(100))