"""have the function SimpleAdding(num) add up all the numbers from 1 to num.
# For the test cases, the parameter num will be any number from 1 to 1000."""

def add(n):
    total=0

    for i in range(n):
        total +=i
    print(f"After adding {n} number the sum is: {total}")
num=int(input("Enter a number to add :"))
add(num)