"""Write a function to return 'Up' if the input number is positive, 'Down'
if it's negative, and 'Zero' if it's zero.

Example
input:5
output:'Up'
"""

def up_down(n):
    # if n > 0:
    #     return "Up"
    # elif n == 0:
    #     return "Zero"
    # else:
    #     return "Down"

    return "Zero" if n==0 else "Up" if n>0 else "Down"

n=int(input("Enter a number :"))
print(up_down(n))