"""def max(num):
    maximum=num[0]
    for num in num:
        if num>maximum:
            maximum=num
    return maximum

l=[4,5,8,20,45,9,8,24,65,72,3,49,10,54,56,61,47,85,91,97,72,46,40,68]
maximum_num=max(l)
print(f"maimum number in list is:",maximum_num)
"""

l=[2,5,7]
l.sort(reverse=False)
print(l)
sum=0
for i in l:
    sum =sum +i
print("sum of list:",sum)