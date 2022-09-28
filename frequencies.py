"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        item = str(item)
        if(not frequencies.__contains__(item)):
            frequencies[item] = 1
        else:
            frequencies[item] = frequencies[item] + 1
    # Your code goes here
    return frequencies

print(frequencies(["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "b", "b", "b"]))