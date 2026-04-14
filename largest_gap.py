'''Write a function to find the largest gap between consecutive
numbers in a list.

For this input:[1, 3, 6, 7, 8]
the result should be:3
Reason: The largest gap in the sorted list is between 3 and 6, which is 3.

Input:[2, 4, 7, 9]
output:3

Input:[1, 3, 6, 7, 8]
output:3
'''


def largest_gap(numbers):
    # gap=[]
    # for i in range(0,len(numbers)):
    #     new = numbers[i] - numbers[i-1]
    #     gap.append(new)
    #
    # print( max(gap))

    return max([numbers[i]-numbers[i-1] for i in range(1,len(numbers))])


print(largest_gap([1, 3, 6, 7, 8]))