''' Write a function to maximize the first number by using the digits of second number .
-Given two integers num1 and num2 ,return the maximum value of num1 that can be achieved by
 replacing its digits at certain positions with digits from num2 .
-For example, for num1=723 and num2=556, we can replace num1's secand digit (2) with num2's
 third digit (6) to make the value of num1 763.
-Again, we can replace the third digit 3 with num2's 1st or 2nd digit (5), as both are the same,
to make the value of num1 765, which is the maximum possible value through digit replacement,

Input :num1:274 , num2:583
Output : 875
Reason: We can replace num1's 1st and 3rd digit (2 and 4) with num2's 2nd and 1st digit (8 and 5) respectively
        to create the maximum number.

Input : num1 = 3333  ,num2 = 6666
Output : 666
Reason: We can replace each digit of num1 with the corresponding digit of num2 to create the maximum number.

Input: 123 ,321
Output :323

Input :455 ,333
Output :455

Input : 54321 ,98765
Output :98765

'''


def maximize_first_number(num1, num2):
    new = ''
    str_1 = str(num1)
    l2 = list(str(num2))
    l2.sort(reverse=True)
    print(str_1, l2)

    for i in str_1:
        for j in l2:
            if int(i) < int(j):
                print(f"for {i} , {j} is smaller")
                new += j
                l2.remove(j)
                break
            else:
                print(f"for {i} , {j} is bigger ")
                new += i
                break

    return new

n1 = 274
n2 = 583
print(maximize_first_number(n1, n2))
