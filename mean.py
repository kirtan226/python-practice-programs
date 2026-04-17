def ismean(a,b):
    mean=(a*b)/(a+b)
    print("The mean value is:",mean)

def isgreater(a,b):
    if(a>b):
        print(a," is greater number")
    elif(a==b):
        print(a," & ",b ," both are equal number")
    else:
        print(b," is greater number")


c=20
d=30
ismean(c,d)
isgreater(c,d)

e=int(input("e="))
f=int(input("f="))
ismean(e,f)
isgreater(e,f)