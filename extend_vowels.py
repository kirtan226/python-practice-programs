"""
write a function to extend a vowels in string .
1. Define a function that takes a string and an integer n as input.
2. Inside the function, repeat each vowel n times.
3. Return the resulting string with extended vowels.

input:'hello' 3
output:'heeellooo'
Reason: The vowels in 'hello' are 'e' and 'o'. When each is repeated 3 times, the result is 'heeellooo'.

Input:apple' 2
Output: aapplee

Input:banana' 4
Output:baaaanaaaanaaaa

"""

def extend_vowels(word, n):
    vowels = 'aeiou'
    new =''

    for char in word:
        if char in vowels:
            new+=char*n
        else:
            new+=char
    return new


print(extend_vowels("aiaoauaia", 3))