# Given a string, remove any characters that are unique from the string.

# Example:

# input: "abccdefee"

# output: "cceee"

# Solution

def only_duplicates(string):
    letters = set(string)
    for letter in letters:
        if string.count(letter) == 1:
            string = string.replace(letter, '')
    return string