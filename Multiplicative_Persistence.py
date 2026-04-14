# Using the Python language, have the function MultiplicativePersistence(num) take the num parameter being passed
# which will always be a positive integer and return its additive persistence
# which is the number of times you must multiply the digits in num until you reach a single digit.
# For example: if num is 39 then your program should return 3 because 3*9=27 and 2*7=14 and 1*4=4 ,you stop at 4.

def MultiplicativePersistence(num):
    l=list(num)
    count=0

    while len(l)>1:
        mul=1
        for i in range(0,len(l)):
            mul=mul*int(l[i])
            print(f"After muktiplying {l[i]} :",mul)

        count += 1
        l=list(str(mul))
        print(l)

    print("Multiplicative Persistence :",count)

n=input("Enter a number:")
MultiplicativePersistence(n)

