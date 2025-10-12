# -----------------------------
# Python Set Operations - DSA
# -----------------------------

# 1. Creating sets
s1 = {1, 2, 3, 4}             # Create a set with elements
s2 = set([3, 4, 5, 6])        # Another way to create a set from a list
s_empty = set()                # Create an empty set

print("Initial sets:")
print("s1:", s1)
print("s2:", s2)
print("Empty set:", s_empty)
print()

# 2. Basic operations
print("2. Basic Set Operations")
print("Length of s1:", len(s1))   # len() -> Returns number of elements in set

s1.add(5)                        # add() -> Adds an element to the set
print("After adding 5 to s1:", s1)

s1.discard(2)                     # discard() -> Removes element if exists; no error if not found
print("After discarding 2 from s1:", s1)

s_copy = s1.copy()                # copy() -> Creates a shallow copy of the set
print("Copy of s1:", s_copy)

s1.clear()                        # clear() -> Removes all elements from the set
print("s1 after clear():", s1)
print()

# 3. No indexing
print("3. No Indexing:")
try:
    print(s2[0])  # ❌ Not allowed; sets are unordered
except TypeError as e:
    print("Error:", e)
print()

# 4. Membership
print("4. Membership Test")
print("3 in s2?", 3 in s2)        # in -> Checks if element exists
print("10 not in s2?", 10 not in s2)  # not in -> Checks if element does NOT exist
print()

# 5. Set Operations (Union, Intersection, Difference, Symmetric Difference)
print("5. Set Operations")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("a:", a)
print("b:", b)

print("Union (a | b):", a | b)                 # Union -> All elements from both sets
print("Intersection (a & b):", a & b)          # Intersection -> Common elements
print("Difference (a - b):", a - b)           # Difference -> Elements in a but not in b
print("Symmetric Difference (a ^ b):", a ^ b) # Symmetric Difference -> Elements in a or b but not both
print()

# 6. Iterating over a set
print("6. Iterating over set b:")
for elem in b:
    print(elem, end=' ')   # Loop through set elements (order may vary)
print("\n")

# 7. Removing duplicates from a list
print("7. Removing duplicates from a list:")
arr = [1, 2, 2, 3, 4, 4, 5]
unique_arr = list(set(arr))   # Convert list to set -> removes duplicates, then back to list
print("Original list:", arr)
print("Unique elements:", unique_arr)
print()

# 8. Subset / Superset
print("8. Subset / Superset")
x = {1, 2}
y = {1, 2, 3, 4}
print("x:", x)
print("y:", y)
print("Is x subset of y?", x.issubset(y))       # issubset() -> True if all elements of x are in y
print("Is y superset of x?", y.issuperset(x))   # issuperset() -> True if y contains all elements of x
