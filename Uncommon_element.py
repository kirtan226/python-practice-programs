""" Write a function to find and return uncommon elements in a list of lists .
Input : [[1,2,3],[2,3,4],[4,5,6]]
Output : [1,5,6]

Input : [[7, 8], [8, 9], [9, 10]]
Output : [7, 10]

Input : [[11], [12], [13]]
Output : [11, 12, 13]

Input : [[14,15],[15],[14]]
Output : []
"""


def uncommon_elements(lists):
    l = []
    d = {}
    for i in lists:
        for j in i:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1

    for key, value in d.items():
        if value == 1:
            l.append(key)
    return l


print(uncommon_elements([[1, 2, 3], [1, 2, 3], [1, 0, 3]]))
