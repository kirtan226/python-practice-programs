'''Write a function to censor words that are longer than four characters in a sentence.
Input :'The quick brown fox jumps over the lazy dog'
Output :The ***** ***** for ***** over the lazy dog
Reason: The words 'quick', 'brown', 'jumps', and 'lazy' are longer than four characters,
  so they are replaced with asterisks.

Input :'Hello, my name is John Doe'
Output :'****** my name is John Doe'

Input:'I love programming in Python'
Output:'I love *********** in ******'

Input:'This is a test sentence'
Output:'This is a test ********'
'''


def censor_words(sentence):
    new = sentence.split(' ')
    print(new)
    st = []
    for i in new:
        if len(i) > 4:
            st.append('*' * len(i))
        else:
            st.append(i)
    return ' '.join(st)

s = 'The quick brown fox jumps over the lazy dog'
print(censor_words(s))
