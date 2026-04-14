''' Write a function to calculate the digit distance between two integers .
1. Define a function that takes two integers as input.
2. Inside the function, convert the integers to strings, and for each corresponding pair of digits in the two strings, calculate the absolute difference.
3. Return the sum of all these differences.

input:12345,54321
output:12
Reason: The digit distances are 4, 2, 0, 2, and 4. Their sun is 12.

Input:11111,22222
Output:5

Input:33333,77777
Output:20

Input:99999 ,11111
Output:40
'''


def digit_distance(num1, num2):
    # # Convert both integers to strings
    # str1 = str(num1)
    # str2 = str(num2)
    #
    # # Make sure both strings have the same length by padding the shorter one with zeros
    # max_len = max(len(str1), len(str2))
    # str1 = str1.zfill(max_len)
    # str2 = str2.zfill(max_len)
    #
    # # Calculate the sum of absolute differences between corresponding digits
    # distance_sum = sum(abs(int(d1) - int(d2)) for d1, d2 in zip(str1, str2))
    # return distance_sum

    a = str(num1)
    b = str(num2)
    result = 0
    for i in range(len(a)):
        result += abs(int(a[i]) - int(b[i]))
    return result

print(digit_distance(12345,54321))