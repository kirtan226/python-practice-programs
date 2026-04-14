'''
Instructions
1. Define a function hat takes a list of integers and an integer kas inputs.
2. Inside the function, calculate the sum for each subsequence of length k.
3. Return the maximum sum found.
Example
For this input:[1, 2, 3, 4, 5]  ,2
output:9
Reason: The subsequences of length 2 are [1,2], [2,3], [3,4], and [4,5].
        The subsequence with the largest sun is [4,5], which surns to 9.

Input:[6, 7, 8, 9]  ,3
Output:24

Input:[10, -2, -3, -4] ,1
Output:10
'''

def largest_sum_subsequence(numbers,k):
    numbers.sort(reverse=True)
    max=0
    for i in range(0,len(numbers)):
        if i<k:
            max+=numbers[i]

    return max


print(largest_sum_subsequence([1, 2, 20, 3, 10, 4, 30, 5], 3))