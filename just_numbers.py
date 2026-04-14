''' Write a function to extract all the numbers from a given string .
return None if no number found .

Input : 'hello123world456'
Output : '123456'

Input :'abc789xyz101112'
Output : '789101112'

Input :'noNumbersHere'
Output : None

Input : '123abc456def789'
Output :'123456789'
'''
def extract_numbers(s):
    number = ''
    for i in s:
        if i.isdigit():
            number += i
    return number if len(number) >= 1 else None


print(extract_numbers('abc789xyz101112'))
