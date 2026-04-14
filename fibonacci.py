'''
Write a function to get Fibonacci sequqnce.
The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it. Starting with 0 and 1, the sequence goes: 0, 1, 1, 2, 3, 5, 8, and so on.
1. Define a function that takes an integer as input.
2. Inside the function, use recursion to calculate the Fibonacci sequence up to the input number.
3. Return the Fibonacci sequence up to the input number.
Example

input:7
output:[0,1,1,2,3,5,8]

Input:10
Output:[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''

def fibonacci(ni):
    def fibo(n):
        if n <= 1:
            return n
        else:
            return fibo(n - 1) + fibo(n - 2)

    new=[]
    for i in range(ni):
        new.append(fibo(i))
    return new
n=int(input("Enter a number to print fibonacci sequence : "))
print(fibonacci(n))