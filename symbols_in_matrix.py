'''Write a function to add the values of symbols in a matrix.
The matrix will contain numbers and symbols, where '+' represents addition, represents subtraction,
'*' represents multiplication and '/' represents division.
1. Define a function that takes a 2D list (matrix) as input.
2. Inside the function, iterate over each element in the matrix. If it's a number, add it to the total.
 If it's an operator symbol, perform the corresponding operation on the total.
3. Return the final result after performing all operations.

input:[[1, '+', 2], ['', 3], ['*', 2]]
output:0
Reason: The function starts with 1, adds 2 (resulting in 3), subtracts 3 (resulting in 0) and then multiplies
        by 2. The final result is 0.

Input:[[5, '*', 2], ['+', 3], ['-', 1]]
Output:12

Input:[[10, '/', 2], ['+', 5]]
Output:10.0
'''

def add_matrix_values(matrix):
    result = 0
    current = '+'
    for i in matrix:
        for j in i:
            if isinstance(j, (int, float)):
                if current == '+':
                    result += j
                elif current == '-':
                    result -= j
                elif current == '*':
                    result *= j
                elif current == '/':
                    if j != 0:
                        result /= j
                    else:
                        return "Error"
            elif j in ['+', '-', '*', '/']:
                current = j
    return result
l=[[1, '+', 2], ['-', 3], ['*', 2]]
print(add_matrix_values(l))