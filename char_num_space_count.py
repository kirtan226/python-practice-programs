def calculate(s):
    char_c=0
    c={}

    num_c=0
    n={}

    special_character="!@#$%^&*()_-+={}[]|\:;'<>,.?/"
    special_character_count=0
    special_character_repeat={}

    space_c=0

    for char in s:              # check in input string

        if char.isalpha():      # check for alphabet in input string
            char_c+=1

            if char in c:       # create a dictionary for character repeat
                c[char]+=1
            else:
                c[char]=1

        elif char.isdigit():    #check for numerical value in input string
            num_c+=1

            if char in n:       # create a dictionary for numerical repeat
                n[char]+=1
            else:
                n[char]=1

        elif char in special_character:            #check for special character value in input string
            special_character_count+=1
            if char in special_character_repeat:     # create a dictionary for special character repeat
                special_character_repeat[char]+=1
            else:
                special_character_repeat[char]=1

        elif char.isspace():        #check for space in input string
            space_c+=1


    print(f"Number of character found is : {char_c} and its repitation is {c}")

    print(f"Number of digit found is :{num_c} and its Repitation {n} " )
    print(f"Number of  special character found is : {special_character_count} and its repitation is {special_character_repeat}")
    print("Number of space found is : ",space_c)



string=input("Enter any string : ")
calculate(string)