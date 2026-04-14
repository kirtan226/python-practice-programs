''' Write a function to return indices of the two that add up to a target number .
The indices should be returned in ascending order.
1. Define a function that takes a list of integers and an integer as inputs.
2. Inside the function, find two numbers in the list that add up to the target.
3. If found, return their indices in ascending order.
Assume there are no multiple combinations.

input:[2, 7, 11, 15], 9
output:[0, 1]
Reason: The numbers 2 and 7 add up to 9. Their indices are 0 and 1, respectively.

Input:[3, 2, 4],6
Result:[1, 2]

Input:[3, 3],6
Result:[0, 1]

Input:[-1,-2,-3,-4,-5], -8
Your Result:[2, 4]


'''

def two_sum(nums, target):
    lst =[]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                lst.append(i)
                lst.append(j)
    return lst

print(two_sum([2, 7, 11, 15], 9))