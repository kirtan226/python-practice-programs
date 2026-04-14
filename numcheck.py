# Using the Python language, have the function CheckNums(num1,num2) take both parameters being passed and
# return the string true if num2 is greater than num1, otherwise return the string false.
# If the parameter values are equal to each other then return the string -1.

def numeric(n1,n2):

    if n2>n1:
        return "true"
    elif n1>n2:
        return "false"
    elif n1==n2:
        return "-1"

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print(numeric(num1,num2))