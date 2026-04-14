'''
Write a function to check if a list is balanced or not.
Instructions
A list is considered balanced if the sum of the first half of the list is equal to the sum of the second half.

input:[1, 2, 3, 3, 2, 1]
output:True
Reason: The sum of the first half [1, 2, 3] is 6 and the sum of the second half [3, 2, 1] is also 6.

Input:[1, 2, 3, 4, 5]
Output:False

Input:[2, 2, 2, 2]
Output:True
'''

def is_balanced(lst):
    first_sum=[]
    second_sum=[]
    a= len(lst)/2
    for i in range(0,len(lst)):
        if len(lst)%2==0:
            for i in range(0,len(lst)):
                if i >=a:
                    second_sum.append(lst[i])
                    # print('first lst : ',second_sum)
                else:
                    first_sum.append(lst[i])
                    # print('second list :',first_sum)
            sum_first = sum(first_sum)
            sum_second = sum(second_sum)
            # print(f"First sum : {sum_first} and Second sum : {sum_second}")
            return True if sum_first==sum_second else False

        else:
            return False


print(is_balanced([1, 2, 3, 3, 2, 0]))


