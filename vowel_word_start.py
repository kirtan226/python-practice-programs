''' write a function to find all words in sentance that start with a vowel .
return a list of words that start with vowels .

Input:Hello, how are you?
Output:['are']

Input:I am doing fine.
Output:['I', 'am']

Input:The weather is nice today.
Output:['is']

Input:No words start with a vowel.
Output:['a']
'''

def find_vowel_words(sentence):
    vowels = 'aeiouAEIOU'
    new=sentence.split(' ')
    print(new )
    vowels_start=[]

    for char in new:
        if char[0] in vowels:
            vowels_start.append(char)

    # print(vowels_start)
    return vowels_start


print(find_vowel_words("hello , How are you ?"))