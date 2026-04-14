"""
Given a string , the task is to convert the string into an integer

Example :
Input : three hundred million
Output : 300,000,000

Input : five hundred thousand
Output : 500,000
"""

def string_to_int(a):
    number = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'hundred': 100,
        'thousand': 1000,
        'million': 1000000,
        'billion': 1000000000,
        'trillion': 1000000000000
    }

    st = a.split(' ')
    print(st)

    value = []
    num = 0
    for i in st:
        print("st of i" , i)
        if i in number:
            value.append(number[i])
            print("value",value)
        else:
            print(f"Not found {i}")

    print( "final value ",value)
    new_int = 1
    for i in value:
        print(f"{new_int}*{i}={new_int}")
        new_int *= i
    return f"Converted Integer value is : {new_int}"

a = input("Enter string to convert into integer value : ")
print(string_to_int(a))