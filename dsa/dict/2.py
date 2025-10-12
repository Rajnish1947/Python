# -----------------------------
# Dictionary Methods in Python
# -----------------------------

# Initial dictionary
student = {"name": "Rajnish", "age": 21, "city": "Delhi"}

print("Original dictionary:", student)

# 1. len() -> count number of key-value pairs
print("Length of dictionary:", len(student))

# 2. pop(key) -> remove a key and return its value
age = student.pop("age")
print("Popped age:", age)
print("After pop:", student)

# 3. update() -> add or update multiple items
student.update({"age": 22, "email": "rajnish@example.com"})
print("After update:", student)

# 4. clear() -> remove all items
copy_dict = student.copy()   # making copy before clear
student.clear()
print("After clear:", student)

# 5. keys() -> returns all keys
print("Keys:", copy_dict.keys())

# 6. values() -> returns all values
print("Values:", copy_dict.values())

# 7. items() -> returns all (key, value) pairs
print("Items:", copy_dict.items())

# 8. get(key, default) -> safe access
print("Get existing key:", copy_dict.get("name"))
print("Get non-existing key:", copy_dict.get("salary", "Not Found"))

# 9. copy() -> creates shallow copy of dictionary
dict_copy = copy_dict.copy()
print("Copied dictionary:", dict_copy)
