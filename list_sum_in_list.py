'''writea function to find the smallest sublist with a sum grater than given value.
Return the length of smallest sublist whose sum is greater than a given value .

Input : [1,2,3,4,5] ,9
Output:2
Reason:The smallest sublist with the sum greater than 9 is [4,5] , which has length 2 .

Input:[1, 4, 2, 5, 3],8
Output:2

Input:[10,20],15
Output:1

Input:[2, 3, 1, 2, 4, 3],7
Output :2
'''

def smallest_sublist(lst, target_sum):
    temp = 0
    lst = sorted(lst, reverse=True)
    for i in range(len(lst)):
        temp = temp + lst[i]
        print(f"After {lst[i]} sum is {temp}")
        if temp >= target_sum:
            return i + 1
    return None

arr = [1, 2, 3, 4, 5]
target = 9
print(smallest_sublist(arr, target))