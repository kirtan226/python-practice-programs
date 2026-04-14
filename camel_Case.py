''' Write a function to convert a given string to camelCase .
- To obtain a string in camel case, we capitalize the first letter of each word
    except the first one.
- Then Join all words without spaces to form the camelCase string.

Input : 'hello world'
Output : 'helloWorld'
Reason: The input string is split into two words: 'hello' and 'world'. In the resulting camelCase string,
only the first letter of the second word is capitalized.

Input : 'this is a test'
Output : thisIsATest

Input : 'convert this to camel case'
Output : convertThisToCamelCase

Input : 'another example here'
Output: anotherExampleHere
'''


def to_camel_case(s):
    l = s.split(' ')
    print(l)

    new = []
    new.append(l[0])
    print(new)

    for i in range(1, len(l)):
        new.append(l[i].capitalize())

    return ''.join(new)


print(to_camel_case('hello world user'))
