"""Write a function to find the three most common characters in the company's logo.
1. Define a function that takes a string as input.
2. Inside the function, count the frequency of each character and then find the three most common characters.
3. Return a list of tuples, where each tuple contains a character and its frequency.

Example
input:'google'
output:[('g', 2), ('o', 2), ('l', 1)] , three most common character

Input:facebook
Output:[('o', 2), ('f', 1), ('a', 1)]

Input:microsoft
Output:[('o', 2), ('m', 1), ('i', 1)]

Input:apple
Output:[('p', 2), ('a', 1), ('l', 1)]
"""
from collections import Counter
from collections import Counter
def find_common_chars(logo):

    # Create a Counter object
    char_counter = Counter(logo)

    # Get the three most common characters
    most_common_chars = char_counter.most_common(3)
    return most_common_chars

    # c = Counter(logo)
    # return c.most_common(3)



print(find_common_chars("microsoft"))

# def find_common_chars(logo):
#
#     frequency={}
#     for i in logo:
#         if i in frequency:
#             frequency[i]+=1
#         else:
#             frequency[i]=1
#
#     list_of_frequency=[]
#     for keys , values in frequency.items():
#
#         list_of_frequency.append((keys,values))
#     print(list_of_frequency)
#
# s="google"
# # print(find_common_chars(s))
# find_common_chars(s)