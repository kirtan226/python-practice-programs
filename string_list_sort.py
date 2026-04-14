"""
Write a function to sort a list of strings by their length.
For this input
['apple', 'cherry', 'date']
output:['date', 'apple','cherry']
Reason: The lengths of the strings are 4, 5 and 6 respectively. Sorting them in ascending order gives ['date', 'apple', 'cherry').

"""

def sort_by_length(lst):
    lst.sort(key=len)
    return lst

    # """or"""
    # sort_list = sorted(lst,key=len)
    # return sort_list

l=['cat','elephant','wolf','horse']
print(sort_by_length(l))