"""
Write a function to validate a given PIN.
The PIN should be exactly 4 or 6 digits long and contain only numbers.
Example
input:'1234'
output:True
Reason: The input string '1234' is exactly 4 characters long and contains only digits, hence it's a valid PIN.

Input:12a3
Output:False
"""

def validate_pin(pin):
    for char in pin:
        if len(pin)==6 or len(pin)==4:
            if pin.isdigit():
                return True

    return False

n='1234'
print(validate_pin(n))