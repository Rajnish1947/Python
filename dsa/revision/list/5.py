# Find the Second Largest Element in a List

nums = [10, 20, 4, 45, 99]

first = second = float('-inf')

for n in nums:
    if n > first:
        second = first
        first = n
    elif n > second and n != first:
        second = n

print("Second largest:", second)


# Example:
# maan lo list = [10, 20, 4, 45, 99]
# Starting:

# first = -inf
# second = -inf

# Step 1 → n = 10

# Check: if 10 > -inf ✅
# Toh:

# second = first   → second = -inf
# first = n        → first = 10


# ➡️ ab tak largest = 10, second largest = -inf

# Step 2 → n = 20

# Check: if 20 > 10 ✅
# Toh:

# second = first   → second = 10
# first = n        → first = 20


# ➡️ ab tak largest = 20, second largest = 10

# Step 3 → n = 4

# Check: if 4 > 20 ❌
# ➡️ kuch nahi badla.

# Step 4 → n = 45

# Check: if 45 > 20 ✅
# Toh:

# second = first   → second = 20
# first = n        → first = 45


# ➡️ ab tak largest = 45, second largest = 20

# Step 5 → n = 99

# Check: if 99 > 45 ✅
# Toh:

# second = first   → second = 45
# first = n        → first = 99


# ✅ Final:
# first = 99
# second = 45
