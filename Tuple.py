# it is umutable
# we can change it value


# ---------------------------
# 1. Creating Tuples
# ---------------------------

# Regular tuple
t1 = (1, 2, 3)
print("Tuple t1:", t1)

# Tuple without parentheses
t2 = 4, 5, 6
print("Tuple t2:", t2)

# Single element tuple (comma is important)
single = (10,)
print("Single element tuple:", single)

# Tuple with mixed data types
mixed = ("hello", 5.6, True)
print("Mixed type tuple:", mixed)

# ---------------------------
# 2. Accessing Elements
# ---------------------------

t = (10, 20, 30, 40)
print("First element:", t[0])     # 10
print("Last element:", t[-1])     # 40

# ---------------------------
# 3. Tuple Operations
# ---------------------------

# Concatenation
a = (1, 2)
b = (3, 4)
c = a + b
print("Concatenated tuple:", c)

# Repetition
print("Repeated tuple:", a * 3)

# Length of tuple
print("Length of a:", len(a))

# Membership test
print("Is 2 in a?", 2 in a)

# ---------------------------
# 4. Tuple Methods
# ---------------------------

t3 = (1, 2, 3, 2, 4)
print("Count of 2:", t3.count(2))
print("Index of 3:", t3.index(3))

# ---------------------------
# 5. Tuple Unpacking
# ---------------------------

student = ("Ravi", 85)
name, marks = student
print("Name:", name)
print("Marks:", marks)

# ---------------------------
# 6. Tuple in Loops
# ---------------------------

students = [("Anita", 90), ("Ravi", 85), ("Karan", 78)]
for name, score in students:
    print(f"{name} scored {score}")

# ---------------------------
# 7. Tuple vs List Comparison
# ---------------------------

my_tuple = (1, 2, 3)         # Immutable
my_list = [1, 2, 3]          # Mutable

# my_tuple[0] = 10           # ❌ Will raise error (uncomment to test immutability)
my_list[0] = 10              # ✅ Allowed
print("Modified list:", my_list)

# ---------------------------
# 8. Tuple Use Case: Returning Multiple Values
# ---------------------------

def get_student_info():
    return ("Priya", 20)

student_name, student_age = get_student_info()
print("Student Name:", student_name)
print("Student Age:", student_age)

# ---------------------------
# End of File
# ---------------------------
