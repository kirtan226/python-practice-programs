''' Write a function to find the first letter in a string that occurs only once.
Return an empty string if no such character exists.

Example
input:"Hello World"
output: "H"
Reason: In the stringappears only once'Hello World' ,ʼH' is the first character that

Input
Programming
output :P
'''

def single_occurrence(s):
    # d={}
    #
    # for i in s:
    #     if i in d:
    #         d[i]+=1
    #     else:
    #         d[i]=1
    # print(d)
    # new=[]
    # for key,value in d.items():
    #     if value == 1:
    #         new.append(key)
    # print(new)
    # return new[0]

    l=[]

    for i in s:
        if i in l:
            l.remove(i)
        else:
            l.append(i)

    return l[0]

print(single_occurrence("helloh"))