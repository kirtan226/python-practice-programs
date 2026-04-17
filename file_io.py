'''f = open('myfile1.txt','r') # 'r' for read , 'w' for writing , 'a' for appending
#print(f)

read_text =f.read()
print(read_text)
f.close()'''

f=open("INFOLABZ/myfile1.txt", 'w') # with using 'W' we can directly crete a file
f.write("i am kirtan patel ")
f.truncate(5)# print only 5 letter
f.close()


'''with open("myfile1.txt",'a') as f:
    f.write("\ni am from mehsana")'''

#for read multiple lines
"""f = open('myfile1.txt','r')
while True:
    line=f.readline()
    if not line:
        break
    print(line)
f.close()

#for write multiple lines

with open("myfile1.txt","w")as f:
    lines=["line1\n","line2\n","line3"]
    f.writelines(lines)"""

"""with open("myfile1.txt","r")as f:
    f.seek(10)#skip first 10 index
    data=f.read(5)# after skip indeax read 5 letter
    print(data)
    print(f.tell()) # current position"""