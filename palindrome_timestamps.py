"""A palindrome timestamp is defined as one that reads the same in hours:minutes
format as it does in minutes:hours format.
For example, 02:20 is a palindrome timestamp.

input:12:21
15:51
output:4

Reason:
Within the range from 12:21 to 15:51, the palindrome timestamps are: 12:21, 13:31, 14:41 and 15:51.
"""

from datetime import datetime, timedelta

def is_palindrome_timestamp(time):
    hh, mm = time.strftime("%H:%M").split(':')
    return hh == mm[::-1]

def count_palindrome_timestamps(start_time, end_time):
    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")
    count = 0
    current = start

    while current <= end:
        if is_palindrome_timestamp(current):
            count += 1
        current += timedelta(minutes=1)

    return count

# Example usage
start_time = "12:21"
end_time = "15:51"
output = count_palindrome_timestamps(start_time, end_time)
print(output)  # Output: 4
