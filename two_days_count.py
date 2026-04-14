'''Write a function to calculate the number of days between two given dates .
Hint: of Python, you can subtract two date objects to get a timedelta object representing
    the difference between them. The (.days) attribute of a timedelta object gives the number of days.
Input : '2022-05-01', '2022-05-30'
Output : 29

Input :'2023-01-01' , '2023-12-31'
Output :364

Input : '2022-02-01' , '2022-02-28'
Output : 27

'''

from datetime import datetime


def calculate_days(date1, date2):
    format = '%Y-%m-%d'
    d1 = datetime.strptime(date1, format)
    d2 = datetime.strptime(date2, format)

    difference = abs((d2 - d1).days)
    print(difference)


calculate_days('2022-05-01', '2022-05-30')
