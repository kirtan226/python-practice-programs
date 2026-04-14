''' Write a function to count the number of zeros in the binary representation of a given number.

Return the count of zeros in the binary representation of the input number.
Input : 18
Output : 3
Reason: The binary representation of 18 is 10010 , which contains 3 zeroes.

Input: 16
Output: 4

Input: 32
Output: 5

Input: 64
Output: 6
'''


def count_zeroes(n):
    b = str(bin(n))
    # print(b)

    zero='0'
    count=0

    for i in range(2,len(b)):
        # print(b[i])
        if b[i]==zero:
            count+=1
    return count

print(count_zeroes(200))