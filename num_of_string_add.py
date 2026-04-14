# Using the Python language, have the function NumberSearch(str) take the str parameter,
# search for all the numbers in the string, add them together, then return that final number.
# For example: if str is "88Hello 3World!" the output should be 91.
# You will have to differentiate between single digit numbers and multiple digit numbers like in the example above.
# So "55Hello" and "5Hello 5" should return two different answers. Each string will contain at least one letter or symbol.

import re

def NumberAddition(str):
    l=re.split(r'[^0-9]',str)
    print(l)

    num=[]
    total = 0

    for i in l:
        if i.isdigit():
            num.append(int(i))
            total+=int(i)
    # print(total)
    # print(num)
    return total


print(NumberAddition("hello55 h2oyou11"))