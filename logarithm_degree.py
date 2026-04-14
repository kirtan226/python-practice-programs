"""The function takes two integer as input representing the base and the result of the exponential equation
Example:

input:2(base) 8(result)
output : 3.0
reason : 2^1 = 2 {1.0} ,2^2 = 4{2.0} , 2^3 = 8 {3.0}(output)


input:10(base) 10000(result)
output : 4.0
"""

import math
def solve_exponential(base, result):
    count=0
    new = 0
    for i in range(1,100):
        new = base**i
        count+=1
        print(f"value {base}^{i} and {new}")
        if new ==result:
            return count
        else:
            continue

    # count = 0
    # for i in range(1, 100):
    #     count += 1
    #     if base ** i == result:
    #         return float(count)
    #     else:
    #         continue
base = 10
result = 10000

print(solve_exponential(base,result))