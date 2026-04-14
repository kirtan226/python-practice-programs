"""
Write a function to calculate duration in minutes between a starting time and a final time.

input:"14:30" "16:00"
output:90
Reason: For the given input, starting from 14:30 and with a duration of 90 minutes,
the final time would be 16:00.
"""

from datetime import datetime

def calculate_duration(start_time, final_time):

    time_format = '%H:%M'

    t1= datetime.strptime(start_time,time_format)
    t2 = datetime.strptime(final_time,time_format)

    difference = t2 - t1

    duration_in_minutes = difference.total_seconds() / 60

    return int(duration_in_minutes)


print(calculate_duration("14:30", "16:00"))