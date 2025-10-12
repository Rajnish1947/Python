
# Python Tuple Operations


# 1. len() → length of tuple
print(len(t1))  # 5

# 2. Indexing (positive & negative)
print(t1[0])   # 10 (first element)
print(t1[-1])  # 50 (last element)

# 3. Slicing
print(t1[1:4])  # (20, 30, 40)
print(t1[:3])   # (10, 20, 30)
print(t1[::-1]) # (50, 40, 30, 20, 10) → reversed

# 4. count() → count occurrences
print(t3.count(2))  # 3

# 5. index() → find first index of element
print(t3.index(3))  # 2

# 6. min() → smallest element
print(min(t1))  # 10

# 7. max() → largest element
print(max(t1))  # 50

# 8. sum() → sum of numeric elements
print(sum(t1))  # 150

# 9. Nesting tuples
nested = (t1, t2)
print(nested)  # ((10, 20, 30, 40, 50), ('apple', 'banana', 'cherry'))

# 10. Concatenation (+)
t4 = (60, 70)
print(t1 + t4)  # (10, 20, 30, 40, 50, 60, 70)

# 11. Repetition (*)
print(t2 * 2)   # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# 12. Membership (in / not in)
print(30 in t1)     # True
print("mango" not in t2)  # True

# 13. Converting list ↔ tuple
lst = [1, 2, 3]
tpl = tuple(lst)   # list → tuple
print(tpl)         # (1, 2, 3)

lst2 = list(t2)    # tuple → list
print(lst2)        # ['apple', 'banana', 'cherry']

# 14. Iterating through tuple
for item in t2:
    print(item)

