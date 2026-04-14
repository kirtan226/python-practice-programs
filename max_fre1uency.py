'''Return the most common character in the string.
In case of more than one character, return the first character.

Example
input:'hello world'
output:'1'
Reason: The character 'l' appears 3 times in 'hello world', which is more than any other character.'''

def most_common_character(s):
    freq={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    return str(max(freq, key=freq.get))


print(most_common_character("hello , my name is kirtannnnn"))