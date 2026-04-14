"""Question: An array and a number A is given. Determine if any two numbers within the array sum to A."""

def twosum(arr,a):
    num=[]
    for i in range(0,len(arr)):
        sum = a- arr[i]
        # print(f"sum:{sum} , a={a},arr[i]={i} ,{arr[i]}")

        if sum in num:
            return True
        num.append(arr[i])
        # print(num)
    return False
arr=[1,5,8,9,5]
a=9
print(twosum(arr, a))