# Different ways to reverse a list in Python

# Original list
arr = [1, 2, 3, 4, 5]
print("Original List:", arr)

# 1. Using reverse() → modifies the same list
arr1 = arr.copy()
arr1.reverse()
print("1. reverse() method:", arr1)

# 2. Using slicing [::-1] → creates a new list
arr2 = arr[::-1]
print("2. Slicing [::-1]:", arr2)

# 3. Using reversed() function → gives iterator, convert to list
arr3 = list(reversed(arr))
print("3. reversed() function:", arr3)

# 4. Using Two-Pointer Swap (manual way, interview style)
arr4 = arr.copy()
i, j = 0, len(arr4) - 1
while i < j:
    arr4[i], arr4[j] = arr4[j], arr4[i]  # swap elements
    i += 1
    j -= 1
print("4. Two-pointer swap:", arr4)
