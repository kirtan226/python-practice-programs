'''
Write a function to rearrange a string in sorted order of alphabets
followed by the sum of integers.

input:'dcba4321'
the result should be:'abcd10'
Reason: The alphabets in sorted order are 'abcd' and the sum of numbers is 10. Therefore, the output is 'abcd10'.

Input : 'gfed7654'
Output : 'defg22'

Input :'zyxw9876'
Output : 'wxyz30'

Input :'lkji1111'
Output :'ijkl4'
'''


def rearrange_string(s):
    character = []
    numbers = 0
    l = list(s)
    # print(l)

    for i in range(0, len(l)):
        if l[i].isalpha():
            # print("alpha", l[i])
            character += l[i]
            character.sort()

        if l[i].isnumeric():
            # print("number", l[i])
            numbers += int(l[i])

    character.append(str(numbers))
    return ''.join(character)


st = 'yknamacnposkndcuierknvkernrvirejk4554121346451454845484843'
print(rearrange_string(st))
