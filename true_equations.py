"""
Write a function to find the equations that are true from the given list.
Return a list of equations that are true.

input:['2+2=4', '3*3=6', '1+1=3', '5/5=1']
output:['212-4', '5/5-1']
Reason: The equations *2+2=4" and "5/5=1' are true, while the others are not.

Input:['7-3=4', '8*0=0', '9/3=2']
Output:['7-3=4', '8*0=0']

Input:['100/10=11','200*0=20','300-300=30']
Output:[]

"""

def find_true_equations(equations):
    new=[]
    for char in equations:
        left  ,right = char.split('=')
        if eval(left)==eval(right):
            new.append(char)

    return new

print(find_true_equations(['100/10=11','200*0=20','300-300=30']))
