'''
Write a function to generate the first n terms of the Empty Square Sequence .

Instructions
1. Define a function that takes an integer n as input.
2. Inside the function, calculate the nth term of the sequence by subtracting the square of n from the
   square of (n+1).
3. Return a list containing the first n terms of the sequence.
Hint: The Empty Square Sequence is defined as follows: The nth term is obtained by subtracting the square of n from the
square of (n+1). For example, for n=1, we have (2^2-1^2) = 3. For n=2, we have (3^2 -2^2) = 5. And so on.

input:5
output:[3, 5, 7, 9, 11]
Reason: The first five terms of the Empty Square Sequence are calculated
as follows:
For n=1: (2^2-1^2) = 3
For n=2: (3^2-2^2) = 5
For n=3: (4^2-3^2) = 7
For n=4: (5^2-4^2) = 9
For n=5: (6^2-5^2) = 11

Input:6
Output:[3, 5, 7, 9, 11, 13]

Input:10
Output:[3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
'''

def empty_square_sequence(n):
    new=[]
    for i in range(1,n+1):
        if len(new)==n:
            break
        a = ((i+1)**2 - i**2)
        new.append(a)
    return new

print(empty_square_sequence(5))