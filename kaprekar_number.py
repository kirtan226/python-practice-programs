"""
A Kaprekar number is a positive integer where the representation of its square can be partitioned into
two parts that add up to the original number.
For example, 9 is a Kaprekar number because 9^2 = 81, and 8 + 1 = 9.

input:45
output:True
Reason: The square of 45 is 2025. Splitting this into two parts gives us 20 and 25, which add up to give
        us back our original number, 45. Hence, it's a Kaprekar Number.

Input:297
Output:True

Input:46
Output:False
"""

# def is_kaprekar(n):
#
#     square =n**2
#     print(square)
#     new=list(str(square))
#     print(new)
#
#     l=(len(new)//2)
#     print("len",l)
#     part1=''
#     part2=''
#     for i in range(0,len(new)):
#         if i>=l:
#             part2+=new[i]
#             print("l2:",part2)
#         else:
#             part1+=new[i]
#             print("l1:",part1)
#     total = int(part1)+int(part2)
#     print(total)
#
#     return True if total==n else False
#
# print(is_kaprekar(297))

