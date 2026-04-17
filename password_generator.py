import random

char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:',<.>/?"""
n=int(input("Enter the length of the password : "))
passwowd = ''

for i in range(n):
    passwowd+=random.choice(char_set)

print(f"Generated password :{passwowd}")