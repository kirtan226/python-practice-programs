# Using the Python language, have the function SimpleSymbols(str) take the str parameter being passed
# and determine if it is an acceptable sequence by either returning the string true or false.
# The str parameter will be composed of + and = symbols with several letters between them
# (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol.
# So the string to the left would be false. The string will not be empty and will have at least one letter.


def SimpleSymbols(s):
    # Add '+' to both ends of the string to simplify edge cases
    s = '+' + s + '+'

    # Iterate through each character in the string
    for i in range(len(s)):
        # If the current character is a letter
        if s[i].isalpha():
            # Check if it's surrounded by '+' symbols
            if s[i - 1] != '+' or s[i + 1] != '+':
                return "false"

    return "true"


# Test cases
print(SimpleSymbols("++d+===+c++=+a"))  # Output: false
# print(SimpleSymbols("+f+=+g+"))  # Output: true
# print(SimpleSymbols("+a+"))  # Output: false
# print(SimpleSymbols("+z+z+z+"))