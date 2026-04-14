'''Write a function to implement zig zag iterator in list .
- The zigzag iterator should take two 1D integer lists as input and return the
  elements alternately from each of the lists.

Input : [1,2] ,[3, 4, 5, 6]
Putput : [1, 3, 2, 4, 5, 6]
Reason: The zigzag sequence for the given inputs is: 1 (from first list), 3 (from
second list), 2 (from first list), 4 (from second list), then remaining elements
from second list as first list is exhausted.

Input ,[7,8],[9]
Output :[7, 9, 8]

Input : [],[10]
Output : [10]

Input : [11] ,[]
output : [11]
'''


def zigzag_iterator(list1, list2):
    new = []
    i = 0
    j = 0
    l1_len = len(list1)
    l2_len = len(list2)

    while i < l1_len or j < l2_len:
        if i < l1_len:
            new.append(list1[i])
            i += 1
        if j < l2_len:
            new.append(list2[j])
            j += 1
    return new


l1 = [7, 8]
l2 = [9]
print(zigzag_iterator(l1, l2))
