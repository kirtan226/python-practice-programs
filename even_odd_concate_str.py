"""
a string is given  , create two string from it , one from even indice and one from odd , and add even + odd string
, and return new string
"""
def index_shuffle(txt):
    even=txt[::2]
    odd= txt[1::2]

    print(even)
    print(odd)
    add = even+odd
    print(add)

    # return ''.join(txt[::2] + txt[1::2])
index_shuffle("abcdef")