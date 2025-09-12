#  Python Data Types: Tuple, List, Set, Dictionary
# ---------------------------------------------

#  1. TUPLE: Ordered, Immutable, Allows Duplicates
t = (1, 2, 3, 2)  # Round brackets ( )
print("Tuple:", t)
print("Type:", type(t))
# t[0] = 100      Not allowed (immutable)

# ---------------------------------------------

#  2. LIST: Ordered, Mutable, Allows Duplicates
l = [1, 2, 3, 2]  # Square brackets [ ]
print("\nList:", l)
print("Type:", type(l))
l[0] = 100        #  Allowed (mutable)
print("Modified List:", l)

# ---------------------------------------------

#  3. SET: Unordered, Mutable, No Duplicates
s = {1, 2, 3, 2}  # Curly brackets { } with no key:value
print("\nSet:", s)
print("Type:", type(s))
s.add(4)          #  Add element
print("Modified Set:", s)
# Sets automatically remove duplicates

# ---------------------------------------------

# 4. DICTIONARY: Unordered (3.6+ keeps insertion order), Key-Value Pairs, No Duplicate Keys
d = {"name": "Raj", "age": 21}  # Curly brackets { } with key: value pairs
print("\nDictionary:", d)
print("Type:", type(d))
d["age"] = 22        #  Modify value
d["city"] = "Delhi"  #  Add new key:value pair
print("Modified Dictionary:", d)

# ---------------------------------------------
#  Summary of Differences

print("\n Summary:")
print("Tuple      → Immutable, Ordered, Duplicates Allowed")
print("List       → Mutable, Ordered, Duplicates Allowed")
print("Set        → Mutable, Unordered, No Duplicates")
print("Dictionary → Mutable, Unordered, Key-Value Pairs, Keys Unique")

# End of file
