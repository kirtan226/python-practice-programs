'''Write a function to get the diagonals of a square matrix.
input:[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output:([1, 5, 9], [3, 5, 7])
Reason: The main diagonal of the matrix is [1, 5, 9] and the secondary diagonal is [3, 5, 7).
'''

# def get_diagonals(matrix):
#     front=[]
#     back = []
#     for i in range(3):
#         front.append(matrix[i][i])
#         back.append(matrix[i][2 - i])
#
#     return (front,back)
#
# l=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(get_diagonals(l))


def get_diagonals(matrix):
    front = []
    back = []
    for i in range(0, len(matrix)):
        front.append(matrix[i][i])

    for i in range(0, len(matrix)):
        back.append(matrix[i][2 - i])

    return(front , back)

l=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(get_diagonals(l))


# def get_diagonals(matrix):
#     front = []
#     back = []
#     for i in range(0, len(matrix)):
#         front.append(matrix[i][i])
#
#     matrix.reverse()
#     for i in range(0, len(matrix)):
#         back.append(matrix[i][i])
#     back.reverse()
#
# l=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(get_diagonals(l))
