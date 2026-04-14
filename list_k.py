"""Instructions
1. Define a function that takes a list of integers and a target number as inputs.
2. Inside the function, iterate over the list and keep track of the cumulative sum. If at any point, the cumulative sum equals the target or the cumulative sum minus an earlier sum equals the target, return True.
3. Return True if such sublist exists, otherwise return False.
Example
input:[23, 2, 4, 6, 7] , 6
output:True
Reason: The sublist [2, 4] has a sum equal to 6, which is the target number.

input:[1,2,3],5
output:True

Input :[1, 2, 3] ,7
output : False
"""
def check_sublist_sum(nums, k):
    for i in range(0,len(nums)):
        if nums[i]+nums[i-1]==k:
            return True
    return False
ls=[5,0,0]
k=0
print(check_sublist_sum(ls, k))

'''
"""The integer list and a number is entered , if at any point the sum of
 (i) and (i+1) is equals to (i+2) and only if (i+2) is equals to entered integer
 number then return True else return False
 Example:-
 input:[23,2,4,6,5,9] , k=6
 output:true
 reason : i=2 ,(i+1)=4 so (i)+(i+1)=6 which is (i+2) and also equals to k   """
def check_sublist_sum(nums, k):

    for i in range(0,len(nums)):
        if k in nums:
            if nums[i-1]+nums[i-2]==nums[i] and nums[i]==k:
                return True
    return False
   
ls=[1,2,3]
k=5
# print(check_sublist_sum(ls, k))

'''