"""
1. Define a function that takes a string as input.
2. Inside the function, use recursion to compare the first and last characters
   of the string. If they are equal, call the function again with the string
   excluding the first and last characters. If they are not equal, return False.
   If all characters have been checked and are equal, return True.
3. Return True if the input string is a palindrome, otherwise return False.

Example
input:racecar
output :True
Reason: The word 'racecar' reads the same backwards as forwards, so it is a palindrome.

input:madam
output :True

input:python
output :false
"""

def is_palindrome(s):
    sl = list(s)
    sli = len(sl)
    sl_centre=len(sl)//2

    for i in range(0,len(sl)):
        if i == sl_centre:
            # print(f" pass  , {sl[i]}, {i} , {sl[-(i + 1)]} ,{-(i + 1)} even True")
            break

            # """ for check even and odd , but in this case not necessary """
            # if sli%2==0:
            #     # print("Even True")
            #     break                   # if i reched in centre and even length ,  break the loop
            # else:
            #     # odd string , so no need to check the last value
            #     # print(" odd True")
            #     break                   # if i reched in centre and odd length ,  break the loop

        else :
            if sl[i]==sl[-(i+1)]:       # if first and last is same ,pass
                # print(f" pass  , {sl[i]}, {i} , {sl[-(i + 1)]} ,{-(i + 1)} even True")
                pass
            else:                       # if first and last is not same ,return false
                return False
    return True
s=input("Enter a string : ")
print(is_palindrome(s))
