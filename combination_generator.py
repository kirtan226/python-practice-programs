'''Write a function to generate all possible combinations of a given list of items.
The itertools module in Python provides various functions that work on
iterators to produce complex iterators. The combinations() function in
itertools allows us to generate all possible combinations for an iterable.

Input:['d', 'e']
Output:[('d',), ('e',), ('d', 'e')]

Input:['g','h','i','j']
Output :[('g',), ('h',), ('i',), ('j',), ('g', 'h'), ('g', 'i'), ('g', 'j'), ('h', 'i'),
 ('h', 'j'), ('i', 'j'), ('g', 'h', 'i'), ('g', 'h', 'j'), ('g', 'i', 'j'), ('h', 'i', 'j'),
 ('g', 'h', 'i', 'j')]

Input:['a', 'b', 'c']
Output :[('a',), ('b',), ('c',), ('a', 'b'), ('a', 'c'), ('b', 'c'), ('a', 'b', 'c')]
'''

import itertools
def generate_combinations(lst):
    all_combinations = []
    for r in range(1, len(lst) + 1):
        combinations_r = list(itertools.combinations(lst, r))
        all_combinations.extend(combinations_r)
    return all_combinations


print(generate_combinations(['1', '2', '3',4]))