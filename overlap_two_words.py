''' Write a function to overlap two words , creating a merged word .
- Given two words, we can create a new word by overlapping them. The new word should combine
  the end of the first word with the beginning of the second word, producing the shortest
  possible word that retains the essence of the both words.

Input :"python" ,"online"
Output : 'pythonline'

Input :"night" ,"tight"
Output : 'nightight'

Input : "wind", "window"
Output : 'window'

Input : "classroom" , "roomy"
Output : 'classroomy'
'''


def merge_words(word1, word2):
    w1 = list(word1)
    w2 = list(word2)
    for i in range(0 , len(word2)):
        if i in word1:
            if word1[i+1] == word2[i+1]:
                print(word1[i] , word2[i+1])
        else:
            print('not common ')


merge_words("python", "online")
