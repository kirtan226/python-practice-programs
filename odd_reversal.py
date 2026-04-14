''' Write a functon to reverse all the world in a sentence that have odd Length .

Input : 'Hello world this is a test'
Output : 'ollet dlrow this is a test'
Reason: The words 'Hello', 'world', and 'a' have odd lengths in the original sentence. So,
 they are reversed in the output.

Input : 'I love Python programming'
Output : 'I love Python gnimmargorp'

Input : 'This is an example sentence'
Output : 'This is an elpmaxe sentence'

Input : 'Odd words are reversed here'
Output : 'ddO sdrow era reversed here'
'''

def reverse_odd_words(sentence):
    new=sentence.split(" ")
    st=[]
    for i in new:
        if len(i)%2==0:
            st.append(i)
        else:
            st.append(i[::-1])

    return ' '.join(st)


print(reverse_odd_words('Hello world this is a test'))
