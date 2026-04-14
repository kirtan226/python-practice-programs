''' Write a function to check if the number is ugly or not .

An ugly number is a positive integer whose prime factors only include 2, 3, and 5.
1. Define a function that takes an integer as input.
2. Return True if the number is ugly, otherwise return False.
Hint: Inside the function, continuously divide the number by 2, 3, and 5 until it cannot
be divided anymore. If the remaining number is 1, it's an ugly number

input:6
output:True
Reason: The prime factors of 6 are 2 and 3. Therefore, it's an ugly number
'''


def is_ugly(num):
    prime = [2, 3, 5]

    if num <= 0:
        return False
    else:
        for i in prime:
            while num % i == 0:
                num //= i

    return True if num == 1 else False

print(is_ugly(5))