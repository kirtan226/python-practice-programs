"""Write a function to move all the zeros in an integer to the end.
Return the resulting integer with all zeroes moved to the end.
Example
input : 1020304050
output : 1234500000
"""


def zero_end(numbers):
    s=str(numbers)
    new=[]
    new1=[]
    for i in s:
        if i=='0':
            new.append(i)
        else:
            new1.append(i)
    new1.extend(new)
    # return "zero:",new , "no 0:",new1

    return ''.join(new1)

n=int(input("Enter a number :"))
print(zero_end(n))
