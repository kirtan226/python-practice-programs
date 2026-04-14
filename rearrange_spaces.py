''' Write a function to rearrange spaces between words in a sentence so that they are evenly distributed.

Input : "This___is__a___sentence_"
Output :This___is___a___sentence
Reason: The input string has 9 spaces and 4 words. The spaces are distributed evenly between the words,
resulting in 3 spaces between each word.

Input:Hello___world
Result:Hello___world

Input:__I_love___Python__
Result:I____love____Python

Input:Singleword
Result:Singleword

'''

def rearrange_spaces(text):
    a=text.split(' ')
    print(a)
    word = [i for i in a if len(i) > 0]
    print("Word count:",len(word))
    space_count=0
    space=''

    for i in text:
        if i.isspace():
            space_count+=1
    print("Space Count: ",space_count)

    if space_count <= 0:
        return text


    rearrange = space_count // ( len(word) - 1)
    print("Space should be come after each Word :",rearrange)

    st =''
    for i in word:
        if i==word[-1]:
            st += i
            break
        else:
            st+=i
            # print("new word:",st)
            st+= '_'*rearrange
            # print("after Space:",st,"_")
    # print(st)
    return st


print(rearrange_spaces("  I love   Python  " ) )
