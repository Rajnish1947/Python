# String Input
name = input("Enter your name: ")

# Integer Input
age = int(input("Enter your age: "))

# Float Input
height = float(input("Enter your height (in cm): "))

# Boolean Input (converted from string)
is_student_input = input("Are you a student? (yes/no): ")
is_student = is_student_input.lower() == "yes"

# Multiple values in one line (space-separated)
marks = input("Enter your 3 subject marks (space-separated): ").split()
marks = [int(mark) for mark in marks]  # Convert each to int

# List Input using comma separation
hobbies_input = input("Enter your hobbies (comma-separated): ")
hobbies = [h.strip() for h in hobbies_input.split(",")]

# Dictionary-style input
city = input("Enter your city: ")
pin = input("Enter your area pin code: ")
address = {
    "city": city,
    "pin": pin
}

# Summary output
print("\n--- User Profile ---")
print("Name:", name)
print("Age:", age)
print("Height:", height, "cm")
print("Is Student:", is_student)
print("Marks:", marks)
print("Hobbies:", hobbies)
print("Address:", address)
