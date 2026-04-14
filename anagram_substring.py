''' Write a function to check if a anagram of string is a substring of another string .
1. Define a function that takes two strings as input.
2. Inside the function, create all possible anagrams of the first string and check if any of them is a substring of the second string.
3. Return True if an anagram of the first string is a substring of the second string, otherwise return False.

Input :'abc', 'cbade'
Output :True
Reason: The string 'cba' is an anagram of 'abc' and it is a substring of 'cbade'. Therefore, the function returns True.

Input:'xyz' , 'zyxabc'
Output :True

Input: 'def', 'defghij'
Output :True

'''


def is_anagram_substring(s1, s2):
    new=s1[::-1]
    print(new)
    check =[]
    for i in new:
        if i in s2:
            check.append(i)

    a=''.join(check)
    print(a)

    if new == a:
        return True
    else:
        return False


print(is_anagram_substring('abc', 'cbade'))