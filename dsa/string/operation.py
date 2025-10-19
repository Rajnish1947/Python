

# The split() function is used to break a string into a list of words or parts based on a 
# separator (by default, space " ").
# # String Operations in Python

s = "datastructure"

# 1. Length
print("Length:", len(s))

# 2. Indexing & Slicing
print("First char:", s[0])
print("Last char:", s[-1])
print("Slice (2:6):", s[2:6])

# 3. Concatenation & Repetition
print("Concat:", "data" + "structure")
print("Repeat:", "DSA " * 3)

# 4. Searching
print("'str' in s?", "str" in s)
print("Find 't':", s.find("t"))    # index of first t
print("Index 'data':", s.index("data"))

# 5. Modification (creates new string)
print("Upper:", s.upper())
print("Lower:", s.lower())
print("Replace:", s.replace("a", "x"))

# 6. Splitting & Joining
s2 = "a,b,c,d"
print("Split:", s2.split(","))
lst = ["data", "structure"]
print("Join:", "-".join(lst))

# 7. Reversing
print("Reversed:", s[::-1])

# 8. Counting
print("Count of 't':", s.count("t"))

# 9. Checks
s3 = "Python3"
print("Is Alpha:", s3.isalpha())
print("Is Digit:", s3.isdigit())
print("Is Alnum:", s3.isalnum())
print("Startswith 'Py':", s3.startswith("Py"))
print("Endswith '3':", s3.endswith("3"))
