""" Write a function to check if a number is deficient
A number is deficient if the sum of its proper divisors is less than the number itself.
Return True if the number is deficient, False otherwise.

input:12
output:False
Reason: The proper divisors of 12 are 1, 2, 3, 4, and 6. Their sum is 16, which is greater than 12.
        Therefore, 12 is not a deficient number.

Input:15
Output:True

Input:6
Output:False

Input:10
Output:True
"""
def is_deficient(n):
    divisors_list=[]
    for i in range(1,n):
        if n%i==0:
            divisors_list.append(i)
    print(divisors_list)

    # a=sum(divisors_list)
    # print(a)

    return True if sum(divisors_list)<n else False


number =int(input("enter a number :"))
print(is_deficient(number))