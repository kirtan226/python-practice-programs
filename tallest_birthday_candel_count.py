'''Write a function to find the number of tallest candles on a birthday cake
input:[4, 4, 1, 3]
output:2
Reason: The tallest candle has a height of 4, and there are 2 such candles.

Input:[3, 2, 1, 3]
Output:2

Input:[5, 5, 5]
Output:3
'''


def tallest_candles(candles):
    # candles.sort(reverse=True)
    # max=candles[0]
    # # print(max)
    #
    # count =0
    # for i in candles:
    #     if i==max:
    #         count+=1
    # return count

    return candles.count(max(candles))

print(tallest_candles([4,4.4,4.5,4.60,4.43,4,6.61, 4, 1, 3]))