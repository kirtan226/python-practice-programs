"""
Write a function to calculate the total time spent washing hands
1. Define a function that takes two integers as input: the number of times you
wash your hands in a day and the number of months.
2. Return the total time spent washing hands in minutes and seconds.
Note: Assume each month has 30 days. One hand wash takes 21 seconds.
Example
input: 8(times)  7(months)
output:'588 minutes and 0 seconds'
Reason: If you wash your hands 8 times a day for 7 months, you will spend a
total of 588 minutes and 0 seconds washing your hands.

Input :10  6
Output:630 minutes and 0 seconds
"""
def total_washing_time(times_per_day, months):

    second = 21
    day = 30

    total_wash = times_per_day * months * day
    total_second = total_wash * second

    minutes = total_second//60
    second = total_second%60

    return f"{minutes} minutes and {second} seconds"

t = int(input("How many times you wash your hands per day : "))
m= int(input("For how many months : "))
print(total_washing_time(t, m))