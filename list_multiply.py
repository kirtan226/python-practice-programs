"""
Write a function to multiply every item in a list by two.
Return the updated list where each item is multiplied by two.
Example
input:[1, 2, 3, 4]
output:[2, 4, 6, 8]
Reason: The function multiplies each number in the list by two. The original list is [1, 2, 3, 4],
 and after multiplying each number by two we get [2, 4, 6, 8].

"""
def multiply_by_two(numbers):
    x=list(map(lambda x:x*2,numbers ))
    return x


print(multiply_by_two([2, 4, 6, 8, 10]))

