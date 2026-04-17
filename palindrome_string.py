'''string=input("Enter any string:")
reversed_string=string[::-1]
print(f"reversed string of original is {reversed_string}")

if string==reversed_string:
    print(f"{string} is palindrome")
else:
    print(f"{string} is not pallindrome")
'''

def reverse(string):
    rev_string=string[::-1]
    print(f"reverse string is {rev_string}")

    if string == rev_string:
        print(f"{string} is palindrome")
    else:
        print(f"{string} is not pallindrome")

s=input("Enter a string to check pallindrome or not:")
reverse(s)

