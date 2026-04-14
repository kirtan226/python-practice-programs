'''Write a function to format a number with a thousands separator.

input:1000000
output:'1,000,000'
Reason: The input number 1000000 is formatted with a thousands separator to become '1,000,000'.

Input:50000
Output:50,000
'''


def format_number(n):
    # str_n = str(n)
    # result = []
    # for x in range(len(str(n)) - 1, -1, -1):
    #     result.append(str_n[x])
    #     if ((len(str(n)) - x) % 3 == 0 and x != 0):
    #         result.append(",")
    # result.reverse()
    #
    # return "".join(result)

    # print(f"{n:,}")


    return f"{n:,}"

print(format_number(1000000))
