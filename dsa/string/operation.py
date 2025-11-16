

# The split() function is used to break a string into a list of words or parts based on a 
# separator (by default, space " ").
# # String Operations in Python

s = "datastructure"

# 1. Length
print("Length:", len(s))                     # Output: Length: 13

# 2. Indexing & Slicing
print("First char:", s[0])                   # Output: First char: d
print("Last char:", s[-1])                   # Output: Last char: e
print("Slice (2:6):", s[2:6])                # Output: Slice (2:6): tastr[2:6]→‘tastructu’ Wait check string: datastructure indexes:
# 0 d
# 1 a
# 2 t
# 3 a
# 4 s
# 5 t
# 6 r
# So [2:6] gives t a s t => “tast”
# Correction:
print("Slice (2:6):", s[2:6])                # Output: Slice (2:6): tast

# 3. Concatenation & Repetition
print("Concat:", "data" + "structure")       # Output: Concat: datastructure
print("Repeat:", "DSA " * 3)                 # Output: Repeat: DSA DSA DSA 

# 4. Searching
print("'str' in s?", "str" in s)             # Output: 'str' in s? True
print("Find 't':", s.find("t"))              # Output: Find 't': 2
print("Index 'data':", s.index("data"))      # Output: Index 'data': 0

# 5. Modification (creates new string)
print("Upper:", s.upper())                   # Output: Upper: DATASTRUCTURE
print("Lower:", s.lower())                   # Output: Lower: datastructure
print("Replace:", s.replace("a", "x"))       # Output: Replace: dxtxstructure

# 6. Splitting & Joining
s2 = "a,b,c,d"
print("Split:", s2.split(","))               # Output: Split: ['a', 'b', 'c', 'd']
lst = ["data", "structure"]
print("Join:", "-".join(lst))                # Output: Join: data-structure

# 7. Reversing
print("Reversed:", s[::-1])                  # Output: Reversed: erutcurtsatad

# 8. Counting
print("Count of 't':", s.count("t"))         # Output: Count of 't': 3

# 9. Checks
s3 = "Python3"
print("Is Alpha:", s3.isalpha())             # Output: Is Alpha: False
print("Is Digit:", s3.isdigit())             # Output: Is Digit: False
print("Is Alnum:", s3.isalnum())             # Output: Is Alnum: True
print("Startswith 'Py':", s3.startswith("Py"))  # Output: Startswith 'Py': True
print("Endswith '3':", s3.endswith("3"))        # Output: Endswith '3': True
