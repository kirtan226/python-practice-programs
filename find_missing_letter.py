"""Write a function to find the missing letter in a given string of consecutive alphabets.

input::'abcdfg'
output:"e"
Reason: The input string is 'abcdfg'. The letter 'e' is missing from this sequence of alphabets.

"""

def find_missing_letter(s):
    # s_list=[]
    # missing=0
    # for i in s:
    #     print(i , ord(i))
    #     s_list.append(ord(i))
    # start=s_list[0]
    # end=s_list[-1]
    # new=[]
    # for i in range(start ,end+1):
    #     new.append(i)
    # print(s_list)
    # print(new)
    #
    # if s_list == new:
    #     return None
    # else:
    #     for i in new:
    #         if i not in s_list:
    #             missing+=i
    #
    #
    #     print(missing)
    #     print(chr(missing))
    #     return chr(missing)
    #

    for i in range(1,len(s)):
        if ord(s[i]) - ord(s[i-1]) > 1: return chr(ord(s[i-1]) + 1)


print(find_missing_letter('abcdfg'))