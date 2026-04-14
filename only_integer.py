'''Write a function to filter out only the integers from a list.

Return the new list containing only integers.
input:[1, 'a', 2, 'b', 3]
output:[1,2, 3]
Reason: The integers in the input list are 1, 2, and 3. The function filters these
out and returns them in a new list.

Input:[4, 'c', 5, 'd', 6]
Output:[4, 5, 6]

'''

def filter_integers(lst):
    new=[]
    for i in lst:
        if isinstance(i  ,int ):
            new.append(i)

    return new

print(filter_integers([1, 'a', 2, 'b', 3]))