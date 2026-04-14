"""
Write a function to find the date of the first Tuesday of a given month and year.
input:1 2022
output:'2022-01-04
Reason: The first Tuesday in January 2022 falls on January 4th.

Input:12  2024
Output:2024-12-03

Input:3 2023
Output:2023-03-07
"""

# from datetime import datetime, timedelta , date
# def first_tuesday(year, month):
#     # Start with the first day of the given month and year
#     first_day = datetime(year, month, 1)
#
#     # Calculate the number of days to add to reach the first Tuesday
#     days_to_add = (1 - first_day.weekday() + 7) % 7
#     first_tuesday = first_day + timedelta(days=days_to_add)
#
#     return first_tuesday.strftime('%Y-%m-%d')
#
#
# print(first_tuesday(2024, 7))

def is_ugly(num):
    if num%2==1:
        return True
    else:
        if num%3==1:
            return True
        else:
            if num%5==1:
                return True
    return False


print(is_ugly(5))