''' Write a function to add two binary strings and return their sum as a binary string .
Input : "11" (3) , "1" (1)
Output: "100" (4)
reason : The binary representation of 3 is "11" and 1 is "1" , their sum is 4, which in binary is "100"

Input :'1010','1011'
Output : '10101'

Input : '1111' ,'1111'
Output :'11110'
'''


def add_binary(a, b):
    n1 = int(a,2)
    n2 = int(b,2)

    # print(n1 , n2)
    sum = n1+n2

    # print(bin(sum)[2:])
    return bin(sum)[2:]
add_binary('1010' , '1011')