"""Longest Word
Have the function LongestWord(sen) take the sen parameter being passed and return
the longest word in the string. If there are two or more words that are the same length,
return the first word from the string with that length. Ignore punctuation and assume
sen will not be empty. Words may also contain numbers, for example "Hello world123 567"

Input: "fun&!! time"
Output: time

Input: "I love dogs"
Output: love"""

def longestWord(sen):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    word =""
    for char in sen:
        if char not in punctuations:
            word=word+char

    split_word = word.split(" ")
    # print(split_word)

    biggest_word=split_word[0]

    for char in split_word:
        if len(char) > len(biggest_word):
            biggest_word=char

    return biggest_word

print(longestWord("fun&!! time"))