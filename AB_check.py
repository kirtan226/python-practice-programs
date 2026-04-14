# Using the Python language, have the function ABCheck(str) take the str parameter being passed and
# return the string true if the characters a and b are separated by exactly 3 places anywhere in the string at least once
# (ie. "lane borrowed" would result in true because there is exactly three characters between a and b). Otherwise return the string false.

def ABCheck(str):

    list1=list(str)
    l=len(str)

    for i in range(l):
        if list1[i]=="a":
            if l-i>=4:
                if list1[i+4]=="b":
                    return "true"

        elif list1[i]=="b":
            if l-i>=4:
                if list1[i+4]=="a":
                    return "true"

    return "false"

print(ABCheck("lane borrowed"))