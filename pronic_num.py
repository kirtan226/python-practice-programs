"""Write a function to check if a given number is a Pronic number or not.
A Pronic number is a number that is the product of two consecutive integers.
That means n is Pronic if and only if there are two consecutive integers i and i+1 such that n= i*(i+1).
For this input :6 , here n=6 ,so i=2 , (i+1)=(2+1)=3
the output should be:True

True case : 42 , 6 , 110
 """

def is_pronic(n):
    for i in range(1,99):
        if i*(i+1)==n:
            # print(True)
            return True
            # break
        # else:
    return False
    # print(False)
n=int(input("Enter a number to check :"))
print(is_pronic(n))