"""Write a function to check if a number is Disarium or not.
A number is considered Disarium when the sum of its digits, each raised to the power of
their respective positions, equals the number itself.
For example, consider the number 175. Here,
1^1 + 7^2 + 5^3 = 175
So, 175 is a Disarium.

Example
input:135
output:True

input:518
output:True

because 1^1 + 3^2 + 5^3 = 135"""

def is_disarium_number(num):
    st = str(num)
    total = 0
    for i in range(0,len(st)):
        total += pow( int(st[i]) , i+1)

        """Uding lambda function"""
        # x = int(st[i])
        # total += (lambda x, i: x ** (i + 1)) (x, i)

        # print(f"After doing {int(st[i])}^{i+1} total is  : {total} ")

    if total == num:
        return True
    else:
        return False

num=int(input("Enter a number to check :"))
print(is_disarium_number(num))

# print(2**3)