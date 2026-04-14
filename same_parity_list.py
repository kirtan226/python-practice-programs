''' Write a function to return a list that contains elements with the same parity (odd or even) as the first element of the list.
Example
input:[1, 2, 3, 4]
output:[1, 3]
Reason: The first number in the list is 1, which is odd. So, we include all other odd numbers from the list in our output. These are 1 and 3.

Input:[4, 5, 6, 7]
Output:[4, 6]
'''

def same_parity(numbers):
    # even=[]
    # odd=[]
    # if numbers[0]%2==0:
    #     # for i in numbers:
    #     #     if i%2==0:
    #     #         even.append(i)
    #     # return even

    # else:
    #     # for i in numbers:
    #     #     if i%2!=0:
    #     #         odd.append(i)
    #     # return odd

    if numbers[0] % 2 == 0:
        even = [i for i in numbers if i % 2 == 0]
        return even
    else:
        odd = [i for i in numbers if i % 2 != 0]
        return odd

print(same_parity([1, 2, 3, 4]))