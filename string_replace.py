'''Write a function to replace "yt" in string "Python" with given sub string .
input : "abc"
output : Pabchon

Input : 'uvwx'
Output : Puvwxhon

Input :'1234'
Output : P1234hon
'''


def replace_substring(sub):
    a = 'Python'.replace('yt', sub)
    return a

    # return "p"+sub+"hon"


b = "abc"
print(replace_substring(b))
