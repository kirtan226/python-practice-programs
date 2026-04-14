"""Write a function to alter a list of numbers such that even numbers are halved and 1 is subtracted from odd numbers.
Example
input :[2, 3, 4, 5]
output :[1.0, 2, 2.0, 4]
Reason: The original list is [2, 3, 4, 5]. After altering: [1.0 (half of 2), 2 (3-1), 2.0 (half of 4), 4 (5-1)].

Input:[6, 7, 8] -- Output:[3.0, 6, 4.0]
Input :[9,10] --Output:[8, 5.0]
"""

def alter_numbers (numbers):
    new= []

    for i in range(0,len(numbers)) :
        if numbers[i]%2==0:
            new_num = float(numbers[i]/2)
            new.append(new_num)
        else:
            new_num =numbers[i]-1
            new.append(new_num)

    print(new)

alter_numbers ([2, 3, 4, 5])