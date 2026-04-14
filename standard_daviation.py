"""The stdev() function from the statistics module calculates the standard deviation for a sample of data.
Round off your result to two decimal places.
Example
input:[1, 2, 3, 4, 51
output:1.58
Reason: The standard deviation of [1, 2, 3, 4, 5] is approximately 1.58 when rounded off to two decimal places.
Input:[6, 7, 8, 9, 10]
Output:1.58
"""


from statistics import stdev
def find_standard_deviation(numbers):
    s = stdev(numbers)

    return round(s,2)


n=[11, 12, 13, 14, 15]
print(find_standard_deviation(n))
