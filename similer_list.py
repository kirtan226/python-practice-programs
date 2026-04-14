"""
Write a function to group similar items from a list into a dictionary.
Return a dictionary where the keys are the items and the values are lists of indices where the items are found
in the original list.

input:['apple', 'banana', 'apple', 'banana', 'cherry', 'apple']
output:{'apple': [0, 2, 5], 'banana': [1, 3], 'cherry': [4]}
Reason: The item 'apple' appears at indices 0, 2, and 5. The item 'banana' appears at indices 1 and 3.
The item 'cherry' appears at index 4. Therefore, these are grouped into a dictionary accordingly.

Input:['dog', 'cat', 'dog', 'bird', 'cat']
Output:{'dog': [0, 2], 'cat': [1, 4], 'bird': [3]}

"""

# for char in lst:
#     d.append(char: [lst.index(char)])
#     return d


def group_items(lst):
    item_dict = {}
    for index, item in enumerate(lst):
        if item in item_dict:
            item_dict[item].append(index)
        else:
            item_dict[item] = [index]
    return item_dict
l=['red', 'blue', 'green', 'red']
print(group_items(l))