def smiley_convert(s):
    return s.replace(':)',"😊")
    # text=list(s)
    # l=len(text)
    # new=""
    # for char in range(0,l):
    #     if text[char]==':' and text[char+1]==")" :
    #         new=new+"😊"
    #         print("i am")
    #
    #     else:
    #         new=new+text[char]
    #     print(text[char])
    # return new

s='hello :) '
print(smiley_convert(s))


