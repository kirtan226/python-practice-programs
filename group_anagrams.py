''' Write a function to group anagrams together from a given list of strings .
Input : ['cat', 'dog', 'tac', 'god', 'act']
Output : [['act', 'cat', 'tac'], ['dog', 'god']]

Input : ['abcd','dcba','lll']
Output : [['abcd', 'dcba'], ['lll']]

Input : ['a']
Output : [['a']]

Input : ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
Output : [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]
'''
from collections import defaultdict


def group_anagrams(strs):

    anagrams = defaultdict(list)
    for i in strs:
        sorted_string = ''.join(sorted(i))
        print('sorted : ',sorted_string)
        anagrams[sorted_string].append(i)
        print(anagrams)

    return list(anagrams.values())


l = ['tea', 'eat', 'tan', 'ate', 'nat', 'bat']
print(group_anagrams(l))
