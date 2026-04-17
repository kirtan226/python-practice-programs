def repeat_char(string):
    repeat_character=[]
    char_count={}
    count_char=0

    for char in string:
        count_char+=1
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] =1

    for char,count in char_count.items():
        if count>1:
            repeat_character.append(char)

    if ' ' in repeat_character and ' ' in char_count:
        repeat_character.remove(' ')
        char_count.pop(' ')


    print("repeated char is:",repeat_character)
    print("count:",char_count)
    print("count of each char:",count_char)

s=input("Enter any string: ")
repeat_char(s)