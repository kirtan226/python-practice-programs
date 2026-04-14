"""
Enter string 1 : silent
Enter string 2 : listen
True

Enter string 1 : hello world
Enter string 2 : world hi
False

Enter string 1 : cinema
Enter string 2 : iceman
True
"""

def Anagram_Checker(str1,str2):
    s1=sorted(str1)
    s2=sorted(str2)

    if s1==s2:
        return True
    else:
        return False
str1=input("Enter string 1 : ")
str2=input("Enter string 2 : ")
print(Anagram_Checker(str1, str2))
