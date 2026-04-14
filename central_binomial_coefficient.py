""" write a function to calculate central binomial coefficient for a given number

Return the central binomial coefficient of the input number.
The central binomial coefficient is defined as (2n choose n) = (2n)! / ((n!)^2), where n! denotes the factorial of n.

input:4
output:70
Reason: The central binomial coefficient for n=4 is calculated as (8 choose 4)=81/((41)^2) = 70.

Input:3
Output:20

Input:5
Output:252

"""
import math

def central_binomial_coefficient(n):
    # def fectorial_of_number(num):
    #     if num==0 or num==1:
    #         return 1
    #     else:
    #         return num*(fectorial_of_number(num-1))
    #
    # coefficeint = fectorial_of_number(2*n) / (fectorial_of_number(n)**2)
    # return int(coefficeint)

    result = math.factorial(2 * n) // (math.factorial(n) ** 2)
    return result
print(central_binomial_coefficient(5))