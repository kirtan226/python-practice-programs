"""
Write a function to find the longest sequence of consecutive zeros in a binary string.

input:101001000100001
output:4
Reason: The longest sequence of consecutive zeros in the binary string '101001000100001' is '0000', which has a length of 4.

Input:11111111
Output:0

"""

def longest_zero_sequence(binary_string):
    max_count = 0
    frequency = 0
    for i in binary_string:
        if i=='0':
            frequency+=1
            if frequency>max_count:
                max_count=frequency
        else:
            frequency=0
    return max_count


print(longest_zero_sequence('1010010001000'))
