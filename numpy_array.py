import numpy as np
"""
(1) Equal Spacing Check (linspace logic)
- Given start, end, and num, create an array using NumPy and return the step difference between elements.

Input :
start = 2
end = 10
num = 5

Output :
[2. 4. 6. 8. 10.]
Step = 2.0
"""
print("============== Question : 1 ==============")
# start = 2
# end = 10
# num = 5
# question_1 = np.linspace(start, end, num)
# print(question_1)

class GenerateArray:
    def question_1(self, start, end, num):
        question_1_ans = np.linspace(start, end, num)
        return question_1_ans

start = int(input("Start: "))
end = int(input("End: "))
num = int(input("Number: "))
ans_1 = GenerateArray().question_1(start, end, num)
print(ans_1)


"""
(2) Reshape + Indexing Combo

Create a NumPy array from 1 to 12, reshape it into (3,4), then:

Print 2nd row
Print last column
Print element at position (2,3)

Output : 
Matrix:
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]

Second row: [5 6 7 8]
Last column: [ 4  8 12]
Element (2,3): 12

"""
print("============== Question : 2 ==============")

array = np.arange(1,13).reshape(3,4)
print(f"Matrix:\n",array)

print("Second row", array[1])
print("Last column", array[:,3])

print("Element (2,3):",array[2,3])

"""
(3) Given an array, add 5 to all elements, then multiply result by 2.
Input:
np.array([1, 2, 3, 4])

Output : After adding 5: [6 7 8 9]
Final result: [12 14 16 18] 

"""
print("============== Question : 3 ==============")

array3 = np.array([1, 2, 3, 4])
after_add = array3 + 5
print(f"After adding 5: {after_add}")
multiply = after_add*2
print(f"After multiply: {multiply}")

"""
(4) From given dataset, filter only values greater than mean.

Input: arr = np.array([10, 20, 30, 40, 50])

Output : 
Mean = 30
Filtered Output: [40 50]

"""
print("============== Question : 4 ==============")

array4 = np.array([10, 20, 30, 40, 50])
mean_of_array = array4.mean()
print(f"Mean: {mean_of_array}")
greater_than_mean = array4[array4 > mean_of_array]
print(f"Greater than: {greater_than_mean}")


"""
(5) Multiply two matrices using NumPy.

"""
print("============== Question : 5 ==============")
n1 = np.arange(1,5).reshape(2,2)
n2 = np.arange(11,15).reshape(2,2)

print(f"n1: {n1}")
print(f"n2: {n2}")

n3 = np.dot(n1, n2)
print(f"n3: {n3}")


"""
(6) Given input features and weights, compute prediction.


(6.1)
Input:
data = np.array([[1, 2],
                 [3, 4]])

weights = np.array([10, 20])

Output = [50 110]

(6.2)
Input:
data = np.array([10, 20])

weights = np.array([[1, 2],
                 [3, 4]])

Output = [ 70 100]

"""

print("============== Question : 6.1 ==============")
data = np.array([[1, 2],
                 [3, 4]])

weights = np.array([10, 20])

prediction = np.dot(data, weights)
print(f"Prediction: {prediction}")

print("============== Question : 6.2 ==============")
data = np.array([10, 20])

weights = np.array([[1, 2],
                 [3, 4]])


prediction = np.dot(data, weights)
print(f"Prediction: {prediction}")