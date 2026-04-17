'''
- You have been tasked with analyzing an array of integers representing waiting times in a queue. Your goal is to identify
the longest strictly increasing consecutive segment within this array. A segment is considered strictly increasing if each element
is greater than the previous one. If multiple segments have the same maximal length, you should return the one that starts earliest
in the array.
- Write a function that receives an array of integers (waiting times) and returns a tuple containing two integers: the starting index
of the segment and the length of the longest strictly increasing consecutive segment. Indexing starts at 0. If the array is empty,
return (-1, 0). For an array of length 1, treat it as an increasing segment of length 1 starting at index 0.

-- Example 1 --
Input: [3, 5, 7, 2, 4, 5, 1, 2, 3, 4]
Output: (6, 4)
Explanation: The longest strictly increasing segment is [1, 2, 3, 4], which starts at index 6 and has a length of 4.

-- Example 2 --
Input: [10, 20, 30, 15, 16, 17, 12]
Output: (0, 3)

Explanation: There are two increasing segments of maximal length, one from index 0 to 2 ([10, 20, 30]) and another from
index 3 to 5 ([15, 16, 17]), both having length 3. Since the first segment starts earlier, the output is (0, 3).

Requirements:
The function should accept an array of integers representing waiting times. It must identify the longest strictly increasing
consecutive segment in the array and return a tuple containing the starting index and the length of that segment.
If multiple segments have the same maximum length, the one with the earliest starting index should be returned.
If the array is empty, return (-1, 0). The array length can range from 0 to 10,000, and each element in the array is an integer in
the range 0 to 600. The solution should be efficient and run in O(n) time, and no external libraries should be used.
'''

def solution(arr):
    if len(arr) == 0:
        return (-1, 0)

    max_start = 0
    max_length = 1

    current_start = 0
    current_length = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current_length += 1
        else:
            current_start = i
            current_length = 1

        # update max if needed
        if current_length > max_length:
            max_length = current_length
            max_start = current_start

    return (max_start, max_length)


# a = list(map(int, input("Enter a numer :").split()))
a = [3, 5, 7, 2, 4, 5, 1, 2, 3, 4]
print(solution(a))