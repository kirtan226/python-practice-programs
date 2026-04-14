''' Write a function to check if the number is composite or not
Return True if the number is composite, otherwise return False.
A composite number is any positive integer greater than one that is not a prime number.

input:4
output:True
Reason: The number 4 has three divisors: 1, 2, and 4. Therefore, it's a composite number.

Input:15
Output:True

Input:17
Output:False

Input:23
Output:False

Input:4
Output:True
'''

def is_composite(n):
    divisors_list=[]
    for i in range(1,n+1):
        if n%i==0:
            divisors_list.append(i)
    print(divisors_list)
    return True if len(divisors_list)>2 else False

print(is_composite(17))