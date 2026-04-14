# Using the Python language, have the function ArrayAdditionI(arr) take the array of numbers stored in arr
# and return the string true if any combination of numbers in the array ca be
# added up to equal the largest number in the array, otherwise return the string false.
# For example: if arr contains [4, 6, 24, 10, 1, 3] the output should return true
# because 4 + 6 + 10 + 3 +1 = 24. The array will not be empty, will not contain all
# the same elements, and may contain negative numbers

def array(l):

    l.sort()
    largest=l.pop()
    # print(l)
    # print(largest)
    total=sum(l)
    # print(total)

    if total==largest:
        return "True"
    else:
        return "false"

a=[4,6,24,10,1,3]
print(array(a))
