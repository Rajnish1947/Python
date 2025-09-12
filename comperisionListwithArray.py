# Importing array module
import array



# A list can hold multiple data types
my_list = [1, "hello", 3.14, True]  # Mixed types are allowed

# Accessing list elements
print("List element at index 1:", my_list[1])  # Output: "hello"

# Adding elements to the list
my_list.append("new item")
print("Updated List:", my_list)

# Removing an element
my_list.remove(1)  # Removes the value 1
print("List after removal:", my_list)


# Iterating through the list
print("List elements:")
for item in my_list:
    print(item)


#  Using Python Array


# Creating an array of integers only
my_array = array.array('i', [10, 20, 30, 40])  # 'i' = integer type

# Accessing array elements
print("\nArray element at index 2:", my_array[2])  # Output: 30

# Adding elements to the array
my_array.append(50)
print("Updated Array:", my_array)

# Removing an element
my_array.remove(20)  # Removes value 20
print("Array after removal:", my_array)

# Iterating through the array
print("Array elements:")
for item in my_array:
    print(item)


#  What array CANNOT do


# Uncommenting the next line will raise an error because it's not an integer
# my_array.append("hello")  # 


# Summary

print("\nSummary:")
print("List can hold mixed types:", my_list)
print("Array can hold only integers:", my_array.tolist())  # .tolist() converts array to list for printing
