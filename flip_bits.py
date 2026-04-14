'''Write a function to flip the bits of given number .
In binary representation ,fliping a bit means changing 1 to 0 and vice versa .

Input : 5 (101)
Output : 2 (010)

Input :15 (1111)
Output: 0 (0000)

Input : 10 (1010)
Output : 5 (0101)

Input : 20 (10100)
Output : 11 (01011)
'''


def flip_bits(n):
    new = ''
    a = bin(n)[2:]
    print(f"Binary of {n} :",a)
    for i in a:
        if i == '1':
            new += '0'
        else:
            new += '1'

    print('New Binary :',new)
    print("New Number :",int(new, 2))
    return int(new, 2)

flip_bits(200)