''' Write a function to sort a string based on its last character .
1. Define a function that takes a string as input.
2. Inside the function, split the string into words, sort them based on the last character
 of each word, and then join them back into a single string.
3. Return the sorted string.

Input hello world this is python
Output: world python hello this is

Input : my name is john doe
Output : name doe john is my

Input : sorting strings can be fun
Output :be sorting can fun strings

Input : the quick brown fox jumps over the lazy dog
Output : the the dog quick brown over jumps fox lazy
'''


def sort_string(s):
    # new = s[::-1].split(' ')
    # new.sort()
    # print(new)
    # a = []
    # for i in new:
    #     a.append(i[::-1])
    #
    # return ' '.join(a)

    new = s.split(' ')
    word = sorted(new, key=lambda x: x[-1])
    return ' '.join(word)

print(sort_string('the quick brown fox jumps over the lazy dog'))
