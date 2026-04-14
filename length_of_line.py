''' Write a function to calculate the length of line segment joining two given points .
1. Define a function which takes in two arguments point1 and point2 .
2. Inside the function calculate the length of the line segment joining point1 and point2
Input : (15 , 7), (22 , 11)
Output : 8.06
Note: Round off the result to two decimal places.

Input : (0,0) ,(1, 1)
Output : 1.41
'''

import math
def calculate_line_length(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    print(x1, x2)
    print(y1, y2)
    a = (x2 - x1) ** 2 + (y2 - y1) ** 2
    distance = math.sqrt(a)

    return round(distance, 2)


print(calculate_line_length((15, 7), (22, 11)))
