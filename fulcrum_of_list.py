'''Write a function to find the fulcrum of a list.
The fulcrum of a list is an integer such that all elements to the left and all
elements to the right sum to the same value.
If no fulcrum exists, return None

input:[3, 7, 2, 4, 6]
output:2
Reason: In this list, 2 is the fulcrum because4 + 6 =10 and , 3 +7=10

Input:[7, -1, 0, -1, 7]
output:0

Input:[9, 3, -4]
output:None

Input:[8, 8, 8]
output:8
'''


def find_fulcrum(lst):
    l= len(lst)//2
    print(l)

    # left , right = lst[:l] ,lst[l+1:]
    # l_sum =sum(left)
    # r_sum = sum(right)
    #
    # return lst[l] if l_sum==r_sum else False

    l_sum=0
    r_sum=0
    for i in range(0,len(lst)):
        if i>l:
            print(lst[i])
            r_sum+=lst[i]
        elif i<l:
            print(lst[i])
            l_sum+=lst[i]
    print(l_sum , r_sum)
    return lst[l] if l_sum==r_sum else None


print(find_fulcrum([3, 7, 2, 4, 6]))