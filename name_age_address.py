"""Write a function to return a person's information.
1. Take the person's name, age, and address as inputs.
2. Store the inputs in variables and return them.
3. Return the person's name, age, and address.
Example

Input:John Doe' 25 'New York
Output:{'Name': 'John Doe', 'Age': 25, 'Address': 'New York'}

Input:Jane Smith' 30 'Los Angeles
Output:{'Name': 'Jane Smith', 'Age': 30, 'Address': 'Los Angeles'}
"""

def get_user_info(name, age, address):
    # new_dict = {}
    # new_dict['Name']=name
    # new_dict['Age']=age
    # new_dict['Address']=address
    # Or

    new_dict={'Name':name , 'Age':age , 'Address':address}
    return new_dict

n=input("Enter a name :")
a=input("Enter an age :")
add=input("Enter an address :")
print(get_user_info(n , a ,add ))