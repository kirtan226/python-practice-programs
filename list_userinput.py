def repeat(l):
    new=[]
    l_repeat=[]

    for i in l:
        if i in new:
            l_repeat.append(i)
        else:
            new.append(i)

    print("Repeated list is :",l_repeat)

# Create a list using user input
list1=[]
list_element=int(input("Enter the length of list:"))

for i in range(list_element):
    element_input=input(f"Enter the list element {i}:")
    list1.append(element_input)

print(f"your list is {list1}")
print(type(list1))
temp_list=list(list1)
print(temp_list)
repeat(temp_list)

'''
# Dictionary user input
dict={}

n = int(input("Enter the limit for dictionary:"))

for i in range(n):
    key=input(f"enter the {i+1} key : ")
    value=input(f"Enter the value for {key} :")

    dict[key]=value

print(dict)

'''