''' Write a function to filter all the string from the list .

Input:[1, 'a', 2, 'b', 3]
output:[1, 2, 3]

Input:[4,'f','g',5,'h']
output:[4, 5]

Input:['c', 'd', 'e']
output:[]
'''


def filter_strings(lst):
    return [i for i in lst if isinstance(i, (int, float))]


print(filter_strings([1, 'c', 6, 'd', 8, 'e', 20]))