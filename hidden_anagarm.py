''' Write a function to find a hidden anagram in a given string.
1. Define a function that takes two strings as input: the first one is the text to search and
    the second one is the anagram to find.
2. Inside the function, iterate over the text and check if a substring of the first string is
    an anagram of the second string.
3. Return the first found anagram. If no anagram is found, return 'Anagram not found'.

Input :'I am lord Voldemort' ,'Tom'
Output : 'Anagram not found'

Input :'Silent Study' ,'Listen'
Output : 'silent'

Input :'The quick brown fox jumps over the lazy dog' ,'god'
Output : 'dog'
'''

def find_anagram(text, word):
    new = text.split(' ')
    # print(new)

    for i in new:
        if sorted(list(i.lower())) == sorted(list(word.lower())):
            return i
    return "Anagram not found"


text = 'I am lord Voldemort'
word = 'Tom'
print(find_anagram(text, word))
