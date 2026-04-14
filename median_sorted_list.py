""" You write a function to find the median of two sorted lists .
1. Define a function that takes two sorted lists as input.
2. Inside the function, merge the two sorted lists into one and find the median.
3. Return the median of the merged list.
Hint: The median is the middle value in an ordered integer list. If the size of the
 list is even, there is no middle value and the median is the mean of the two middle numbers.
Example
For this input
[1, 3]
[2]
the output should be:
2.0
Ronson: The merged list is [1,2,3] and its median is 2

Input:[1, 2]  [3, 4]
Output:2.5
"""

def find_median(nums1, nums2):
    nums1.extend(nums2)
    sum = 0

    for i in range(0, len(nums1)):
        sum += nums1[i]

    return float(sum / len(nums1))

nums1=[i for i in range(1000,2000)]
nums2=[i for i in range(100,200)]
print(find_median(nums1, nums2))