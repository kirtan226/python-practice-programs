""" read the array of strings stored in strArr which will contain 2 elements: the first element
will represent a list of comma-separated numbers sorted in ascending order, the second element
will represent a second list of comma-separated numbers (also sorted). Your goal is to
return a comma-separated string containing the numbers that occur in elements of strArr in sorted order.
If there is no intersection, return the string false."""
"""Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
   Output: 1,4,13
   
   Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
   Output: 1,9,10 pip"""

def find_intersection(arr):
    set1=list(map(int,arr[0].split(',')))
    # print(set1)

    set2=list(map(int,arr[1].split(',')))
    # print(set2)

    intersection=[]
    for i in set1:
        if i in set2:
            intersection.append(i)

    if len(intersection)==0:
        print("False")
    else:
        pass

    convert_to_int=','.join(map(str,intersection))
    print(convert_to_int)

l=["4,5,8","8,7,1,2"]
find_intersection(l)