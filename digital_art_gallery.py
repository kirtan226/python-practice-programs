"""
- You manage a digital art gallery where paintings are displayed on a linear wall. Each painting has a unique
integer ID. Sometimes, art critics visit the gallery and provide a list of preferred painting IDs in arbitrary order.
Your task is to prepare an exhibition by displaying only those paintings whose IDs appear in the critics' preferred list,
and the final display must maintain the ascending order of the painting IDs.
- You are given an array gallery representing the IDs of paintings currently hung on the wall. The array is unsorted and contains
unique integers. You are also given an array preferred containing the critics' preferred painting IDs, which are also unique
integers and may be in any order. Your task is to return a new list of painting IDs that are present in both gallery and preferred,
sorted in ascending order.
- Input is provided in two lines. The first line contains space-separated integers representing the gallery. The second line
contains space-separated integers representing the preferred painting IDs. The output should be a single line of space-separated
integers that are common in both arrays and sorted in ascending order. If no common elements are found, print an empty line.

-- Example 1 --
Input:
7 2 5 10 3
10 2 3
Output:
2 3 10
Explanation: The painting IDs 2, 3, and 10 are present in both gallery and preferred.
After sorting them in ascending order, the result is 2 3 10.

-- Example 2 --

Input:
4 8 15 16 23
42 99

Output:      (Empty)
Explanation: There are no painting IDs common to both arrays, so the output is empty.

--- Example 3 ---
Input:
9 8 7 6 5
5 6 7
Output:
5 6 7

--- Example 4 ---
Input:
100 200 300 400
50 60 70

Output:      (Empty)

--- Example 5 ---
Input:
10 20 30 40 50
50 40 30 20 10
Output:
10 20 30 40 50


- Requirements:
The input should consist of two space-separated lines, the first representing the gallery and the second representing
the preferred IDs. The output must contain only those IDs that are present in both arrays, sorted in ascending order. All
IDs are unique and fall within the range of 1 to 100000. The length of the arrays satisfies 1 ≤ m ≤ n ≤ 10000. The solution should
be efficient and complete in O(n log n) time or better. Edge cases such as no common elements, all elements being common, or the
preferred list being smaller or equal to the gallery list must be handled correctly.

"""
# Optimized solution
def Solution(first, second):
    first = [int(i) for i in first.split()]
    second = [int(i) for i in second.split()]

    result = sorted(set(first) & set(second))

    return ' '.join(map(str, result))

# basic for beginner
# def Solution(first, second):
#     first = first.split()
#     second = second.split()
#
#     first = [int(i) for i in first]
#     second = [int(i) for i in second]
#
#     set_first = set(first)
#     set_second = set(second)
#
#     result = set_first.intersection(set_second)
#     result = sorted(list(result))
#
#     result = ' '.join(map(str, result))
#     return result


gallery = input("Enter gallery IDs: ")
preferred = input("Enter preferred IDs: ")

result = Solution(gallery, preferred)
print(result)