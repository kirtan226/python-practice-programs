""" Write a function to check if the number is both cubic and square .
Return True if the number is both a square and a cubic, otherwise return False.
input:64
output:True
Reason: The number 64 is both a perfect square (8*8) and a perfect cube (4*4*4).

Input:1
Output:True

Input:729
Output:True

Input:125
Output:False
"""

# import math
#
# a=int(round(math.exp(math.log(64)/3), 6))
# print(a)

# import math
# def is_cubic_square(n):
#     a=math.sqrt(n)
#     b=round(math.exp(math.log(n)/3), 6)
#     print(a)
#     print(b)
#     if a.is_integer() and b.is_integer():
#         return True
#     else:
#         return False
#
#
# print(is_cubic_square(65))


def is_cubic_square(n):
    square_root=int(n**(1/2))
    cubic_root = round(n**(1/3))

    return True if square_root ** 2 == n and cubic_root ** 3 == n else False

print(is_cubic_square(64))
