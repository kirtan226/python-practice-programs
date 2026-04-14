''' Write a function to implement Mubashir cipher .
- The Mubashir Cipher takes a string and replaces each letter with the letter that
is directly opposite it in the English alphabet. Hint: In English alphabet, 'a' is opposite
to 'z', 'b' is opposite to 'y', 'c' is opposite to 'x', and so on. The same rule applies for
uppercase letters.

Input :'abc'
Output : 'zyx'
Reason : In English alphabet, 'a' is opposite to 'z', 'b' is opposite to 'y',
and 'c' is opposite to 'x'. So, when we apply Mubashir Cipher on 'abc', we get 'zyx.

Input :'mubashir'
Output : 'nfyzhsri'

Input : 'cipher'
Output : 'xrksvi'

Input : 'hello world'
Output : 'svool dliow'

'''
# a - 97 , z - 122

def mubashir_cipher(text):

    new =''
    max=122

    for i in text:
        if i==' ':
            new+=" "
        else:
            current = ord(i)
            change = max - current
            print(change + 97)
            new+=chr(change + 97)

    print(new)
    return new

mubashir_cipher('abc')
