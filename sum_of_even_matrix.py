''' Write a function to calculate the sum of all even numbers in a matrix .
input =[[1,2,3],[4,5,6],[7,8,9]]
output=20
Reason = sum of even number 2+4+6+8=20

Input:[[2, 4], [6, 8]]
Output:20

Input:[[10, 15], [20, 25]]
Output:30
'''

def sum_of_evens(matrix):
    sum=0

    for i in matrix:
        for j in i:
            if j%2==0:
                sum+=j
    return sum

print(sum_of_evens([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))