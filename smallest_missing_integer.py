""" Write a function to find the smallest missing positive integer from a list.

input:[3, 4, -1, 1]
output:2
Reason: After sorting the list, we get [-1, 1, 3, 4]. The smallest missing positive integer is 2.

Input:[1, 2, 0]
Your Result :3

Input:[7, 8, 9, 11, 12]
Your Result :1

Input:[-10,-20,-30]
Your Result :1

"""


def find_missing(numbers):
    # numbers.sort()
    # # print(numbers)
    #
    # new = [i for i in numbers if i > 0]
    # print(new)
    # smallest = 1
    # if smallest in new:
    #     for i in range(0, len(new)):
    #         if i > 0:
    #             print("if i > 0")
    #             current = new[i]
    #             print("current",current)
    #             previous = new[i] - 1
    #             print("previous",previous)
    #             next =current+1
    #
    #             if previous >= new[0] and previous not in new:
    #                 print('missing',previous)
    #                 return previous
    #             else:
    #                 return next
    # else:
    #     return smallest

    num = 1
    while num in numbers:
        num += 1
    return num
print(find_missing([1, 2, 0]))
