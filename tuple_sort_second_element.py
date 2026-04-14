""" Write a function to sort a tuples based on second item in each tuple .
Input : (('a', 3), ('b', 2), ('c', 1))
Output : [('c', 1), ('b', 2), ('a', 3)]

Input : (('d', 4), ('e', 3), ('f', 6))
Output : [('e', 3), ('d', 4), ('f', 6)]

Input : (('g', 9), ('h', -8), ('i',7))
Output : [('h', -8), ('i', 7), ('g', 9)]

Input : (('j',0),('k',0))
Output : [('j', 0), ('k', 0)]

"""


def sort_tuples(tuples):
    l = list(tuples)
    print(l)

    new = sorted(l, key=lambda x: x[1])
    return new


t = (('a', 3), ('b', 2), ('c', 1))
print(sort_tuples(t))
