"""Write a function to find the product of a list except for the current Challenge List

Return a list where each element is the product of all other elements in the list except for itself.
If there's only one element, return an empty list.

input:[1, 2, 3, 41
output:[24, 12, 8, 6]
Reason: For each index in the list: 0, 1, 2, and 3, we calculate the product of every number except
this index. So for index 0, we have 2*3*4=24; for index 1, we have 1*3*4 12 for index 2, we have 1*2*48;
and finally for index 3, we have 1*2*3=6. So our final output is [24, 12, 8, 6].

Input:[10,20,30]
Output:[600, 300, 200]

Input:[5]
Output:[]
"""

from functools import reduce
def product_except_self(nums):
    if len(nums) == 0 or len(nums) == 1:
        return []

    product = reduce(lambda x,y:x*y,nums)
    # print(product)
    new =[]
    for i in nums:
        sum=product/i
        new.append(int(sum))

    return new

l = [1,2,3,4,5,6,7,8,9,10 ]
print(product_except_self(l))