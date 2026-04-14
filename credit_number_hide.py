""" Write a function that takes the credit card number as input and return masked number .
input :1234567812345678
output:************5678
"""

# def credit(card_number):
#     print(card_number[-4:])
#     new=''
#     for i in range(0,len(card_number)):
#         new=new+'*'
#         print(card_number[i])
#         # print(new)
#         if i==card_number[-4]:
#             break
#     print(new+card_number[-4:])
#
# card_number=input('enter your card number : ')
# credit(card_number)

def credit(card_number):
    card_number =str(card_number)
    if len(card_number)<16:
        return "Enter valid number !!!"

    number = "*"*(len(card_number)-4)+card_number[-4:]

    return number

card_number=input('enter your card number : ')
print(credit(card_number))
