"""
The built-in Python functions int() and bin() can be used to convert between integers and binary strings.
input:*1010' '1011'
output:'10101'
Reason: The binary representation of 10 is '1010' and of 11 is '1011'. Their sum is 21, which in binary is '10101'.

Input:'111' '111'
Output:1110

Input:'100' '1000'
Output:1100
"""

def add_binary_strings(bin_str1, bin_str2):
   b1 = int(bin_str1,2)
   b2 = int(bin_str2,2)

   sum = b1+b2
   bi_sum=bin(sum)
   print(bi_sum[2:])

s1="1010"
s2="1011"
add_binary_strings(s1,s2)