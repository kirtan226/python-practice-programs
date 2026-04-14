'''
Write a function to calculate the lowest common multiple (LCM) of two numbers.
The lowest common multiple (LCM) of two numbers is the smallest positive integer that is perfectly divisible by both numbers.
The formula to calculate LCM is
1cm(a, b) = abs(a*b) // gcd(a, b), where gcd() is the greatest common divisor of a and b.

Example
input:12,15
output:60

Input:5 ,7
Output:35

Input:8 ,9
Output:72
'''

import math
def calculate_lcm(num1, num2):
    return math.lcm(num1, num2)


print(calculate_lcm(5, 7))