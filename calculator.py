def addition(a,b):
    print(f"addition of {a} & {b} is:", a + b)

a = int(input("A="))
b = int(input("B="))
print("entrt 1 for addition(+)\nenter 2 for subtraction(-)\nenter 3 for multiplication(*) \nenter 4 for divison(/)")
x = int(input("enter the arithmatic operator which you want to perform:"))

match x:
    case 1:
        addition(a,b)

    case 2:
        print(f"subtraction of {a} & {b} is:", a - b)
        print("subtraction of ",a," and ",b," is ",a-b)

    case 3:
        print(f"multiplication of {a} & {b} is:", a * b)

    case 4:
        print(f"multiplication of {a} & {b} is:", a / b)

    case _:
        print("invalid")


