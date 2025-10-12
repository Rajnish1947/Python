# A dictionary is a collection of key-value pairs.

# Keys → Unique, immutable (string, number, tuple, etc.)

# Values → Can be any type
# -----------------------------
# Python Dictionary Operations - DSA
# -----------------------------

# 1. Creating Dictionaries
dict1 = {"name": "Rajnish", "age": 21, "city": "Delhi"}   # Normal dictionary
dict2 = dict(id=101, branch="CSE")                       # Using dict()
empty_dict = {}                                          # Empty dictionary

print("Initial Dictionaries:")
print("dict1:", dict1)
print("dict2:", dict2)
print("empty_dict:", empty_dict)
print()

# 2. Accessing Values
print("2. Accessing Values")
print("Name:", dict1["name"])              # Access using key
print("Age (get method):", dict1.get("age"))   # get() avoids error if key missing
print("Invalid key with get():", dict1.get("salary", "Not Found"))
print()

# 3. Adding / Updating
print("3. Adding / Updating Values")
dict1["email"] = "rajnish@example.com"     # Add new key-value
dict1["age"] = 22                          # Update existing key
print("After add/update:", dict1)
print()

# 4. Removing items
print("4. Removing Items")
dict1.pop("city")                          # pop() -> remove key and return value
print("After pop city:", dict1)
dict1.popitem()                            # popitem() -> removes last inserted key-value pair
print("After popitem:", dict1)
del dict1["age"]                           # del -> delete a key
print("After del age:", dict1)
dict1.clear()                              # clear() -> remove all items
print("After clear:", dict1)
print()

# 5. Dictionary Methods
dict3 = {"a": 1, "b": 2, "c": 3}
print("5. Dictionary Methods")
print("Keys:", dict3.keys())               # keys() -> returns all keys
print("Values:", dict3.values())           # values() -> returns all values
print("Items:", dict3.items())             # items() -> returns (key, value) pairs
print()

# 6. Copy
dict4 = dict3.copy()                       # copy() -> shallow copy
print("6. Copy of dict3:", dict4)
print()

# 7. Iterating
print("7. Iterating Dictionary")
for k, v in dict3.items():                 # Loop through key-value pairs
    print(f"{k} : {v}")
print()

# 8. Dictionary Comprehension
print("8. Dictionary Comprehension")
squares = {x: x*x for x in range(5)}       # Create dict with comprehension
print("Squares dict:", squares)
print()

# 9. Nested Dictionary
print("9. Nested Dictionary")
students = {
    "101": {"name": "Rajnish", "marks": 90},
    "102": {"name": "Aman", "marks": 85}
}
print("Students dict:", students)
print("Student 101 Name:", students["101"]["name"])
