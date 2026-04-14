"""Array Challenge
take the array of numbers stored in azz and return the string "Arithmetic" ,
if the sequence follows an arithmetic pattern or return "Geometric" if it
follows a geometric pattern. If the sequence doesn't follow either pattern return -1.
An arithmetic sequence is one where the difference between each of the numbers is
consistent, where as in a geometric sequence, each term after the first is multiplied
by some constant or common ratio.
Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54].
Negative numbers may be entered as parameters, O will not be entered, and no array will contain all the same elements.

Input: [5,10,15]
Output: Arithmetic

Input: [2,4,16,24]
Output: -1                          """

def array(arr):
    arith, geo = True, True
    arithmetic_difference=arr[1]-arr[0]
    geomatric_difference=arr[1] / arr[0]

    for num in range(1, len(arr) - 1):
        if arr[num + 1] - arr[num] !=arithmetic_difference :
            arith = False
        if arr[num + 1] / arr[num] !=geomatric_difference :
            geo = False
    return "Arithmetic" if arith else "Geometric" if geo else -1

arr=[2,4,16,24]
print(array(arr))


# a=255
# b=64
# c=a/b
# print(c)
# print(type(c))