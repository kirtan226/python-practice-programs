"""
Write a functon to convert bird names into four letter bird codes .

1. Define a function that takes a string as input.
2. Inside the function, split the bird name into words.
3. If there is only one word, take the first four letters.
4. If there are two words, take the first two letters from each word.
5. If there are three or more words, take the first letter from each of the first
    three words and add the first letter of the last word.
6. Return the four-letter bird code in uppercase.

Input : 'Northern Cardinal'
Output : NOCA

Input : 'American Crow'
Output : AMCR

Input : 'Bald Eagle'
Output : BAEA

Input : 'Black-capped Chickadee'
Output : BLCH
"""


def bird_code(name):
    st = ''
    new = name.split(' ')

    for i in new:
        st += i[0] + i[1]
    print(st.upper())

    return st.upper()


print(bird_code('Northan Cardinal'))
