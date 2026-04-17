
"""Remove Number from the string"""

def num_remove(s):
    num='0123456789'
    new_string= " "

    for i in s:
        if i not in num:
            new_string = new_string + i

    print("Befor :",s)
    print("After removing :",new_string)

# n=input("Enter any string : ")
# num_remove(n)

"""Remove String from numbers"""

def str_remove(s):
    alphabet ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_num=""

    for i in s:
        if i not in alphabet:
            new_num = new_num + i

    print("Befor :",s)
    print("After removing :", new_num)

# s=input("Enter any String :")
# str_remove(s)


"""Remove Vowels form list"""
def v_remove(s):
    vowels = "aeiouAEIOU"
    removed_text=""
    for i in s:
        if i not in vowels:
            removed_text = removed_text +i

    print("After removing vowels from string: ",removed_text)

# vr=input("Enter any string to remove vowels:")
# v_remove(vr)
