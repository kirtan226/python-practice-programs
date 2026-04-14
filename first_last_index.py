'''Write a function to find the first and last index of a given element in a list.

Return a tuple containing the first and last index of the element in the list.

input:[1, 2, 3, 2, 4, 2] , 2
output:(1,5)
Reason: The number 2 appears at indices 1, 3, and 5. So its first index is 1 and its last index is 5.

Input:[5, 6, 7, 5, 8] , 5
Output:(0, 3)

Input:[9,10] , 10
output:(1,1)

Input:[11],11
Output:(0, 0)
'''

def first_last(lst, n):
    lst_index=[]
    for i in range(0,len(lst)):
        if lst[i]==n:
            lst_index.append(i)

    # print(index)
    return lst_index[0],lst_index[-1]

lst=[1, 2, 3, 2, 4,2]
n=2
print(first_last(lst, n))