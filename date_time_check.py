"""Write a function to determine if the 13th day of a given month and year falls on a Friday
Instructions
Create a date object for the 13th day of the given month and year. Then check if this date is a Friday.
Return True if the 13th day of the given month and year is a Friday, otherwise return False.

Hint: In Python's datetime module, Monday is 0 and Sunday is 6. So, Friday is 4

Example:
input: 8   2021
output :True
Reason: The 13th day of August in the year 2021 falls on a Friday
"""

import datetime

def is_friday_13(month, year):
    # Create a date object for the 13th day of the given month and year
    date_13th = datetime.date(year, month, 13)

    # Check if the weekday of the 13th day is Friday (4)
    return date_13th.weekday() == 4

# Test the function
print(is_friday_13(9, 2024))  # Output: True
