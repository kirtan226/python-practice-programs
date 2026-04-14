# Using the Python language, have the function AdditivePersistence(num) take the num parameter being passed
# which will always be a positive integer and return its additive persistence
# which is the number of times you must add the digits in num until you reach a single digit.
# For example: if num is 2718 then your program should return 2 because 2 + 7 + 1 + 8 = 18 and 1 + 8 = 9 and you stop at 9.


def AdditivePersistence(num):

    ln=list(num)
    count=0
    while len(ln)>1:
        sum=0
        for i in range(0,len(ln)):
            sum=sum+int(ln[i])
            print(f"After adding {ln[i]} sum is :",sum)

        ln=list(str(sum))
        count+=1
        print(ln)

    print("Additive persistence:",count)

n=input("Enter a number : ")
AdditivePersistence(n)
