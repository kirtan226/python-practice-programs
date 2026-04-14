'''Write a function to check if a given string is in spongecase.
If the case of each character alternates between upper and lower case, it is in spongecase.
Return True if the string is in spongecase, otherwise return False.

input:'SpOnGeCaSe'
output:True
Reason: The input string 'SpOnGeCaSe' alternates between upper and lower case letters, so it is in spongecase.
'''

def is_spongecase(s):
    new = list(s)
    check = []

    if new[0].isupper():
        for i in range(0, len(new)):
            if i % 2 == 0 and new[i].isupper():
                check.append(new[i])
            elif i % 2 != 0 and new[i].islower():
                check.append(new[i])

    if new[0].islower():
        for i in range(0, len(new)):
            if i % 2 != 0 and new[i].isupper():
                check.append(new[i])
            elif i % 2 == 0 and new[i].islower():
                check.append(new[i])

    return True if new == check else False

print(is_spongecase('SpnGeCaSe'))