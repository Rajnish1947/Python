# Negative index starts from end
# You can also create the list like this
my_list1 = list(("pooja", "rani", "sachin"))  # or just ["pooja", "rani", "sachin"]
print(my_list1)

# 1. Create a list
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)
print(type(my_list))

# 2. Extend list with another list
my_list.extend(my_list1)
print("After extending with my_list1:", my_list)

# 3. Access elements
print("First Element:", my_list[0])
print("Last Element:", my_list[-1])
print("Current List:", my_list)

# 4. Update element
my_list[1] = 10
print("After updating 2nd item to 10:", my_list)

# 5. Add elements
my_list.append(6)
print("After append(6):", my_list)

my_list.insert(2, 99)
print("After insert(99 at index 2):", my_list)

# 6. Extend again
my_list.extend([7, 8, 9])
print("After extend([7, 8, 9]):", my_list)

# 7. Remove elements
my_list.remove(10)
print("After remove(10):", my_list)

my_list.pop()
print("After pop():", my_list)

my_list.pop(2)
print("After pop(2):", my_list)

# 8. Search in list
print("Is 3 in list?", 3 in my_list)
if 4 in my_list:
    print("Index of 4:", my_list.index(4))
else:
    print("4 is not in list")

# 9. Count occurrences
print("Count of 1:", my_list.count(1))

# 10. Sort the list (only numeric part)
numbers = [4, 2, 7, 1, 9]
numbers.sort()
print("Sorted list (ascending):", numbers)

numbers.sort(reverse=True)
print("Sorted list (descending):", numbers)

# 11. Reverse the list
my_list.reverse()
print("Reversed my_list:", my_list)

# 12. Copy the list
copy_list = my_list.copy()
print("Copied List:", copy_list)

# 13. Clear the list
copy_list.clear()
print("Cleared copy_list:", copy_list)

# 14. Loop through list
print("Looping through my_list:")
for item in my_list:
    print(item, end=' ')
print()

# 15. List comprehension
squares = [x**2 for x in range(5)]
print("List comprehension (squares):", squares)

# 16. Join list into string
words = ['hello', 'world']
sentence = " ".join(words)
print("Joined sentence:", sentence)

# 17. Split string into list
split_text = sentence.split()
print("Split sentence into list:", split_text)

# 18. Length of list
print("Length of my_list:", len(my_list))
