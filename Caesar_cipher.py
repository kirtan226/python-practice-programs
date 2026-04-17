'''Caesar Cipher
Implement a Caesar cipher encryption and decryption program.
'''

text = input("Enter a text : ")
key=int(input("Enter a shift :"))

print(" Enter 1 to convert plain-Text to encrypted-text(Cipher Text). \n "
      "Enter 2 to convert Cipher Text to decrypted-text(plain-Text).")
x=int(input("Enter your selection : "))

match x:
    case 1:
        print("Plain Text message to Cipher Text : ")
        result = ''
        for char in text:
            if char.isalpha():
                shift = 65 if char.isupper() else 97
                result+= chr((ord(char) - shift + key ) %26 + shift)
            else:
                result+=char

        print(result)
    case 2:
        print("Cipher Text message to Plain Text : ")
        result = ''
        for char in text:
            if char.isalpha():
                shift = 65 if char.isupper() else 97
                result += chr((ord(char) - shift - key) % 26 + shift )
            else:
                result += char
        print(result)
    case _:
        print("Invalid selection please enter right value !!!")
""" To convert plain-text to caesar text """




# def caesar(word ,key ):
#     result =''
#     for char in word:
#         if char.isalpha():
#             shift = 65 if char.isupper() else 97
#             result+= chr((ord(char) - shift + key ) %26 + shift   )
#         else:
#             result+=char
#
#     return result
# word=input("Enter a word :")
# key=int(input("Enter a shift :"))
#
# print(caesar(word, key))

""" To convert cipher text to caesar text """
# def caesar(word ,key ):
#     result =''
#     for char in word:
#         if char.isalpha():
#             shift = 65 if char.isupper() else 97
#             result += chr((ord(char) - shift - key) % 26 + shift )
#         else:
#             result+=char
#
#     return result
# word=input("Enter a word :")
# key=int(input("Enter a shift :"))
#
# print(caesar(word, key))