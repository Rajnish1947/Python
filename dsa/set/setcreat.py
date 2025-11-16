# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Empty set
s = set()

# Set with elements
s1 = {1, 2, 3, 4}
s2 = set([2, 3, 4, 5])

print(s)    # Output: set()
print(s1)   # Output: {1, 2, 3, 4}
print(s2)   # Output: {2, 3, 4, 5}
