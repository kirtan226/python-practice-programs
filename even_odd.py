# Even Number : 2, 4, 6, 8, 10, 12, 14,…
# Odd Number : 1 , 3, 5, 7, 9, 11, 13, 15,…


print("Enter 1 for Even Number list\nEnter 2 for Odd Number list ")
x=int(input("Enter Your choice:"))

match x:
    case 1: # Even number

        n=int(input("Enter the limit to print Even number:"))
        even_list=[]
        for i in range(2,n+1,2):
            even_list.append(i)

        print(f"The list of even numbers is :{even_list}")

    case 2: #odd number
        n = int(input("Enter the limit to print Odd number:"))
        odd_list=[]

        for i in range(1,n+1,2):
            odd_list.append(i)

        print(f"The list of odd numbers is : {odd_list}")

    case _:
        print("Enter valid option...")

"""
def even_odd(n):

    odd=[]
    even=[]
    for i in range(1,n):
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)

    print("Odd number list : ",odd)
    print("Even number list : ",even)

n=int(input("Enter limit to print Even and Odd number : "))
even_odd(n)
"""