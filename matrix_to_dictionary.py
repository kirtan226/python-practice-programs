''' Write a function to convert matrix into dictionary .
The dictionary keys should be the row indices and the values should be lists
containing the elements of each row.

Input :[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output :{0: [1, 2, 3], 1: [4, 5, 6], 2: [7, 8, 9]}
Reason: The function converts each row in the matrix to a list and adds it to the dictionary with its index
as key. The first row becomes {0: [1,2,3]}, second row becomes {1: [4,5,6]}, and third row becomes
{2: [7,8,9]}. These are combined to form one dictionary.

Input:[[10,11],[12,13]]
output:{0: [10, 11], 1: [12, 13]}

Input:[[14],[15],[16]]
output:{0: [14], 1: [15], 2: [16]}
'''

def matrix_to_dict(matrix):
    d = {}
    for i in range(0, len(matrix)):
        d[i] = matrix[i]
    return d

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_to_dict(l))
