'''Write a function to check if a list contains three consecutive common numbers.

input:[1, 2, 2, 2, 3]
output:True
Reason: The list contains three consecutive 2s.

Input:[3, 3, 3]
output:True

Input:[4,5,6]
output:False

Input:[7, 7, 8, 8, 9, 9]
output:False
'''


def check_consecutive_numbers(numbers):
    d = {}
    for i in numbers:
        d[i] = numbers.count(i)
    print(d)
    for value in d.values():
        print( value)
        if value >= 3 in d :
            return True
    return False

print(check_consecutive_numbers([1, 2, 2, 2, 3]))