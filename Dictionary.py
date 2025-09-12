# its not allowed dublicates


# 1. Create a dictionary
my_dict = {
    'name': 'rajnish',
    'age': 21,
    'city': 'Rampur'
}
print("Original Dictionary:", my_dict)

# 2. Accessing values
print("Name:", my_dict['name'])             # Direct access
print("Age using get():", my_dict.get('age'))  # Safe access

# 3. Add or update values
my_dict['email'] = 'raj@example.com'        # Add new key
my_dict['age'] = 22                         # Update existing key
print("After update:", my_dict)

# 4. Delete values
del my_dict['city']                         # Delete specific key
print("After deleting 'city':", my_dict)

popped_email = my_dict.pop('email')         # Remove and return value
print("Popped Email:", popped_email)
print("After pop:", my_dict)

# 5. Check if key exists
if 'name' in my_dict:
    print("'name' key exists in dictionary")

# 6. Loop through dictionary
print("\nLoop through dictionary (keys):")
for key in my_dict:
    print(key, "=>", my_dict[key])

print("\nLoop through dictionary (key-value pairs):")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 7. Dictionary methods
print("\nKeys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

# 8. Copy dictionary
copy_dict = my_dict.copy()
print("Copied Dictionary:", copy_dict)

# 9. Nested dictionary
student = {
    'name': 'Rajnish',
    'marks': {
        'math': 90,
        'science': 85
    }
}
print("Math Marks:", student['marks']['math'])

# 10. Create dictionary from list of tuples
pairs = [('a', 1), ('b', 2)]
dict_from_pairs = dict(pairs)
print("From pairs:", dict_from_pairs)

# 11. Set default value if key doesn't exist
my_dict.setdefault('gender', 'male')
print("After setdefault:", my_dict)

# 12. Dictionary comprehension
squares = {x: x*x for x in range(5)}
print("Squares dictionary:", squares)

# 13. Merge two dictionaries (Python 3.9+)
dict1 = {'a': 1}
dict2 = {'b': 2}
merged = dict1 | dict2
print("Merged Dictionary:", merged)

