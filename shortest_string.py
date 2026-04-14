"""
Write a function to find the shortest word in a given string.
If more than one word has the same length, return the first word.

input:"This is an example sentence'
output:is
Reason: The words in the sentence are 'This', 'is', 'an', 'example', 'sentence'. The shortest word among them is 'is'.

Input:Hello world
Output:Hello

Input:Find the smallest word in this sentence
Your Output:in
"""

def shortest_word(sentence):
    li= sentence.split(" ")
    shortest = li[0]
    # print(len(shortest))

    for i in range(len(li) - 1):
        # print(len(li[i]))

        if len(li[i])>len(li[i+1]):
            shortest=li[i+1]

    return shortest


print(shortest_word("I love Python programming"))

# def max_sum(l):
#     sum=0
#     # print(max(l))
#     sum+=max(l)
#     l.pop()
#     # print(max(l))
#     sum+=max(l)
#     # print(sum)
#
# l= [1,2,3,4,5,6,7]
# max_sum(l)