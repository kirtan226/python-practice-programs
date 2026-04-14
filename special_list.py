'''Write a function to check if the list is special por not .
A list is special if every element at an even index is even and every element
at an odd index is odd.
Input : [2, 5, 4, 3, 6, 1]
Output : True
Reason: Here, every element at an even index (0, 2, 4) is even (2, 4, 6), and
every element at an odd index (1, 3, 5) is odd (5, 3, 1).

Input : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Output : False

Input : [2, 1, 4, 3, 6, 5]
Output : True

'''

def is_special(lst):
    for i in range(0, len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            return False
        elif i % 2 != 0 and lst[i] % 2 == 0:
            return False
        else:
            pass
    return True

is_special([2, 5, 4, 3, 6, 1])
