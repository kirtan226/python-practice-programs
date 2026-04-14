"""Write a function to alidate triple function .
1. Define a function that takes three boolean values as input.
2. Inside the function, return True if all inputs are True, otherwise return
False.
3. Return a boolean value - True if all inputs are True, otherwise False .

input:True , True , True
output:True
Reason: All input values are true, so the function returns true.

Input:False,True ,True
Output :False

"""


def triple_function(a, b, c):

    if a==True and b==True and c==True:
        return True
    else:
        return False


print(triple_function(True, True, True))