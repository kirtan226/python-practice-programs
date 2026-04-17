print("left side pyrimid  ")
n = int(input("Enter length of pyramid : "))
for i in range(n):
    pattern = ' 1 '
    pattern = pattern * i
    print(pattern)

for i in range(1,n):
    i-=1
    pattern = '*'
    pattern = pattern * i
    print(pattern)