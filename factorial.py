def factorial(num):
    if(num==1 or num==0):
        return 1
    else:
        return(num*factorial(num-1))

num=int(input("Enter number to find factorial:"))

print("factoril is:",factorial(num))

# #factorial(n)=n*(n-1)
#
# def factorial1(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n*factorial1(n-1)
#
# print(factorial1(5))
