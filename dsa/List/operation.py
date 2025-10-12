
# Python List Operations

# Initial list
numbers = [10, 20, 30, 40, 50]

# 1. len() → length of list
print(len(numbers))  # 5

# 2. Negative Indexing → access from end
print(numbers[-1])   # 50 (last element)
print(numbers[-2])   # 40 (second last)

# 3. append() → add element at the end
numbers.append(60)
print(numbers)  # [10, 20, 30, 40, 50, 60]

# 4. extend() → add multiple elements
numbers.extend([70, 80])
print(numbers)  # [10, 20, 30, 40, 50, 60, 70, 80]

# 5. insert() → add element at specific index
numbers.insert(2, 25)
print(numbers)  # [10, 20, 25, 30, 40, 50, 60, 70, 80]

# 6. remove() → remove specific element
numbers.remove(25)
print(numbers)  # [10, 20, 30, 40, 50, 60, 70, 80]

# 7. pop() → remove element (default: last)
numbers.pop()
print(numbers)  # [10, 20, 30, 40, 50, 60, 70]
numbers.pop(2)  # remove element at index 2
print(numbers)  # [10, 20, 40, 50, 60, 70]

# 8. clear() → remove all elements
temp = numbers.copy()
temp.clear()
print(temp)  # []

# 9. min() → smallest element
print(min(numbers))  # 10

# 10. max() → largest element
print(max(numbers))  # 70

# 11. sort() → sort in ascending (default)
numbers.sort()
print(numbers)  # [10, 20, 40, 50, 60, 70]
# sort in descending
numbers.sort(reverse=True)
print(numbers)  # [70, 60, 50, 40, 20, 10]

# 12. slicing → access part of list
print(numbers[1:4])   # [60, 50, 40]
print(numbers[:3])    # [70, 60, 50]
print(numbers[::2])   # [70, 50, 20]

# 13. count() → count occurrences
nums = [1, 2, 2, 3, 2, 4]
print(nums.count(2))  # 3

# 14. reverse() → reverse list in-place
nums.reverse()
print(nums)  # [4, 2, 3, 2, 2, 1]

# 15. copy() → create shallow copy
copy_nums = nums.copy()
print(copy_nums)  # [4, 2, 3, 2, 2, 1]

# 16. index() → find position of element
print(nums.index(3))  # 2 (first occurrence)
