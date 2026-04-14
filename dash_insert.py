# Using the Python language, have the function DashInsert(str) insert dashes ('-') between each two odd numbers in str.
# For example: if str is 454793 the output should be 4547-9-3. Don't count zero as an odd number.

def dash(n):
   li=list(n)
   i=0

   while i <len(li)-1:
       if int(li[i])%2!=0 and int(li[i+1])%2!=0:
           li.insert(i+1,'-')
           i+=2
       else:
           i+=1

   return ''.join(li)

num=input("Enter the numbers :")
print(dash(num))