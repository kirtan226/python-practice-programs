''' Write a function to find the symmetric difference of two sets .
Return the resulting set which is the symmetric difference of the input sets.
The symmetric difference of two sets is a set of elements which are in either of the sets but not in their intersection.

input:{1, 2, 3, 4},{3, 4, 5, 6}
output:{1, 2, 5, 6}
Reason: The elements 1 and 2 are only in the first set and 5 and 6 are only in the second set.
    Hence these four numbers form the symmetric difference.
'''


def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

symmetric_difference({1,2,3,4},{3,4,5,6})